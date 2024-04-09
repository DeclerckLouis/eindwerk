from requests import request
import json, os

### NetBoxClient class ###
class caller():
# initialize the client with the url and token file, authenticate immediately
    def __init__(self, url, token_file):
        self.url = url
        with open(token_file, "r") as tokenfile:
            self.token = tokenfile.read().strip()
        self.headers = self.authenticate()

    def authenticate(self):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Token {self.token}"
        }
        return headers

    def get_cluster_types(self):
        url = f"{self.url}/virtualization/cluster-types/"
        headers = self.headers
        response = request("GET", url, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(
                f'Request failed with status code {response.status_code}, {response.json()["detail"]}')
        else:
            return response.json()

    def get_clusters(self):
        url = f"{self.url}/virtualization/clusters/"
        headers = self.headers
        response = request("GET", url, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(
                f'Request failed with status code {response.status_code}, {response.json()["detail"]}')
        else:
            return response.json()

    def get_virtual_machines(self, cluster=None):
        url = f"{self.url}/virtualization/virtual-machines/"
        headers = self.headers
        if cluster:
            response = request("GET", url, headers=headers, params=f"cluster={cluster}", verify=False)
        else:
            response = request("GET", url, headers=self.headers, verify=False)
        return response


### NetBoxParser class ###
class parser()  :
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

class NetBoxCreator:
    def __init__(self, client):
        self.client = client
        self.url = client.url
        self.headers = client.headers
        
    def cluster_type(self, data):
        url = f"{self.url}/virtualization/cluster-types/"
        headers = self.headers
        response = request("POST", url, headers=headers, json=data, verify=False)
        if response.status_code != 201:
            raise Exception(
                f'Request failed with status code {response.status_code}, {response.json()["detail"]}')
        else:
            return response.json()
        
    def vm(self, data):
        url = f"{self.url}/virtualization/virtual-machines/"
        headers = self.headers
        response = request("POST", url, headers=headers, json=data, verify=False)
        if response.status_code != 201:
            raise PermissionError(
                f'Request failed with status code {response.status_code}, {response.json()["detail"]}')
        else:
            return response.json()