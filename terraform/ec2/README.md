# Criação da orquestração do Airflow no EC2

Ambiente onde teremos nosso orquestrador Airflow funcionando.

### Requerimentos
- [Terraform instalado](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Conta na AWS](https://aws.amazon.com/pt/)
- [Credenciais configuradas no AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

### Construção
#### Crie uma chave ssh na sua máquina caso ainda não tenha
Para criação da instância no EC2 está sendo utilizada a chave ssh da máquina host do projeto.   
Se necessário utilize essa [doc de ajuda do GitHub](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux) para criar a chave ssh.   
Após a criação da chave talvez seja necessário alterar o valor da variável ssh_public_key no arquivo `variables.tf`

#### Crie a instância
~~~sh
terraform init
terraform apply -var-file="secrets.tfvars"
~~~

> ⚠️ **IMPORTANTE**  
> Para testes locais esse plano do terraform já visa a liberação do ip público local (máquina que está rodando-o). Em casos em que o ip público local foi redefinido, por exemplo ao reiniciar a máquina, é necessário rodar `terraform apply` novamente, para assim ser atualizado o ip público liberado no banco.