# imports
import netbox_client as nc
import variables as vars # type: ignore
import json

# Set netboxclient variables
client_url = vars.netbox_url
client_tokenfile = "netbox-api-tests/secrets/token"
parser_results_dir = "netbox-api-tests/results/"

# Create a NetBoxClient object
client = nc.caller(client_url, client_tokenfile)
parser = nc.parser(client, parser_results_dir)


clustertypes = client.get_cluster_types()
parser.write_results(clustertypes, "clustertypes.json")

vms = client.get_virtual_machines()
parser.write_results(vms.json(), "vms.json")

clusters = client.get_clusters()
parser.write_results(clusters, "clusters.json")

proxmox_vms = client.get_virtual_machines("ProxMox_staging")
parser.write_results(proxmox_vms.json(), "proxmox_vms.json")

# new_clustertype = {
#     "name": "test_cluster_type",
#     "slug": "test_cluster_type",
#     "description": "A test cluster type",
#     "vm_count": "1"

# }

# response = client.create_cluster_type(new_clustertype)
# print(response)
