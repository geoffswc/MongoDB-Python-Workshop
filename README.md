# MongoDB-Python-Workshop

### Short Description

This tutorial is an introduction to reading, building, and querying data using MongoDB and the Covid-19 Open Research dataset from the Allen institute. 

https://pages.semanticscholar.org/coronavirus-research

### Long Description

MongoDB is a document oriented database that makes it possible to build and query collections of JSON documents.

This tutorial will consist of a series of notebooks and tutorial exercises. Rather than discussing the MongoDB format in the abstract, participants learn to build and interact with a MongoDB, with an emphasis on using Python through Jupyter Notebook. Through these exercises, participants will use MongoDB and the CORD-19 dataset from the Allen institute to:

1. Create a local MongoDB and populate it with JSON objects built through code as Python dictionaries.

2. Write basic queries to retrieve JSON documents from a Mongo DB, including how to limit results to specific document fields based on filters. 

2. Populate a local MongoDB with JSON documents downloaded from the CORD-19 dataset using command based mongo commands and shell (bash) scripts. 

3. Populate a a local MongoDB using pymongo (as opposed to shell commands)

4. Connect to a remote MongoDB through pymongo using the public URI provided through the ATLAS projec

### Prerequisites

This tutorial is designed for workshop participants who are have some experience working with JSON documents in Python. For backround material, please see the Python and JSON workshop material at: https://github.com/geoffswc/python-json-workshop 

## Workbooks

This tutorial consists of a series of notebooks. Further explanatory text is available in the notebook for each section or the tutorial. With the exception of "Covid-19-Data-Atlas.ipynb", which hosts a MongoDB available through a public URI, all workbooks require a MongoDB running on your local machine (see "Installation and Setup" for instructions). 

### Covid-19-Data-Atlas.ipynb

How to use python to connect to and query a public Covid-19 MongoDB,

### Installation and Setup

How to install MongoDB and create a document database through the Unix shell. 

### CORD-19-Reseach-Data-Set.ipynb

How to install multiple documents into a MongoDB through the mongo command line. How to create and query a text index to search for sub text within a document element. 

### MongoDB-Tutorial.ipynb

How to create and insert documents into a MongoDB through code. How to query documents based on search parameters. How to specify which elements of a document should be returned from a query. 

### Mongo-Import-Through-Python.ipynb

How to insert JSON multiple documents into a MongoDB documents using Python code. 




