from flask import Flask

app = Flask(__name__)
@app.route("/")
def samplefunction():
    return "Sample output"
print(samplefunction())

