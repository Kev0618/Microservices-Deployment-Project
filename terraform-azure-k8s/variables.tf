variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "k8s-rg"
}

variable "location" {
  description = "The Azure region to deploy the resources"
  type        = string
  default     = "East US"
}

variable "cluster_name" {
  description = "The name of the AKS cluster"
  type        = string
  default     = "myAKSCluster"
}

variable "dns_prefix" {
  description = "The DNS prefix to use for the cluster"
  type        = string
  default     = "myaks"
}

variable "node_count" {
  description = "The number of nodes in the default node pool"
  type        = number
  default     = 3
}

variable "vm_size" {
  description = "The size of the VMs to use for the nodes"
  type        = string
  default     = "Standard_DS2_v2"
}
