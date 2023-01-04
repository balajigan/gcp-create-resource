# Module for vm
resource "google_compute_instance" "my_instance" {
  name		= var.name	
  machine_type	= "f1-micro"
  zone		= "us-central1-a"	
  allow_stopping_for_update	= true

  boot_disk {
	initialize_params {
		image = "debian-10-buster-v20220719"
	}   	
   }
  network_interface {
	network = "default"
	access_config {

	}
 }
}
