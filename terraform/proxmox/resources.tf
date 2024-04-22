resource "proxmox_virtual_environment_vm" "little-cluster" {
  name      = "terraform-clustertest-node-${count.index + 1}" # Depending on where we are in the "cound" loop, the name is incremented by 1
  node_name = var.node                                        # TODO: make this dynamic, a variable possibly passed from an ansible playbook
  description = "Deployed using terraform"
  tags = ["louis", "terraform", "cluster" ]

  count = 3                                                   # Create 3 VMs, essentially runs this block 3 times

  vm_id = 500 + count.index                                   # Depending on where we are in the "cound" loop, the vm_id is also incremented by 1
  
  clone {                                                     # Clone from template with ID 400, 
    full         = true                                       # TODO: check if it's needed to create a full clone or not
    vm_id        = 400                                        # TODO: create multiple templates and choose which one to clone from (also a variable passed from an ansible playbook?)
    datastore_id = "vm-store"
    node_name = var.templatenode
  }

  startup {
    order = 3
  }

  cpu {                                                       # TODO: This gets ignored, why?
    cores = 2
    sockets = 2
    type = "x86-64-v2-AES"
  }

  memory {                                                    # TODO: This also gets ignored, why?
    dedicated = 2048  
  }

  network_device {
    vlan_id = 0                                               # TODO: make this a variable, passed from the ansible inventory?
    bridge = "vmbr0"                                          # Is this really necessary? Since already set in the packer template
  }

  initialization {
    # user_account {                                          # Setup a initioal user account, it's not needed since they're already in the template (ALSO: deprecation warning, util.py user type of string is deprecated, use users: [dict] )
    #   username = "terraform"
    #   password = "Test123"
    # }
    datastore_id = "vm-store"                                 # TODO: make this a variable, passed from the ansible inventory?
    ip_config {
      ipv4 {
        address = "10.10.31.10${count.index+1}/24"           # Depending on where we are in the "cound" loop, the IP address is incremented by 1 (starting from 151)
        gateway = "10.10.31.1"        
      }
    }
    
    dns {
      domain  = "dotocean.local"
      servers = ["10.10.31.2", "172.16.0.2"]                 # TODO: make this a variable, passed from the ansible inventory?
    }
  }

  started       = true                                        # Start the VM after creation
  timeout_clone = 300                                         # Timeout for the clone operation (300 seconds)

  agent {                                                     # QEMU Guest Agent, should already be enabled, but just to be sure
    enabled = true
  }

}
