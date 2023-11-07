# DE Module

## Docker Containers

### Operational DB
Set up a database with a name at your choice and define a user to be able to access the data inside your notebook.

Example:
- Host: local
- Port: 5432
- Default Login: user_ds / pwd
- Database Name: daredatachallenge

## Folder Structure

* `db_admin`: contains the configuration SQL files that run upon starting the database for the first time. Used to create the users, for example.
* `load`: contains the SQL files to load csv or excel files into the database.
* `docker`: configures the Docker image for the SQL database -> Database connection.
