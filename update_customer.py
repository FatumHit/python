#!/usr/bin/python3.8

import csv
import os
import socket
import smtplib
from email.mime.text import MIMEText
from colorama import Fore, Back, Style


#SendMail Function
def sendMail(subj,msg,bcc_list):
    mailto=['mail@gmail.com']
    bcc = bcc_list
    bcc.extend(['new-mail@gmail.com' , 'new-mail2@gmail.com', 'new-mail3@gmail.com'])
    #bcc.append('grigory@caab.io')
    toaddrs = [mailto] + bcc
    efrom="my-mail@gmail.com"
    #mailfrom=socket.gethostname()
    SUBJECT=subj
    smObj=smtplib.SMTP('SMTP-SERVER-NAME',25)
    smObj.login('MY-USER-NAME','MyPASS')
    msg=MIMEText(msg.replace('\n','<br>'),'html')
    #msg=MIMEText(msg, 'html')
    msg['Subject']=SUBJECT
    msg['Reply-To'] = "my-mail@gmail.com"
    msg['To']=", ".join(mailto)
    msg['From']="my-mail@gmail.com"
    msg['Content-Type']='text/html; charset=UTF-8'
    #msg['Content-Transfer-Encoding']='7bit'
    smObj.sendmail(efrom,toaddrs,msg.as_string())
    smObj.quit()

owner_email = []

# Add here a user and his sub user or group . if this user exist in a list sub user also will receive a massage 
# Add user damian with sub user grigory example: 'main@google.com' : 'user@google.com'
# Add user damian with group example:            'main@google.com' : ['user-1@google.com' , 'user-2@google.com']
#                           ****use comma between each user ***
vip_users = { 'vip1@gmail.com' : ['sub1@gmail.com', 'sub2@gmail.com', 'sub3@gmail.com'] }
            

approve = input(Fore.GREEN +"      Your are going to send email to customers from file users.csv,\n      please Enter 'YES' to approve: ")
print(Style.RESET_ALL)

if approve.lower() == "yes".lower():

    with open('users.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            site = int(row['siteId'])
            if  site == 233 or site == 30 or site == 238 or site == 423 :
                owner_email.append(row['ownerEmail'])
            else :
                owner_email.append(row['parentUserEmail'])

    
    no_duplicates_owners = list(dict.fromkeys(owner_email))     

    
    for key, value in vip_users.items():
        if key in no_duplicates_owners:
            #Check if value is list and not string
            if isinstance(vip_users[key], list): 
                no_duplicates_owners.extend(value)
            else:
                no_duplicates_owners.append(value)


 


    print(no_duplicates_owners)


    msg =  """
    START TIME: Sunday, 20th of December 2020, 01:00:00 IST
    ESTIMATED END TIME: Sunday, 20th of December 2020, 03:00:00 IST 
    RANGE: 2 HOURS
    DATA CENTER: ANY


    Dear Customer,

    As part of a wide system upgrade and infrastructure reconfiguration in c Center, a reboot of multiple physical servers is required. 
    During the reboot time, your server will not be available and the running operating system, application, and services will be restarted.
    Though such work is normally done without any interference in the infrastructure level, this reconfiguration cannot be done on-the-fly 
    without interfering with normal server functionality and this work requires a reboot (Power Off and Power On) one or more of your servers.
    If you have any questions or concerns please reply at any time.

    Thank you for understanding and sorry for the inconvenience,  




    """

    subj = ' SYSTEM MAINTENANCE  '

    ### move all variables to Send Mail function     
    sendMail(subj,msg,no_duplicates_owners)