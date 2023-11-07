# I used the official PostgreSQL image as the base image

# Sets up the base image for PostgreSQL 
FROM postgres:latest

# Define PostgreSQL environment variables
ENV POSTGRES_DB daredatachallenge
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_READ_ONLY_USER ds_user
ENV POSTGRES_READ_ONLY_PASSWORD ds_user


# Install PostgreSQL dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Copy the initialization scripts
COPY modules/de/db_admin/*.sql /docker-entrypoint-initdb.d/

# Copy the data loading scripts
COPY modules/de/load/*.csv /docker-entrypoint-initdb.d/
COPY modules/de/load/*.sql /docker-entrypoint-initdb.d/
