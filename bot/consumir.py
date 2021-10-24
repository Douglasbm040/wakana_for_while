# import requests

# def buscar_dados():
#     request = requests.get("http://127.0.0.1:5000/")
#     print(request.content)


# from flask import Flask , request
# from Untitled4 import
# import consumir as api

# dados= bot()

# app=Flask('webscrape')

# @app.route("/bot",methods=['GET'])

# def bot ( ):
#      return {'html':dados.texto}

# #@app.route('/buscar',methods=['POST'])
# #def buscar ():
# #    
# #    jsona=request.form['local']
# #    essavai=bot.web()
# #    return essavai
# #

from flask import Flask , request
import webbot as bott
import consumir as api

 
app=Flask('webscrape')
@app.route('/buscar',methods=['POST'])
def buscar ():

    jsona=request.form['local']
    bot()
    return essavai


@app.route("/bot",methods=['GET'])

def bot ( ):
     return {'html':bott.texto}




app.run()
