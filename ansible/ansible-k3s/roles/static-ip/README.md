Static-IP
=========

This role simply takes all the ip addreses in the inventory file, and sets them as static on the hosts.
To use this role, set the static_ip variable to true in the inventory file.  

```yaml
  vars:
    static_ip: true
    static_ip_network: "YOUR NETWORK RANGE"
    static_ip_subnet: "YOUR SUBNET CIDR"
    static_ip_gateway: "YOUR DEFAULT GATEWAY"
    static_ip_dns1: "YOUR DNS SERVER"
    static_ip_dns2: "YOUR SECOND DNS SERVER"
```  
  
Requirements
------------

See the above snippet from the inventory file.  

Role Variables
--------------

Also see the above snippet from the inventory file  

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
         - static-ip
```  

Author Information
------------------

Louis Declerck
