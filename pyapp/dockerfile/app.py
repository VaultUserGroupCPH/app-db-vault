from flask import Flask
import hvac


app = Flask(__name__)


@app.route("/")
def main():
    print "asdlf"
    return "Welcome!"

@app.route("/read")
def read():
    client = hvac.Client()
    client = hvac.Client(url='http://localhost:8200')
    client = hvac.Client(url='http://localhost:8200', token=os.environ['VAULT_TOKEN'])
    return "Read!"


if __name__ == "__main__":
    print "Hello world"
    app.run(host="0.0.0.0", debug=True)

