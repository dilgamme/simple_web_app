### Switch to adminuser
sudo su adminuser
### Install tools
sudo apt-get install nano

### Create repos folder
mkdir repos

cd repos

### Clone Git repository:
git clone https://github.com/dilgamme/dlgm-python-app.git

### Install Ngnix
sudo apt install nginx

### Create an NGINX configuration file for the app
sudo nano /etc/nginx/sites-enabled/flask_app

### Add the below text in settings file:

server {
    listen 80;
    server_name 172.201.45.91;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

Ctrl+X and Yes

### Disable the NGINX’s default configuration file by removing its symlink:

sudo unlink /etc/nginx/sites-enabled/default

### Reload the NGINX configuration file:

sudo nginx -s reload

In the /home directory, install Python 3:

sudo apt install python3

### Install pip3, the standard package manager for Python:

sudo apt install python3-pip

### Install flask
pip3 install flask

### Install Gunicorn
sudo apt-get install gunicorn

### Run Gunicorn with workers
gunicorn -w 3 app:app



