from requests import request
import json, os

### ProxMoxClient class ###
class ProxMoxClient:
# initialize the client with the url, username and password file, authenticate immediately
    def __init__(self, url, username, password_file): # password_file is the path to the file containing the password (like secrets/password)
        self.url = url
        self.username = username
        with open(password_file, "r") as passwordfile:
            self.password = passwordfile.read().strip()
        self.ticket = self.authenticate_proxmox()

# authenticate to proxmox
    def authenticate_proxmox(self):
        url = f"{self.url}/access/ticket"
        data = {
            "username": self.username,
            "password": self.password,
        }
        response = request("POST", url, data=data, verify=False)
        if response.status_code != 200:
            raise PermissionError(
                f"Request failed with status code {response.status_code}, please check your credentials")
        else:
            return response.json()["data"]["ticket"]

# get cluster info
    def get_cluster_info(self):
        url = f"{self.url}/cluster"
        cookies = {"PVEAuthCookie": self.ticket}
        response = request("GET", url, cookies=cookies, verify=False)
        return response.json()

# get all resources (careful, this is a massive json)
    def get_all_resources_info(self):
        url = f"{self.url}/cluster/resources"
        cookies = {"PVEAuthCookie": self.ticket}
        response = request("GET", url, cookies=cookies, verify=False)
        return response.json()

# get all resources of a specific type    
    def get_resources_info_per_type(self, type):
        url = f"{self.url}/cluster/resources?type={type}"
        cookies = {"PVEAuthCookie": self.ticket}
        response = request("GET", url, cookies=cookies, verify=False)
        return response.json()['data']
    
# get all resources that are vm type and their correspondng node
    def get_all_vms(self):
        url = f"{self.url}/cluster/resources?type=vm"
        cookies = {"PVEAuthCookie": self.ticket}
        response = request("GET", url, cookies=cookies, verify=False)
        return response.json()["data"]
    
    def get_corresponding_node(self, vmid):
        allvms = self.get_all_vms()
        for vm in allvms:
            if vm["vmid"] == vmid:
                return vm["node"]
        return None

# from a vm, get the network device
    def get_vm_config(self, vmid):
        node = self.get_corresponding_node(vmid)
        url = f"{self.url}/nodes/{node}/qemu/{vmid}/config"
        cookies = {"PVEAuthCookie": self.ticket}
        response = request("GET", url, cookies=cookies, verify=False)
        return response.json()["data"]
    
    def get_vm_with_tag(self, tag):
        allvms = self.get_all_vms()
        tagged_vms = []
        for vm in allvms:
            obj_type = vm["type"]
            vmid = vm["vmid"]
            vm_config = self.get_vm_config(vmid)
            print(f"Getting tags for vmid {vmid}")
            if obj_type == "qemu":
                try:
                    tags = vm_config["tags"]
                except KeyError:
                    continue  # If the "tags" key is not present, skip this VM
                if tag in tags:
                    tagged_vms.append(vm)  # If the required tag is in the tags, append the vm to the list
                else:
                    continue # If the required tag is not in the tags, skip this VM
            else:
                print(f"VM {vmid} is not a qemu type, skipping. Type is {type}")
                continue
        return tagged_vms
    
    def get_vm_config_with_tag(self, tag):
        tagged_vms = self.get_vm_with_tag(tag)
        tagged_vms_config = {}
        for vm in tagged_vms:
            node = vm["node"]
            vmid = vm["vmid"]
            tagged_vms_config[f"{node}_{vmid}"] = self.get_vm_config(vmid)
        return tagged_vms_config

    # def create_vm(self, node, vmid, name, ostype="Linux", ide2="ceph-fs:iso/ubuntu-22.04.3-live-server-amd64.iso,media=cdrom,size=2083390K", bootdisk, virtio0, sockets, cores, memory, net0):
    #     url = f"{self.url}/nodes/{node}/qemu"
    #     cookies = {"PVEAuthCookie": self.ticket}
    #     data = {
    #         'name': name,
    #         'vmid': vmid,
    #         'ostype': ostype,
    #         'ide2': ide2,
    #         'bootdisk': bootdisk,
    #         'virtio0': virtio0,
    #         'sockets': sockets,
    #         'cores': cores,
    #         'memory': memory,
    #         'net0': net0,
    #     }
    #     response = request("POST", url, cookies=cookies, data=data, verify=False)
    #     return response.json()


### ProxMoxParser class ###
class ProxMoxParser:
    def __init__(self, client, results_dir):
        self.client = client
        self.results_dir = results_dir

    def write_results(self, results, filename):
        # used os.path.join to make the code platform independent (windows uses \, linux uses /)
        with open(os.path.join(self.results_dir, filename), "w") as file:
            if isinstance(results, str):
                try:
                    json.loads(results)
                    file.write(results)
                except json.JSONDecodeError:
                    file.write(results)
            else:
                try:
                    json.dump(results, file, indent=2)
                except TypeError:    
                    file.write(results)
    
    def parse_all_vm_config_network(self):
        vms = self.client.get_all_vms()
        network_devices = {}
        for vm in vms:
            node = vm["node"]
            vmid = vm["vmid"]
            status = vm["status"]
            obj_type = vm["type"]
            name = vm["name"]
            print(f"Getting network information for node {node} and vmid {vmid}")
            if status != "running":
                print(f"VM {vmid} is not running, skipping")
                continue
            elif obj_type != "qemu":
                print(f"VM {vmid} is not a qemu type, skipping. Type is {type}")
                continue
            elif status == "running":
                print(f"VM {vmid} is running, getting network information")
                vm_config = self.client.get_vm_config(node, vmid) # this returns the entire config, we only need the network information
                output = {
                    "vmid": vmid,
                    "name": name,
                    "node": node,
                    "network": vm_config.get("net0"),
                    "macaddr": vm_config.get("net0").split(",")[0].split("=")[1]
                }
                network_devices[f"{node}_{vmid}"] = output
        self.write_results(network_devices, "network_devices.json")
        return network_devices
    