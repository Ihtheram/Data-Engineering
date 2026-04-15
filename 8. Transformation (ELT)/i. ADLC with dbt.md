# dbt (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**

## ETL & ELT

* **Extract**: Data is collected from various sources, often in unstructured or semi-structured formats.
  <small>
  - Managed ELT/ETL Connectors:	**Fivetran**
  - Open‑source ingestion: **Airbyte**
  - Streaming ingestion:	**Kafka**, Kinesis, Pub/Sub  
  </small>
* **Load**: The data is loaded into a data warehouse.
<small>  
  - Warehouse: **Snowflake**, **BigQuery**, Redshift
  - Lakehouse: **Amazon S3**, Google Cloud Storage, Azure Data Lake Storage
  - Orchestration for loading: **Airflow**, Dagster, Prefect
</small>

* **Transform**: The data undergoes a transformation process, cleaning, formatting, and structuring it for analysis.  
<small>  
  - ELT (in‑warehouse SQL transforms): **dbt**, SQL (Snowflake/BigQuery/Redshift), LookML
  - ETL (compute outside warehouse): **Apache Spark**, PySpark, Databricks, AWS Glue
  - Streaming transforms: Kafka Streams, Spark Streaming, Flink
  - Orchestration for transforms: **Airflow**, Dagster, Prefect  
</small>



### Naming Conventions 
In working on this project, we established some conventions for naming our models.

* **Sources** (`src`) refer to the **raw table data** that have been *built in the warehouse through a loading process*.  

* **Staging** (`stg`) refers to models that are built directly on top of sources. These have a one-to-one relationship with sources tables. These are used for *very light transformations* that shape the data into what you want it to be. These models are used to clean and standardize the data before transforming data downstream. *Note: These are typically materialized as views*.

* **Intermediate** (int) refers to any **models that exist between final fact and dimension tables**. These should be built on staging models rather than directly on sources to leverage the data cleaning that was done in staging.

* **Fact** (`fct`) refers to any data that represents something that occurred or is occurring. Examples include **sessions, transactions, orders, stories, votes**. These are typically skinny, long tables.

* **Dimension** (`dim`) refers to data that represents a person, place or thing. Examples include **customers, products, candidates, buildings, employees.**  

<small> Note: The Fact and Dimension convention is based on previous normalized modeling techniques. </small>  

### Reorganize Project  
- When dbt run is executed, dbt will automatically run every model in the models directory.
- The subfolder structure within the models directory can be leveraged for organizing the project as the data team sees fit.
- This can then be leveraged to select certain folders with dbt run and the model selector.
- Example: If dbt run -s staging will run all models that exist in models/staging. (Note: This can also be applied for dbt test as well which will be covered later.)
- The following framework can be a starting part for designing your own model organization:
- Marts folder: All intermediate, fact, and dimension models can be stored here. Further subfolders can be used to separate data by business function (e.g. marketing, finance)
- Staging folder: All staging models and source configurations can be stored here. Further subfolders can be used to separate data by data source (e.g. Stripe, Segment, Salesforce). (We will cover configuring Sources in the Sources module)