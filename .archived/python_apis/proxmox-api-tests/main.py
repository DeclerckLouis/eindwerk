# imports
import json
import proxmox_client as pc
import variables as vars # type: ignore

# Set proxmoxclient variables
client_url = vars.proxmox_url
client_user = vars.proxmox_user
client_passwordfile = "eindwerk/.archived/python_apis/proxmox-api-tests/secrets/password"
parser_results_dir = "./results/"

# utilise the classes
# Client is used to make the requests to the proxmox api (returns responses in JSON format)
client = pc.ProxMoxClient(client_url, client_user, client_passwordfile)

# Parser is used to parse the responses from the client into a more readable format, or to a format that can be used for NetBox
parser = pc.ProxMoxParser(client, parser_results_dir)


# GET ALL NODES MEMORY USAGE, PRINT THE NODE WITH THE LOWEST MEMORY USAGE
# This can be used in ansible playbooks to deplay VMs on the node with the most memory available (#TODO add this to the ansible playbook)
####################################################################################################################################################
resource = client.get_resources_info_per_type("node")
print(json.dumps(resource, indent=2))
# parser.write_results(resource, "vmnode.json")
nodes = {}
nodestats = []
for node in resource:
    if node["status"]=="offline": # skip offline nodes
        continue
    else:
        maxmem = node["maxmem"] #get the maxmem from the request
        mem = node["mem"] #get the mem from the request
        mempercent = round((mem/maxmem)*100, 2) # calculate the percentage of memory used
        nodes[mempercent] = node["node"] # add the percentage of memory used and the node name to the nodes dictionary (so we can sort it later)
sorted_nodes = list(sorted(nodes.items(), reverse=True)) # sort the nodes by memory usage
print(sorted_nodes[0][1]) # select the node with the lowest memory usage
####################################################################################################################################################

# print(json.dumps(resource, indent=2))


# GET NETWORK DEVICE FORM A SPECIFIC VM
# THIS CAN BE USED TO GET THE MAC ADDRESS WHICH CAN LATER BE CHECKED AGAINST NETWORK SCANS (not sure if it's useful yet)
resp = client.get_vm_config( 132)
parser.write_results(resp, "vm_132_config.json")
# print(json.dumps(resp, indent=2))

# GET ALL NETWORK DEVICES
parser.parse_all_vm_config_network()

# GET ALL VMS WITH A SPECIFIC TAG
tagged_vms = client.get_vm_with_tag("louis")
parser.write_results(tagged_vms, "tagged_vms_louis.json")
