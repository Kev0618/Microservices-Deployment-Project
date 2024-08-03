output "resource_group_name" {
  description = "The name of the resource group"
  value       = azurerm_resource_group.rg.name
}

output "aks_cluster_name" {
  description = "The name of the AKS cluster"
  value       = azurerm_kubernetes_cluster.k8s.name
}

output "node_pool_name" {
  description = "The name of the node pool"
  value       = azurerm_kubernetes_cluster_node_pool.agentpool.name
}
