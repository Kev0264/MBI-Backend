# MBI-Backend

This is as Flask app which serves as the backend application for the Angular frontend.

## API Endpoints

There are two endpoints available on the server:
1. GET /generate
2. POST /verify

The requirements for generating and verifying a correct MBI were pulled from the PDF available here: [CMS Medicare Beneficiary Identifiers](https://www.cms.gov/medicare/new-medicare-card)

To get everything working, run the commands below to setup and run the project. This was created in a Linux environment. If running on Windows, the main difference should only be that instead of `cp` you would use `copy` (unless you're using PowerShell, in which case either works). First we will create a virtual environment *env* then activate it. Then from within the virtual environment we will install the required pip modules, make sure our environment variables are set, and then run the Flask application. Note that using environment variables mainly means that we do not need to run the command `export FLASK_APP=mbiapp` (or `set FLASK_APP=mbiapp` in Windows).
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
flask run
```

---

To run unit tests, run the following:
```
python3 -m pytest
```
---
To test in the brower, issue a GET request to the `/generate` endpont like so:
`http://localhost:5000/generate`

You should get a JSON response which conforms to the Medicare Beneficiary Identifier (MBI) format.

To test the verify endpoint, issue a POST request to:
`http://localhost:5000/verify`
with a parameter called `mbi` that has a string value of an MBI to test (such as "5JF9-X86-RR04"). 

You should get a response of **true** if the MBI is valid.

You can view the Angular app deployment on Heroku [here](https://mbi-frontend.herokuapp.com/).