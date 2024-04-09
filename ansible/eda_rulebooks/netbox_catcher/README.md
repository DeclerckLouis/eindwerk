To setup SSL certificates for the netbox webhooks, do the following steps:
1. Generate a key and certificate for the webhook server (see the certgenerator directory)
2. using scp, sftp, or whatever you like, copy the key and certificate to the NetBox Host.
3. Move the key to the /etc/ssl/private directory
4. Move the certificate to the /etc/ssl/certs directory
5. Create a webhook in NetBox:
    - Name: <whatever you want>
    - Description: <whatever you want>
    - Tags: <whatever you want, these can be useful in your playbooks>
    - URL: https://<EDA-host>:<port>
    - HTTP method: POST
    - HTTP content type: application/json
    - Additional headers: *none*
    - Body Template: *none*
    - Secret: <none yet, maybe in the future>
    - SSL
    - SSL Verification (since it's self signed)
    - CA File Path: *none* (since we moved them to the default place)  

**Please keep in mind that i'm still learning how all this works, the EDA documentation isn't quite there yet so it's a lot of trial and error.**

## TODO
- [ ] Add a secret to the webhook (HMAC) for added integrity of the received webhook data.

Verification (on the netbox host): 
```bash
root@netbox:~# ls -l /etc/ssl/certs/ | grep dotOcean-test*
-rw-rw-r-- 1 declercklouis declercklouis   2004 Apr  3 07:05 dotOcean-test.crt
root@netbox:~# ls -l /etc/ssl/private/ | grep dotOcean-test*
-rw------- 1 declercklouis declercklouis 3272 Apr  3 07:05 dotOcean-test.key
```

Verification (on the EDA host):
While the rulebook was running, i updated the `cluster` field of a test Virtual Machine, which triggered the rules in our rulebook.
1. Cluster: ProxMox_staging
    Rule (condition): 
    ```yaml
    event.payload.data.cluster.name == "ProxMox_staging"
    ```
2. Cluster: k8s_staging
    Rule (condition): 
    ```yaml
    event.payload.data.cluster.name == "k8s_staging"
    ```
This is the output of the rulebook:

```bash
ansible-rulebook -r rulebook_vms.yml -i inventory.yml
PLAY [Say thanks] **************************************************************

TASK [Debug a message] *********************************************************
ok: [localhost] => {
    "msg": "K8S, Thank you, my friend!"
}

TASK [Debug all variables] *****************************************************
ok: [localhost] => {
    "ansible_eda.event": {
        "meta": {
            "endpoint": "",
            "headers": {
                "Accept-Encoding": "identity",
                "Content-Length": "2280",
                "Content-Type": "application/json",
                "Host": "192.168.0.124:5000",
                "User-Agent": "python-urllib3/2.2.1"
            },
            "received_at": "2024-04-03T08:10:18.642979Z",
            "source": {
                "name": "ansible.eda.webhook",
                "type": "ansible.eda.webhook"
            },
            "uuid": "a7f28881-7844-43cc-9074-e6f31982e2cd"
        },
        "payload": {
            "data": {
                "cluster": {
                    "display": "k8s_staging",
                    "id": 2,
                    "name": "k8s_staging",
                    "url": "/api/virtualization/clusters/2/"
                },
                "comments": "",
                "config_template": null,
                "created": "2024-04-02T18:36:45.591169Z",
                "custom_fields": {},
                "description": "",
                "device": null,
                "disk": 34,
                "display": "test_webhook",
                "id": 10,
                "interface_count": 0,
                "last_updated": "2024-04-03T08:10:18.334682Z",
                "local_context_data": {
                    "message": "THIS IS THE CONFIG CONTEXT",
                    "message2": "The cluster is proxmox"
                },
                "memory": 2,
                "name": "test_webhook",
                "platform": null,
                "primary_ip": null,
                "primary_ip4": null,
                "primary_ip6": null,
                "role": null,
                "site": {
                    "display": "DotoceanHQ",
                    "id": 1,
                    "name": "DotoceanHQ",
                    "slug": "dotoceanhq",
                    "url": "/api/dcim/sites/1/"
                },
                "status": {
                    "label": "Active",
                    "value": "active"
                },
                "tags": [
                    {
                        "color": "e91e63",
                        "display": "HPE",
                        "id": 6,
                        "name": "HPE",
                        "slug": "hpe",
                        "url": "/api/extras/tags/6/"
                    }
                ],
                "tenant": null,
                "url": "/api/virtualization/virtual-machines/10/",
                "vcpus": 1.0,
                "virtual_disk_count": 0
            },
            "event": "updated",
            "model": "virtualmachine",
            "request_id": "453897ac-b305-4a68-af72-180ca0c6e733",
            "timestamp": "2024-04-03T08:10:18.518801+00:00",
            "username": "louis.declerck"
        }
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

PLAY [Say thanks] **************************************************************

TASK [Debug a message] *********************************************************
ok: [localhost] => {
    "msg": "PROXMOX, Thank you, my friend!"
}

TASK [Debug all variables] *****************************************************
ok: [localhost] => {
    "ansible_eda.event": {
        "meta": {
            "endpoint": "",
            "headers": {
                "Accept-Encoding": "identity",
                "Content-Length": "2291",
                "Content-Type": "application/json",
                "Host": "192.168.0.124:5000",
                "User-Agent": "python-urllib3/2.2.1"
            },
            "received_at": "2024-04-03T08:10:35.340549Z",
            "source": {
                "name": "ansible.eda.webhook",
                "type": "ansible.eda.webhook"
            },
            "uuid": "36e19d8b-314c-404a-b777-a1792c8ea62c"
        },
        "payload": {
            "data": {
                "cluster": {
                    "display": "ProxMox_staging",
                    "id": 1,
                    "name": "ProxMox_staging",
                    "url": "/api/virtualization/clusters/1/"
                },
                "comments": "",
                "config_template": null,
                "created": "2024-04-02T18:36:45.591169Z",
                "custom_fields": {},
                "description": "",
                "device": null,
                "disk": 34,
                "display": "test_webhook",
                "id": 10,
                "interface_count": 0,
                "last_updated": "2024-04-03T08:10:35.140575Z",
                "local_context_data": {
                    "message": "THIS IS THE CONFIG CONTEXT",
                    "message2": "The cluster is proxmox"
                },
                "memory": 2,
                "name": "test_webhook",
                "platform": null,
                "primary_ip": null,
                "primary_ip4": null,
                "primary_ip6": null,
                "role": null,
                "site": {
                    "display": "DotoceanHQ",
                    "id": 1,
                    "name": "DotoceanHQ",
                    "slug": "dotoceanhq",
                    "url": "/api/dcim/sites/1/"
                },
                "status": {
                    "label": "Active",
                    "value": "active"
                },
                "tags": [
                    {
                        "color": "e91e63",
                        "display": "HPE",
                        "id": 6,
                        "name": "HPE",
                        "slug": "hpe",
                        "url": "/api/extras/tags/6/"
                    }
                ],
                "tenant": null,
                "url": "/api/virtualization/virtual-machines/10/",
                "vcpus": 1.0,
                "virtual_disk_count": 0
            },
            "event": "updated",
            "model": "virtualmachine",
            "request_id": "8530244f-6158-44d8-8afa-aa9d78a2f046",
            "timestamp": "2024-04-03T08:10:35.229824+00:00",
            "username": "louis.declerck"
        }
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```