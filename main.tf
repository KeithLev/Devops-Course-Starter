terraform{
    required_providers{
        azurerm={
            source = "hashicorp/azurerm"
            version = ">= 3.8"
        }
    }

    backend "azurerm" {
      resource_group_name = "LV21_KeithLeverton_ProjectExercise"
      storage_account_name = "tfstate2090145315"
      container_name = "tfstate"
      key = "terraform.tfstate"
    }
    
}


provider "azurerm" {
    features{}
}

data "azurerm_resource_group""main"{
    name = "LV21_KeithLeverton_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
    name = "${var.prefix}-terraasp"
    location = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    os_type = "Linux"
    sku_name = "B1"
}

resource "azurerm_linux_web_app" "main" {
    name = "${var.prefix}-terratodoappkl"
    location = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    service_plan_id = azurerm_service_plan.main.id

    site_config{
        application_stack{
            docker_image = "keithleverton/todo-app"
            docker_image_tag = "latest"
        }
    }
    app_settings = {
        "DOCKER_REGISTRY_SERVER_URL" = var.DOCKER_REGISTRY_SERVER_URL
        "MONGODB_PRIMARY_KEY" = azurerm_cosmosdb_account.main.connection_strings[0]
        "FLASK_APP" = "todo_app/app"
        "FLASK_ENV" = var.FLASK_ENV
        "GIT_HUB_CLIENT_ID" = var.GIT_HUB_CLIENT_ID
        "GIT_HUB_SECRET" = var.GIT_HUB_SECRET
        "LOGIN_DISABLED" = var.LOGIN_DISABLED
        "SECRET_KEY" = "secret_key"
        "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"



    }
}

resource "azurerm_cosmosdb_account" "main"{
    name = "${var.prefix}-terracomosaccount"
    location = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    offer_type = "Standard"
    kind = "MongoDB"
    capabilities {name = "EnableServerless"}
    capabilities{name = "MongoDBv3.4"}
    capabilities{name = "EnableMongo"}
    geo_location{
        location = "uksouth"
        failover_priority = 0
    }
    consistency_policy{
        consistency_level = "Session"
    }
}

resource "azurerm_cosmosdb_mongo_database" "main"{
    name = "${var.prefix}-terramongodb"
    resource_group_name = data.azurerm_resource_group.main.name
    account_name = azurerm_cosmosdb_account.main.name
}
