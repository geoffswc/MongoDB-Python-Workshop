import glob
import os

json_docs = glob.glob('data/*.json')
for f in json_docs[:1]:
    os.system('mongoimport --uri "mongodb+srv://username_read_write:password@python-mongo-workshop.unmjr.gcp.mongodb.net/covid-19" --collection noncomm-subset --file=' + f)
        
    