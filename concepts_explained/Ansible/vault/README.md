# Ansible Vault
Ansible Vault is a feature of Ansible that allows you to keep sensitive data such as passwords or keys in encrypted files,  
rather than as plaintext in your playbooks or roles. These encrypted files can then be safely stored in version control systems or distributed to other users.

> Good for data at rest, not for data in transit. expand with hashicorp vault? also ssl, HMAC, etc.