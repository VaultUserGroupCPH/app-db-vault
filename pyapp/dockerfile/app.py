import os

import hvac

# Using plaintext
client = hvac.Client()
client = hvac.Client(url='http://localhost:8200')
client = hvac.Client(url='http://localhost:8200', token=os.environ['VAULT_TOKEN'])

## Using TLS
#client = hvac.Client(url='https://localhost:8200')
#
## Using TLS with client-side certificate authentication
#client = hvac.Client(url='https://localhost:8200',
#                     cert=('path/to/cert.pem', 'path/to/key.pem'))
#