<<<<<<< HEAD
Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
=======
<img src="https://static.wixstatic.com/media/95af51_ae2122aebc944721a96afd10f3ccfe0c~mv2.png/v1/fill/w_329,h_45,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/95af51_ae2122aebc944721a96afd10f3ccfe0c~mv2.png" alt="drawing" width="200"/><a name="top-">

<p align="center">

[![Run CI pipe for dbt projects](https://github.com/eon-collective/the_office/actions/workflows/dbt_sql_linting.yml/badge.svg)](https://github.com/eon-collective/the_office/actions/workflows/dbt_sql_linting.yml)

<p align="center">

[![Run CI pipe for dbt projects](https://github.com/eon-collective/the_office/actions/workflows/dbt_ci_pipe.yml/badge.svg)](https://github.com/eon-collective/the_office/actions/workflows/dbt_ci_pipe.yml)

</p>

<p align="center">

[![Run CI pipe for dbt projects](https://github.com/eon-collective/the_office/actions/workflows/evaluator_pipe.yml/badge.svg)](https://github.com/eon-collective/the_office/actions/workflows/evaluator_pipe.yml)

</p>

# Welcome to Eon Collective dbt® Project Template

## Table Of Contents <a name="toc-"></a>
- [Versions](#versions-)
    - [Revision History](#project_revisionhistory)
    - [dbt Project Version](#dbt_project_version_info)
- [Overview](#dbt_project_overview)
- [Application Functional Overview](#dbt_project_components)
    - [Project Input](#dbt_project_input)
        - [Source Data from Raw Layer](#dbt_project_input_source_tables)
        - [Static/Seeds](#dbt_project_input_static_or_seeds)
    - [Cleansing/Transformation](#dbt_project_cleansing_and_transformation)
    - [Project Output](#dbt_project_output)
    - [Data Lineage](#dbt_project_data_lineage)
    - [Functional Context](#dbt_project_functional_context)
- [Using This dbt Project](#dbt_project_using_this_one)
    - [Project Structure](#dbt_project_structure)
    - [Permissions](#dbt_project_permissions)
    - [Project Settings](#dbt_project_settings)
    - [Project Packages/Dependencies](#dbt_project_packages_dependencies)
    - [Development Environment Setup](#dbt_project_development_environnment)
        - [Local Development: VSCode/Atom etc](#dbt_project_input_local_development)
        - [Developing in the Cloud IDE](#dbt_project_input_cloud_ide_development)
- [dbt Commands: How to Run](#dbt_project_howtorun)
    - [To get dependencies](#dbt_howtorun_deps)
    - [To compile the dbt project](#dbt_howtorun_compile)
    - [To get the documentation](#dbt_howtorun_docsgenerate)
    - [Loading static/seed files](#dbt_howtorun_seed)
    - [Mart build](#dbt_howtorun_martbuild)
    - [List Project resources](#dbt_howtorun_ls)
- [Control/Audit Framework/Monitoring](#dbt_project_audit_control_framework)
- [Testing](#dbt_project_testing)
    - [Continuos Integration: Bitbucket Pipelines](#dbt_project_ci)
        - [Credentials](#dbt_project_ci_credentials)
        - [Pipe Setup](#dbt_project_ci_pipe_setup)
    - [dbt Tests](#dbt_ci_dbt_tests)
- [Deployment](#dbt_project_deployment)
    - [Continuous Deployment: dbt_runner](#dbt_cd_dbt_runner)
        - [Credentials](#dbt_project_cd_credentials)
        - [Alerts](#dbt_project_cd_alerts)
        - [Job Names](#dbt_project_cd_job_names)
        - [Adhoc Runs](#dbt_project_adhoc_runs)
            - [(Re-)Loading seeded files](#dbt_project_adhoc_runs_seeds)
            - [(Re-)Loading static S3 files](#dbt_project_adhoc_runs_s3_files)
        - [Orchestration](#dbt_project_cd_orchestration)
- [Support Team Structure](#dbt_project_support_team_structure)
- [Service Level Agreements (SLA)](#dbt_project_sla)
- [Troubleshoot/ F.A.Q](#dbt_troubleshoot)
    - [known Issues](#dbt_troubleshoot_known_issues)
    - [Debugging](#dbt_troubleshoot_debugging)
- [Migration Notes](#dbt_project_migration_notes)
- [Resources](#resources-)
- [Cutover Plan](#cutover_plan)


# Versions <a name="versions-"></a> [↑](#toc-)

## Revision History <a name="project_revisionhistory"></a> [↑](#toc-)

|**Version** | **Revision Date** |
| :-------: | :-------------: |
|v1.0       | May 20, 2022    |

## dbt Project Version <a name="dbt_project_version_info"></a> [↑](#toc-)

|**Version** | **Latest Version used for testing** | 
| :--------: | :---------------------------------: | 
| 1.0.0      |   1.0.3                             | 


# Overview <a name="dbt_project_overview"></a> [↑](#toc-)

TODO: Add dbt project Documentation - The purpose/objective of this project.

![Scheme](etc/images/UMM_Objective.png)

[↑](#toc-)
# Application Functional Overview <a name="dbt_project_components"></a> 

TODO: Add dbt project Documentation - The high level overview of application overview.
*you can put functional architecture diagram here: where is the data coming from? what does your application do at, any downstream applications etc*

```mermaid
graph LR
A[source_A] -- ELT --> W{this dbt project}
B[source_B] -- ELT --> W
C[source_C] -- ELT --> W
W -- dbt build: on_error --> X(notifications sent)
X -- via --> V>email]
X -- via --> U>slack]
W -- dbt build: on_success --> Y{snowflake objects built}
W -- dbt build --> S((metadata))
S -- stored in --> P>manifest.json]
S -- stored in --> Q>run_results.json]
W -- dbt docs generate --> O((docs site))
O -- generates --> S
S -- stored in --> R>catalog.json]
Y -- consumed by --> T>application]
Y -- consumed by --> Z>dashboard]


```
[↑](#toc-)
## Project Input <a name="dbt_project_input"></a> 

[↑](#toc-)
###  Source Data from Raw Layer  <a name="dbt_project_input_source_tables"></a>

The following raw tables are consumed by this project

| **DATABASE** | **SCHEMA**  | **TABLE** | **NOTES** |
|:------------:|:-----------:|:---------:|:---------:|
| RAW          | JAFFLE_SHOP | CUSTOMERS |   Data from a customer table in Jaffle Shop has been loaded from a CSV file located in a public [S3 bucket](s3://dbt-tutorial-public/jaffle_shop_customers.csv)        |
| RAW          | JAFFLE_SHOP | ORDERS    |    Data from an orders table in Jaffle Shop has been loaded from a CSV file located in a public S3 bucket.       |
| RAW          | SNOWPLOW    | EVENTS    |    No records in the dw       |
| RAW          | STRIPE      | PAYMENT   |   Data on the payment of Jaffle Shop in Stripe has been loaded from a CSV file located in a public S3 bucket.        |


[↑](#toc-)
###  Static/Seeds <a name="dbt_project_input_static_or_seeds"></a>

The following static tables are used by this project. Non-seed files are located in the 
's3://bose-bucket/*' folder. They get `COPY INTO` the appropriate tables using a storage integration.

| **FILENAME** | **DATABASE** | **SCHEMA**     | **SEED**  | **NOTES** |
|:------------:|:------------:|:--------------:|:---------:|:---------:|
|              | THE_OFFICE   | DBT_AAHMED_DEV | EMPLOYEES |   - Loaded with `dbt seed` command run & Loads static csv file found in the `seeds` folder of the project into snowflake table        |


[↑](#toc-)
## Cleansing/Transformation <a name="dbt_project_cleansing_and_transformation"></a>

This project handles the following transformations/cleansing or curation details during its execution.

| **DATABASE** | **SCHEMA**     | **MODEL**           | **MATERIALIZATION** | **TAGS** | **NOTES** |
|:------------:|:--------------:|:-------------------:|:-------------------:|:--------:|:---------:|
| THE_OFFICE   | DBT_AAHMED_DEV | STG_CUSTOMERS       | VIEW                | []       |  - Renamed `id` to `customer_id`, Created new column `full_name` from  `first_name` and `last_name`         |
| THE_OFFICE   | DBT_AAHMED_DEV | STG_ORDERS          | VIEW                | []       |   - Renamed `user_id` to `customer_id` ,  Created new column `valid_order_date` by filtering when status column        |
| THE_OFFICE   | DBT_AAHMED_DEV | STG_PAYMENTS        | VIEW                | []       |   - Renamed `id` to `payment_id` ,  Renamed `orderid` to `order_id` ,  Used Marcos convert cents to dollars ,  Renamed  `created` to  `created_at`        |
| THE_OFFICE   | DBT_AAHMED_DEV | FCT_ORDERS          | TABLE               | []       |   - Get the `amount` when status = 'success' ,  left join the two source tables        |
| THE_OFFICE   | DBT_AAHMED_DEV | INT_ORDERS          | TABLE               | []       |   - Get the `amount` when status = 'success' ,  left join the two source tables        |

[↑](#toc-)
## Project Output <a name="dbt_project_output"></a>

This project produces the following tables in snowflake i.e models that don't have any child.

| **DATABASE** | **SCHEMA**     | **MODEL**           | **MATERIALIZATION** | **TAGS** | **NOTES** |
|:------------:|:--------------:|:-------------------:|:-------------------:|:--------:|:---------:|
| THE_OFFICE   | DBT_AAHMED_DEV | ALL_DATES           | TABLE               | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | CUSTOMER_ORDERS     | TABLE               | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | STG_PAGE_VIEWS      | INCREMENTAL         | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | INT_ORDERS__PIVOTED | TABLE               | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | DIM_CUSTOMERS       | TABLE               | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | FCT_CUSTOMER_ORDERS | TABLE               | []       |           |
| THE_OFFICE   | DBT_AAHMED_DEV | REPEAT_CUSTOMERS    | EPHEMERAL           | []       |           |

[↑](#toc-)
## Data Lineage <a name="dbt_project_data_lineage"></a>

The full data lineage image isn't reader friendly when outputted to an image as it is too long and too wide. To generate and serve the docs on your machine
see [dbt Commands: How to Run](#dbt_project_howtorun). *Note: In dbt data lineage diagrams green bubbles are sources and blue bubbles are models.*

[↑](#toc-) 
### Sample Data Lineages
![Lineages](https://github.com/eon-collective/the_office/blob/main/resources/Lineage.gif)


## Functional Context <a name="dbt_project_functional_context"></a> [↑](#toc-)


# Using This dbt Project <a name="dbt_project_using_this_one"></a> [↑](#toc-)

## Project structure <a name="dbt_project_structure"></a> [↑](#toc-)

The project structure defined for dbt projects is as defined below:

```commandline
.
├── README.md
├── analyses
├── dbt_project.yml
├── macros
│   ├── cents_to_dollars.sql
│   ├── clean_stale_models.sql
│   └── grant_select.sql
├── models
│   ├── 1_Legacy
│   │   └── customer_orders.sql
│   ├── 2_staging
│   │   └── jaffle_shop
│   │       └── jaffle_shop.md
│   │       └── src_jaffle_shop.yml
│   │       └──stg_customers.sql
│   │       └── stg_jaffle_shop.yml
│   │       └──stg_orders.sql
│   │   └── snowplow
│   │       └── src_snowplow.yml
│   │       └── stg_page_views.sql
│   │   └── strip
│   │       └── src_stripe.yml
│   │       └── stg_payments.sql
│   ├── 3_mart
│   │   └── core
│   │       └── dim_customers.sql
│   │       └── fct_customer_orders.sql
│   │       └── fct_orders.sql
│   │       └── int_orders__pivoted.sql
│   │       └── repeat_customers.sql
│   │   └── intermediate
│   │       └──int_orders.sql
│   │   └── strip
│   │       ├── src_stripe.yml
│   │       ├── stg_payments.sql
│   ├── all_dates.sql
├── packages.yml
├── scratchpad
├── seeds
├── snapshots
└── tests
```
This same project tree view above is persisted/versioned under *etc/project_tree_structure.md* - If project changes, please update both markdown documents.

[↑](#toc-) 
## Permissions <a name="dbt_project_permissions"></a>

In order for this project to run successfuly, the following permissions are needed on Snowflake. 

| **DATABASE NAME** | **SCHEMA**                                     | **TABLE NAME** | **PERMISSION** |
|-------------------|------------------------------------------------|----------------|----------------|
| `<ENV>_RAW`       | BODS, SAPE03, SAPSHP, SFTPGTSI                 | ALL            | READ           |
| `<ENV>_MARTS`     | UMM_EMEA_REF_DATA, UMM_EMEA_STAGE, UMM_EMEA_DW | ALL            | READ & WRITE   |

**NOTE:** Replace `<ENV>` with the any of the following environment codes: `DEV, TEST or PROD`

## Project Settings <a name="dbt_project_settings"></a> [↑](#toc-)

The project settings for this projects are persisted in the `dbt_project.yml` file

### Application Variables <a name="dbt_application_vars"></a> [↑](#toc-)

This application uses the following variables defined in the `dbt_project.yml` file under the `vars` section.

| **Application Argument** | **Default Value** | **Options**                       |                       **Description/Notes**                        |
|:------------------------:|:-----------------:|-----------------------------------|:------------------------------------------------------------------:|
|           env            |       TEST        | `TEST` `DEV` `PROD`               |       Controls which environment the source data comes from        |


*The variables should be passed to the application from the command line at runtime. Examples:*

1. Run a monthly refresh using the TEST_RAW environment `dbt run --vars '{refresh_type: MONTHLY}'` 
2. Run a refresh from 201801 - 202201 using the PROD_RAW environment `dbt run --vars '{refresh_type: CUSTOM, fmthid_start: 201801, fmth_id_end: 202201, env: PROD}'`

## Project Packages/Dependencies <a name="dbt_project_packages_dependencies"></a> [↑](#toc-)

| Package    | Version | Usage                                       |
|------------|---------|---------------------------------------------|
| dbt_utils  | 0.8.0   | Used for reusable macros and utils from dbt |



## Development Environment Setup <a name="dbt_project_development_environnment"></a> [↑](#toc-)

There are two possible environents where development can happen while building in Bose COE environment. Namely: 
  1. Local Development - this can be IDE that is leveraging dbt core
  2. Cloud IDE - dbt cloud environment

Below are instructions to get setup on both of these environments.

### Local Development: VSCode/Atom etc <a name="dbt_project_input_local_development"></a> [↑](#toc-)


  
1. #### Install Requirements <a name="dbt_project_input_local_development"></a> [↑](#toc-)
    [Install dbt](https://docs.getdbt.com/dbt-cli/installation).   
    Optionally, you can [set up venv to allow for environment switching](https://discourse.getdbt.com/t/setting-up-your-local-dbt-run-environments/2353). 

2. #### Setup<a name="dbt_project_input_local_development"></a> [↑](#toc-)

    Set up a profile called `dbt_project_template` to connect to a data warehouse by following [these instructions](https://docs.getdbt.com/docs/configure-your-profile). If you have access to a data warehouse, you can use those credentials â€“ we recommend setting your [target schema](https://docs.getdbt.com/docs/configure-your-profile#section-populating-your-profile) to be a new schema (dbt will create the schema for you, as long as you have the right privileges). If you don't have access to an existing data warehouse, you can also setup a local postgres database and connect to it in your profile.
    Open your terminal and navigate to your `profiles.yml`. This is in the `.dbt` hidden folder on your computer, located in your home directory.

    On macOS, you can open the file from your terminal similar to this (which is using the Atom text editor to open the file):
    ```console
    $ atom ~/.dbt/profiles.yml
    ```

    Insert the following into your `profiles.yml` file and change out the bracketed lines with your own information.
    [Here is further documentation](https://docs.getdbt.com/docs/available-adapters#dbt-labs-supported) for setting up your profile.
    ```yaml
    dbt_project_template:
        outputs:
            dev:
            type: snowflake
            account: <account>.<region>

            # User/password auth
            user: <email/username>
            authenticator: externalbrowser

            role: <insert role>
            database: <insert db>
            warehouse: <insert warehouse>
            schema: DBT_<YOUR_USERNAME>
            threads: 50
            client_session_keep_alive: True
            query_tag: <insert tag>
        target: dev                        
    ```

    | Configuration Key              | Definition                                                                                                                                                                                                              |
    | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | my_project                     | This is defining a profile - this specific name should be the profile that is referenced in our dbt_project.yml                                                                                                         |
    | target: dev                    | This is the default environment that will be used during our runs.                                                                                                                                                      |
    | outputs:                       | This is a prompt to start defining targets and their configurations. You likely won't need more than `dev`, but this and any other targets you define can be used to accomplish certain functionalities throughout dbt. |
    | dev:                           | This is defining a target named `dev`.                                                                                                                                                                                  |
    | type: [warehouse_name]         | This is the type of target connection we are using, based on our warehouse. For Bose COE, snowflake should be used: Can be [env]_EDW_WH or [env]_MARTS_WH for example in DEV environment, the warehouse for EDW layer would be `DEV_EDW_WH`                                                               |
    | threads: 50                    | This is the amount of concurrent models that can run against our warehouse, for this user, at one time when conducting a `dbt run`                                                                                      |
    | account: <account>.<region>1 | Change this out to the warehouse's account.  Defaulted to Bose COE Snowflake URL                                                                                                                                         |
    | user: [your_username]          | Change this to use your own username that you use to log in to the warehouse. Use Bose® userid of format ABC1234                                                                                                          |
    | authenticator: authenticator   | To use with Bose® Single Sign On, use `authenticator` as the value to be prompted for a sign on window from Snowflake. Must use MFA during sign in.                                                                       |
    | role: transformer              | This is the role that has the correct permissions for working in this project.                                                                                                                                          |
    | database: analytics            | This is the database name where our models will build                                                                                                                                                                   |
    | schema: dbt_[userid]        | Change this to a custom name. Follow the convention `dbt_userid`. This is the schema that models will build into / test from when conducting runs locally.                                          |

3. Clone this repository
    
    ```console
    $ git clone git@bitbucket.org:<organization>/dbt_project_template.git 
    ```

4. Change into the `dbt_project_template` directory from the command line:
    ```console
    $ cd dbt_project_template
    ```

5. Try running the following generic/common commands one at a time from your command line:
    - `dbt debug` - tests your connection. If this fails, check your profiles.yml.
    - `dbt deps`  - installs any packages defined in the packages.yml file.  
    For project specific commands see the section below on [dbt Commands: How to Run](#dbt_project_howtorun)


### Developing in the Cloud IDE <a name="dbt_project_input_cloud_ide_development"></a> [↑](#toc-)

The easiest way to contribute to this project is by developing in dbt Cloud. If you have access, navigate to the develop tab in the menu and fill out any required information to get connected.

In the command line bar at the bottom of the interface, run the following generic/common commands one at a time:

- `dbt deps`  - installs any packages defined in the packages.yml file.

For project specific commands see the section below on [dbt Commands: How to Run](#dbt_project_howtorun)

# dbt Commands: How to Run <a name="dbt_project_howtorun"></a> [↑](#toc-)
Assuming you have your environment setup as described in previous section, you can run the following commands to manage this dbt project during deployment.

### To get dependencies:  <a name="dbt_howtorun_deps"></a> [↑](#toc-)

[dbt docs on deps command](https://docs.getdbt.com/reference/commands/deps)

    dbt deps

### To compile the dbt project  <a name="dbt_howtorun_compile"></a> [↑](#toc-)
Generates executable SQL from source model, test, and analysis files. You can find these compiled SQL files in the target/ directory of your dbt project in your development environment. [See dbt docs on compile](https://docs.getdbt.com/reference/commands/compile)

    dbt compile

### To get the documentation:  <a name="dbt_howtorun_docsgenerate"></a> [↑](#toc-)
Generate documentation for the project. [See dbt docs on docs generate](https://docs.getdbt.com/reference/commands/cmd-docs#dbt-docs-generate)

    dbt docs generate --no-compile

NOTE: since this project uses call statements in some of the dbt model that execute directly in the DW (snowflake), if dbt runs any compile step which includes `dbt docs generate`, existing data in the mart is lost since the call statements execute with `delete from {{this}} <where condition>`

To view the generated in local IDE, run the following command to start a webserver on default port 8000 and serve the generated documents. [See dbt docs on docs serve](https://docs.getdbt.com/reference/commands/cmd-docs#dbt-docs-serve)

    dbt docs serve

### Loading static/seed files <a name="dbt_howtorun_seed"></a> [↑](#toc-)
Builds any .csv files as tables in the warehouse. These are located in the data/seed folder of the project. Otherwsie specified in the dbt_project.yml. This materializes the CSVs as tables in your target schema. Note that **not all projects require this step** since the assummption that raw data is already in your warehouse. See [dbt docs on seed](https://docs.getdbt.com/docs/building-a-dbt-project/seeds)

    dbt seed

[dbt docs on seed](https://docs.getdbt.com/docs/building-a-dbt-project/seeds)

### Mart build <a name="dbt_howtorun_martbuild"></a> [↑](#toc-)

There are three types of Mart refreshes that get run at different times of the fiscal month. The variables passed to the project determines how the Mart will get refreshed.
To understand the three refresh types assume that today is April 14, 2022 (202204):
1. Full Refresh - will use the IDs from April 2019 (201904) to April 2022 (202204)
2. Monthly Refresh -  will use the IDs from January 2022 (202201) to March 2022 (202203)
3. Weekly Refresh -  will use the IDs from February 2022 (202202) to April 2022 (202204)

#### The Default Values (SOFT Full Refresh w/ TEST_RAW Environment)

    dbt run

#### A Monthly Refresh w/ the TEST_RAW environment

    dbt run --vars '{refresh_type: MONTHLY}'

#### A Custom Refresh from 201801 - 202201 w/ the PROD_RAW Environment 

    dbt run --vars '{refresh_type: CUSTOM, fmthid_start: 201801, fmth_id_end: 202201, env: PROD}'

#### A HARD Full Refresh w/ the PROD_RAW Environment

    dbt run --full-refresh --vars'{env: PROD}'

<i> Both a HARD & SOFT Full Refresh reloads the previous 36 months of data. A HARD refresh drops and recreates the table whereas a SOFT refresh drops and recreates the data.</i>

### List Project resources <a name="dbt_howtorun_ls"></a> [↑](#toc-)

List project resource. [dbt docs on ls command and reference to resource selection syntax](https://docs.getdbt.com/reference/commands/list#overview)

    dbt ls

# CRT Models [↑](#toc-)
In the `models/onboarding/*` folder there is a collection of models with the prefix `crt_`. These models are a reference/tool to help migrate the data from Redshift to Snowflake.
They simply execute a `CREATE TABLE IF NOT EXISTS` command to create tables in Snowflake with structures identical to Redshift. Once those tables are converted to DBT models the crt_model
becomes irrelevant because DBT uses the `CREATE OR REPLACE` command. 

# Control/Audit Framework <a name="dbt_project_audit_control_framework"></a> [↑](#toc-)

##	Introduction [↑](#toc-)
Mart Auditor is a dbt package developed to capture runtime information about marts being executed in Bose COE data loads. These runtime metrics can be used to analyze data marts executed in past and for auditing purpose.
##	Design
Any data mart that is developed in Bose COE project can plug in Mart Auditor package to capture data mart run time metrics. Mart Auditor creates two different tables i.e., Batch and Batch_Loging for all marts in database. These tables can be used to query to know past executions, errors, execution re tryâ€™s etc. 

![Scheme](etc/images/mart_audit_model.png)

Mart Auditor is a light weight dbt package that inserts records into above tables as mart progresses and creates table or views as part of model creating and execution. There is only one entry per execution of Mart in Batch table and multiple entries one per model in batch_logging table. Association between batch and batch_logging table is: 1 -> M



###	Batch table structure [↑](#toc-)
To get the DDL Structure from Snowflake, run the command: `select get_ddl('table', 'dev_marts.cf.batch');` and it will output the following:

```jql
create or replace TABLE BATCH (
	BATCHID NUMBER(38,0),
	RETRY_CNT NUMBER(38,0),
	DBT_MART VARCHAR(16777216),
	DBT_MART_REFRESH_TYPE VARCHAR(16777216),
	START_DATE TIMESTAMP_NTZ(9),
	END_DATE TIMESTAMP_NTZ(9),
	DURATION_IN_SECONDS NUMBER(38,0),
	LOAD_STATUS VARCHAR(16777216)
);
```

###	Batch_logging table structure [↑](#toc-)
To get the DDL Structure from Snowflake, run the command: `select get_ddl('table', 'dev_marts.cf.batch_logging');` and it will output the following:

```jql
create or replace TABLE BATCH_LOGGING (
	BLG_KEY NUMBER(38,0),
	BATCHID NUMBER(38,0),
	DBT_MART VARCHAR(16777216),
	DBT_MART_REFRESH_TYPE VARCHAR(16777216),
	DBT_MODEL_NAME VARCHAR(16777216),
	SF_TABLE_NAME VARCHAR(16777216),
	ROWS_BEFORE NUMBER(38,0),
	ROWS_AFTER NUMBER(38,0),
	STARTDATE TIMESTAMP_NTZ(9),
	COMPLETEDATE TIMESTAMP_NTZ(9),
	ERROR_MESSAGE VARCHAR(16777216)
);
```

##	Macros developed in Mart Auditor:  [↑](#toc-)
Total 4 macros are developed as part of Mart Auditor dbt package. These macros can be called by any dbt mart by deploying into their dbt mart project.

###	Insert_batch : [↑](#toc-) 
This macro inserts a record into batch table as soon as mart stars execution. Status in batch table will be inserted as â€œStartedâ€ along with Mart name, BatchID, StartDateTime etc.

###	insert_batch_logging : [↑](#toc-)
This macro inserts a record into batch_logging table as soon as any model in dbt mart stars executing. It will insert all the information about models that we execute as part of data mart. Important information like model name, mart name, rows in table/view before model executes, model execution start date time and model execution status as â€œStartedâ€ will be captured into table.

###	update_batch_logging: [↑](#toc-) 
This macro is developed to validate the model executed by data mart. If a model in mart is executed successfully then this macro updates the previously inserted record in batch_logging table with updated values like status will be updated as completed, rows in table after model executes, end date time for model and Table or View name that macro creates in database.

###	Update_batch : [↑](#toc-)
Once all the models in data mart are executed successfully then this macro updates batch table record by changing status to completed and captures information like duration in seconds, retry_count etc. If any of the model in the mart is failed then this macro updates batch table with failed status and increase the retry count value by one.

##	Steps to use Mart Auditor in your dbt mart: [↑](#toc-) 

*Note*: Mart Auditor is available in bitbucket at following location: 

Bitbucket Location: 
> ``

1.	Add Mart Auditor package in packages.yml file like below example:


2.	Execute `dbt deps` command to deploy mart auditor package into your dbt mart

3.	You can find mart auditor deployed into your dbt *packages* folder of your project

4.	You can call above macros in your dbt_proejct.yml file with below example:

    1. Insert_batch(dbt_mart_name, dbt_mart_refresh_type) : 
        This macro accepts two parameters for Mart_name and Mart_refresh_type. Mart_refresh_type is optional parameter and if you donâ€™t provide refresh type parameter then it will insert NULL value into batch table. Call this macro at â€œon-run-startâ€ section of dbt_project.yml.

    2. insert_batch_logging (dbt_mart_name, dbt_model_name, table_name, refresh_type):
    This macro accepts four parameters for Mart_name, model_name, table_name and refresh_type. Table_name and refresh_type are optional parameters where table name takes model name and refresh_type takes null value by default if you donâ€™t supply. Call this macro at pre-hook section of dbt_project.yml. Pass current model name to the macro with keyword â€œthisâ€.

    3. Update_batch_logging (dbt_mart_name, dbt_model_name, table_name, refresh_type):
    This macro accepts four parameters for Mart_name, model_name, table_name and refresh_type. Table_name and refresh_type are optional parameters where table name takes model name and refresh_type takes null value by default if you donâ€™t supply. Call this macro at post-hook section of dbt_project.yml

    4. update_batch (dbt_mart_name, dbt_mart_refresh_type) : 
    This macro accepts two parameters for Mart_name and Mart_refresh_type. Mart_refresh_type is optional parameter and if you donâ€™t provide refresh type parameter then it will insert null value into batch table. Call this macro at â€œon-run-endâ€ section of dbt_project.yml.

Dataops Queries for this auditing this mart run are provided in the `analysis` folder with the file name `mart_auditor_dataops.sql`

# Testing <a name="dbt_project_testing"></a> [↑](#toc-)

*documentation placeholder - call out any tests being run in the project* 

[dbt docs on testing](https://docs.getdbt.com/docs/building-a-dbt-project/tests)

## Continuos Integration: Bitbucket Pipelines <a name="dbt_project_ci"></a>                                                             [↑](#toc-)


### Credentials <a name="dbt_project_ci_credentials"></a> [↑](#toc-)

Credentials in a bitbucket pipe are passed through Repository variables. See more on Bitbucket pipeline and environment variables: [User-defined variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/). 
The following variables have been configured with `DEV` service account details.

| **Custom Variable** | **Variable Description**                           |
|---------------------|----------------------------------------------------|
| DBT_TARGET_TYPE     | Type of DW for dbt to use : default is `snowflake` |
| DBT_TARGET_URL      | snowflake url: <account>.<region>                  |
| DBT_USER            | snowflake username for authentication              |
| DBT_PASSWORD        | snowflake password for authentication              |

Most parameters are configured as a secret in Bitbucket and cannot be viewed.

### Bitbucket Pipe Setup <a name="dbt_project_ci_pipe_setup"></a> [↑](#toc-)

This dbt project CI pipe is configured as step in a shared bitbucket pipeline yml file (at root level of this repo). The following is the settings for this mart. 

```yml
      - step:
          name: 'dbt_project_template_DBT - Compile'
          trigger: manual
          script:
            - echo "Starting build for dbt_project_template_DBT"
            - echo "$DBT_PROJECT_BITBUCKET_PUB_CERT" > ~/.ssh/authorized_keys
            - mkdir ~/.dbt
            - touch ~/.dbt/profiles.yml
            - 'echo -e "dbt_project_template:\n  outputs:\n    dev:\n      type: $DBT_TARGET_TYPE\n      account: $DBT_TARGET_URL\n\n      user: $DBT_USER\n      password: $DBT_PASSWORD\n\n      role: $DBT_ROLE\n      database: DEV_MARTS\n      warehouse: $DBT_WH\n      schema: dbt_dbt_project_template\n      threads: $DBT_NUM_THREADS\n      client_session_keep_alive: True\n      query_tag: dbt\n  target: dev\n " >> ~/.dbt/profiles.yml'
            - cd dbt_project_template/
            - ls -ltr
            - dbt deps
            - dbt compile
            - echo "Done build for dbt_project_template_DBT"
```
## dbt Tests <a name="dbt_ci_dbt_tests"></a> [↑](#toc-)

# Deployment<a name="dbt_project_deployment"></a> [↑](#toc-)

## Continuous Deployment: dbt_runner <a name="dbt_cd_dbt_runner"></a> [↑](#toc-)

This project can be run in Bose COE TMC environment using the [dbt_runner template](). This template is available on all environments and leveraged during from SIT to Deployment phase of a build project. 
The dbt_runner artifcat/template is responsible for: 

1. Cloning the latest code from specified branch and url in a repo
2. Setting up a profiles.yml for the tasks run based on the provided credentials.
3. Execute a `dbt deps` to get the project prepared for any commands passed
4. Run the provided dbt commands - send notification incase of error during this run
5. At job end, upload the dbt artifact files to S3 for technical lineage harvesting. The following files are uploaded to S3: `manifest.json`, `catalog.json (if available)` and the `run_results.json`

The three Bose COE environments available for building and deployment of dbt projects: 

| **ENVIRONMENT** | **PURPOSE**                | **Branch used**               |
|-----------------|----------------------------|-------------------------------|
| DEV             | System Integration Testing | feature/[more_descptive_name] |
| TEST            | User Acceptance Testing    | feature/[more_descptive_name] |
| PROD            | Deployment (Go Live)       | main                          |

All developer unit testing are done on the local/Cloud IDE. See [Setting development environment](#dbt_project_input_local_development)

Bose® corp leverages “continuous deployment” or “direct promotion” for branching strategy.
The diagram below illustrates the branching strategy as used at Bose® for dbt project development.

```mermaid
graph TD
A((main)) -- clone --> B{FeatureA branch}
B -- pull request --> A
B -- fork --> D>builder1 branch]
D -- pull request--> B
B -- fork --> E>builder2 branch]
E -- pull request --> B
A -- clone --> F{FeatureB branch}
F -- pull request --> A 
F -- fork --> G>builder3 branch]
G -- pull request--> F
F -- fork --> H>builder4 branch]
H -- pull request --> F
```

### Credentials <a name="dbt_project_cd_credentials"></a> [↑](#toc-)

The [dbt_runner]() in Bose COE TMC uses [Credentials Vaulting Framework]() to store credentials for various projects. dbt_runner needs two main credentials to run. The following credentials are used to run this project across all Bose COE Environments

| **\\**                            | **DEV**                       | **TEST**                       | **PROD**                                                         |
|---------------------------------|-------------------------------|--------------------------------|------------------------------------------------------------------|
| Bose COE_SNOWFLAKE_CredVaultKey  | `dev/snowflake/mart/dbt_project_template` | `test/snowflake/mart/dbt_project_template` | `prod/snowflake/mart/dbt_project_template`                                   |
| Bose COE_BUGTRACKER_CredVaultKey | `N/A- Not Applicable`                | `N/A- Not Applicable`                 | `bose/prod/operations/alerts/bug_tracker_service` |



### Alerts <a name="dbt_project_cd_alerts"></a> [↑](#toc-)
The dbt_runner template has a notification/alerting mechanism incase of any WARNING, ERROR or FATAL messages. To configure notification in dbt_runner for this project;

1. In the advanced parameter `Email_Notify` parameter, provide the value `true`
2. In the advanced parameter `Bose COE_BUGTRACKER_CredVaultKey` parameter, provide a valid credential key provided by the Bose COE platform team. See the values to use per environment in [above section](#dbt_project_cd_credentials)


### Job Names <a name="dbt_project_cd_job_names"></a> [↑](#toc-)
The following is a list of dbt_runner tasks needed to run this mart successfully end to end

| **JOB_NAME**                                                    | **JOB_DESCRIPTION**                                                                    | **JOB_RUN_PARAMETERS**                                                                                               | **NOTES**                                                                                                       |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| DBT_RUNNER-MCA-SEED                             | Load static files with seed                                                            | `dbt seed`                                                                                                           | run one time during project deployment/initialization or incase of a change in the csv files within the project |


### Adhoc Runs

#### (Re-)Loading seeded files <a name="dbt_howtorun_seed"></a> [↑](#toc-)

Incase of changes to the static files that hosted within the dbt project in the `data` or `seeds` folder (varies with the project as specified by the seed-paths config in *dbt_project.yml*)
Below steps should be followed to reload the seeded data once this project has been deployed to PRODUCTION.

1. Create a new feature branch from main
2. Checkout feature branch to IDE
3. Replace the existing files in the data/ref_data_seeds folder.
4. Commit the changes to seed files and push to remote feature branch
5. Create a Pull Request from feature branch to main
6. Merge the feature branch into main
7. Run the TMC Task `DBT_RUNNER-MCA-SEED` to refresh the Ref Data for MCA project.
    - If no new files are provided but Seed data has to be refreshed, then only Run the TMC Task `DBT_RUNNER-MCA-SEED`

##### (Re-)Loading static S3 files <a name="dbt_howtorun_seed"></a> [↑](#toc-)

Incase of changes to the static files that hosted within Bose COE S3 folders
Below steps should be followed to reload the snowflake data once this project has been deployed to PRODUCTION.

1. Load the new files to S3 production bucket: check in `macros/init_project.sql` for precise S3 data locations.
2. Run the TMC Task `DBT_RUNNER-MARTS-GTSi_EMEA-INIT_PROJECT` to refresh the Ref Data for UMM_EMEA.
    - If no new files are provided but Seed data has to be refreshed, then only Run the TMC Task `DBT_RUNNER-MARTS-GTSi_EMEA-INIT_PROJECT`

### Orchestration <a name="dbt_project_cd_orchestration"></a> [↑](#toc-)

To run this project end to end, the following diagram illustrates all the steps and dependencies and their orchestration flow

Below is the orchestrated steps to execute the full refresh run for this project

![Scheme](etc/images/full_refresh_orchestration.png)

Below is the orchestrated steps to execute the openweek run for this project

![Scheme](etc/images/openweek_orchestration.png)

Below is the orchestrated steps to execute the closeweek run for this project

![Scheme](etc/images/closeweek_orchestration.png)

# Support Team Structure <a name="dbt_project_support_team_structure"></a> [↑](#toc-)

Below is the support team structure for this project:

| **Team**      | **Contact Information**                      |
|---------------|----------------------------------------------|
| Build Team    | EON Collective - Talend to dbt Migration project |
| Run Team      | run-team@bose                   |
| Source Team   | source-team@bose                                            |
| Consumer Team | consumer-team@bose                                             |


# Service Level Agreements (SLA) <a name="dbt_project_sla"></a> [↑](#toc-)

This project utilizes the following SLA schedule.

| **PRIORITY LEVEL** | **TARGET RESPONSE TIME** | **TARGET RESOLUTION TIME** | **SLA CLOCK** |
|--------------------|--------------------------|----------------------------|---------------|
| 1 - Critical       | 30 Minutes               | 4 Hours                    | 24 x 7        |
| 2 - High           | 40 Hours                 | 1 Business Day             | In Region     |
| 3 - Medium         | N/A                      | 5 Business Days            | In Region     |
| 4 - Low            | N/A                      | 10 Business Days           | In Region     |

# Troubleshoot/ F.A.Q <a name="dbt_troubleshoot"></a> [↑](#toc-)

*documentation placeholder*

## Known Issues <a name="dbt_troubleshoot_known_issues"></a> [↑](#toc-)

1. Existing data is lost or deleted after running `dbt docs generate` without the `--no-compile` flag.
   This is a known issue, since the project uses call statements that execute on the DW directly, if dbt internally executes a `compile` step, the call statements are executed. To avoid this behavior, use the `--no-compile` flag with the dbt docs generate command. See documentation on [dbt-docs-generate with --no-compile flag](https://docs.getdbt.com/reference/commands/cmd-docs#dbt-docs-generate) and [dbt execute](https://docs.getdbt.com/reference/dbt-jinja-functions/execute)
   If existing data is lost, please rerun the data mart build using the **FULLREFRESH** plan and tasks.

## Debugging <a name="dbt_troubleshoot_debugging"></a> [↑](#toc-)
1. [See dbt docs on Debugging errors](https://docs.getdbt.com/docs/guides/debugging-errors#general-process-of-debugging) - this has a comprehensive list and categorization of common errors seen on a typical dbt project. Note the [common pitfalls section](https://docs.getdbt.com/docs/guides/debugging-errors#common-pitfalls) also


# Additional Notes <a name="dbt_project_migration_notes"></a> [↑](#toc-)

During the development of this project ......

> Include any additional notes here for your project

# Resources <a name="resources"></a> [↑](#toc-)

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](http://slack.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
- Check out [dbt Developer blog on git cherry pick](https://docs.getdbt.com/blog/the-case-against-git-cherry-picking)

# Cutover Plan <a name="cutover_plan"></a> [↑](#toc-)
Please review the curover plan as templated in `../etc/CUTOVER_PLAN.md`

[Back to top ↑](#toc-)

>>>>>>> main
