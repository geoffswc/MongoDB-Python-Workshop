for f in *.json
do
	mongoimport --uri "mongodb+srv://user_name:user_password@atlas_mongodb_uri/covid-19" --collection noncomm-subset --file=$f
done