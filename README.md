# MongoDB-Python-Workshop

### Short Description

This tutorial is an introduction to reading, building, and querying data using MongoDB and Covid-19 Research data from the Allen institute and Johns Hopkins. 

### Long Description

MongoDB is a document oriented database that makes it possible to build and query collections of JSON documents.

This tutorial will consist of a series of notebooks and tutorial exercises. Rather than discussing the MongoDB format in the abstract, participants learn to build and interact with a MongoDB, with an emphasis on using Python through Jupyter Notebook. Through these exercises, participants will use MongoDB and the Covid-19 datasets from the Allen institute and Johns Hopkins University to:


1. Query a Sample Mongo DB, using filters and aggregations.

2. Use PyMongo to populate a remote (Atlas) MongoDB with JSON documents downloaded from the CORD-19 research data set. 

3. Query the CORD-19 research data set, create a text search index, and parse results as JSON documents and Pandas dataframes. 

### Prerequisites

This tutorial is designed for workshop participants who are have some experience working with JSON documents in Python. For backround material, please see the Python and JSON workshop material at: https://github.com/geoffswc/python-json-workshop 

### Software Installation and Setup

To participate in this workshop, you'll need to be able to run python 3.6+ code. This workshop will use Jupyter Notebook, though you can follow along with a different IDE if you prefer.

You will also need to create an Atlas DB account, instantiate a sample database, and upload COVID-19 data to a collection. Instructions for this are in Atlas-Setup.md

## Workbooks

This tutorial consists of a series of notebooks. Further explanatory text is available in the notebook for each section or the tutorial.  

### Covid-19-Data-JHU-Overview.ipynb

Connect to and query the Johns Hopkins Covid-19 dataset hosted on MongoDB/Atlas. List available databases and collections. Join (lookup) collections based on common attributes. 

### Covid-19-Data-JHU-Guide.ipynb

Recreate some of the queries in the Johns Hopkins guide for python and mongo in a Jupyter notebook format.

### Sample-Atlas-DB.ipynb

Query a MongoDB hosted on Atlas through Python, including basic querying and regex.

### Atlas-Mongo-Import-Through-Python.ipynb

Write data to a remote Atlas MongoDB collection through PyMongo. This workbook uses the CORD-19 dataset from the Allen institute to demonstrate. 

### CORD-19-Reseach-Data-Set-Atlas.ipynb

Query the CORD-19 dataset you uploaded to MongoDB. Create and search documents through a text index on a field in the collection. 

## Installation and Setup

For the Atlas-related notebooks, you'll need to create an Atlas account. Instructions are in the workbooks. 

For the local installation notebooks, you'll need to install MongoDB and populate a document database with JSON files from the CORD-19 dataset. Instructions are in the CORD-19-Reseach-Data-Set.ipynb workbook.

## Data and Links

### Links to Datasets

Covid-19 Research Dataset from the Allen Institute for AI

https://pages.semanticscholar.org/coronavirus-research

Covid-19 Dashboard dataset from Johns Hopkins University

https://github.com/CSSEGISandData/COVID-19

### Links to Documentation and Tutorials

MongoDB Reference Manual:

https://docs.mongodb.com/manual/reference/

Pymongo documentation and quickstart: 

https://pymongo.readthedocs.io/en/stable/

Johns Hopkins dataset using Python and Mongo

https://developer.mongodb.com/article/johns-hopkins-university-covid-19-data-atlas#covid19-python







