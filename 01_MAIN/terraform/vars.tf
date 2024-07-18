# Please refer to the docs (https://registry.terraform.io/providers/bpg/proxmox/latest/docs) for more information on the following variables
variable "endpoint" {
  type        = string
  description = "The endpoint for the Proxmox Virtual Environment API ending with / (example: https://host:port/)"
}

variable "token" {
  type        = string
  sensitive   = true
  description = "The token for the Proxmox Virtual Environment API (example: user@pve!token_name=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)"
}

variable "node" {
  type        = string
  description = "The node to deploy the VMs on (example: prox10)"
}

variable "templatenode" {
  type        = string
  description = "The node where the template is located (example: prox10)"
}

# variable "ipv4" {
#   description = "IPv4 configuration"
#   type = object({
#     address = string
#     gateway = string
#   })
# }