# RJHack

Codes - Rajasthan Hackathon 4.0

## Basic Git Commands

**To Clone**:

	git clone https://github.com/alphacrash/RJHack.git

**Usage**:

	git pull
	git add .
	git commit -m "Message"
	git push

## Django

**Setting up your Development Environment**

1. Clone this repository (as shown above).

2. Migrate your database.

		python3 manage.py makemigrations
		python3 manage.py migrate 

3. Run the live development server on your machine and test it.
    
    	python3 manage.py runserver
    

Once the server is started, open http://127.0.0.1:8000