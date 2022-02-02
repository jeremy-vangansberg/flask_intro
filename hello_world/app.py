from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return render_template('hello_world.html')
 
if __name__ == "__main__":
    app.run(port=5000)