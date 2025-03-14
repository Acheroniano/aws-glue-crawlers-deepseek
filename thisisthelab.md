## LAB DeepSeekR1 >> AWS S3 >> AWS Glue Crawler >> AWS Glue Database >> AWS Athena >> SQL

<div>
   <a href="https://www.paypal.com/donate/?business=C5ZXDE6A7M28E&no_recurring=0&item_name=Donation+for+Owner+of+this+PayPal+Account&currency_code=BRL" target="_blank">
       <img src="https://www.paypalobjects.com/paypal-ui/logos/svg/paypal-color.svg" alt="PayPal Donation" width="100" height="50">
   </a><br>
   @@@ Doações:<br>Pix: altaperformancenubank@gmail.com<br>
</div>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/f%C3%A1bio-samuel-dos-santos-canedo-2708b533/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Acheroniano)

[![Amazon](https://img.shields.io/badge/Amazon%20Mais%20Vendidos-39E09B?style=social&logo=amazon&logoColor=39E09B)](https://amzn.to/3SYdXzY)
[![Amazon](https://img.shields.io/badge/Amazon%20Ofertas-39E09B?style=social&logo=amazon&logoColor=39E09B)](https://amzn.to/3XbudAb)

<h2> 🤖 Tecnologias utilizadas</h2>

<div>
  <a href="https://www.w3schools.com/aws" target="_new"><img src="https://img.shields.io/badge/aws-239120?style=for-the-badge&logo=aws&logoColor=white" alt="aws link"></a>
  <a href="https://www.w3schools.com/sql" target="_new"><img src="https://img.shields.io/badge/sql-239120?style=for-the-badge&logo=sql&logoColor=white" alt="sql link"></a>
  <!-- <a href="https://www.w3schools.com/js" target="_new"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=blue" alt="html link"></a>
-->
</div>

# 1 - DeepSeekR1

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
##### ** Gerar o conteúdo do arquivo *customer.csv:* ** 
###### - Abra o link *https://chat.deepseek.com/*
###### - Use o prompt providenciado no arquivo *PromptedDeepSeekR1.md* no DeepSeekR1 e espere ele gerar a lista de dados...
###### - Cole no DeepSeekR1 o conteúdo do jeito que você copiar do arquivo [![Markdown badge](https://img.shields.io/badge/PromptedDeepSeekR1.md-%23000000?logo=markdown&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/PromptedDeepSeekR1.md) a AI vai tratar de acordo.
###### - Copie a lista de dados que o DeepSeekR1 gerar e cole em um editor de texto, salve como *customer.csv*, o arquivo será usado em breve.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
##### ** Generate the data for the file *customer.csv:* ** 
###### - Open the url *https://chat.deepseek.com/*
###### - Look at the prompt provided in the file [![Markdown badge](https://img.shields.io/badge/PromptedDeepSeekR1.md-%23000000?logo=markdown&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/PromptedDeepSeekR1.md), copy and paste it in DeepSeekR1, wait it generate the list of data...
###### - Paste the prompt without modifications in DeepSeekR1, the AI will manage it.
###### - Copy the list of data in a text editor and save it as *customer.csv*, it will be used later.

# 2 - Amazon S3 

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
##### ** Abra o Amazon S3 no console da Amazon **

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
##### ** Open the Amazon S3 console **

![S3 Console](./images/1a-S3inConsoleA.jpg)

# 2.1 - Amazon S3 - Create Buckets 

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
##### ** Escolha a Região na AWS para criar dois buckets **
###### Escolha qualquer uma, eu tenho buckets em Ohio e North Virginia 
###### e depois de escolher a região, clique no botão *Create Bucket*
###### crie dois buckets:
###### - um para receber o arquivo [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv)
###### - o segundo bucket irá receber arquivos gerados pelo AWS ATHENA.
###### - usado os nomes : *bucket-for-csv-rawdata-2025-03* e *bucket-for-athena-queries-2025-03*

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
##### ** Choose a AWS Region to create two buckets **
###### I have a couple of buckets in North Virginia and Ohio.
###### after choosing the region, click in the *Create Bucket* button.
###### create two buckets:
###### - one to receive the file [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv)
###### - other will receive files created by AWS ATHENA.
###### - used the names : *bucket-for-csv-rawdata-2025-03* and *bucket-for-athena-queries-2025-03*

![S3 AWS Region](./images/2a-S3Region.jpg)
![S3 Create Bucket](./images/3a-S3CreateABucket.jpg)
![S3 Buckets Names](./images/4a-S3BucketsCriadosX.jpg)

# 2.2 - Amazon S3 Upload [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv)

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
##### ** Clique no botão upload para escolher o arquivo [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) **
###### - depois que escolher o arquivo e também após fazer o upload, algumas informações relevantes sobre ele aparecem na tela.
###### - abra o bucket *bucket-for-csv-rawdata-2025-03* e confira o arquivo [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) salvo no bucket.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
##### ** Click on upload button to choose the file [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) **
###### - after choosing the file and also after uploading, some relevant information appears on the screen.
###### - open the bucket *bucket-for-csv-rawdata-2025-03* and check the file [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) saved in the bucket.

![S3 Upload customer.csv](./images/5a-S3RawDataUpload.jpg)
![S3 Upload customer.csv info](./images/6a-S3CustomerCSV.jpg)
![S3 After Upload customer.csv info](./images/7a-S3CustomerCSVSuccess.jpg)
![S3 customer.csv in the bucket](./images/8a-S3CustomerCSVSuccess2.jpg)

# 3 - AWS Glue 

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Abra o AWS GLUE
###### Abra no menu lateral o item CRAWLERS

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Open the AWS GLUE
###### Open CRAWLERS in lateral menu

![AWS Glue](./images/9a-AWSGlueCalling.jpg)
![AWS Glue Crawlers](./images/10a-AWSGlueCrawlerCalling.jpg)

# 3.1 - AWS Glue - Create Crawler

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Clique em CREATE CRAWLER

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Click CREATE CRAWLER

![AWS Glue Create Crawler](./images/11a-AWSGlueCrawlerScreen.jpg)

# 3.2 - AWS Glue - Crawler Properties

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Preencha as informações para parametrizar o Crawler

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Fill in the information to parameterize the Crawler

![AWS Glue Crawler Properties](./images/12a-AWSGlueCrawlerSetProperties.jpg)

# 3.3 - AWS Glue - Crawler DATA SOURCE Configuration

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Clique no botão *add a Data Source* para poder indicar a fonte dos dados.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Click on the *add a Data Source* button to indicate the data source.

![AWS Glue Crawler Data Source](./images/13a-AWSGlueCrawlerDataSource.jpg)

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Faça a parametrização do *Data Source* com o bucket *bucket-for-csv-rawdata-2025-03*
###### Clique no botão *ADD an S3 data source*. 

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Parameterize the *Data Source* with the bucket *bucket-for-csv-rawdata-2025-03*
###### Click on the *ADD an S3 data source* button. 

![AWS Glue Crawler Parametrization](./images/14a-AWSGlueCrawlerAddDataSource.jpg)
![AWS S3 Bucket as a Data Source](./images/15a-AWSGlueCrawlerDataSource.jpg)

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Confira a parametrização do *Data Source* com o bucket *bucket-for-csv-rawdata-2025-03*

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Check *Data Source* parametrization with the bucket *bucket-for-csv-rawdata-2025-03*

![AWS Glue Crawler with a S3 bucket as Data Source](./images/16a-AWSGlueCrawlerDataSource.jpg)

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Nas configurações de segurança crie uma IAM ROLE para AWS GLUE.
###### Confira as configurações realizadas.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### In security settings create a IAM ROLE for AWS GLUE.
###### Check the settings.

![AWS Glue Crawler IAM ROLE](./images/17a-AWSGlueCrawlerIAMRole.jpg)
![AWS Glue Crawler IAM ROLE Name](./images/18a-AWSGlueCrawlerIAMRoleName.jpg)
![AWS Glue Crawler security settings](./images/19a-AWSGlueCrawlerRoleCreated.jpg)

# 3.4 - AWS Glue - Crawler Database Configuration

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Configuração do *banco de dados* baseado no arquivo [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) salvo no bucket *bucket-for-csv-rawdata-2025-03*.
###### Confira as informações do banco de dados criado.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Database configuration based on the file [![Files badge](https://img.shields.io/badge/customer.csv-%23000000?logo=Files&logoColor=yellow&labelColor=blue)](https://github.com/Acheroniano/aws-glue-crawlers-deepseek/blob/main/customer.csv) saved in the bucket *bucket-for-csv-rawdata-2025-03*. 
###### Check the information about the database creation.

![AWS Glue Crawler Database](./images/20a-AWSGlueCrawlerDataBaseCreation.jpg)
![AWS Glue Crawler Database 2](./images/20a-AWSGlueCrawlerDataBaseCreation2.jpg)
![AWS Glue Crawler Database Created](./images/21a-AWSGlueCrawlerDataBaseCreated.jpg)
![AWS Glue Crawler Database Target](./images/22a-AWSGlueCrawlerDataBaseTargetChoosed.jpg)

# 3.5 - AWS Glue - Create Crawler

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Finalmente revise as configurações e clique em *CREATE CRAWLER*.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Finally review the settings and click on *CREATE CRAWLER*.

![AWS Glue Create Crawler](./images/23a-AWSGlueCrawlerFinalScreen.jpg)

# 3.6 - AWS Glue - Run Crawler

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Clique no botão *RUN CRAWLER* para iniciar a execução do Crawler.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Click on the *RUN CRAWLER* button to start the Crawler execution.

![AWS Run Crawler](./images/24a-AWSGlueCrawlerFinalScreen2.jpg)
![AWS Run Crawler Success](./images/25a-AWSGlueCrawlerRUNSuccess.jpg)

# 3.7 - AWS Glue - Database Tables

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### No menu da esquerda clique em Database e Tables para visualizar informações do banco de dados criado.
###### Clique em *Table data* para invocar o AWS ATHENA e rodar declarações SQL no banco de dados criado.
###### Um alerta será emitido sobre cobranças realizadas pelo AWS ATHENA.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### On the left menu click on Database and Tables to view information about the database
###### Click on *Table data* to invoke AWS ATHENA and run SQL statements in the database.
###### An alert will be emitted about AWS ATHENA charges.

![AWS Glue Database Tables](./images/26a-AWSGlueCrawlerDatabaseTables.jpg)
![AWS Glue Database View Data](./images/27a-AWSGlueCrawlerDatabaseTablesViewData.jpg)

# 4 - AWS Athena

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### o AWS ATHENA irá alertar que precisa de um bucket de saída para salvar os resultados dos SQL Queries realizados.
###### Clique no botão *Edit settings*

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### AWS ATHENA will alert that it needs an output bucket to save the results of the SQL Queries performed.
###### Click on the *Edit settings* button.

![AWS Athena Output query bucket](./images/28a-AWSAthenaOutputQueryResultLocation.jpg)

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Escolha o bucket *bucket-for-athena-queries-2025-03* como destino dos SQL Queries realizados.
###### Confira a escolha e depois clique em *Editor*.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Choose the bucket *bucket-for-athena-queries-2025-03* as the destination of the SQL Queries performed.
###### Check the choice and then click on *Editor*.

![AWS Athena choosing S3 bucket destination for Queries](./images/29a-AWSAthenaChoosingTheOtherBucket.jpg)
![AWS Athena Editor](./images/30a-AWSAthenaChoosingTheOtherBucket.jpg)

# 5 - AWS Athena - SQL Queries

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Em *Editor*, tem o local para editar as declarações SQL, o botão Run e o (+) para criar novas declarações SQL.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### in *Editor*, has a place to edite the SQL statements, the *Run* button and the (+) to create new SQL statements.

![AWS Athena bucket choosed](./images/31a-AWSAthenaChoosingTheOtherBucket.jpg)

### 5.1 - SQL Queries Fun

###### ![Brazil](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/br.png "Brazil") 
###### Agora rode as SQL Queries, modifique elas e execute novamente.
###### Mantenha *"AwsDataCatalog"."customercsv-imperialfiles"."bucket_for_csv_rawdata_2025_03"* na sua declaração e execute.
###### Peça auxílio a alguma AI para gerar SQL Queries mais complexas, se for o caso.

###### ![United States](https://github.com/Acheroniano/flag-icon/blob/master/png/16/country-4x3/us.png "United States") 
###### Now run the SQL Queries, modify them and execute again.
###### Keep *"AwsDataCatalog"."customercsv-imperialfiles"."bucket_for_csv_rawdata_2025_03"* in your declaration and execute.
###### Get help from a AI to generate more complex SQL Queries, if necessary.

![AWS SQL Queries](./images/32a-AWSAthenaChoosingTheOtherBucket.jpg)
![AWS SQL Queries](./images/33a-AWSAthenaChoosingTheOtherBucket.jpg)
![AWS SQL Queries](./images/34a-AWSAthenaChoosingTheOtherBucket.jpg)
![AWS SQL Queries](./images/35a-AWSAthenaChoosingTheOtherBucket.jpg)

# The END!

