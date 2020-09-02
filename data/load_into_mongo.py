import glob
import os

json_docs = glob.glob('*.json')
for f in json_docs[:1]:
    os.system('mongoimport --uri "mongodb+srv://pymongo_workshop_read_write:password@python-mongo-workshop.unmjr.gcp.mongodb.net/covid-19" --collection noncomm-subset --file=' + f)
        
    