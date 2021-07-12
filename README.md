# Disaster_Response_Pipeline
This project will take messages from social media and use machine learning to determine if, and what type of response is needed for a potential disaster. This is to fulfill a project requirement for the Udacity Data Science nanodegree.

## Content
There are 3 main areas of this project, data, models, and app. 
- The data folder has a file called process_data.py. This file will first extract the data from two datasets. Next it will transform the data by cleaning it. Removing duplicate lines and then taking the categories column and splitting it up into individual columns and values. Finally, it will load the data into a database file. 
- The models folder contains train_classifier.py. This file loads in the data from the database file. It then uses a machine learning pipeline to build a simple yet respectable multioutput randomforesstclassdifier model. It then saves this file to be used in the app. 
- The app folder has a template folder which contains the HTML code for the website. It also has the run.py file that builds the app to predict user inputed messages. 

## Installing
- To run this project Click the green button above that say code to clone the project to your local machine using the method of your choice. 

## How to use
- Next, from the main foler and in the IDE of your choice, run the process_data.py file with ```python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db```. Assuming your have provide appropriate messages.csv and catergories.csv it will perform ETL and save as a database file. 
- Once the database file has been created, in the same manner as before, run the train_classifier.py file with ```python models/train_classifier.py data/DisasterResponse.db models/model_2.pkl```. (this make take up to 20 minutes) This will create a model pickle file.
- Now you have all the files your need. You can finally go to the app folder and just like before, run the run.py file with ```python app/run.py```. This will provide you a port ID which you can copy and paste into any web browse to view the app on your local machine. 

## File structure
- app
  - template
    - master.html # main page of web app
    - go.html # classification result page of web app
  - run.py # Flask file that runs app
- data
  - categories.csv # data to process
  - messages.csv # data to process
  - process_data.py
  - DisasterResponse.db # database to save clean data to
- models
  - train_classifier.py
  - model_2.pkl # saved model
- README.md

## Acknowledgements
Thank you to Figure Eight and Udacity for providing the data and project idea respectively. 

## Screenshots
When you first load up the page you are greeted with some overview of the data
![image](https://user-images.githubusercontent.com/58890965/125336168-4dd24e00-e302-11eb-9478-eff6be432f63.png)

Next there is an input box where you can enter a message to be evaluated
![image](https://user-images.githubusercontent.com/58890965/125336392-92f68000-e302-11eb-9e6d-8eb928a9c0f9.png)

You are then taken to the results page
![image](https://user-images.githubusercontent.com/58890965/125336497-b4576c00-e302-11eb-9e32-cbcea6219f05.png)


