   <h1>nc_plus_one-db Database <h1>

  <h2>Overview</h2>
  this project is a backend that manages users, events, venues, and RSVPs.
  It demonstrates how to design and build a relational database-backed application using Python and PostgreSQL, including database setup, schema creation, and data seeding from JSON files.
   
   The project follows a structured workflow:

    - Create and reset the PostgreSQL database
    - Define relational tables with foreign keys
    - Seed the database with sample data
    - Prepare the system for backend development
   extended taask: creating API and endpoint to retrive data from each table using psycopg 


    Features
      Create and drop PostgreSQL databases programmatically
      Define relational database schema (users, events, venues, RSVPs)
      Manage relationships using foreign keys
      Seed database with JSON data
      Modular Python scripts for database operations
      
   <h1>setup</h1>
   
   Creating Github repository.<nc_plus_one_project>

   creating Database nc_plus_one-db. using the sql command : CREATE DATABASE nc_plus_one_project;
   create SQL setup.sql file that drops existing database if existed and creating database nc_plus_one-db and scheema 

   create tables in scheema.sql

   create seed.sql file that insert data into tables.

   connect to database nc_plus_one-db

   How to run setup

   from terminal psql -d nc_plus_one_project -f db/setup.sql
    or
    from psql terminal 
    connect to nc_plus_one_project
    \c nc_plus_one_project
    #nc_plus_one_project
    
    

   <h2>Technology</h2>

   this project mainly uses SQL 

   Application

create .env file and add credentials 
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

configure connection.py with required credentials and establish connection to the database.


connection 

established connection using cridential in .env file

database setup

drop exixting database and re-creating it in setup file
constract scheema b dropping existing tables and creating new ones

Seed Function

creating automatic seeding function that given a path and table name and it will seed any table accordingly.



   
