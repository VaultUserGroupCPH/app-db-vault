from flask import Flask, request, render_template
#from flask import request

import MySQLdb as mdb
import sys
import hvac

app = Flask(__name__)
# TODO get this from env var APP_BOOTSTRAP_TOKEN
_vault_token = "app-bootstrap-token"

@app.route("/")
def main():
    return render_template('index.html')

# This is just for fun/demo purposes
@app.route('/read')
def read():
    print "endpoint 'read' called"
    # Check https://github.com/ianunruh/hvac
    #_vault_token = request.args.get('vault_token', 'no-token provide with vault_token=TOKEN')

    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)

    # The keys are stored in a dict. This prints here are provided to give the reader
    #   an idea of how its stored internally in 'hvac'
    print(client.read('secret/foo'))
    print(client.read('secret/foo')['data'])
    print(client.read('secret/foo')['data']['key'])
    value  = client.read('secret/foo')['data']['key']
    return "Read! token is " + _vault_token + " value of foo is " + value # +  client.read('secret/foo')

# This is just for fun/demo purposes
@app.route('/write')
def write():
    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)
    try:
        client.write('secret/foo', key='value', lease='1h')
    except hvac.exceptions.InvalidRequest, e:
        print "Something went wrong. The error is '%s'" % \
          e.args[0]

    return 'wrote value'

# This is just for fun/demo purposes
@app.route('/delete')
def delete():
    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)
    client.delete('secret/foo')
    return 'Deleted value'


@app.route('/connect')
def connect():
    # TODO get the credentials from Vault
    try:
        con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
        cur = con.cursor()
        cur.execute("SELECT VERSION()")

        ver = cur.fetchone()

        print "Database version : %s " % ver

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

if __name__ == "__main__":
    print "Loading app ..."
    write()

    app.run(host="0.0.0.0", debug=True)
