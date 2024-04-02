from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def some():
    return render_template('index.html')



@app.route("/get")
def getHello():
        return "Welcome here"

if __name__ == "__main__":              
    app.run(debug=True)




