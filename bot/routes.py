from flask import Flask , request
from webbot import web



dados= web()
app=Flask('webscrape')

#@app.route("/bot",methods=['GET'])

#def bot ():
#      return {'html':dados}

@app.route('/buscar',methods=['POST'])
def buscar ():
    
    jsona=request.form['local']
    essavai= web(jsona)
    return essavai


app.run()