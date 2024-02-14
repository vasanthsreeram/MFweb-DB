#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 Script to fill the MF DB tables
'''
# Connect to the DB 
import sqlalchemy as db
import scipy.io
from sqlalchemy import inspect
import time,os
from sqlalchemy.exc import SQLAlchemyError

# Establish the connection with the DB: 
username = "gridgame"
password = "J35pZyjo9kLQjh"
server = "clic.database.windows.net"
database = "clic"

# Variables to modify:
# Warning make sure that these two vaules are the same as the ones in the matlab code if not it will break!
task_range = 101 # number of tasks to insert in the DB
training_range = 101 # number of trainings to insert in the DB  



db_uri = f"mssql+pymssql://{username}:{password}@{server}/{database}"
engine     = db.create_engine(db_uri, echo = True)
metadata   = db.MetaData()
connection = engine.connect()

# print the tables names present in the DB: 
inspector = inspect(engine)
print(inspector.get_table_names())

# Clearing the tables before inserting new data
try:
    connection.execute(db.delete(db.Table('task', metadata, autoload_with=engine)))
    connection.execute(db.delete(db.Table('training', metadata, autoload_with=engine)))
    print("Cleared existing data from tables.")
except SQLAlchemyError as e:
    print("Error occurred while clearing tables:", e)
    connection.rollback()
    exit()

for task_no in range(1,task_range): 
    # modify the range to insert the data for a specific task
    
    folder_usr = '../data/generative/tasks/task_' + str(task_no) + '/'
    file_path = os.path.abspath(folder_usr + 'Task.mat')
    print("Looking for file at:", file_path)

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        continue

    ###########################
    ###### Table: task  #######
    ###########################
    
    # Specify the table you want to insert the data into: 
    table  = db.Table('task', metadata, autoload_with=engine)
    
    #Inserting many records at ones
    query  = db.insert(table) 

    mat = scipy.io.loadmat(folder_usr + 'Task.mat')
    tab = mat.get("Task")
    for i in range(0,len(tab)):
         Tab = dict()
         Tab['TaskNo']              = tab[i,0].tolist()
         Tab['TrialNo']             = tab[i,1].tolist()
         Tab['BlockNo']             = tab[i,2].tolist()
         Tab['Horizon']             = tab[i,3].tolist()
         Tab['ItemNo']              = tab[i,4].tolist()
         Tab['InitialSampleNb']     = tab[i,5].tolist()
         Tab['UnusedTree']          = tab[i,6].tolist()      
         Tab['DisplayOrder1']       = tab[i,7].tolist()
         Tab['DisplayOrder2']       = tab[i,8].tolist()
         Tab['DisplayOrder3']       = tab[i,9].tolist()     
         Tab['TreePositions1']      = tab[i,10].tolist()
         Tab['TreePositions2']      = tab[i,11].tolist()
         Tab['TreePositions3']      = tab[i,12].tolist()
         Tab['TreePositions4']      = tab[i,13].tolist()       
         Tab['InitialSample1Tree']  = tab[i,14].tolist()
         Tab['InitialSample2Tree']  = tab[i,15].tolist()
         Tab['InitialSample3Tree']  = tab[i,16].tolist()
         Tab['InitialSample4Tree']  = tab[i,17].tolist()
         Tab['InitialSample5Tree']  = tab[i,18].tolist()
         Tab['InitialSample1Size']  = tab[i,19].tolist()
         Tab['InitialSample2Size']  = tab[i,20].tolist()
         Tab['InitialSample3Size']  = tab[i,21].tolist()
         Tab['InitialSample4Size']  = tab[i,22].tolist()
         Tab['InitialSample5Size']  = tab[i,23].tolist()
         Tab['Tree1FutureSize1']    = tab[i,24].tolist()
         Tab['Tree1FutureSize2']    = tab[i,25].tolist()
         Tab['Tree1FutureSize3']    = tab[i,26].tolist()
         Tab['Tree1FutureSize4']    = tab[i,27].tolist()
         Tab['Tree1FutureSize5']    = tab[i,28].tolist()
         Tab['Tree1FutureSize6']    = tab[i,29].tolist()
         Tab['Tree2FutureSize1']    = tab[i,30].tolist()
         Tab['Tree2FutureSize2']    = tab[i,31].tolist()
         Tab['Tree2FutureSize3']    = tab[i,32].tolist()
         Tab['Tree2FutureSize4']    = tab[i,33].tolist()
         Tab['Tree2FutureSize5']    = tab[i,34].tolist()
         Tab['Tree2FutureSize6']    = tab[i,35].tolist()
         Tab['Tree3FutureSize1']    = tab[i,36].tolist()
         Tab['Tree3FutureSize2']    = tab[i,37].tolist()
         Tab['Tree3FutureSize3']    = tab[i,38].tolist()
         Tab['Tree3FutureSize4']    = tab[i,39].tolist()
         Tab['Tree3FutureSize5']    = tab[i,40].tolist()
         Tab['Tree3FutureSize6']    = tab[i,41].tolist()
         Tab['Tree4FutureSize1']    = tab[i,42].tolist()
         Tab['Tree4FutureSize2']    = tab[i,43].tolist()
         Tab['Tree4FutureSize3']    = tab[i,44].tolist()
         Tab['Tree4FutureSize4']    = tab[i,45].tolist()
         Tab['Tree4FutureSize5']    = tab[i,46].tolist()
         Tab['Tree4FutureSize6']    = tab[i,47].tolist()
         values_list = [Tab]
         ResultProxy = connection.execute(query,values_list)
   
    ###############################
    ###### Table: training  #######
    ###############################
    
for training_no in range(1,training_range):
    
    folder_usr = '../data/generative/trainings/training_' + str(training_no) + '/'
    print(folder_usr)

    # Specify the table you want to insert the data into: 
    table  = db.Table('training', metadata, autoload_with=engine)
    
    #Inserting many records at ones
    query  = db.insert(table) 

    mat = scipy.io.loadmat(folder_usr + 'Training.mat')
    tab = mat.get("Training")
    for i in range(0,len(tab)):
         Tab = dict()
         Tab['TrainingNo']          = tab[i,0].tolist()
         Tab['TrialNo']             = tab[i,1].tolist()
         Tab['InitialSample1Size']  = tab[i,2].tolist()
         Tab['InitialSample2Size']  = tab[i,3].tolist()
         Tab['InitialSample3Size']  = tab[i,4].tolist()
         Tab['Choice1Size']         = tab[i,5].tolist()
         Tab['Choice2Size']         = tab[i,6].tolist()
         Tab['Choice1Correct']      = tab[i,7].tolist()
         Tab['Choice2Correct']      = tab[i,8].tolist()
      
         values_list = [Tab]
         ResultProxy = connection.execute(query,values_list)
         
         
        


try:
    # ... your existing code for data insertion ...

    # Commit the transaction
    connection.commit()

except SQLAlchemyError as e:
    print("Error occurred:", e)
    connection.rollback() 