# Criação do Banco de Dados no RDS

### Requerimentos
- [Terraform instalado](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Conta na AWS](https://aws.amazon.com/pt/)
- [Credenciais configuradas no AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

### Construção
#### Crie um arquivo `secrets.tfvars` com a senha do banco, como no exemplo abaixo, substituindo \<password> pela senha que deseja:
~~~tfvars
db_password = "<password>"
~~~

#### Crie o banco:
~~~sh
terraform init
terraform apply
~~~