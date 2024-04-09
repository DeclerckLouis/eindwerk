resource "kubernetes_ingress" "nginx" {
  metadata {
    name      = "nginx"
    namespace = kubernetes_namespace.terraform.metadata.0.name
  }

  spec {
    ingress_class_name = "nginx"
    rule {
      host = "localhost"

      http {
        path {
          path     = "/"
          backend {
            service_name = kubernetes_service.nginx.metadata.0.name
            service_port = 80
          }
        }
      }
    }
  }
}