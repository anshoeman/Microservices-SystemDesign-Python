import jwt ,os,datetime
from flask import Flask,request
from flask_mysqldb import MySQL
#we use from and import with the help of from and import keywords

server = Flask(__name__)#__name__ is a special variable
mysql = MySQL(server)   #establish connection with mysql server

#config the database with the server
server.config["MYSQL_HOST"]='localhost'
server.config["MYSQL_USER"]='localhost'
server.config["MYSQL_PASSWORD"]='localhost'
server.config["MYSQL_DB"]='localhost'
server.config["MYSQL_PORT"]='localhost'
#print the values server.config value
print(server.config["MYSQL_HOST"])


#create routes for the server

@server.route("/login",methods=['POST'])
def login():
    auth=request.authorization
    if not auth:
        return "missing creadentials",401
    
    #check db username and password
    
