======== Tutorial ========

======== SETUP DOCKER, build image, dan run container ========

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
dan
$ docker-compose --version

Kemudian build image dengan menggunakan dockerfile yang ada pada repository github ini:
Bisa dengan build dengan menggunakan extension vs code atau dengan command
: docker build 'directory'

Test docker image, apakah dia dapat dijalankan, 
Cek dulu image yang telah dibuat dengan command docker image -ls

Jalankan image tersebut dengan command 
docker run jmeter_generator

Build container dengan command 
$docker-compose up -d --no-deps --build calculationscript

