PLAY [Say thanks] **************************************************************

TASK [Debug a message] *********************************************************
ok: [localhost] => {
    "msg": "Thank you, my friend!"
}

TASK [Debug all variables] *****************************************************
ok: [localhost] => {
    "ansible_eda.event": {
        "meta": {
            "endpoint": "",
            "headers": {
                "Accept": "*/*",
                "Content-Length": "36",
                "Content-Type": "application/json",
                "Host": "127.0.0.1:5000",
                "User-Agent": "curl/7.81.0"
            },
            "received_at": "2024-04-02T13:18:18.385216Z",
            "source": {
                "name": "ansible.eda.webhook",
                "type": "ansible.eda.webhook"
            },
            "uuid": "5cddc7fc-ccc4-4dd3-b1dc-2b8b82c837a3"
        },
        "payload": {
            "message": "Ansible is super cool"
        }
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   