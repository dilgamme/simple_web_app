Step 1: Create a Linux Virtual Machine in Azure
Login to Azure:

Copy code
az login

Choose subscription

az account set --subscription "82a2f20a-df87-401a-bf13-3b2feebf35c7"

Create a Resource Group:

az group create --name YourResourceGroupName --location eastus
Create a Linux VM:


Copy code
az vm create --resource-group YourResourceGroupName --name YourVMName --image UbuntuLTS --admin-username YourUsername --generate-ssh-keys --size Standard_B1s
Step 2: Connect to Your Linux VM
SSH into Your VM:

Copy code
ssh YourUsername@YourVMIPAddress
Step 3: Install Required Software on VM
Update Package Lists:


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
