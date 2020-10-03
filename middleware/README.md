# Middleware

Middleware for the 'MyBudget' application.

## Run Locally

To run locally you will need to
1. Have a postrge server running with the schema provided in `../db/scripts/generate_tables.sql`
2. Ensure you have docker desktop installed.
3. Create an env file for the variables referenced in `api/repository.py` or simply hardcode those variables yourself. These will be used to access your postgre instance.
4. `cd` into `middleware`
5. `docker-compose build`
6. `docker-compose up`

Voila! You should have a two containers running. To hit the endpoints in the api via nginx go to `http://0.0.0.0:80`. If you want to hit the api container directly go to `http://0.0.0.0:5000`.