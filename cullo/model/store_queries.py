import dropbox
import json
import smtplib

#from web.utils import dropbox_connection

from utils import dropbox_connection, variables

mode = (dropbox.files.WriteMode.overwrite)
  

def store_query(query,ip):
    dbx = dropbox_connection.get_dropbox_conn()

    try:
        res = dbx.files_download("/users/queries.txt")
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        
    data = res[1].content.decode('utf-8')
    jsondata = json.loads(data)
    jsondata["details"].append({"query": query,'ip': ip})
    res = dbx.files_upload(json.dumps(jsondata).encode('utf-8'), "/users/queries.txt",mode)
    #send_email("", "", variables.email, "Activation Mail", "Thank you for registering. \n Please click and activate the user. \n http://127.0.0.1:5000/activate?id="+activate_token+"")
    return "Success"


def send_email(user, pwd, recipient, subject, body):

    gmail_user = variables.email
    gmail_pwd = variables.email_pwd
    print(gmail_pwd)
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except Exception as ex:
        print("failed to send mail")
        print(ex)

