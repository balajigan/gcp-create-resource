# Terraform main file

provider "google" {
  project 	= var.project_id
  credentials 	= "${file("credentials.json")}"
  region	= var.region_name
  zone		= var.zone_name
}

resource "google_compute_instance" "my_instance" {
  name		= var.instance_name
  machine_type	= var.machine_type
  zone		= var.zone_name
  allow_stopping_for_update	= true

 boot_disk = {
	initialize_params = {
		image = "debian-10-buster-v20220719"
	}
   }
  network_interface = {
	network = "default"
	access_config = {
	}
 }
}
