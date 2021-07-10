# Disaster_Response_Pipeline
This project will take messages from social media and use machine learning to determine if, and what type of response is needed for a potential disaster. This is to fulfill a project requirement for the Udacity Data Science nanodegree.

## Content
There are 3 main areas of this project, data, models, and app. 
- The data folder has a file called process_data.py. This file will first extract the data from two datasets. Next it will transform the data by cleaning it. Removing duplicate lines and then taking the categories column and splitting it up into individual columns and values. Finally, it will load the data into a database file. 
- The models folder contains train_classifier.py. This file loads in the data from the database file. It then uses a machine learning pipeline to build a simple yet respectable multioutput randomforesstclassdifier model. It then saves this file to be used in the app. 
- The app folder has a template folder which contains the HTML code for the website. It also has the run.py file that builds the app to predict user inputed messages. 

## How to use
- To run this project first clone the project to your local machine. 
- Next, from the main foler and in the IDE of your choice, run the process_data.py file with ```python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db```. Assuming your have provide appropriate messages.csv and catergories.csv it will perform ETL and save as a database file. 
- Once the database file has been created, in the same manner as before, run the train_classifier.py file with ```python models/train_classifier.py data/DisasterResponse.db models/model_2.pkl```. (this make take up to 20 minutes) This will create a model pickle file.
- Now you have all the files your need. You can finally go to the app folder and just like before, run the run.py file. This will provide you a port ID which you can copy and paste into any web browse to view the app on your local machine. 

## File structure
- app
| - template
| |- master.html # main page of web app
| |- go.html # classification result page of web app
|- run.py # Flask file that runs app
- data
|- disaster_categories.csv # data to process
|- disaster_messages.csv # data to process
|- process_data.py
|- InsertDatabaseName.db # database to save clean data to
- models
|- train_classifier.py
|- classifier.pkl # saved model
- README.md
