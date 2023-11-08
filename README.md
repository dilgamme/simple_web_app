## Setup Instructions

```bash
# Switch to adminuser
sudo su adminuser

# Install necessary tools
sudo apt-get update
sudo apt-get install nano
sudo apt-get install nginx
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install gunicorn

# Create a directory for repositories and clone Git repository
mkdir repos
cd repos
git clone https://github.com/dilgamme/simple_web_app.git

# Configure NGINX for the Flask app
sudo nano /etc/nginx/sites-enabled/flask_app

# Add the following configuration, then press Ctrl+X, Y to save changes
server {
    listen 80;
    server_name 172.201.45.91;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

# Disable the NGINX default configuration
sudo unlink /etc/nginx/sites-enabled/default

# Reload NGINX
sudo nginx -s reload

# Install Flask and run the application using Gunicorn
pip3 install flask
cd /path/to/simple_web_app
gunicorn -w 3 app:app
