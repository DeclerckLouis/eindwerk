# Proxmox BPG provider

terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
    }
  }
}

provider "proxmox" {
  endpoint = var.endpoint # THE / IS IMPORTANT, DON'T FORGET (See vars.tf and vars.auto.tfvars)
  api_token = var.token
  insecure = true # Fix certificates
}

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
  sensitive   = false
  description = "Node to deploy the VM on"
}

variable "templatenode" {
  type        = string
  sensitive   = false
  description = "Node where the VM Template resides"
  
}