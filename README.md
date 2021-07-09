# Disater_Response_Pipeline
This project will take messages from social media and use machine learning to determine if, and what type of response is needed for a potential disaster. This is to fulfill a project requirement for the Udacity Data Science nanodegree.

## Content
There are 3 main areas of this project, data, models, and app. 
- The data folder has a file called process_data.py. This file will first extract the data from two datasets. Next it will transform the data by cleaning it. Removing duplicate lines and then taking the categories column and splitting it up into individual columns and values. Finally, it will load the data into a database file. 
- The models folder contains train_classifier.py. This file loads in the data from the database file. It then uses a machine learning pipeline to build a simple yet respectable multioutput randomforesstclassdifier model. It then saves this file to be used in the app. 
- The app folder has a template folder which contains the HTML code for the website. It also has the run.py file that builds the app to predict user inputed messages. 

## How to use
To run this project first clone it to your local machine. Starting the in the data folder, run the process_data.py file to create the database. Next, head over to the models folder and run the train_classifier.py file to make and save a model (this might take 10-20 minutes depending on your PC). Finally, open the app folder and run run.py. This will prompt your with a port number you can copy over into a browser to view the app functionality. From there, type in a message and the program will tell you what type of services will be required. 
