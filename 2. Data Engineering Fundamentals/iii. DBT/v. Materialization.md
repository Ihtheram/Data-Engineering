# **dbt** (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**

##  Materializations

dbt models, by default, are materialized as "views" but can be configured with different ones by setting the value for `materialized` configuration parameter in either of the following three ways:

* Project file

  <small> Studio / File explorer / **<project_directory> /** </small>

  ```yaml
  # dbt_project.yml
  name: project_name
  version: 1.0.0
  config-version: 2

  models:
    project_name:
      model_name:
        # materialize all models in models/events as tables
        +materialized: table
  ```

* Property file

  <small> <project_directory> / **models /** </small>
  ```yaml
  # properties.yml
  models:
    - name: model_name
      config:
        materialized: table
  ```

* Model File

  <small> models / **<model_directory> /** </small>
  ```sql
  <!-- [<model_name>].sql -->
  {{ config(materialized = 'table') }}

  <!-- Queries -->
  ```



#### **`materialized`** Options

  1. **`view`** (default) - Creates a database view, runs the model SQL every time the view is queried.

  2. **`table`** - Creates a physical table, data is stored as static rows until the next `dbt run`.

  3. **`incremental`** - Builds a table once, then only processes new or changed data on subsequent runs. Requires defining an unique_key or incremental logic.

  4. **`ephemeral`** - Does not create a table or view, Compiles into CTEs inside downstream models.

  5. **`materialized_view`** - Creates a materialized view if the warehouse supports it (e.g., Snowflake, BigQuery), warehouse automatically refreshes it.


[Materializations documentation](https://docs.getdbt.com/docs/build/materializations?version=1.12)


### Setting up Materialization

* **View**  
  No configuration needed. Every model is, by default, materialized as view.

* **Table**  
  can be set through
  - Project file: Adding `+materialized: table` under <model name> which is under <project name> which is under 'models' keyword.
  - Property file: Adding `materialized: table` under 'config:' under model name.
  - Model File: Setting Materialized to 'table' as the argument for config.
    
* **Incremental  
  can be set through
  
  * Model File

  <small> models / **<model_directory> /** </small>
  ```sql
  <!-- [<model_name>].sql -->
  {{
    config(
      materialized = 'incremental'
      incremental_strategy = 'append'
    ) 
  }}

  with <model_name> as
  (
    <!-- query -->

    {% if is_incremental() %}
    where <datetime_column> > (select max(current_timestamp_column) from {{this}})
    {% endif %}
  )
  
  ```

#### **`incremental_strategy`** Options  
1. `append`