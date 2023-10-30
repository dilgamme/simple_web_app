Step 1: Create a Linux Virtual Machine in Azure
Login to Azure:

Copy code
az login

Choose subscription

az account set --subscription "82a2f20a-df87-401a-bf13-3b2feebf35c7"

Create a Resource Group:

az group create --name rg-linux-vms-for-apps --location eastus
Create a Linux VM:


Copy code
az vm create --resource-group rg-linux-vms-for-apps --name YourVMName --image Ubuntu2204 --admin-username adminuser --generate-ssh-keys --size Standard_B1s
Step 2: Connect to Your Linux VM
SSH into Your VM:

Copy code
ssh adminuser@20.124.193.206
Step 3: Install Required Software on VM
Update Package Lists:



# Flask-App-Hosted-On-VPS
Files needed to host a flask application on a linux VPS.

## Commands

Run the following commands on the VPS.

### Install Python and Pip

```bash
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install flask
```

### Install and Configure NGINX

Install nginx and create a new configuration file.
```bash
sudo apt install nginx 
sudo nano /etc/nginx/sites-enabled/<directory-name-of-flask-app>
```

The contents of the confiugration file should be as follows:
```bash
server {
    listen 80;
    server_name <public-server-ip>;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Unlink the default config file and reload nginx to use the newly created config file.
```bash
sudo unlink /etc/nginx/sites-enabled/default
sudo nginx -s reload
```

### Installing and Using Gunicorn
```bash
sudo apt-get install gunicorn
```

Run the flask web app with gunicorn. The name of your flask instance must be ```app```.
```bash
gunicorn -w 3 flask_app:app
```
Now navigate to your servers public ip from a web browser! :)

### Credits
This information was summarized from [Linode's Guide](https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/)






Copy code
sudo apt update
Install Python and Pip:

Copy code
sudo apt install python3 python3-pip -y
Install Required Python Packages:

Copy code
pip3 install Flask gunicorn
Step 4: Copy Your Web Application to VM
Copy Your Flask App:
You can use scp to copy your Flask application files from your local machine to the VM.

Copy code
scp -r /path/to/your/flask/app YourUsername@YourVMIPAddress:/path/to/destination/folder

scp -r /path/to/your/flask/app azureuser@10.0.0.1:/home/azureuser/my_flask_app

Step 5: Run Your Flask Application
Navigate to Your App Directory:


Copy code
cd /path/to/destination/folder
Run Flask App with Gunicorn:


Copy code
gunicorn -w 4 -b 0.0.0.0:5000 your_app_file:app
Replace your_app_file with the Python file where your Flask app is defined.

Step 6: Configure Azure Firewall (if necessary)
Configure Network Security Group (NSG):
If your VM has a public IP, configure the NSG to allow incoming traffic on port 5000 (or the port your Flask app is running on).
Step 7: Access Your Web App
Access Your Web App:
Open a web browser and navigate to http://YourVMIPAddress:5000 to access your Flask-based e-learning web application.
