
# variables

variable "project" {
  type        = string
  description = "The project ID of the VM"
}
variable "region" {
  type        = string
  description = "cloud region of the VM"
}
variable "zone" {
  type        = string
  description = "zone of the cloud region, where the VM should be created"
}
variable "name" {
  type        = string
  description = "Name of the VM to be created"
}
