backend "file" {
  path="./vault_backend/"
}

disable_mlock = true

listener "tcp" {
 address = "127.0.0.1:8200"
 tls_disable = 1
}
