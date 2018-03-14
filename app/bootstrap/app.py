#from flask import Flask, request, render_template

#import MySQLdb as mdb
import sys

import hvac

if __name__ == "__main__":
    print "Bootstrap vault..."

    _vault_token = "myroot"
    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)
    try:
        client.create_token(token_id="app-bootstrap-token")
    except hvac.exceptions.InvalidRequest, e:
        print "Something went wrong. (If its a a duplicate ID, I think you will be fine anyways). The error is '%s'" % e.args[0]
