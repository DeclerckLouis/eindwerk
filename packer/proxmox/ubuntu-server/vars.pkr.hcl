# please refer to the docs (https://developer.hashicorp.com/packer/integrations/hashicorp/proxmox/latest/components/builder/iso) 
variable "proxmox_api_url" {
  type = string
  description = "The url of the proxmox API (example: https://<server>:<port>/api2/json)"
}

variable "proxmox_api_token_id" {
  type = string
  description = "The username, realm and id of the token (example user@pve!token_name)"
}

variable "proxmox_api_token_secret" {
  type      = string
  description = "The secret of the token (example: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)"
  sensitive = true
}

variable "node" {
  type = string
  description = "The node to create the VM on (example: prox10)"
}

variable "adminpass" {
  type = string
  description = "The password for the admin user"
  sensitive = true
}