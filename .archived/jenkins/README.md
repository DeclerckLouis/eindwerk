# Archived: Jenkins
## Why was it chosen?
Jenkins was the first choice when it came to choosing a triggering system.
It was chosen because it has an incredible amount of plugins, integrations, and it is open-source.
Another thing that made Jenkins a good choice was the fact that it didn't require containers to run the playbooks, I could just setup one "bastion" ansible agent and run the playbooks from there.
This made it easier to secure, since I ddin't have to worry about exposing secrets to the docker hub or any other container registry.

## Why was it abandoned?
The idea of using Jenkins as the main triggering system was abandoned because it had some limitations that made it really hard to work with.
These include:
- It had to be exposed to the internet to receive webhooks from gitlab / github
- It required a lot of plugins. This is not a problem in itself, but this made the whole automation dependent on external maintainers. (I don't like that)
- It was hard to maintain. Requires a lot of manual work to keep it up to date. This defeats the purpose of creating the automation.


## What is the alternative?
After some (a lot of) research and a re-evaluatoin of the requirements, it was decided to go for a much simpler and more lightweight approach. (Event Driven Ansible)
Event Driven Ansible (EDA) requires very little setup and can be run on a single machine. It's currently still in development, but works great for demonstrating the concept of event-driven automation.
Another really good thing about EDA is that since it doesn't require all those plugins, it can easily be swapped in the future for something else. (RedHat Ansible Automation Platform, Ansible Tower, etc.)
> Don't get me wrong, Jenkins might be a great tool and is very widely used. But for this project, it was not the right choice.
> All in all, Jenkins was a great learning experience and chances are that I will be seeing it a lot more in the future.
