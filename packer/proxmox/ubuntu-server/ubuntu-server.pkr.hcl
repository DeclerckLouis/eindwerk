# Ubuntu Server Focal
# ---
# Packer Template to create an Ubuntu Server (Focal) on Proxmox

# Go get the plugin
packer {
  required_plugins {
    proxmox = {
      version = ">= 1.1.7"
      source  = "github.com/hashicorp/proxmox"
    }
  }
}

# Resource Definiation for the VM Template
source "proxmox-iso" "ubuntu-server" {

  # Proxmox Connection Settings
  proxmox_url = "${var.proxmox_api_url}"
  username    = "${var.proxmox_api_token_id}"
  token       = "${var.proxmox_api_token_secret}"
  # (Optional) Skip TLS Verification
  insecure_skip_tls_verify = true

  # VM General Settings
  node                 = "${var.node}" # This should be a variable set by the ansible playbook
  vm_id                = "400" # The ID of the VM, used during creation
  vm_name              = "ubuntu-template-with-users" #this is the name of the template (The artifact created by packer)
  template_description = "Created form ubuntu packer template, includes users, docker and cloud-init\nSetup the IP config in the cloud-init tab after cloning!"

  # VM OS Settings
  # (Option 1) Local ISO File
  iso_file = "cephfs:iso/ubuntu-22.04.4-live-server-amd64.iso"
  # - or -
  # (Option 2) Download ISO
  # iso_url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.3-live-server-amd64.iso"
  # iso_checksum = "f8e3086f3cea0fb3fefb29937ab5ed9d19e767079633960ccb50e76153effc98"
  iso_storage_pool = "cephfs"
  unmount_iso      = true

  # VM System Settings
  qemu_agent = true

  # VM Hard Disk Settings
  scsi_controller = "virtio-scsi-single"

  disks {
    disk_size    = "40G"
    format       = "raw"
    storage_pool = "vm-store"
    # storage_pool_type = "rbd"
    type = "virtio"
  }

  # VM CPU Settings
  cpu_type = "x86-64-v2-AES"
  sockets = "2"
  cores   = "4"
  memory = "4096"

  # VM Network Settings
  network_adapters {
    model    = "virtio"
    bridge   = "vmbr0"
    firewall = "true"
  }

  # VM Cloud-Init Settings
  cloud_init              = true
  cloud_init_storage_pool = "vm-store"

  # PACKER Boot Commands
  boot_command = [
    "c", # open grub command-line
    "linux /casper/vmlinuz --- autoinstall ds='nocloud-net;s=http://{{ .HTTPIP }}:{{ .HTTPPort }}/' ", # this is basically telling the installer to use cloud-init and at the packer host ip and port
    "<enter><wait>",
    "initrd /casper/",
    "<wait><wait><wait>initrd", # this initialized something, the <wait> had to be added because it wouldn't type the whole command sometimes
    "<enter><wait><wait><wait>",
    "boot<enter>"
  ]
  boot      = "c"
  boot_wait = "10s"

  # PACKER Autoinstall Settings
  http_directory = "http"
  # http_bind_address = "192.168.0.124" ## packer runner ip, this doesn't really matter that much
  http_port_min     = 8802
  http_port_max     = 8802

  ssh_username = "ansible"
  # ssh_password = "no"
  ssh_private_key_file = "~/.ssh/id_rsa"
  ssh_timeout = "60m" # Raise the timeout when installation takes longer
}

# Build Definition to create the VM Template
build {

  name    = "ubuntu-server" # Name of the build, not of the template, this is just for the pipeline
  sources = ["source.proxmox-iso.ubuntu-server"]

  # Provisioning the VM Template for Cloud-Init Integration in Proxmox #1
  provisioner "shell" {
    inline = [
      "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Waiting for cloud-init...'; sleep 1; done",
      "sudo rm /etc/ssh/ssh_host_*",
      "sudo truncate -s 0 /etc/machine-id",
      "sudo apt -y autoremove --purge",
      "sudo apt -y clean",
      "sudo apt -y autoclean",
      "sudo cloud-init clean",
      "sudo rm -f /etc/cloud/cloud.cfg.d/subiquity-disable-cloudinit-networking.cfg",
      "sudo sync"
    ]
  }

  # Provisioning the VM Template for Cloud-Init Integration in Proxmox #2
  provisioner "file" {
    source      = "files/99-pve.cfg"
    destination = "/tmp/99-pve.cfg"
  }

  # Provisioning the VM Template for Cloud-Init Integration in Proxmox #3
  provisioner "shell" {
    inline = ["sudo cp /tmp/99-pve.cfg /etc/cloud/cloud.cfg.d/99-pve.cfg"]
  }

  # Install docker
  provisioner "shell" {
    inline = [
      "sudo timedatectl set-timezone Europe/Brussels",
      "sudo apt-get install -y ca-certificates curl gnupg lsb-release",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",
      "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
      "sudo apt-get update -y",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose",
    ]
  }

  provisioner "shell" {
    inline = [
      "wget https://repo.zabbix.com/zabbix/6.5/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.5-1+ubuntu22.04_all.deb",
      "sudo dpkg -i zabbix-release_6.5-1+ubuntu22.04_all.deb",
      "sudo apt-get update -y",
      "sudo apt-get install -y zabbix-agent2 zabbix-agent2-plugin-*",
      "sudo systemctl enable zabbix-agent2",
      "sudo systemctl start zabbix-agent2",
      "sudo rm zabbix-release_6.5-1+ubuntu22.04_all.deb"
    ]
  }
provisioner "shell" {
  inline = [
    "echo 'krb5-config krb5-config/default_realm string DOTOCEAN.NET' | sudo debconf-set-selections",
    "echo 'krb5-config krb5-config/kerberos_servers string ipa1.DOTOCEAN.NET' | sudo debconf-set-selections",
    "echo 'krb5-config krb5-config/admin_server string ipa1.DOTOCEAN.NET' | sudo debconf-set-selections",
    "DEBIAN_FRONTEND=noninteractive",
    "sudo apt-get install -y freeipa-client oddjob-mkhomedir",
    "echo -e 'Name: mkhomedir\nDefault: yes\nPriority: 0\nSession-Type: Additional\nSession:\n  required pam_mkhomedir.so umask=0022 skel=/etc/skel' | sudo tee /usr/share/pam-configs/mkhomedir && sudo chmod 0644 /usr/share/pam-configs/mkhomedir"
  ]
}

  provisioner "shell" {
    inline = [
      # create a cronjob that runs "sudo ipa-client-install --mkhomedir --force-join --server=ipa1.dotocean.net --domain=dotocean.net --realm=DOTOCEAN.net --principal=admin --password='${var.adminpass}' --unattended" and then removes the cronjob
      "echo '@reboot root (sudo ipa-client-install --mkhomedir --force-join --enable-dns-updates --ntp-pool='be.pool.ntp.org' --server=ipa1.dotocean.net --domain=dotocean.net --realm=DOTOCEAN.NET --principal=${var.adminuser} --password=${var.adminpass} --unattended; sed -i \"/@reboot root/d\" /etc/crontab)' | sudo tee -a /etc/crontab > /dev/null"
    ]
  }

  # Remove ubuntu user from the system and sudoers file, and remove the cron job that does this, but do all that ONLY on second boot (after cloud-init has run)
  # If you don't understand, run the following command a couple times, and look at the outputs. however, i do think this leaves a residu
  # (test -f /second_boot_check && (echo "here" && sudo rm /second_boot_check)) || (sudo touch /second_boot_check && echo "not here")
  provisioner "shell" {
    inline = [
      "echo '@reboot root (test -f /second_boot_check && (userdel -r ubuntu; sed -i \"/^ubuntu /d\" /etc/sudoers.d/90-cloud-init-users; sed -i \"/@reboot root/d\" /etc/crontab; rm /second_boot_check) || (touch /second_boot_check))' | sudo tee -a /etc/crontab > /dev/null"
    ]
  }
}
