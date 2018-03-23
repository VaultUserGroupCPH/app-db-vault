#from flask import Flask, request, render_template

#import MySQLdb as mdb
import sys

import hvac


def operator_create_token(client):
    try:
        client.create_token(token_id="app-bootstrap-token")
    except hvac.exceptions.InvalidRequest, e:
        print "Something went wrong. (If its a a duplicate ID, I think you will be fine anyways). The error is '%s'" % \
              e.args[0]


def operator_add_credentials_for_db(client):
    try:
        client.write('secret/environment-test/', key='value', lease='1h')


if __name__ == "__main__":
    print "Bootstrap vault..."

    _vault_token = "myroot"
    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)
    operator_create_token(client)
    operator_add_credentials_for_db(client)
