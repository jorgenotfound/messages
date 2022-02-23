import mysql.connector
import boto3

"""
move the all the logic to send the messages to a new class in a different module, applying the Single Responsibility
Principle
"""
client = boto3.client(
    "sns",
    aws_access_key_id="jhw76321ihdsjbd879213nkjnsd32",
    aws_secret_access_key="dkjhdsd0i324987ldkhfkjq7q61398u9",
    region_name="us-east-1"
)

# This variable is used only inside a specific context, it will be refactored inside an specific method
dic={}
"""
REPLACE cnx with a DB Object to perform queries
GET DATABASE CONFIGURATION PARAMETERS FROM A CONFIG OBJECT
"""
cnx = mysql.connector.connect(user='admin', password='A3djbai$095ndpo#"2', host='127.0.0.1', database='users')

"""
This function will be moved to a new module
"""
def sendMesagge(message, number):
    client.publish(
        PhoneNumber=number,
        Message=message
    )


"""
func03, func04, func05 and func06 will all be replaced by a unique function to send messages, this allows to improve 
the maintainability of the code and reduce the repeated code.
"""
def func03(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table']=cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name+" we have some information about your platinum account, please go to "+service_link+ "to get more details", dic['table'][0]);


def func04(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table']=cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name+" we have some information about your gold account, please go to "+service_link+ "to get more details", dic['table'][0]);


def func05(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table']=cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name+" we have some information about your silver account, please go to "+service_link+ "to get more details", dic['table'][0]);


def func06(user_profile):
    query = "select * from users where profile ="+user_profile
    cursor = cnx.cursor()
    cursor.execute(query)
    for (first_name, last_name, phone_numbers, service_link) in cursor:
        for number in phone_numbers:
            query2 = "select number from phone_number where phone_id="+number
            cursor.execute(query)
            dic['table']=cursor.fetchall()
            sendMesagge("Hey "+first_name+" "+last_name+" we have some information about your bronze account, please go to "+service_link+ "to get more details", dic['table'][0]);


"""
This fuction will be removed because all these calls will be reduced and replaced by a single call to another function.
"""
def func02(x):
    y = x[0]
    if y == "user platinum":
        func03(x[1])
    elif y == "user gold":
        func04(x[1])
    elif y == "user silver":
        func05(x[1])
    elif y == "user bronze":
        func06(x[1])


"""
This function will be refactored changing its name and variables to improve readability.
"""
def func01(line):
    x = line.split(";");
    func02(x)


"""
Move the logic to read the file into a new function in a helper module
"""
f = open ("profileDB_id.txt", "r");
Lines = f.readlines()

"""
Wrap this function to avoid execution when the module is imported 
"""
for line in Lines:
    func01(line)