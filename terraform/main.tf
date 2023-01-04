# Terraform main file

provider "google" {
  project 	= var.project	
  credentials 	= "${file("credentials.json")}"
  region	= var.region
  zone		= var.zone	
}

module "vm" {
  source  = "./modules/vm"
  project = var.project
  region = var.region	
  zone = var.zone
  name = var.name	
}

#resource "google_compute_instance" "my_instance" {
#  name		= var.name	
#  machine_type	= "f1-micro"
#  zone		= "us-central1-a"	
#  allow_stopping_for_update	= true

# boot_disk {
#	initialize_params {
#		image = "debian-10-buster-v20220719"
#	}   	
#   }
#  network_interface {
#	network = "default"
#	access_config {
#	}
# }
#}
