   nc_plus_one-db Database 

  Overview:
   Creating database from sctach creating tables and sseding them with data then connect to it and apply some SQL queries.

   setup
   Creating Github repository.<nc_plus_one_project>

   creating Database nc_plus_one-db. using the sql command : CREATE DATABASE nc_plus_one_project;
   create SQL setup.sql file that drops existing database if existed and creating database nc_plus_one-db and scheema 

   create seed.sql file that insert data into tables.

   connect to database nc_plus_one-db

   How to run setup

   from terminal psql -d nc_plus_one_project -f db/setup.sql
    or
    from psql terminal 
    connect to nc_plus_one_project
    \c nc_plus_one_project
    #nc_plus_one_project
    
    

   Technology:

   this project mainly uses SQL 

   