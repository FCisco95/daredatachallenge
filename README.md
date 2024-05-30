# Technical Assessment

## Introduction

In this technical assessment, you will simulate a model deployment end-to-end: 

* In this challenge, you should train your own data science model, as well as handle a simple setting up of a database (where all input data should come from) and serve new predictions using an API (assuming this is a simple deployment).

You will be mainly working on three parts of a system:

* Setting up a containerized database server using Docker - de module.
* Building a Machine Learning Model using a dataset at your choosing - de module.
* Serving that model using an API framework (for bonus points, deploy it in the cloud!) - deployment module.

For this challenge, we want you to head to Google Dataset Search (https://datasetsearch.research.google.com/) and choose a dataset that you want to work on - when choosing the data set make sure that you are able to find a problem where you can build some type of predictive model (supervised learning) on top of the data. Other than that, the only mandatory requirements regarding the data are:

* The dataset can't be from Kaggle.
* It must be the first time you are looking into that dataset.

This challenge will require three things:

`de`: setting up a simple instance of a database at your choosing. Your database must be set up in a containerized application.
<br>
`ds`: the data science module, where you will deliver a notebook with all the findings about your data and the model you've decided to build, using a target variable at your choosing. Make sure that you manage time carefully in the ds module - we prefer that you show a coherent and structured pipeline than using a really convoluted model.
<br>
`deployment`: this module handles the deployment of the final model using an API service (your API can be served locally, or, if you want to take it further, you can serve it up using any cloud provider).
<br>
We recommend you to read this entire document, as well as each module's documentation before starting.

## Instructions

### Task 1 - Set up a database and load your data.

Your data file should be loaded into a database server (MySQL, PostGres, etc.). You don't need to set up any relational model or complex relationships between the data - just load the CSV or XLSX file into a table format that you can query later in your notebook.

The idea here is that you should be able to work comfortably with SQL instances and be able to understand how to set up and communicate with a database server.

### Task 2 - Build EDA and Model

You should be able to deliver a normal EDA, analysis and model pipeline. In the notebook, we are expecting:

* Exploratory Data Analysis with some statistics and analysis regarding the dataset you've choose and and explanations regarding the model you decided to go with. 
* The model must be supervised.
* During model development, make sure that your code should be able to run outside of a notebook environment. 
* This should be important for Task #3.
* The data you load into the notebook must come from the containerized Docker application. 
* This means that you must use sql queries to your database server to extract the data and can't load it via normal pd.read_csv or pd.read_excel.

### Task 3 - Deploy Model

After developing your model in Task 2, serve it using any API framework you know. The API should have an endpoint predict that is able to obtain predictions for new data points. Add a playbook example of your API and make sure to develop a couple of simple tests to it.

## How to Share Your Challenge Solution

After you finish your challenge, you should do the following in order to share the solution with us:

* create a private Git repository, adding your solution to the main branch.
* share your repo with
* include a SOLUTION.md file at the root of the repository. This file should contain:
* a quick description of the final solution. Feel free to use diagrams, charts, etc. to illustrate your implementation. Mostly, we will be looking at this file and the notebook of model development.
* a detailed timeline of the implementation: time taken for each task, implementation order, etc.
* documentation about design decisions taken (and motives behind them), difficulties faced, and any other thoughts you think are relevant.

## Evaluation Checklist

Here is a checklist to help you keep track of the deliverables:
- [ ]  Fully implement a database server.
- [ ]  Build and explain a data science predictive model.
- [ ]  Deploy the model via API.
- [ ]  Include a SOLUTION.md document in the root of the repository, containing:
- [ ]  A description of the final solution and deployment, decisions taken, etc.
- [ ]  Screenshots of the deployed model in action
- [ ]  A high-level implementation timeline

Other than that, it's also important to have:
* clean and "dry" code.
* a well structured repository.

Good luck and we hope you enjoy this challenge!
