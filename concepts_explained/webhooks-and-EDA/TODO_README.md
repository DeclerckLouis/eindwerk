# What are webhooks and Event-Driven-Automation?
## Webhooks in NetBox
### It all starts with the NetBox inventory
NetBox is in this project considered the "Source of Truth" for all the infrastructure.  
This means that all the information about the infrastructure is stored in NetBox, and all other systems have to match their own information with NetBox.  **THIS IS IMPORTAINT**
>This is important: NetBox is the source of truth, not the destination of truth.
So, say i create a new VM in NetBox, what happens?

### The webhook
When a new VM is created in NetBox, NetBox is set up to send a webhook to the Event-Driven-Ansible (EDA) system.
This webhook contains all the information about the new VM, and is sent to the EDA system. It looks somehing like [this output](output.json).  
You can see it contains a "data" object, which contains all the information about the new VM. This is the information that is needed later down the road.  
It also contains a "event" object, which tells the EDA system what kind of event this is. (created, updated or removed). **This is important becase it's what triggers the logic in terraform, ansible, etc.** 

### The EDA system
The EDA system is a system that listens for triggers from various sources, more about that in the [Event-based pipelines](../event-based-pipelines/TODO_README.md) section.  
When the EDA system receives a webhook, it check if any of the information in the webhook matches any of the triggers it has set up.
If it does, it will start the pipeline that is associated with that trigger.

> This is important: The EDA system is the system that listens for triggers, and starts the pipelines. It does the decision making for which playbooks to run and when.