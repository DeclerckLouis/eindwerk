# What is Hashicorp Vault?
HashiCorp Vault is a tool that provides secrets management, data encryption, and identity management for any infrastructure and application.

## KV Secrets Engine
The KV secrets engine is used to store arbitrary secrets in Vault. It is a versioned key-value store where you can store and manage secrets.
To visualize it a bit easier, it can be compared to the following JSON scheme:
```json
{
    "Secrets": {
        "KVEngine1": {
            "Secret1":{
                "key": "value"
            },
            "Secret2":{
                "key": "value"
            },
            "Secret3":{
                "key": "value"
            }
        },
        "OtherEngine1": {
        }
    }
}
```

Say you now have a Ansible playbook that needs to access the value of "Secret2", you can use the following code to retrieve the secret:
```yaml
secret: "{{ lookup('hashi_vault',
          'secret=KVEngine1/data/Secret1:key
          token=hvs.SomeVeryLongAndAutomaticallyGeneratedToken
          url=https://your.vault.server:8200
          validate_certs=true') }}"
```