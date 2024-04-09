# Event-based automation pipelines
The following is a brief overview of what pipelines are, why they are important and how they were implemented in this project  

## A short introduction
After the explanation of abstraction, we can now talk about pipelines.  
Pipelines are a series of "steps", in which each step gets an input, processes it, and outputs processed data **to the next step**.   
In the context of this project, an event-based automation pipeline is used.  (Event Driven Ansible)
This pipeline is what starts all the different playbooks, scripts, etc. after receiving an event.  

## Overview of pipelining in this project
In this project, the main "pipeline" is #

## Features of EDA
EDA has a few features that make it a good choice for this project.  
- EDA is event-driven, meaning that it listens for events (webhooks) and starts a pipeline when an event is received.  
- EDA is rule-based, meaning that it can be configured to only start a pipeline when a specific rule is met.  
- EDA is asynchronous, meaning that it can run multiple pipelines at the same time. (very useful when dealing with multiple events at the same time)  
- it's officially integrated with Ansible and Zabbix, meaning that it should be really easy to integrate zabbix triggers. (self-healing, yay!)  