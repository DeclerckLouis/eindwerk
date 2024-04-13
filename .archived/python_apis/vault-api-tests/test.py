import hvac

tokenfile = "eindwerk/.archived/python_apis/vault-api-tests/secrets/token"
with open (tokenfile, "r") as tokenfile:
    tokenval = tokenfile.read().strip()

client = hvac.Client(
    url='https://10.10.31.102:8200',
    token=tokenval,
    verify=False
)

read_response = client.secrets.kv.v2.read_secret_version(path='proxmox/data/apitoken')
password = read_response['data']['data']['token']
print(password)