Cara setup docker dan nginx pada Ubuntu
1.	Install juga library docker compose dengan command : 

$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/dockercompose-`uname -s-uname -m` -o /usr/local/bin/docker-compose 


2.	Untuk mengecek kembali apakah docker dan docker compose sudah terinstall, bisa masukkan command: 

     $ docker --version dan $ docker-compose --version


3.	Kemudian build image dengan menggunakan dockerfile yang ada pada repository github ini: Bisa dengan build dengan menggunakan extension vs code atau dengan command : 

      docker build 'directory'


4.	Test docker image, apakah dia dapat dijalankan, Cek dulu image yang telah dibuat dengan command 
         
      docker image -ls


5.	Jalankan image tersebut dengan command 
       
       docker run jmeter_generator     


6.	Build container dengan command 

        $docker-compose up -d --no-deps --build calculationscript


7.	Untuk menjalankan command dalam container, masukkan command

        $ docker exec it 'container ID' /bin/sh


8.	Setelah masuk ke dalam container, masukkan command 


          #python script.py


10.	Kemudian bisa di cek html report pada directory yang dimasukkan pada environment variable

==================================================================================================================

Cara Setup Nginx  
Command yang digunakan 
 


Update installer di ubuntu dan install nginx 
$ sudo apt update 
$ Sudo apt install nginx 
 
Untuk mengecek apakah nginx sudah terinstall 
$ sudo ufw app list 
 
Untuk memberi permission pada service nginx 
$ sudo ufw allow 'Nginx HTTP' 
$ sudo ufw status 
 
Mengecek apabila ufw status sudah running 
$ systemctl status nginx 



Expose html dengan menggunakan nginx 


Buka directory  
etc/nginx/sites-enabled 
 
Kemudian buat file baru dengan nama website yang akan di expose 
 
 server {  
listen 8888;  	 	
server_name index.jmeter.com;  	 	
root /home/ivangananjaya/Documents/Sample; 
index index.html; 
 
     
    #location /jmeter_generator { } 
 
 	#location / {  
 	# 	index index.html; 
 	#} 
 
    #location /images { 	 	 
    #    root /home/ubuntu/data;  
    #} 
 	} 
 
Kemudian bisa di test dengan socket 8888 pada local host pada browser 

