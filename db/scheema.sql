
DROP TABLE IF EXISTS rsvps CASCADE ;
DROP TABLE IF EXISTS events CASCADE ;
DROP TABLE IF EXISTS venues CASCADE ;
DROP TABLE IF EXISTS users CASCADE ;





CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);



CREATE TABLE venues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT ,
    capacity INT
);




CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    starts_at  TIMESTAMPTZ NOT NULL,
    ends_at  TIMESTAMPTZ NOT NULL,
    organiser_id INT,
    venue_id INT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE rsvps (
    id SERIAL PRIMARY KEY,
    attendee_id INT,
    event_id INT,
    created_at TIMESTAMPTZ DEFAULT NOW()
    
   
);


