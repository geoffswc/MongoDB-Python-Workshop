for f in *.json
do
	mongoimport --db=covid-noncomm-use-subset --collection=pmc_content --file=$f
done