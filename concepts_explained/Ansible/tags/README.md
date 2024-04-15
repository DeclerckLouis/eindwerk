# Ansible Tags
Tags are a way to run specific parts of a playbook. They can be used to run only specific tasks, roles or plays.  
This can be useful when you want to run a specific part of a playbook, for example when you only want to install a specific package or when you want to skip a specific part of a playbook.

```yaml
tasks:
- debug:
    msg: "Always runs"
  tags:
  - always

- debug:
    msg: "runs when you use tag1"
  tags:
  - tag1
```

> use this with tags from netbox?