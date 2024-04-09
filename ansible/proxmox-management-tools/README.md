# Proxmox Managment Tools  
## Description  
This repository contains playbooks that can be used to manage proxmox virtual machines.  
**important:** This repository comes with a ansible.cfg file. It contains the location to the inventory file.  
If the playbooks are called from a pipeline, it should work, otherwise, make sure you change the inventory location to the place where you put the inventory.  

## Requirements  
- ansible 2.9 or later  
- python 3.10 or later  

## Playbooks  
### add-vm.yml  
This playbook demonstrates the use of python scripts on the ansible controller to dynamically "choose" which node it will deploy the virtual machine on.
This playbook is still work-in progress, it will be moved to a different directory (pocs)
You can run the playbook using the following command:  
```bash
ansible-playbook add-vm.yml
```