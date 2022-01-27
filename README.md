# MBI-Backend

This is as Flask app which serves as the backend application for the Angular frontend.

## API Endpoints

There are two endpoints available on the server:
1. GET /generate
2. POST /verify

The requirements for generating and verifying a correct MBI were pulled from the PDF available here: [CMS Medicare Beneficiary Identifiers](https://www.cms.gov/medicare/new-medicare-card)

To get everything working locally, run the following command to setup and run the project. This was created in a Linux environment. If running on Windows, the main difference should only be that instead of `cp` you would use `copy`.
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
flask run
```
