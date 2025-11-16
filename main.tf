provider "azurerm" {
  features {}
  subscription_id = "27f13d13-2f09-4e87-98b6-d36e2e7aac18"
  tenant_id       = "6f9e3b1e-1809-444a-81d3-82d40a928812"
  use_cli         = true
}

resource "azurerm_resource_group" "rg_devops" {
  name     = "rg-devops-equipe"
  location = "Brazil South"
}

resource "azurerm_storage_account" "storage" {
  name                     = "storagedevopsequipe3"
  resource_group_name      = azurerm_resource_group.rg_devops.name
  location                 = azurerm_resource_group.rg_devops.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
