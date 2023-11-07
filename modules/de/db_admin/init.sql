-- Create a user named 'admin' with full privileges for the database if it doesn't exist
DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'admin') THEN
    CREATE USER admin WITH PASSWORD 'admin';
    GRANT ALL PRIVILEGES ON DATABASE daredatachallenge TO admin;
  END IF;
END $$;

-- Create a user named 'ds_user' with read-only access to the database if it doesn't exist
DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'ds_user') THEN
    CREATE USER ds_user WITH PASSWORD 'ds_user';
    GRANT CONNECT ON DATABASE daredatachallenge TO ds_user;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON SEQUENCES TO ds_user;
  END IF;
END $$;
