# MAIN
This contains all the working configurations etc for the final project.

## Diagrams
The following diagram shows a typical run of the project. (VM Creation)  

```mermaid
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

Next, the deletion of a VM.
    
```mermaid
sequenceDiagram
    participant User
    participant NetBox
    participant Event-Driven Ansible
    participant Ansible (runner)
    participant Terraform
    participant ProxMox
    participant n8n
    participant Notion
    User-->>NetBox: Delete VM
    NetBox-->>n8n: Webhook (remove IP)
    n8n-->>Notion: Delete page
    NetBox-->>Event-Driven Ansible: Webhook (update VM)
    Event-Driven Ansible-->>Event-Driven Ansible: Drop event (no matching rules)
    Event-Driven Ansible-->>Ansible (runner): Run playbook
    Ansible (runner)-->>Ansible (runner): Check existence, <br/>status, etc
    Ansible (runner)-->>Terraform: Delete Resource
    Terraform-->>ProxMox: Destroy VM
    ProxMox-->>Terraform: VM deleted
    Terraform-->>Ansible (runner): "Finished"
```


## Seperate Components

### NetBox
```mermaid
graph TD
    U[User] <--> |UI| A[NetBox]
    A --> |Webhook| B[Event-driven-ansible]
    B --> |Ansible-Runner| P[Ansible playbooks]
    P --> |API Call| A
    A --> |Webhook| N[n8n]
    N --> |API Call| D[Notion]
    D <--> |UI| U2[Another User]
    A --> |API Call| S[Other Scripts]
    S --> |something| Z[Something else]
    Z --> |Some Feedback| A
```