# app-db-vault
An application that connects to the database using credentials provided from Vault. Thats it.

The setup is not quite there yet. Sofar this is what happens:

1. Vault starts 
2. A bootstrap app simulates the creation of an initial Vault Token, that is provided to the "next"
app via env. var APP_BOOTSTRAP_TOKEN
3. A web app reads the APP_BOOTSTRAP_TOKEN and fetches an initial value from vault with it.



# Prerequisites
docker-compose.
On ubuntu (check dockers homepage)
```
sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

## First time setup

```
docker-compose up
docker-compose down
```
This will start a vault container and some more components.

You can test that vault is running with

```
docker exec appdbvault_main-secrets_1 vault status
```
or, if you have vault installed on you machine
```
export VAULT_ADDR='http://0.0.0.0:8200'
vault status
```

You should get some output along the lines of
```
Sealed: false
Key Shares: 1
Key Threshold: 1
Unseal Progress: 0
Unseal Nonce: 
Version: 0.9.5
Cluster Name: vault-cluster-d9f333db
Cluster ID: 08acf8fd-d81d-0a87-caa6-ce53fba89e54

High-Availability Enabled: false
```

and check out
```
http://localhost:8080/
```
to see something along the lines of **Welcome to Vault Hackathon"**


# First time
## Not used
In the first version of this POC some hand-scripting was added to unseal the vault.
The current version runs vault in "dev" mode. In dev mode the vault is unsealed pr. default
so its not needed to run this at the moment

vault/unseal-vault.sh

