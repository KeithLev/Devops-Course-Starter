variable "prefix" {
  description = "The prefix used for all resources in this enviroment"
}

variable "DOCKER_REGISTRY_SERVER_URL"{
    default = "https://hub.docker.com/repository/docker/keithleverton/todo-app:latest"
}

variable "GIT_HUB_CLIENT_ID"{
    sensitive = true
}

variable "FLASK_ENV"{
    default = "production"
}

variable "GIT_HUB_SECRET"{
    sensitive = true
}

variable "LOGIN_DISABLED"{
    default = "false"
}