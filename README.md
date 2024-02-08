# Healthcare Data Analysis: ETL Pipeline

Using a [CDC dataset](https://data.cdc.gov/Public-Health-Surveillance/Outpatient-Respiratory-Illness-Activity-Map/6svj-q4zv/about_data) of respiratory infections across the country, we will create an ETL data pipeline using Python and AWS technologies to extract data, upload it to a database, and discern patterns for potential future strategies in healthcare. 

## Technologies

AWS, Python

## Pipeline

1. CSV file uploaded to S3 Storage
2. Lambda function triggered to clean data and parse into a list of tuples
3. Connection established to RDS, and SQL insert statement executed
4. Data pulled from RDS to local machine for analysis
5. Results uploaded to EC2-hosted website

Visit the website [here](http://s3amigoshealthcare.net/).

## PEP2.ipynb contains all the Python code written for this project, from file upload to database connection to analysis.