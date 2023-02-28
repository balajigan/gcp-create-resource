# variables

variable "project_id" {
  type        = string
  description = "The project ID of the resource"
}
variable "region_name" {
  type        = string
  description = "cloud region of the resource"
}
variable "zone_name" {
  type        = string
  description = "zone of the cloud region, where the resource should be created"
}
variable "instance_name" {
  type        = string
  description = "Name of the resource to be created"
}
variable "machine_type" {
  type        = string
  description = "Machine type to be created"
}
variable "boot_disk_image" {
  type        = string
  description = "Boot disk image to be created"
}
