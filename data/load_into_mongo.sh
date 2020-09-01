for f in *.json
do
	mongoimport --uri "mongodb+srv://covid-19-admin:covid-19-password@python-mongodb-workshop.unmjr.gcp.mongodb.net/covid-19" --collection noncomm-subset --file=$f
done