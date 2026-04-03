# Data Engineering
Study Materials for Data Engineering

---
**[⇐ Artificial Intelligence](https://github.com/Ihtheram/Artificial-Intelligence)**  

---

## Data Engineering Fundamentals
Data engineering is a blend of machine learning, algorithms, statistics, business intelligence, and programming.

* Database
* Data Lake → raw landing zone
* Data Lakehouse / Warehouse → cleaned, modeled data
* Data Marts → business‑friendly analytics layer

### Processing Data
1. Acquiring Data
2. Storing Data
3. Finding Missing Values
4. Wrangling / Munging Data - Extraction and Cleaning


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


### Data Mart
A subset of structured data from data warehouse, optimized for fast access and simpler analytics for a particular group such as Sales, Marketing, Finance, HR, Operations. It contains only the data that department needs, structured in a way that makes their reporting and analysis easier.

---
### Activate the  following **env** to run an example code
`destudyenv\Scripts\activate`
See [Data Engineering Fundamentals](./2.%20Data%20Engineering%20Fundamentals/README.md)

---
## Data Engineering Learning Roadmap


### [1. **Core Foundations**](./1.%20Core%20Foundations/README.md)
These tutorials introduce key concepts and tools used in modern data pipelines.

| Tutorial | Why It Comes First |
|----------|--------------------|
| [**Data Engineering Fundamentals**](./2.%20Data%20Engineering%20Fundamentals/README.md) | Covers ETL, data modeling, and pipeline architecture. |
| [**Python**](./1.%20Core%20Foundations/i.%20Python.md) | Core language for data engineering, automation, and scripting. |
| [**Python Automation**](./2.%20Data%20Engineering%20Fundamentals/ii.%20Python%20Automation.md) | Applies Python to automate tasks and workflows. |
| [**SQL**](./1.%20Core%20Foundations/ii.%20SQL.md) | Essential for querying and managing relational databases. |
| [**Git & GitHub**](./1.%20Core%20Foundations/iii.%20Git%20&%20GitHub.md) | Version control and collaboration — critical for any engineering workflow. |

---

### [2. **Data Ingestion**](./6.%20Data%20Ingestion/README.md)
Learn how to move data efficiently.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**Fivetran**](./6.%20Data%20Ingestion/i.%20Fivetran.md) | Automates data ingestion from various sources. |

---

### [3. **Data Lake**](./4.%20Cloud%20Platforms%20&%20Infrastructure/README.md)
A centralized repository that stores structured, semi‑structured, and unstructured data in its original format and at any scale. e.g. Amazon S3 Bucket, Azure Data lake, ADLS, GCS

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**AWS S3**](./4.%20Cloud%20Platforms%20&%20Infrastructure/i.%20AWS.md) | Most widely used cloud platform for data engineering. |
| [Azure Data lake](./4.%20Cloud%20Platforms%20&%20Infrastructure/ii.%20Azure.md) | Adds flexibility and multi-cloud experience. |
| [*Terraform*](./4.%20Cloud%20Platforms%20&%20Infrastructure/iii.%20Terraform.md) | Infrastructure as code — automate cloud resource provisioning. |

---

### [4. **Big Data Processing** (Transforming large datasets)](./5.%20Big%20Data%20Processing/README.md)
Handle large-scale data and build insights.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**Spark**](./5.%20Big%20Data%20Processing/i.%20Spark.md) | Distributed computing for big data processing. |
| [Databricks (Spark‑as‑a‑service)](./5.%20Big%20Data%20Processing/ii.%20Databricks%20(Spark‑as‑a‑service).md) | Unified platform for Spark, ML, and analytics. |

---

### [5. **Data Warehouse**](./5.%20Storage%20&%20Warehousing/README.md)
A centralized relational database system that can bring, store, and handle large structured data sets from multiple sources so that organizations can run analytics, reporting, and business intelligence on top of it.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**BigQuery**](./5.%20Storage%20&%20Warehousing/i.%20BigQuery.md)/[**Snowflake**](./5.%20Storage%20&%20Warehousing/i.%20Snowflake.md) | Cloud data warehouse — scalable and fast. |
| [Databricks (Lakehouse)](./5.%20Big%20Data%20Processing/ii.%20Databricks%20.md) | A data lake + data warehouse features on top of it.
---


### 6. **Transformation**
These tutorials introduce key concepts and tools used in modern data pipelines.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**dbt**](./2.%20Data%20Engineering%20Fundamentals/iii.%20DBT.md) | Teaches transformation and modeling in the modern data stack. |

---



### [7. **Orchestration & Workflow Tools**](./3.%20Orchestration%20&%20Workflow%20Tools/README.md)
Learn how to schedule, monitor, and manage data workflows.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [**Apache Airflow**](./3.%20Orchestration%20&%20Workflow%20Tools/i.%20Apache%20Airflow.md) | Industry-standard tool for orchestrating data pipelines. |
| [Jenkins](./3.%20Orchestration%20&%20Workflow%20Tools/ii.%20Jenkins.md) | Useful for CI/CD and automating pipeline deployments. |

---

### [8. Analytics Tools (Optional)](./5.%20Analytics%20Tools/README.md)
Build data insights.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [Power BI](./5.%20Analytics%20Tools/i.%20Power%20BI.md) | Visualization and dashboarding for business insights. |

---

---



### [Project-Based Learning](./7.%20Project-Based%20Learning/README.md)
Apply everything you've learned in real-world scenarios.

| Tutorial | Why It Comes Next |
|----------|--------------------|
| [Data Engineering Real World Projects](./7.%20Project-Based%20Learning/i.%20Data%20Engineering%20Real%20World%20Projects.md) | Practice building pipelines, dashboards, and ETL flows. |
| [AWS Projects / Azure Projects](./7.%20Project-Based%20Learning/ii.%20AWS%20Projects%20or%20Azure%20Projects.md) | Cloud-native implementations. |
| [Snowflake Projects](./7.%20Project-Based%20Learning/iii.%20Snowflake%20Projects.md) |  |
| [Databricks Projects](./7.%20Project-Based%20Learning/iV.%20Databricks%20Projects.md) | Advanced Spark-based projects. |

---

### [Interview Preparation](./8.%20Interview%20Preparation/README.md)
Wrap up with targeted practice for job readiness.

| Tutorial | Why It Comes Last |
|----------|--------------------|
| [Interview Preparation](./8.%20Interview%20Preparation/README.md) | Covers technical and behavioral questions. |
| [SQL FAANG Problems / Python FAANG Problems](./8.%20Interview%20Preparation/ii.%20SQL%20FAANG%20Problems%20or%20Python%20FAANG%20Problems.md) | High-level problem solving for top-tier interviews. |
| [Data Modeling For Data Engineer Interview](./8.%20Interview%20Preparation/iii.%20Data%20Modeling%20For%20Data%20Engineer%20Interview.md) | Deep dive into schema design and optimization. |


## 8-week sprint

### Phase 1: The Modern Stack (Weeks 1–2)

**Goal**: Move from local Python scripts to Cloud-based Data Warehousing.

 * **Get a Cloud Warehouse**: Sign up for a Snowflake or Google BigQuery free trial. This is where your data will live.
 * **Master dbt** (Data Build Tool): This is the most important tool for a 2026 Data Engineer.
   * Take the free "dbt Fundamentals" course on their website.
   * Learn how it turns your SQL queries into modular, version-controlled models.
 * **Advanced SQL Refresh**: Ensure you can write Window Functions (`RANK()`, `LEAD()`, `LAG()`) and CTEs (WITH statements) from memory. These are the "LeetCode" of data engineering interviews.

### Phase 2: The "Hero" Portfolio Project (Weeks 3–4)
**Goal**: Build one end-to-end pipeline that proves you can handle "messy" real-world data.
 * **The Ingestion**: Write a **Python** script using the requests library to pull data from a public API (e.g., OpenWeather, Spotify, or a Financial API).
 * **The Storage**: Use your Python `os` and `pathlib` skills to save that data as a JSON/CSV and upload it to an **AWS S3** bucket.
 * **The Transformation** (SQL/dbt): Load that data into **Snowflake**. Use **dbt** to clean it (e.g., using re patterns via SQL or Python UDFs) and transform it into a "Gold" table ready for analysis.
 * **The Orchestration**: Use **GitHub Actions** or a basic **Apache Airflow** setup to make this run automatically every day at 8:00 AM.

### Phase 3: The Resume & "The Hook" (Week 5)
**Goal**: Optimize your background for ATS (Applicant Tracking Systems).
 * **The GitHub README**: Your project shouldn't just be code. Your README needs a system architecture diagram (use Lucidchart or Excalidraw). Recruiters love seeing how data flows from A to B.
 * **The CSE Degree**: Put this at the very top. It is your "Gold Medal" in a competitive market.
 * The "Sub-Teacher" Pivot: On your resume, describe your teaching as "Technical Documentation and Stakeholder Communication." Data Engineering is 50% technical and 50% explaining complex data logic to people who don't understand it. You have an edge here.

### Phase 4: The Application Blitz (Weeks 6–8)
Goal: Get your first "No" so you can get to your first "Yes."
 * LinkedIn Strategy: Don't just "Easy Apply." Filter for "Junior Data Engineer" or "Associate Analytics Engineer."
 * The 2nd Project (Quick Win): Use your openpyxl skills to build a "Legacy to Cloud" tool. Many companies have old Excel data they need to move to the cloud. Showing you can automate this is a huge selling point.
 * Interview Prep: Practice explaining Idempotency (the ability to run a script twice without breaking the data) and Data Lineage. These are common CSE-level interview questions.

#### Your 2026 "Cheat Sheet" for Interviews
| Mention this... | To prove you are... |
|---|---|
| "I used dbt tests for data quality." | Not just a coder, but a reliable engineer. |
| "I used Docker to containerize my script." | Ready for a modern DevOps environment. |
| "I handled API rate-limiting in Python." | Experienced with real-world infrastructure. |

#### Immediate Next Step
Go to the dbt Labs website and start their free "dbt Fundamentals" course today. It will take you about 5 hours, and it’s the single most important certification to add to your resume alongside your degree.
Would you like me to give you a specific API and a "messy data" scenario to use for your Hero Project?





