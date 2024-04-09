# imports
import json
import yaml
import os

# vars
results_dir = "netbox-api-tests/results/"

#convert the results/cluster.json file to a yml file
with open(os.path.join(results_dir, "clusters.yml"), "w") as file:
    with open(os.path.join(results_dir,"clusters.json"), "r") as jsonfile:
        data = json.load(jsonfile)
        yaml.dump(data["results"], file, default_flow_style=False)

# This script will convert a json file to a yml file
# the idea was to use the json output of a request to the proxmox api, parse it and then convert it to a yml file  
# This yaml file could then be used as a ansble inventory file
# Thankfully, there is a netbox inventory plugin for ansible, so this script is not needed