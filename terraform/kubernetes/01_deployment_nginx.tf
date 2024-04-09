# create a deployment in the terraform namespace
resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "nginx"
    namespace = kubernetes_namespace.terraform.metadata.0.name
  }

  spec {
    replicas = 3
    selector {
      match_labels = {
        app = "nginx-terraform-deployed"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx-terraform-deployed"
        }
      }

      spec {
        container {
          image = "nginx:1.7.8"
          name  = "nginx"
          port {
            container_port = 80
          }

          resources {
          }
        }
      }
    }
  }
}