Tutorial:

SETUP DOCKER, build image, dan run container
Sebelum menggunakan docker, docker file harus di install dulu pada OS, apabila OS yang digunakan adalah ubuntu, masukkan command berikut:

$ sudo apt install apt-transport-https ca-certificates curl software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

$ sudo apt update

$ apt-cache policy docker-ce

Install juga library docker compose dengan command : 

$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

Untuk mengecek kembali apakah docker dan docker compose sudah terinstall, bisa masukkan command:
$ docker --version
$ docker-compose --version
