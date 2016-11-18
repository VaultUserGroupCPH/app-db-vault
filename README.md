# app-db-vault
An application that connects to the database using credentiels provided from Vault. Thats it.

## First time setup


docker-compose down
docker build -t pyappbacking pyappbacking
docker build -t pyapp pyapp/dockerfile
docker-compose up
vault/unseal-vault.sh

