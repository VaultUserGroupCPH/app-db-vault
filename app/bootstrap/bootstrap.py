#from flask import Flask, request, render_template

#import MySQLdb as mdb
#import sys

import hvac
import os

_vault_token = os.environ['VAULT_TOKEN']

def operator_create_token(client):
    try:
        client.create_token(token_id="app-bootstrap-token")
    except hvac.exceptions.InvalidRequest, e:
        print "Something went wrong. (If its a a duplicate ID, I think you will be fine anyways). The error is '%s'" % \
              e.args[0]


def operator_add_credentials_for_db(client):
    try:
        client.write('secret/environment-test', key='value', lease='1h')
    except hvac.exceptions.InvalidRequest, e:
        print "Something went wrong. The error is '%s'" % \
              e.args[0]


if __name__ == "__main__":
    print "Bootstrap vault..."

    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)
    operator_create_token(client)
    #operator_add_credentials_for_db(client)
