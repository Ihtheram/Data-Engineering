# Foundational Tools for Data Engineering
Learning Resources for Mastering Data Engineering Foundations

**[⇐ Data Engineering](../README.md)**

* [Python](./i.%20Python.md)
* [SQL](./ii.%20SQL.md)
* [Git & GitHub](./iii.%20Git%20&%20GitHub.md)

------------------------------
## Data Pipeline (The "Umbrella" Term)
A data pipeline encompasses any series of automated processes that move data. It can handle structured, semi-structured, and unstructured data. Pipelines can be used to stream real-time data, sync APIs, back up data, or feed machine learning models. Both ETL and ELT are types of data pipelines, but a pipeline itself doesn't require a transformation step. [1, 2, 3, 4, 5] 

### Tools used to build Data Pipelines & Orchestration Tools
When building end-to-end data pipelines, you need a "brain" to orchestrate the entire workflow—scheduling tasks, managing dependencies, and sending alerts if a step fails.

* Apache Airflow: The global standard for workflow orchestration, allowing engineers to write pipelines as Python code (Directed Acyclic Graphs, or DAGs).
* Prefect: A modern, lightweight competitor to Airflow designed for simpler Python setup and faster real-time data handling.
* Apache Kafka: The industry standard for continuous, real-time streaming data pipelines rather than scheduled batch loads.

## ETL (Extract, Transform, Load)
In ETL, data is cleaned, filtered, and restructured (transformed) before it gets saved into its final destination (such as a data warehouse). [5] 

* Process: Data is extracted from sources $\rightarrow$ transformed on a separate processing server $\rightarrow$ loaded into the destination.
* Best For: Strict compliance requirements (e.g., stripping out PII before it lands in storage), structured data environments, and conserving target-database compute power. [5, 6, 7]



### Tools used to build ETL pipelines
Traditional ETL tools are used when data must be modified before reaching its destination, often for legacy systems, strict on-premise governance, or intensive pre-processing.

* Informatica PowerCenter: The long-standing enterprise giant for on-premise, enterprise-grade ETL pipelines.
* Talend Open Studio: A hybrid data integration tool offering powerful, drag-and-drop graphical interfaces for complex workflows.
* AWS Glue: A fully managed, serverless Spark-based ETL service used to prepare and load data specifically within the Amazon Web Services ecosystem.

## ELT (Extract, Load, Transform)
In ELT, raw data is loaded directly into the destination first, and all transformations occur inside the destination storage system. [8] 

* Process: Data is extracted $\rightarrow$ loaded into target cloud storage $\rightarrow$ transformed using the data warehouse's own computational power (e.g., using SQL or dbt).
* Best For: Modern cloud data warehouses (like Snowflake, Amazon Redshift, or Google BigQuery), dealing with massive volumes of data, and situations where you want to keep raw data accessible for future, flexible analysis. [6, 8, 9, 10, 11]

### Tools used to build ELT pipelines
Modern cloud data engineering relies heavily on ELT. The industry standard is to separate the Extract/Load (EL) phase from the Transform (T) phase using two distinct types of tools.

#### Data Ingestion (The "EL" Part)
These tools automate pulling raw data from applications, databases, and APIs, and dumping it directly into cloud data warehouses.

* Fivetran: A fully managed SaaS tool with automated, zero-maintenance data connectors.
* Airbyte: The open-source alternative to Fivetran, highly popular for its flexibility and developer-centric customization.

#### Data Transformation (The "T" Part)
Once the raw data is safely inside the cloud warehouse, specialized tools handle the SQL modeling, version control, and data testing.

* dbt (data build tool): The undisputed industry standard for managing SQL transformations, data lineage, and documentation directly inside cloud data warehouses.

------------------------------
## Key Differences at a Glance

| Feature [1, 5, 8, 9, 12] | Data Pipeline | ETL (Extract, Transform, Load) | ELT (Extract, Load, Transform) |
|---|---|---|---|
| Primary Focus | Moving data from A to B. | Modifying and standardizing data. | Storing everything first, modifying later. |
| Transformation Location | Can happen at any point or not at all. | Happens on an external server before loading. | Happens directly inside the data warehouse. |
| Destination Data State | Cleaned or raw. | Always structured and ready to query. | Raw and transformed versions both exist. |
| Scalability | Varies by architecture. | Limited; can become a bottleneck for huge data loads. | Highly scalable; leverages massive cloud compute power. |

[ETL vs ELT: The Real Difference in Modern Data Pipelines](https://www.youtube.com/watch?v=FlLwo99Q568&t=668), YouTube · The Data Signal · 2026 M01 6  

[1] [https://www.youtube.com](https://www.youtube.com/watch?v=nO-VMAzqOV8&t=16)  
[2] [https://medium.com](https://medium.com/@mguanuradha/etl-elt-and-data-pipelines-871b1c708fc7)  
[3] [https://www.rudderstack.com](https://www.rudderstack.com/learn/etl/etl-vs-elt/)  
[4] [https://www.matillion.com](https://www.matillion.com/blog/etl-vs-data-pipeline)  
[5] [https://cribl.io](https://cribl.io/blog/data-pipeline-vs-etl-which-is-best-for-your-data-strategy/)  
[6] [https://aws.amazon.com](https://aws.amazon.com/compare/the-difference-between-etl-and-elt/)  
[7] [https://harshakumavat.medium.com](https://harshakumavat.medium.com/etl-vs-elt-vs-etlt-the-data-pipeline-evolution-you-should-know-6db63cf8dab3)  
[8] [https://rivery.io](https://rivery.io/blog/etl-vs-elt/)  
[9] [https://medium.com](https://medium.com/@rangdalmayura/understanding-etl-and-elt-for-data-pipelines-06496215bd80)  
[10] [https://blog.purestorage.com](https://blog.purestorage.com/purely-technical/etl-vs-elt/)  
[11] [https://peliqan.io](https://peliqan.io/blog/etl-vs-elt/)  
[12] [https://www.reddit.com](https://www.reddit.com/r/dataengineering/comments/1owt21l/is_the_difference_between_etl_and_elt_purely/)  
