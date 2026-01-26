# Git and GitHub
Documentation on Git and GitHub

**[⇐ Foundational Tools>(./README.md)**

## Download links
git: https://git-scm.com/downloads
GitHub: https://desktop.github.com/download/

## Basic CLI Commands
Change Directory: cd <path>
Create Directory: mkdir <(filepath/)filename>
Create File: touch <(filepath/)filename>

## Git Commands
- Version: `git --version`
- Clone : `git clone <url>`
- Initialize Repository: `git init`

- Restore file to last committed state: `git restore <filename>`
- Stage: `git add <filename or .>`
- Unstage file: `git restore --staged <filename>`

- Commit: `git commit -m "<message>"`
- Undo Last Commit: `git reset --soft HEAD~1`
- Delete Last Commit: `git reset --hard HEAD~1`
- Switch to an older commit: `git checkout <commit_id>`

- Pull: `git pull`
- Push: `git push`
- Status: `git status`
- Log: `git log --oneline --graph`
- Difference: `git diff`

- Check branches: `git branch`
- Create and switch to a new branch: `git checkout -b <branch_name>`
- Switch branch: `git checkout <branchname>`
- Merge a branch with the active branch: `git merge <other_branch_name>`

## Rebase
Rebase moves or reapplies commits on top of another branch's latest commits creating a clean straight timeline.
* Keeps history linear (no unnecessary merge commits)
* useful when feature branch is behind `main` branch
* Rebase Command: `git rebase main`

## Squash
Squashing combines multiple small commits into one meaningful commit.
* Cleaner history before merging
* Easier code review
* Removes 'typo' or "fix print" commits
* Squash Command: `git rebase -i HEAD~<number_of_commits>` [Note: pick -> the commit to be merged into, squash or s -> commits to be merged]

## ETL Pipeline

An ETL pipeline refers to a data integration process that involves three key steps: Extract, Transform, and Load. It is designed to move data from various sources, process it into a usable format, and store it in a target system such as a data warehouse or database. This process ensures that data is clean, consistent, and ready for analysis or reporting.

Key Steps in an ETL Pipeline

Extract: Data is collected from multiple sources, which can include databases, APIs, flat files, or SaaS applications. This step ensures that raw data is gathered for further processing.

Transform: The raw data is cleaned, formatted, and transformed to meet the requirements of the target system. This can involve filtering, aggregation, schema alignment, and data validation.

Load: The transformed data is loaded into the destination system, such as a data warehouse, where it can be used for analytics, reporting, or machine learning workflows.

Benefits of ETL Pipelines

Data Centralization: Combines data from disparate sources into a unified repository, making it accessible for analysis.

Improved Data Quality: Cleanses and validates data to ensure consistency and accuracy.

Time Efficiency: Automates data preparation, reducing manual effort and enabling faster insights.

Support for Analytics: Prepares data for advanced analytics, business intelligence, and decision-making.

Use Cases

ETL pipelines are widely used across industries for tasks such as data warehousing, migrating legacy data to modern systems, and integrating data for business intelligence tools. For example:

Retail: Analyzing customer purchase patterns.

Healthcare: Consolidating patient data for better care.

Finance: Detecting fraud through real-time data processing.

ETL vs. Data Pipeline

While an ETL pipeline focuses on transforming data before loading it into a target system, a data pipeline is a broader concept that involves moving data between systems, with or without transformation. ETL pipelines are a subset of data pipelines, specifically tailored for structured data integration and transformation.

Emerging Trends

Modern ETL pipelines are evolving to include real-time processing, AI-driven automation, and cloud-native architectures, enabling faster and more scalable data workflows. These advancements are critical for businesses aiming to stay competitive in a data-driven world.

## Data Quality Engine
