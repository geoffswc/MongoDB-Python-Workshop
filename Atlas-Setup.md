#Atlas-Setup


This page concatains instructions for setting up and populating a MongoDB on Atlas. You'll query and populate this database through Python in the workshop Jupyter notebooks. 

### Create an Atlas account

https://www.mongodb.com/cloud/atlas

Note - you can use the free tier for this workshop. 

### Create a project

Create a project, give it a name (no specific restrictions here, but choose something descriptive like "mongo-python-workshop")

### Set up a cluster

After creating a project, set up a Cluster 

Make sure you name it! You may need to scroll to the bottom of the page. 
This is a one-time setup: once your cluster is created, you won't be able to change its name.

### Load the Sample Dataset

Click on Collections

Load a Sample Dataset

You might want to take a little time to click around and look through the sample dataset before proceeding to the python section of the workshop. 

### Provide read access to the sample dataset

Create a read-only access account

Create a database user:

under "database access" select: database users

Click on: "new database user"

username and password

we'll set up "read only" access. 

Provide network access

You can either make this world-readable or limit to specific IP address.

To limit to your current connection, use your IP address (note - if you don't have a persistent or permanent IP address, you won't have access next time you log in. If this is the case, you'll need to update your network access next time you try to read from this account outside your Atlas login).

To make it world-readable (no IP restrictions)
0.0.0.0/0

### Connect to MongoDB through a Jupyter Notebook
z

Get a connection string to your MongoDB instance: 

In your cluster

click on "connect"

select "connect your application"

choose "python, 3.6 or later" and copy it

your connection string should look like this (the URI should be slightly different):

mongodb+srv://pymongo_workshop_user:<password>@python-mongo-workshop.unmjr.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority
	
### Connect to MongoDB through a Jupyter Notebook

open up the jupyter notebook

Sample-Atlas-DB.ipynb

Insert your URL, with username and password, into the MDB_URL variable.

At this point, you should be able to run the jupyter notebook.

### Load COVID-19 data into MongoDB on Atlas

We'll use the coronavirus research dataset from the Semantic Scholar team at the Allen Institute.

To to:

https://pages.semanticscholar.org/coronavirus-research

CLick on "get started"

go to "downloads"

and "all releases"

For the workshop, we'll only upload a subset of this data. 

I'm looking for something small, so I'm going to download the original release, cord-19_2020-03-13.tar.gz (0.3 GB)

Untar it, you should get a folder named: 

2020-13-13

within this folder, expand the noncomm-use-subset

### Add the Data to a Collection

Back in your Atlas cluster:

go to collections
create database

db name: covid-19-data
collection name: noncomm-subset

next, create a user with write privs

create a new database user
naae: pymongo_workshop_reaad_write
you can autogenerate a password or choose one
(if you autogenerate it, save it somewhere)
give this user write privs, but not full admin 

### Upload the COVID data to MongoDB using PyMongo

You can use the Atlas-Mongo-Import-Through-Python.ipynb notebook or the load_into_mongo.py script to insert this data into the covid-19.noncomm_subset collection on Atlas. You will need to put the json files in the data directory for this repository, or change the path to the json files in the notebook or scropt.  

### Access the New Collection through Python

You should now be able to run almost all cells in the CORD-19-Research-Data-Set-Atlas.ipynb notebook.


### Create an Index on the covid_19.noncomm_subset collection

There is one cell that won't work - you'll need to create an index to do full text search.

In Atlaas, go to the clusters->collections->covid-19.noncomm-subset, and create an index. 

we'll allow a search of the body_text

create index
{
  "body_text.text": "text"
}

In Atlas, review and confirm this index. 

Now, the cell that uses the index in the jupyter notebook should run. 
    
    














