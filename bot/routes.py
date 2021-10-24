from flask import Flask , request
import webbot as botmaps
import consumir as api


dados=bot.texto

app=Flask('webscrape')

@app.route("/bot",methods=['GET'])

def bot ( ):
      return {'html':dados}

@app.route('/buscar',methods=['POST'])
def buscar ():
    
    jsona=request.form['local']
    essavai=bot.web()
    return essavai


app.run()