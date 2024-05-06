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
terraform apply -var-file="secrets.tfvars"
~~~

> ⚠️ **IMPORTANTE**  
> Para testes locais esse plano do terraform já visa a liberação do ip público local (máquina que está rodando-o). Em casos em que o ip público local foi redefinido, por exemplo ao reiniciar a máquina, é necessário rodar `terraform apply` novamente, para assim ser atualizado o ip público liberado no banco.