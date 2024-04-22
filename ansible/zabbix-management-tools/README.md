# Zabbix Managment Tools  
## Description  
This repository contains a collection of playbooks that can be used to manage zabbix server and agents.  
**important:** This repository comes with a ansible.cfg file. It contains the location to the inventory file.  
If the playbooks are called from a pipeline, it should work, otherwise, make sure you change the inventory location to the place where you put the inventory.  

## Requirements  
- community.zabbix collection  
This collection can be installed using the following command:  
```bash
ansible-galaxy collection install community.zabbix  
```
- ansible 2.9 or later  
- python 3.10 or later  

## Playbooks  
### agent-setup.yml  
This playbook can be used to install zabbix agent on a remote host.  
The playbook will install the zabbix agent and configure it to communicate with the DotOcean zabbix server.  
You can run the playbook using the following command:  
```bash
ansible-playbook agent-setup.yml
```
### add-to-server.yml  
This playbook can be used to add hosts to the zabbix server.   
The playbook will add the host to the zabbix server and add the necessary tags, templates, etc.  
You can run the playbook using the following command:  
```bash
ansible-playbook add-to-server.yml
```