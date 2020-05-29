#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 Script to fill the MF DB tables
'''

# Connect to the DB 
import sqlalchemy as db
import scipy.io

# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

# print the tables names present in the DB: 
engine.table_names()

for user_i in range(1,10):
    
    folder_usr = '../webapp_taskdata/data/user_' + str(user_i) + '/'
    
    ###########################
    ###### Table: task  #######
    ###########################
    
    # Specify the table you want to insert the data into: 
    table  = db.Table('task', metadata, autoload=True, autoload_with=engine)
    
    #Inserting many records at ones
    query  = db.insert(table) 

    mat = scipy.io.loadmat(folder_usr + 'Task.mat')
    tab = mat.get("Task")
    for i in range(0,len(tab)):
         Tab = dict()
         Tab['UserNo']              = tab[i,0].tolist()
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
    
    # Specify the table you want to insert the data into: 
    table  = db.Table('training', metadata, autoload=True, autoload_with=engine)
    
    #Inserting many records at ones
    query  = db.insert(table) 

    mat = scipy.io.loadmat(folder_usr + 'Training.mat')
    tab = mat.get("Training")
    for i in range(0,len(tab)):
         Tab = dict()
         Tab['UserNo']              = tab[i,0].tolist()
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
         
         
        


