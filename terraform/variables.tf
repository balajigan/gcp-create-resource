# variables

variable "project" {
  type        = string
  description = "The project ID of the resource"
}
variable "region" {
  type        = string
  description = "cloud region of the resource"
}
variable "zone" {
  type        = string
  description = "zone of the cloud region, where the resource should be created"
}
variable "name" {
  type        = string
  description = "Name of the resource to be created"
}
