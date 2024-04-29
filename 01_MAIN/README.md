# MAIN
This contains all the working configurations etc for the final project.

## Diagram
The following diagram shows a typical run of the project. (VM Creation)  

```Mermaid
sequenceDiagram
    participant User
    participant NetBox
    participant Event-Driven Ansible
    participant Ansible (runner)
    participant Terraform
    participant ProxMox
    participant n8n
    participant Notion
    User-->>NetBox: New VM created
    NetBox-->>Event-Driven Ansible: Webhook
    Event-Driven Ansible-->>Ansible (runner): Run playbook
    Ansible (runner)-->>Ansible (runner): Check existence, <br/>status, etc
    Ansible (runner)-->>NetBox: VM status: "Staged"
    Ansible (runner)-->>Terraform: New Resource
    Terraform-->>ProxMox: Create VM
    ProxMox-->>Terraform: VM IP, MAC, etc
    Terraform-->>Ansible (runner): tfstate
    Ansible (runner)-->>NetBox: VM status: "Active", IP, MAC, etc
    NetBox-->>n8n: Webhook
    n8n-->>Notion: Create new page
```