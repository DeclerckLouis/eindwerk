# Archived: Python APIs
## Why was it chosen?
Initially, the idea was to create a set of scripts that would poll the NetBox API for changes, and then trigger the automation based on those changes.
I also thought about using the REST API's to fetch information about for instance, the proxmox nodes, and then use that info to decide on which node to deploy the VM's.

## Why was it abandoned?
The idea was not entirely abandoned, but it was decided to go with pre-written libraries instead of writing everything from scratch.  
The main reason for this was that using libraries meant that we could get up and running faster, and that we could rely on the community to maintain the libraries.  
> I realise that this is might seem contradictory to the initial pitch of the project, but choosing to use libraries makes the project more maintainable and reliable in the long run.

## What is the alternative?
The alternative to writing everything from scratch is to use libraries that are already available.
For instance, instead of writing a script that makes a REST API call to NetBox, we could use the [pynetbox](https://pynetbox.readthedocs.io/en/latest/) library.
This library is maintained by the community, and is used by a lot of people, which means that it is more likely to be maintained and updated in the future.
Another example is the [proxmoxer](https://proxmoxer.readthedocs.io/en/latest/) library, which is used to interact with the Proxmox API.
For ansible invenotries, we could use the [nb_inventory](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/nb_inventory_inventory.html) plugin. Combine that with [NetBox Webhooks](https://netbox.readthedocs.io/en/stable/additional-features/webhooks/) and you have an abundance of information for the inventory.  
