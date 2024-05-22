# ancine-database

PUC Minas Projeto 4 - Desenvolvimento de um Projeto de Big Data Analytics - 2024/01  

Projeto original utilizando AWS - ambiente produtivo, portanto com um custo monetário atrelado ao seu desenvolvimento.  
Para um desenvolvimento sem custo se vê necessário a troca de hospedagem do banco PostgreSQL e do orquestrador Airflow, respectivamente originariamente hospedados no RDS e EC2 (AWS).

### Arquitetura
<img width="600em" src="doc/architecture.png">

## Passos para Construção do Projeto

### Infraestrutura

Para construção e funcionamento do projeto primeiro precisamos criar e configurar sua infraestrutura, por padrão o projeto está utilizando produtos da AWS, como EC2 e RDS.   
Para o desenvolvimento da infraestrutura:

1. [EC2](https://github.com/matbragan/ancine-database/tree/main/terraform/ec2)
2. [RDS](https://github.com/matbragan/ancine-database/tree/main/terraform/rds)
3. [GitHub Action](https://github.com/matbragan/ancine-database/tree/main/.github/workflows)