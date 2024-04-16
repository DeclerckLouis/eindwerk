# Archived: Python Eventlistener
## Why was it chosen?
The idea of writing a Python Eventlistener was chosen because i wanted something faster then EDA.
EDA can listen for event asynchronously, but will trigger the playbooks synchronously. this means that no matter the amount of events, only one playbook will be executed at a time.

## Why was it abandoned?  
The idea of using the Python Eventlistener was abandoned because it was too complex for the current state of the project.  
It required a lot of queue management, extra checks and was not as reliable as the current solution.