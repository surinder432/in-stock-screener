# GotoLong

GotoLong is an Indian Stock Advisor (ISA) that can be used to identify stocks for buy and sale.

It relies on 

(a) Financial data (last 10 year) of Top 500 (BSE-500/Nifty-500) stocks

(b) investor's existing portfolio of stocks

It is still in Beta phase and developers can experiment with it. Once it can be used by any user with basic knowledge of
computer, it will be tagged as v1.0

## Repository

git clone https://github.com/surinder432/gotolong

## Heroku Deployment

On Heroku, the clone of repository can be connected using github.

Attach postgresql database to the heroku app.

heroku login

heroku addons:create heroku-postgresql:hobby-dev

heroku pg:info

heroku pg:credentials:url DATABASE

heroku config

gotolong_db_schema_install.sh import_pgsql "${DATABASE_URL}"

To reset the database in PostgreSQL

heroku login heroku pg:reset --app <appname>

gotolong_db_schema_install.sh import_pgsql "${DATABASE_URL}"

##    

## Quick Installation - steps

Download *.whl and *.tar.gz from dist directory.

1> Install Software

pip install gotolong*.whl

2> Install required data files
 
cd $HOME/gotolong-data

tar -xvzf gotolong-data.tar.gz

3> Add following to ~/.profile

export GOTOLONG_DATA=$HOME/gotolong-data

##  Software Installation Pre-Req

### Installation - for end use

Download Python 3.*

Download mariadb (for DB) - used mariadb10.4

Download PostgreSQL (v13) - for validation with Heroku

Dev Env:

pip -r requirements/requirements_full.txt

Heroku Env:

pip -r requirements/requirements_heroku.txt

## Software Configuration
 
###  Install Database schema

#### Create Schema

gotolong_db_schema_install.sh create_mysql

#### Install Schema for MySQL

gotolong_db_schema_install.sh import_mysql

#### Install Schema for PgSQL

gotolong_db_schema_install.sh import_pgsql

### Share Configuration

#### setup DATABASE_URL (explorer)

For MySQL

export DATABASE_URL=mysql://root:root@localhost:3306/gotolong

For PgSQL

export DATABASE_URL=postgres://postgres:root@localhost:5432/gotolong

#### data/config/gotolong-config.ini (loader)

Switch this also to DATABASE_URL.

For DB name, user and password

## Browser based Data Loader & Explorer

### Django Web Server

The django project is capable of browsing the data stored in 'gotolong' database.

cd django_gotolong/

python manage.py runserver

Starting development server at http://127.0.0.1:8000/

### Web browser : URL

Use the following URL to browse the reports

http://127.0.0.1:8000/

## Non-Browser Data Loader & Explorer

### Input Data

#### user scope

Gather and store files like demat summary and demat detailed data in input-user-data

Check following directory

{GOTOLONG_DATA}/data/input-output/

### One step load data for all modules

gotolong_all_report.sh

NOTE: This may be out of sync as the focus is to load the data directly through web browser.

## For Developers : Module Description

## amfi module

mapping of ticker and mcap and captype

## isin module

mapping of ticker and ISIN

## Giving Back Score

Module : bse -> corpact

## 52-week high and low and CMP (yesterday)

Modules : bhav, ftwhl, nse

## demat module (icici direct portfolio)

demat transaction details

demat summary details

Module name : demat

NOTE: add support for any broker.

## screener module

financial data of bse 500 for 10 years

## trendlyne module

for broker average target of healthy stocks

## gweight module

global weight module

assign weight by captype

user weight is not used right now

Name : global_weight

## fratio module

Financial Ratio module

You can specify financial ratio filters like debt to equity ratio (der)

## greco module

Global recommendation module

Uses trendlyne module and fratio module

## phealth module

identify companies at healthy price

Dependency :

## dividend module

create dividend matrix by company and month.

Dependency : nach -> dividend

# Installation - additional for development

Download PyCharm

Download HeidiSQL : DB browser

Download VIM

Download GoogleDrive to store the input data and output reports.

Download Git (includes Git-Bash)
