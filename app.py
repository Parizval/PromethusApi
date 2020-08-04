from flask import Flask, render_template, request, redirect, url_for, session

import process

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"

@app.route('/')
def Home():

    data = process.RenderTable()
    length = len(data)
    print(length)
    return render_template("index.html",data=data,length=length-1)

@app.route('/request', methods=['POST'])
def GetData():
    reponse = {}
    for key,val in request.form.items():
        print(key,val)
        reponse[key] = val+"mod"

    reponse['check'] = True
    return reponse 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)