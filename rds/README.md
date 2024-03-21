# Criação do Banco de Dados no RDS

### Requerimentos
- [Terraform instalado](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Conta na AWS](https://aws.amazon.com/pt/)
- [Credenciais configuradas no AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

### Construção
#### Criar um arquivo `.tfvars` com a senha do banco, como no exemplo abaixo:
~~~tfvars
db_password = "<password>"
~~~

#### Criar o banco:
~~~sh
terraform init
terraform apply
~~~