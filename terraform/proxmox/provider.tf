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
  insecure = true
}