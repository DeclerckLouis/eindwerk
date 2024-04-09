terraform {
    required_providers {
        kubernetes = {
            source  = "hashicorp/kubernetes"
        }
    }
}

provider "kubernetes" {
    config_path = ".kube/config"
}

resource "kubernetes_namespace" "terraform" {
    metadata {
        name = "terraform"
    }
}

resource "helm_release" "nginx_ingress" {
  name       = "nginx-ingresscontroller"
  repository = "https://charts.helm.sh/stable"
  chart      = "nginx-ingress"
  cleanup_on_fail = true
  connection {
    host = "https://192.168.0.237:6443"
  }
}

