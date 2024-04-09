# DNS certs to host (haproxy)
This is basically a overcomplicated way to get the certs from certmanager in k8s and put them on the haproxy server  
This playbook is meant to be run periodically, for example every 12 hours, to keep the certs up to date.  
Have a great day!   
  

**INSTALL THE ANSIBLE-GALAXY KUBERNETES MODULE FOR THE USER THAT WILL RUN THE PLAYBOOK**  
**NEXT, ON THE KUBERNETES NODE, INSTALL PIP**