# Data Engineering Fundamentals
Documentation on Data Engineering Fundamentals


**[⇐ Data Engineering](../README.md)**

* [Python Automation](./Python%20Automation/ii.%20Python%20Automation.md)
* [DBT (Data Build Tool)](./iii.%20DBT.md)


## Data Engineering Fundamentals

* Database
* Data Lake → raw landing zone
* Data Lakehouse / Warehouse → cleaned, modeled data
* Data Marts → business‑friendly analytics layer

### Data
A collection of a distinct small unit of information e.g. text, numbers, media, bytes etc.

#### Types of Data
* Structured - stored in a standardized format like rows and columns, e.g. SQL databases, Exel files etc.
* Semi-structured - uses **tags** or **markers** to define elements, fields, and records, e.g. XML, JSON
* Unstructured - unorganized, e.g. no-SQL databases, document files, images, audio, video etc.

### Database
An organized collection of data stored in a computer system managed by a database management system (DBMS). Most commonly used are:
* Relational Databases
* No-SQL Databases

## Data Warehouse

A centralized relational database system that can bring, store, and handle large structured data sets from multiple sources so that organizations can run analytics, reporting, and business intelligence on top of it.

Common Warehouse Technologies:
* **Snowflake**
* Amazon **Redshift**
* Google **BigQuery**
* Azure **Synapse Analytics**
* Databricks **SQL Warehouse**

## Data Mart
A subset of structured data from data warehouse, optimized for fast access and simpler analytics for a particular group such as Sales, Marketing, Finance, HR, Operations

It contains only the data that department needs, structured in a way that makes their reporting and analysis easier.

## Data Lake
A centralized repository that stores structured, semi‑structured, and unstructured data in its original format and at any scale.

* **Snowflake**
* Amazon **S3 Bucket**
* Google **BigQuery**
* Azure **Data lake**
* **Databricks**
* ADLS
* GCS