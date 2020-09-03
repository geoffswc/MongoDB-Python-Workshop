# MongoDB-Python-Workshop

### Short Description

This tutorial is an introduction to reading, building, and querying data using MongoDB and the Covid-19 Open Research dataset from the Allen institute. 

https://pages.semanticscholar.org/coronavirus-research

### Long Description

MongoDB is a document oriented database that makes it possible to build and query collections of JSON documents.

This tutorial will consist of a series of notebooks and tutorial exercises. Rather than discussing the MongoDB format in the abstract, participants learn to build and interact with a MongoDB, with an emphasis on using Python through Jupyter Notebook. Through these exercises, participants will use MongoDB and the CORD-19 dataset from the Allen institute to:
 

1. Query a Sample Mongo DB, using filters and aggregations.

2. Use PyMongo to populate a remote (Atlas) MongoDB with JSON documents downloaded from the CORD-19 research data set. 

3. Query the CORD-19 research data set, create a text search index, and parse results as JSON documents and Pandas dataframes. 

### Prerequisites

This tutorial is designed for workshop participants who are have some experience working with JSON documents in Python. For backround material, please see the Python and JSON workshop material at: https://github.com/geoffswc/python-json-workshop 

### Software Installation and Setup

To participate in this workshop, you'll need 

## Workbooks

This tutorial consists of a series of notebooks. Further explanatory text is available in the notebook for each section or the tutorial.  

### Sample-Atlas-DB.ipynb

Query a MongoDB hosted on Atlas through Python, including basic querying and regex.

### Atlas-Mongo-Import-Through-Python.ipynb

Write data to a remote Atlas MongoDB collection through PyMongo. This workbook uses the CORD-19 dataset from the Allen institute to demonstrate. 

### CORD-19-Reseach-Data-Set-Atlas.ipynb

Query the CORD-19 dataset you uploaded to MongoDB. Create and search documents through a text index on a field in the collection. 

## Installation and Setup

For the Atlas-related notebooks, you'll need to create an Atlas account. Instructions are in the workbooks. 

For the local installation notebooks, you'll need to install MongoDB and populate a document database with JSON files from the CORD-19 dataset. Instructions are in the CORD-19-Reseach-Data-Set.ipynb workbook.





