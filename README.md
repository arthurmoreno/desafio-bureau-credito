# Desafio Bureau de Credito

## Problema

Aqui trabalhamos constantemente com grande volume e complexidade de dados. Sabendo disso,
precisamos que você elabore uma solução que ofereça armazenamento, processamento e disponi-
bilização desses dados, sempre considerando que tudo deve estar conforme as boas práticas de
segurança em TI. Afinal, nosso principal ativo são dados sensíveis dos consumidores brasileiros.

## Arquitetura proposta

![Arquitetura](https://github.com/arthurmoreno/desafio-bureau-credito/blob/master/arquitetura.svg)

## Armazenamento

### Base A

#### Descrição
A primeira delas, que chamamos de Base A, é extremamente sensível e deve ser protegida com os maiores níveis de segurança, mas o acesso a esses dados não precisa ser tão performática.

#### Dados:
* CPF
* Nome
* Endereço
* Lista de dívidas

* Como acessar de maneira extremamente segura?

#### Segurança

Iniciei minha pesquisa para escolher a arquitetura da base de dados A, pesquisando sobre segurança de dados e dados sensiveis na web. Essa pesquisa inicial me trouxe muitas informações essenciais e deixou o assunto mais claro (?). Ela elucidou os principais pontos fracos na segurança de dados e também deixou claro as principais medidas utilizadas pelas empresas para garantir a segurança dos dados. Abaixo um resumo das principais informações obtidas nessa primeira etapa.

-->> Pesquisa inicial na web

    --> Top 10 considerations when choosing a Database Management system
    https://datahq.co.uk/knowledge-centre/blog/top-10-considerations-when-choosing-a-database-management-system

    (...)
    3) Security
    It is important to consider both the physical risk to data (e.g. the risk from fire, theft, etc.) and the risks from hacking, or from unintentional corruption of data through human error. Any system you implement must address the issue of keeping your data secure.

    --> Top five database security threats
    https://www.imperva.com/Resources/Whitepapers/top-5-database-security-threats

    1. Excessive, Inappropriate and Unused Privileges
    2. Privilege abuse
    3. Insufficient Web Application Security
    4. Weak audit trails
    5. Unsecured storage media

    --> 7 Database Security Best Practices
    https://www.esecurityplanet.com/network-security/6-database-security-best-practices.html

    1. Ensure Physical Database Security
    2. Use Web Application and Database Firewalls
    3. Harden Your Database to Fullest Extent Possible
    4. Encrypt Your Data
    5. Minimize Value of Your Database
    6. Manage Database Access Tightly
    7. Audit and Monitor Database Activity

Apesar dessa pesquisa ter ajudado em como deixar a sua aplicação mais segura e como utilizar melhor os recursos de um banco de dados, ela não deixava claro como efetuar uma boa escolha em relação a qual Sistema de Gerenciamento de Banco de Dados (DMS) utilizar. Por essa razão comecei a realizar outra pesquisa para responder a outra pergunta:

 - Como escolher uma base de dados (DMS) para dados sensíveis? pagina 31

Após passar algum tempo pesquisando comparações na internet sobre os diversos sistemas de banco de dados disponíveis no mercado e na comunidade. Percebi que posts de usuários na internet muitas vezes não são conclusivos e as vezes tendenciosos. (Nesse ponto havia escolhido o OracleDB para a Base de dados A)

    --> A Oracle foi Declarada Líder em Segurança de Banco de Dados
    https://www.oracle.com/br/database/security/index.html

    --> SQLite vs MySQL vs PostgreSQL: A Comparison Of Relational Database Management Systems
    https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems

    --> MySQL vs Oracle
    https://itxdesign.com/mysql-vs-oracle/

Felizmente após realizar uma busca um pouco mais extensa sobre o assunto na internet, descobri o livro 'Database Hacker's Handbook' em uma resposta no stackoverflow
    --> PostgreSQL's Security Compared to MySQL, etc
    https://stackoverflow.com/questions/6475228/postgresqls-security-compared-to-mysql-etc

--=== Continuar a redação desta parte ===--

* quantidade de issues de segurança em cada DMS
* diferentes DMS foram analisadas de formas diferentes, algumas estão a mais tempo no mercado e foram analisadas por mais estudos. Além disso cada uma delas tem falhas diferentes das outras, 
* As métricas, critérios e condições para avaliar qual a base de dados mais segura são quase infindaveis e pode ser perigoso tomar uma decisão sobre qual a melhor base de dados num contexto geral pode ser perigoso
* Finalmente, quanto mais você sabe sobre um sistema, melhor você será capaz de torna-lo seguro.
* Por fim, a base de dados mais segura é aquela que você mais tem conhecimento e experiência!


    --> Leveis de segurança do postgres
    https://www.postgresql.org/docs/7.0/static/security.htm


#### Detalhes de acesso a base

A base precisa ser extremamente segura!!! Não precisa de performance.

A base A somente poderá ser acessada de determinados hosts com ips cadastrados no banco(?). Os microserviços e nano-serviços que acessarem a base A deverão estar devidamente cadastrados.

Além disso as ROLES desses serviços devem ser bem restritas ao seu uso. Não conceder permissões desnecessárias.
Desenvolvedores não devem possuir acesso total a base de dados A. Apenas as aplicações que as consomem devem possuir esse acesso. (-- como garantir que isso ocorra na prática ? --)

O acesso a base de dados A deverá ser monitorado (em dashboards ou relatórios) para permitir aos responsaveis da base de dados A poder conferir se os acessos à ela estão sendo condizentes com o uso pelos micro serviços.

Como administrar USERs e ROLEs em um banco de dados seguro?

Proteger a base de dados A de SQL Injection e Web shell (Para evitar web shell proteger as credenciais das aplicações que consomem a base de dados A).

Auditoria da base de dados A!!! (diferencial) de preferencia a auditoria da base deve ficar separada do servidor da aplicação. Garantir o entendimento dos dados e informações providas pelas ferramentas de auditoria de bases.

Aplicação de normas de segurança ----- ISO/IEC 27000
    links:
        http://www.iso27001security.com/html/27000.html
        http://standards.iso.org/ittf/PubliclyAvailableStandards/c073906_ISO_IEC_27000_2018_E.zip (donwload da mais recente)
        https://www.portalgsti.com.br/2013/12/as-normas-da-familia-iso-27000.html (diferenças entre as familias)

Qual das variações da norma utilizar?
O texto e leitura é muito extenso, como referenciar a norma ou utilizar RAPIDO?
        como extrair informações uteis em pouco tempo da norma para aplicar conceitos no desafio?


#### Escolha:
* PostgreSQL

### Base B

A segunda, é a Base B que também possui dados críticos, mas ao contrário da Base A, o acesso precisa ser um pouco mais rápido. Uma outra característica da Base B é que além de consultas ela é utilizada para extração de dados por meio de algoritmos de aprendizado de máquina.

#### Dados:
O segundo, acessa a Base B que contém dados para cálculo do Score de Crédito. O Score
de Crédito é um rating utilizado por instituições de crédito (bancos, imobiliárias, etc) quando
precisam analisar o risco envolvido em uma operação de crédito a uma entidade.
* Idade
* Lista de bens (Imóveis, etc)
* Endereço
* Fonte de renda

#### Escolha:
* MySQL

MySql possui segurança e é mais rápido do que Postgres
Postgres é lento (1)
Elastic search não prove funcionalidades de segurança (2)

    -links:
        1 - https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems

        2 - https://www.quora.com/Why-shouldnt-I-use-ElasticSearch-as-my-primary-datastore


### Base C

A última base, é a Base C, que não possui nenhum tipo de dado crítico, mas precisa de um acesso
extremamente rápido.

#### Dados:
O último serviço, acessa a Base C e tem como principal funcionalidade, rastrear eventos rela-
cionados a um determinado CPF.
* Última consulta do CPF em um Bureau de crédito.
* Movimentação financeira nesse CPF.
* Dados relacionados a última compra com cartao de crédito vinculado ao CPF.

#### Escolha:
* MongoDB

#### Motivo:
Por se tratar de alta velocidade de acesso aos dados e não necessitar de segurança nos dados. Além de possuir familiaridade com a ferramenta.

    --> MongoDB vs MySQL Comparison: Which Database is Better?
    https://hackernoon.com/mongodb-vs-mysql-comparison-which-database-is-better-e714b699c38b

    --> Evaluating NoSQL performance: Which database is right for your data?
    https://jaxenter.com/evaluating-nosql-performance-which-database-is-right-for-your-data-107481.html

## Trafego

### Micro Serviço A

O papel do micro serviço A é acessar a base de dados A e realizar todo tipo de autenticação complicada que precise ser feita. Para fornecer dados em shemas padronizados, no formato de payloads. Dessa maneira cria-se uma camada de abstração para que a aplicação web apenas consuma essas informações sem ter que lidar com gerenciamento do tráfego e com questões de segurança.

### Micro Serviço B

O papel do micro serviço B é consumir os dados da base B e realizar o cálculo do Score. Fornecendo apenas o ultimo para a camada da aplicação. O cálculo do Score deverá ser realizado por uma lib externa, para simular a proteção do conhecimento necessário para realizar essa operação. Para entregar a informação do score de maneira otimizada uma cache será utilizada

### Micro Serviço C

O micro serviço C deve ser capaz de condensar todas as informações referentes a um CPF em um único payload para que seja consumido pela camada da aplicação.

## Disponibilização dos Dados

Inicialmente imaginei uma solução em django com uma logica que iria atualizar uma quarta base de dados (base D). Essa quarta base de dados se comportaria como uma cache. Quando um dado fosse solicitado pelo front-end a aplicação django iria verificar a existencia do mesmo na quarta base (através do ORM do django), e caso o dado não existisse ele deveria ser solicitado aos micro-serviços. Porém ao pesquisar se existia algum tipo de pacote que resolvesse o problema, percebi que essa solução poderia ser bastante lenta, pois o front-end estaria aguardando a atualização dos dados na base de dados D.
Após isso imaginei em algum pacote que realizasse algum tipo de ORM que consumisse APIs. Porém após achar uma biblioteca um pouco desatualizada,
    --> django-wham
    https://github.com/mbylstra/django-wham

me deparei com uma resposta no stackoverflow que indagava se o django era o melhor framework no caso de consumir dados apenas de APIs.
    --> Django models using API instead of database
    https://stackoverflow.com/questions/44730317/django-models-using-api-instead-of-database/44736662#44736662

Talvez a melhor solução fosse utilizar algum framework que utiliza-se javascript. Mas qual deles? Após analisar algumas tendencias e dar uma olhada rápida na comparação entre vue vs react que existe no site do vue.js.

    --> Top JavaScript Libraries & Tech to Learn in 2018
    https://medium.com/javascript-scene/top-javascript-libraries-tech-to-learn-in-2018-c38028e028e6

    --> Comparação com Outros Frameworks
    https://br.vuejs.org/v2/guide/comparison.html

Escolhi fazer a camada de Disponibilização dos Dados com React. Outro fator que influenciou minha decisão foi um projeto que ajudei a desenvolver, onde o front-end consumia os dados de APIs de maneira semelhante.
