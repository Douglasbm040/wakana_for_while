from flask import Flask , request
from webbot import web

app=Flask('webscrape')

@app.route('/service/<local>',methods=['GET'])

def service (local):
    data = web(local)
    return data

app.run()