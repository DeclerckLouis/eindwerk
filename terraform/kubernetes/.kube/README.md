## About this file
This file is a placeholder for the kubeconfig file that is used to authenticate with the Kubernetes cluster.
It is created by the [ansible playbook that creates the Kubernetes cluster](../../../ansible/ansible-k3s/setup.yml).  
So, congrats, you just found the certificates for a nonexistent Kubernetes cluster! 🎉

## How to use it
As you can see, the cluster is as default as it gets, with the default namespace and everything.  
This is because it's meant as a **testing** environment, for internal learning of kubernetes, ansible, terraform, containers, etc.  
If you want to use this in a production environment, setup your own cluster, put the kubeconfig in this folder, and then run the necessary terraform scripts to deploy the applications.