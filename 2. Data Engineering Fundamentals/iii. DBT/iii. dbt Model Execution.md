# dbt (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**

## **dbt** Model Execution

## SQLs
Each .sql file represents one model. dbt uses Jinja to write SQL.

### Jinja
Jinja is a template engine for Python that accomodates embedding logic inside text files.


### Source Data set up on Data Warehouse

* **Snowflake** → Projects → Workspaces → Open or create: [<source_table>.sql]
    - Example Query:
    ```sql
    <!-- <source_table>.sql -->
    create or replace database
      <database>;

    create or replace table
      [<database>.public.<source_table>] (
        id integer,
        name string,
        salary integer,
        hiredate date,
        address string
    );

    INSERT INTO
      [<database>.PUBLIC.<source_table>](id, NAME, SALARY, HIREDATE, ADDRESS) 
    VALUES
        (101, 'Alice Johnson', 72000, '2021-05-14', '123 Maple St, Denver, CO'),
        (102, 'Brian Smith', 85000, '2020-11-02', '45 Oak Ave, Austin, TX'),
        (103, 'Carla Mendes', 93000, '2022-03-28', '789 Pine Rd, Seattle, WA'),
        (104, 'David Lee', 67000, '2019-07-19', '56 Elm Blvd, Chicago, IL'),
        (105, 'Emily Carter', 102500, '2023-01-09', '890 Willow Ln, Boston, MA');

    SELECT * FROM [<database>.PUBLIC.<source_table>];
    ```


### Creating Models and Models Configuration Files
<small>

* **dbt** / Studio /
  - Change Branch / Git Branch → [<feature_branch>]  
  - File explorer / [<project_directory>] / **models** /
    - → Create: [<model_directory>] /
      - → Create: [<model_name>.sql]


</small>


### Model Query  
<small> **dbt** / Studio / File explorer / [<project_directory>] / models / [<model_directory>] / [<model_name>].sql </small>  

#### Using CTE to import table from Data Warehouse
```sql
-- [<model_name>].sql
WITH [<model_name>] AS (

  SELECT * FROM [<db_name>.PUBLIC.<source_table_name>]
)
SELECT * FROM [<model_name>];
```
<small>

* Generates a View by default, to modify see [Materializations](v.%20Materialization.md)
* To see the generated SQL query in dbt that creates a view with the given model_name, go to: **dbt** / Commands / [<model_name>] → Debug logs

* To see the **dbt** generated view in Data Warehouse, go to: Snowflake / Database Explorer / Objects / Filter / [database_name] / PUBLIC / Views / [model_name] → ... / Edit definition

</small>

### Transformation  
Example of transforming source data by splitting some column data into multiple columns.  
```sql
with [<model_name>] as (

    select
        id as emp_id,
        split_part(name, ',', 1) as emp_firstname,
        split_part(name, ',', 2) as emp_lastname,
        salary as emp_salary,
        hiredate as emp_hiredate,
        split_part(address, ',', 1) as emp_street,
        split_part(address, ',', 2) as emp_city,
        split_part(address, ',', 3) as emp_country,
        split_part(address, ',', 4) as emp_zipcode
    from [database].public.[source_table]
)
select * from employee
```

### **dbt** Core Commands
* `dbt run` - runs all models
* `dbt run --select [model name]` - runs a particular model
* `dbt build` - tests models then run if tests pass
* `dbt build --select [model name]`

<small>  

### Access **dbt** models on Snowflake

To check the transformed data in data warehouse go to the source table in Snowflake and add query `SELECT * FROM [database].PUBLIC.[model_name]` or go to:

**Snowflake** / Horizon Catalog / **Catalog** / Database Explorer / [Expand → <database_created_by_current_project>] / PUBLIC / Tables / [model_name] → Data Preview

</small>

### Sources
Sources are dbt’s way to declare and describe the raw data loading into warehouse before dbt touches it.

* the entry point of data pipeline
* a contract describing where raw tables live
* a metadata layer that lets dbt track lineage, freshness, and documentation
* Instead of hardcoding table names like raw_database.public.raw_table directly in SQL files, we can use the source() function.

### How to Define a Source
Sources are defined in .yml files within models/ directory. Here is a basic structure:
```YAML
version: [version]

# models configurations...

sources:
  - name: [model_name]
    database: [database_name]
    schema: PUBLIC
    tables:
      - name: [source_table]

```

### How to Use a Source in SQL
Once defined, you reference the source in your model using the {{ source() }} macro. This creates a dependency in dbt's eyes.

```sql
<!-- models/[model_name].sql -->

select
    id as payment_id,
    amount,
    status
from {{ source('model_name', 'source_table') }}
```

---  


