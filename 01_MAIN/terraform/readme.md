# Terraform
## vars.auto.tfvars
This directory contains a working example of the terraform files used to deploy a VM in Proxmox.  
I encrypted the contents of the vars.auto.tfvars file using ansible-vault.  
For those of you wondering how i use them if i want to deploy a vm: I don't! I use the ansible playbook to deploy the VM. (gotcha!)  

## resources.tf
You'll see that there are still a lot of comments here, this is because this file was used to create the template (see the ansible playbook).
