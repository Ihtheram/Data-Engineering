# dbt (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**

## Setting Up **dbt** with **Snowflake**

### Snowflakes partner connect with **dbt**
1. **Snowflakes**
    - → Admin
        - → Partner Connect
            - → **dbt**
2. Complete Registration steps
3. **dbt**
    - → Studio
        - → Version Control
            - → **Initialize dbt project**
            - → Commit to new branch

4. Upgrade to a plan
    - **dbt**
        - → [Profile Name]
            - → Your Profile
                - → Settings
                    - → Billing
                    - → Select Plan
                        - → [Select a plan]
                        - → Switch to [PlanName]

### **dbt** Cloud Overview
1. Dashboard
    - Recent activity → View run history
    - Models built by month
    - Deployment environments
2. **Studio**
    - → Version control
    - → File explorer
3. Canvas: GUI that can be used to develop, test and deploy models
4. **Orchestration** 
    - → Runs: History of all the executed jobs
    - → Jobs
    - → Environments
        - → Deployments
        - → Developments
    - → Data sources
5. Documentation

### Updating **dbt**'s Default Credentials 
* **Snowflake**
    - [profile name]
        - Account → [account name]
            - View account details
                - Account → Copy **Account Identifier**

    - Manage → Compute
        - Warehouses → Copy a **warehouse name** e.g. COMPUTE_WH

    - Horizon Catalog → Catalog
        - Database Explorer
            - **+ Database**
        - Governance & Security → Users & roles
            - roles → Copy a **role** e.g. ACCOUNTADMIN (super user)
    
    - Work with data → Projects
        * My Workspace
            - **+ Add new**
                - SQL File → 'DBT.sql'
                    - Query:
                    ```postgresql
                    CREATE OR REPLACE DATABASE DBT_DB;
                    ```
                    → Copy **database name**


* **dbt**
    * [Profile Name]

        - Your Profile → Credentials
            - Project: "Partner Connect Trial"
    
                - Connection Details   
                    - Connections → snowflake → Edit
                        - Settings
                            - Account → Paste **Account Identifier**
                            - Database → Paste **database name** e.g. DBT_DB
                            - Warehouse → Paste **warehouse name** e.g. COMPUTE_WH
                        - Optional Settings
                            - Role → Paste **role** e.g. ACCOUNTADMIN (super user)
                    
                - → Save → Continue
                
        - Your Profile → Credentials
            - Project: "Partner Connect Trial" → Edit
                
                - Connection Details
                    - Role → Paste **role** e.g. ACCOUNTADMIN (super user)
                    - Database → Paste **database name** e.g. DBT_DB
                    - Warehouse → Paste **warehouse name** e.g. COMPUTE_WH

                - Development credentials
                    - Auth method: Username and password
                    - Username: [Snowflake account Username]
                    - Password: [Snowflake account Password]
                    - Schema: PUBLIC
                    - → Test connection
                
                - → Save