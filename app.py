from flask import Flask, render_template, request, redirect, url_for, session

import process

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"

@app.route('/')
def Home():

    data = process.RenderTable()
    return render_template("index.html",data=data)

@app.route('/request', methods=['POST'])
def GetData():
    data = request.form['name']
    print(data)
    reponse = {}
    reponse['check'] = True
    return reponse 
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)