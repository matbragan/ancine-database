# Criação do Github Action

Esse workflow tem como funcionalidade o deploy automático no ambiente produtivo - EC2, orquestrador do projeto.

### Construção
Com o EC2 já criado e configurado, é necessário criar os segredos de repositório (repository secret) no repositório do projeto no GitHub.   
Os segredos necessários são:
- **EC2_USER** - nome do usuário no EC2, caso tenha usado o mesmo ami padrão do projeto provavelmente esse valor será ubuntu.
- **EC2_HOST** - ip público da instância criada no EC2.
- **EC2_SSH_KEY** - chave ssh privada criada para a construção da instância.