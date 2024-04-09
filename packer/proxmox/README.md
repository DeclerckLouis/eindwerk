# Packer Proxmox
## why doesn't it work?
So, this is still under very heavy development.
The idea is to create a packer template that can be used to create a base image for the virtual machines in ProxMox.
Later on, i'll probably add some more features to this, such as:
- presinstalled freeIPA client
- presinstalled zabbix-agent
- ... 

> This is still a work in progress, it requires a lot of hard-coded values and is not yet ready for any production environment.

## How to use
To use this packer template, you'll need to have packer installed on your system.
1. setup SSH keys
    ```bash
    ssh-keygen -t rsa -b 4096 -C "automation-controller"
    ```
2. Setup the packer variables
    ```bash
    cp vars.auto.pkrvars.hcl.example vars.auto.pkrvars.hcl
    ```
    Edit the vars.pkrvars.hcl file to match your environment.

3. run packer init (in the ubuntu-server dir)
    ```bash
    packer init .
    ```

4. run packer build (in the ubuntu-server dir)
    ```bash
    packer build .
    ```

5. Nice!

## Notes
I'm no longer working with double var files, this is because i'm still checking how packer handles variables and secrets.  
I'd like ansible to fill in a vars file, which can then be used by packer.
> If this can be done, it would for instance be possible to have a playbook that runs every night,  
> and updates the base image with the latest updates, rotates SSH keys and passwords, etc. (or just use LDAP for that, i'm not sure yet)  