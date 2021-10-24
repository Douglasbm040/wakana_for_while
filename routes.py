from flask import Flask , request
#import Untitled4 as bot
import consumir as api

#dados=bot.texto 
app=Flask('webscrape')

#@app.route("/bot",methods=['GET'])

#def bot ( ):
#     return {'html':dados}

@app.route('/buscar',methods=['POST'])
def buscar ():

    jsona=request.get_json()
    return jsona


app.run()
