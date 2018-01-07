import os

try:  
    dropbox_token = os.environ["dropbox_token"]
    email = os.environ["email"]
    email_pwd = os.environ["email_pwd"]
except KeyError: 
    print("set the environmental variables properly")