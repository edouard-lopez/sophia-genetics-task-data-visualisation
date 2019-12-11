# User Usage Evolution Dataviz

* The database will be provisioned automatically it for you.
* Frontend display only first user data.
* Choosed a line chart in order to
  * see evolution and tendency
  * compare predicted vs. actual data

## Onboarding

In the project directory `task/`, you can run:

### Run

    make serve-backend
    make serve-frontend

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Tests

_todo_: end-to-end tests

#### Backend

    make test-backend

## User stories

### Simple Dataviz

* As a business manager
* Given a user's real usage data
* I want to see its usage evolution over the last 12 months

### Compare Real vs. Estimated Usage

* As a business manager
* Given a user's real and estimated data 
* I want to compare usage evolution over the last 12 months

### Add Backend

* As a data scientist
* I want to process data before sending them to the front

### Add Database

* As a data scientist
* I want to query my data
