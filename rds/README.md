# Criação do Banco de Dados no RDS

### Requerimentos
- [Terraform instalado](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Conta na AWS](https://aws.amazon.com/pt/)
- [Credenciais configuradas no AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

### Construção
#### Criar um arquivo chamado `variables.tf` com a senha do banco, como no exemplo abaixo, trocando o `<password>` pela senha:
~~~tf
variable "password" {
    type    = string
    default = "<password>"
}
~~~
#### Criar o banco:
~~~sh
terraform init
terraform apply
~~~