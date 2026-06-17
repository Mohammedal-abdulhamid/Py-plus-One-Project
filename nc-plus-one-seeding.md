# 01 - Project Setup

**Goal:** Create your own copy of the project repository, clone it locally, and add a README.

## Steps

**1. Create your repository**

Navigate to the provided template repository. 

[Template Repository](https://github.com/northcoders/py-nc-plus-one)

Click **Use this template** and select **Create a new repository**.

When configuring the new repository:
- Set yourself as the owner
- Set the visibility to **Public** - this project will form part of your portfolio

> Do not fork the repository. Use the template button only.

**2. Clone the repository**

Once your repository has been created, clone it to your local machine:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

**3. Add a README**

Create or update `README.md` at the root of the project. It should briefly describe what the project is — what it does and what technologies it uses. This is the first thing a prospective employer will read.

Commit and push the README before moving on to the next ticket:

```bash
git add README.md
git commit -m "Add project README"
git push
```

## Acceptance criteria
- Your repository is public and listed under your own GitHub account
- The repository was created from the template, not forked
- A README exists at the root of the project and has been pushed


<br /><br />
---
<br /><br />


# 02 - Create the Database

**Goal:** Create a local PostgreSQL database and a SQL script that can reliably recreate it from scratch.

## Requirements

- Create a local database named `nc_plus_one`
- Create a SQL script at `db/setup.sql` that drops and recreates the database — this allows any developer to get a clean setup with a single command
- Update the README with a **Database Setup** section explaining how to run the script

## Acceptance criteria
- `nc_plus_one` database exists locally and can be connected to
- `db/setup.sql` exists and contains the drop and create statements
- The README documents how to run `db/setup.sql`


<br /><br />
---
<br /><br />


# 03 - Create the Seed Function

**Goal:** Create a `seed` function that will be responsible for resetting the database to a known initial state.

## Background

Production databases change constantly as users interact with them. For testing purposes, we need a database that is predictable - one we can reset to a fixed starting point before each test run so that expected outcomes are always consistent.

The `seed` function is responsible for three things, in order:

1. Removing any data from previous runs
2. Rebuilding the table schemas
3. Inserting the test data

Because these are distinct responsibilities, you are encouraged to break the implementation across several smaller functions rather than handling everything in one place.


![Database ERD](https://assets.northcoders.com/nc-plus-one-erd.png "520px 500px Database ERD")

## Requirements

- Review the ERD before writing any code — make sure you understand the tables, their columns, and how they relate to each other
- Create a `seed` function in an appropriate location within the project
- The function should be invocable directly, so the database can be reset at any point during development
- At this stage the function can be empty - functionality will be added in subsequent tickets

## Acceptance criteria
- The ERD has been reviewed and the database structure is understood before proceeding
- A `seed` function exists and can be invoked


<br /><br />
---
<br /><br />


# 04 - Database Connection

**Goal:** Create a reusable database connection object that reads credentials from environment variables rather than hardcoded values.

## Requirements

- Create a `connection.py` file that establishes a connection to `nc_plus_one`
- Credentials should be stored in a `.env` file and loaded using `python-dotenv` — they must not be hardcoded anywhere in the codebase
- Create a `.env.example` file containing the same keys but no values, so other developers know what credentials are required without exposing your own
- Add `.env` to `.gitignore` before making any commits — credentials must never be pushed to source control

## Acceptance criteria
- `connection.py` exists and successfully connects to `nc_plus_one`
- All credentials are loaded from `.env` via `python-dotenv`
- `.env` is present in `.gitignore`
- `.env.example` is committed to the repository with the required keys but no values
- Update `README.md` to explain that to other devs that a `.env` should be created with the individual's local database credentials


<br /><br />
---
<br /><br />


# 05 - Seed Users

**Goal:** Implement the users portion of the seed function — dropping, recreating, and populating the users table.

![Database ERD](https://assets.northcoders.com/nc-plus-one-erd.png "520px 500px Database ERD")

## Requirements

- Drop the users table if it exists
- Create the users table according to the schema defined in the ERD
- Read the user data from the JSON file in the `data` directory and bulk insert it into the newly created table
- Any utility functions written to normalise or manipulate data before insertion must be built using TDD

## A note on structure

This ticket adds real functionality to the seed function. As with the seed function itself, consider whether the logic is best handled in one place or broken down into smaller, focused functions. Each responsibility — dropping, creating, inserting — is a candidate for its own function.

## Acceptance criteria
- The users table is dropped and recreated each time the seed function runs
- All user records from the JSON file are inserted into the table
- Any data transformation logic lives in a utility function covered by TDD
- Running the seed function multiple times produces the same result with no errors


<br /><br />
---
<br /><br />


# 06 - Seed Venues

**Goal:** Implement the venues portion of the seed function — dropping, recreating, and populating the venues table.

![Database ERD](https://assets.northcoders.com/nc-plus-one-erd.png "520px 500px Database ERD")

## Requirements

- Drop the venues table if it exists
- Create the venues table according to the schema defined in the ERD
- Read the venue data from the JSON file in the `data` directory and bulk insert it into the newly created table
- Any utility functions written to normalise or manipulate data before insertion must be built using TDD

## A note on structure

This ticket adds real functionality to the seed function. As with the seed function itself, consider whether the logic is best handled in one place or broken down into smaller, focused functions. Each responsibility — dropping, creating, inserting — is a candidate for its own function.

## Acceptance criteria
- The venues table is dropped and recreated each time the seed function runs
- All venue records from the JSON file are inserted into the table
- Any data transformation logic lives in a utility function covered by TDD
- Running the seed function multiple times produces the same result with no errors


<br /><br />
---
<br /><br />


# 07 - Seed Events

**Goal:** Implement the events portion of the seed function — dropping, recreating, and populating the events table.

![Database ERD](https://assets.northcoders.com/nc-plus-one-erd.png "520px 500px Database ERD")

## Requirements

- Drop the events table if it exists
- Create the events table according to the schema defined in the ERD
- Read the event data from the JSON file in the `data` directory and bulk insert it into the newly created table
- Any utility functions written to normalise or manipulate data before insertion must be built using TDD

## A note on structure

This ticket adds real functionality to the seed function. As with the seed function itself, consider whether the logic is best handled in one place or broken down into smaller, focused functions. Each responsibility — dropping, creating, inserting — is a candidate for its own function.

## Acceptance criteria
- The events table is dropped and recreated each time the seed function runs
- All event records from the JSON file are inserted into the table
- Any data transformation logic lives in a utility function covered by TDD
- Running the seed function multiple times produces the same result with no errors


<br /><br />
---
<br /><br />


# 08 - Seed RSVPs

**Goal:** Implement the RSVPs portion of the seed function — dropping, recreating, and populating the RSVPs table.

![Database ERD](https://assets.northcoders.com/nc-plus-one-erd.png "520px 500px Database ERD")

## Requirements

- Drop the RSVPs table if it exists
- Create the RSVPs table according to the schema defined in the ERD
- Read the RSVP data from the JSON file in the `data` directory and bulk insert it into the newly created table
- Any utility functions written to normalise or manipulate data before insertion must be built using TDD

## A note on structure

This ticket adds real functionality to the seed function. As with the seed function itself, consider whether the logic is best handled in one place or broken down into smaller, focused functions. Each responsibility — dropping, creating, inserting — is a candidate for its own function.

## Acceptance criteria
- The RSVPs table is dropped and recreated each time the seed function runs
- All RSVP records from the JSON file are inserted into the table
- Any data transformation logic lives in a utility function covered by TDD
- Running the seed function multiple times produces the same result with no errors
