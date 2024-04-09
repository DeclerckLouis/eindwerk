# k3s-ansible ([semaphore](https://www.semui.co/))
A project to setup or reset a [k3s cluster](https://k3s.io/) using [ansible](https://www.ansible.com/).
All ansible playbooks, roles and inventory files are stored in this gitlab project.

## Description
This project contains ansible [playbooks](.) and [roles](./roles/) to setup a k3s cluster on either a set of VMs (tested using ubuntu 22.04.3) or a set of raspberry pi's.
The [tests]() directory can be ignored.


## How to use
### Prerequisites (***For a TEST ENVIRONMENT***, this is still work in progress)
Please see also the [assets](./assets/node_setup/) folder for a script that does all this, it's pretty straightforward.
- A set of VMs or raspberry pi's
- A user with sudo rights on all the VMs or raspberry pi's (tested using a user called `ansible`, which coudl run `sudo` without password)
- Ansible on the host machine
- SSH keys for the user on the host machine to be able to connect to the VMs or raspberry pi's  
- A version of the inventory, see [semaphore_inventory.yaml](./inventories/SEMAPHORE_TOCOPY_INVENTORY.yaml) for an example.

### Setup (in semaphore)  
1. Create a new project in semaphore.  
2. In gitlab, either create a Personal Access Token (with repo read rights), or add your ssh key to the project.  
3. In semaphore, go to the Key Store and add new key (either ssh key (SSH Key), or Personal Access Token (login with password and leave username blank)).  
4. Add the private key that corresponds to the public key you added to the VMs or raspberry pi's to the Key Store aswell
4. If your user has to fill in a password when using sudo, you can add the password to the key store as well.
5. Add the repository to the project, use "main" branch, and access key is the one you just created.  
6. Next, go to environment and add new environment.  
7. Give the environment a name (empty) and just put {} in both fields.  
8. Now, go to inventory and add new inventory.
9. Give the inventory a name, User Credentials should be the name of the SSH or PAT key you made in the key store. Sudo credentials are self explanatory.  
10. Add the hosts to the inventory. For this, take a look at the [semaphore_inventory.yaml](./inventories/SEMAPHORE_TOCOPY_INVENTORY.yaml) file.  
11. Now, the task itself. Go to tasks and add new task.  
12. Give the task a name (setup), set the Playbook Filename to `setup.yml`, and select the inventory you just created. Repository is this one, environment the empty one we created.
13. Click save and you can now run the task!  

### Reset (in semaphore)
This is after the setup has been done, we can reuse all the settings we just made.
1. Go to tasks and add new task.
2. Give the task a name (reset), set the Playbook Filename to `reset.yml`, and select the inventory you created before. Repository is this one, environment `empty`.
3. Click save and you can now run the task!

## TODO
- [ ] **Raspberry pi PXE boot setup**
- [ ] Add support for dynamic inventory (cobbler?)
- [ ] Check cleanup temporary files after playbook run


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.