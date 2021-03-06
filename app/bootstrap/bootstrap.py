# from flask import Flask, request, render_template

# import MySQLdb as mdb
# import sys
import time
import hvac
import os

_vault_token = os.environ['VAULT_TOKEN']
_mysql_root_password = os.environ['MYSQL_ROOT_PASSWORD']


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

# In this case, secret backend does not mean that secret data is stored in PosgreSQL/MySQL.
#  It means that Vault can create (and revoke) users for databases on demand.
def operator_setup_mysql_backend(client):
    client.enable_secret_backend('mysql')
    client.enable_secret_backend('mysql', mount_point='jesper')
    # I magically know the root password to make this work. I think its possible to do this without ever knowing the
    #   password (its about parsing the output when creating a mysql db, and get the password there)
    client.write('mysql/config/connection', connection_url="root:%s@tcp(main-db:3306)/" % _mysql_root_password)
    client.write('mysql/config/lease', lease="5s", lease_max="1h")
    client.write('mysql/roles/readonly',
                 sql="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}';GRANT SELECT ON *.* TO '{{name}}'@'%';")

    client.write('jesper/config/connection', connection_url="root:%s@tcp(main-db:3306)/" % _mysql_root_password)
    client.write('jesper/config/lease', lease="1m", lease_max="1h")
    client.write('jesper/roles/readonly',
                 sql="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}';GRANT SELECT ON *.* TO '{{name}}'@'%';")


if __name__ == "__main__":
    print "Bootstrap vault..."
    # Wait for db to start
    time.sleep(5)
    client = hvac.Client(url='http://main-secrets:8200', token=_vault_token)

    operator_setup_mysql_backend(client)
    operator_create_token(client)
    # operator_add_credentials_for_db(client)
    print "...Vault Bootstrapped"
