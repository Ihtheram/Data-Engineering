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


