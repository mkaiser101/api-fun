# SendGrid public API usage

#Obtain An API Key from SendGrid's website

#Set environment variables
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env

#Install Package
pip install sendgrid
