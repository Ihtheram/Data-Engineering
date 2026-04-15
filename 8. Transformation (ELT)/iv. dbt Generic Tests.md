# **dbt** (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**


## **dbt** Generic Tests

### Default Generic Tests

dbt has four built-in data tests
* `unique`: the order_id column in the orders model should be unique
* `not_null`: the order_id column in the orders model should not contain null values
* `accepted_values`: the status column in the orders should be one of 'placed', 'shipped', 'completed', or 'returned'
* `relationships`: each customer_id in the orders model exists as an id in the customers table (also known as referential integrity)


Example:
```yaml
models:
    
  - name: orders    
    columns:
      
      - name: order_id
        data_tests:
          - unique
          - not_null
      
      - name: status
        data_tests:
          - accepted_values:
              
              arguments: -- # available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.
                
                values: ['placed', 'shipped', 'completed', 'returned']
                
                config:
                  severity: warn
      
      - name: customer_id
        data_tests:
          - relationships:
              
              arguments:
              
                to: ref('customers')
                
                field: id
                
                config:
                  severity: error
                  error_if: ">1000"
                  warn_if: ">10"
```

### Severity
* `severity`: `error` or `warn` (default: `error`)
* `error_if`: conditional expression (default: `!=0`)
* `warn_if`: conditional expression (default: `!=0`)

[Default Generic Tests documentation](https://docs.getdbt.com/docs/build/data-tests?version=1.12)


### Custom Generic Tests
<small>

* **dbt** → Studio → File explorer → [<project_folder>] → tests → Create directory: generic → Create file: [test_<test_name>.sql]

</small>
 
**Example Test:**

Query:
```sql
-- test_[test_name].sql
{% test [<test_name>](model, column_name) %}

select *
from
  {{ [<model>] }}
where
  {{ [<column_name>] }} < 1000 
 ```

YAML

```yaml

models:
  - name: [<model_name>]
    columns:
      - name: [<column_name>]
        data_tests:
          - [<test_name>]


```

[Custom Generic Tests documentation](https://docs.getdbt.com/best-practices/writing-custom-generic-tests?version=1.12)


### **dbt** Core Command to Run Test
```
dbt test --select [<table_name>]
```