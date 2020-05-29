#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 Script to create the MF DB tables
 
'''

# Connect to the DB 
import sqlalchemy as db
from sqlalchemy import VARCHAR, ARRAY

# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'task', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   db.Column('TrialNo', db.Integer), 
   db.Column('BlockNo', db.Integer), 
   db.Column('Horizon', db.Integer), 
   db.Column('ItemNo', db.Integer), 
   db.Column('InitialSampleNb', db.Integer),
   db.Column('UnusedTree', db.Integer),
   
   db.Column('DisplayOrder1', db.Integer),
   db.Column('DisplayOrder2', db.Integer),
   db.Column('DisplayOrder3', db.Integer),    
   
   db.Column('TreePositions1', db.Integer),
   db.Column('TreePositions2', db.Integer),
   db.Column('TreePositions3', db.Integer),
   db.Column('TreePositions4', db.Integer),  
   
   db.Column('InitialSample1Tree', db.Integer),
   db.Column('InitialSample2Tree', db.Integer),
   db.Column('InitialSample3Tree', db.Integer),
   db.Column('InitialSample4Tree', db.Integer),
   db.Column('InitialSample5Tree', db.Integer),
   
   db.Column('InitialSample1Size', db.Integer),
   db.Column('InitialSample2Size', db.Integer),
   db.Column('InitialSample3Size', db.Integer),
   db.Column('InitialSample4Size', db.Integer),
   db.Column('InitialSample5Size', db.Integer),
   
   db.Column('Tree1FutureSize1', db.Integer),
   db.Column('Tree1FutureSize2', db.Integer),
   db.Column('Tree1FutureSize3', db.Integer),
   db.Column('Tree1FutureSize4', db.Integer),
   db.Column('Tree1FutureSize5', db.Integer),
   db.Column('Tree1FutureSize6', db.Integer),
   
   db.Column('Tree2FutureSize1', db.Integer),
   db.Column('Tree2FutureSize2', db.Integer),
   db.Column('Tree2FutureSize3', db.Integer),
   db.Column('Tree2FutureSize4', db.Integer),
   db.Column('Tree2FutureSize5', db.Integer),
   db.Column('Tree2FutureSize6', db.Integer),
    
   db.Column('Tree3FutureSize1', db.Integer),
   db.Column('Tree3FutureSize2', db.Integer),
   db.Column('Tree3FutureSize3', db.Integer),
   db.Column('Tree3FutureSize4', db.Integer),
   db.Column('Tree3FutureSize5', db.Integer),
   db.Column('Tree3FutureSize6', db.Integer),
   
   db.Column('Tree4FutureSize1', db.Integer),
   db.Column('Tree4FutureSize2', db.Integer),
   db.Column('Tree4FutureSize3', db.Integer),
   db.Column('Tree4FutureSize4', db.Integer),
   db.Column('Tree4FutureSize5', db.Integer),
   db.Column('Tree4FutureSize6', db.Integer),  
   
)
metadata.create_all(engine)


# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'training', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   db.Column('TrialNo', db.Integer), 
   
   db.Column('InitialSample1Size', db.Integer),
   db.Column('InitialSample2Size', db.Integer),
   db.Column('InitialSample3Size', db.Integer),
   
   db.Column('Choice1Size', db.Integer),
   db.Column('Choice2Size', db.Integer),
   db.Column('Choice1Correct', db.Integer),
   db.Column('Choice2Correct', db.Integer),
   
)

metadata.create_all(engine)


# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'behaviour', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   db.Column('BlockNo', db.Integer), 
   db.Column('BlockStartTime', db.Text(length=10000)), 
   db.Column('BlockFinishTime', db.Text(length=10000)), 
   db.Column('TreeColours', db.Text(length=10000)), 
   db.Column('ChosenTree', db.Text(length=10000)), 
   db.Column('ChosenAppleSize', db.Text(length=10000)), 
   db.Column('AllKeyPressed', db.Text(length=10000)), 
   db.Column('ReactionTimes', db.Text(length=10000)), 
   db.Column('Horizon', db.Text(length=10000)), 
   db.Column('ItemNo', db.Text(length=10000)), 
   db.Column('TrialNo', db.Text(length=10000)), 
   db.Column('UnusedTree', db.Text(length=10000)), 
   db.Column('InitialSamplesNb', db.Text(length=10000)), 
   db.Column('InitialSamplesTree', db.Text(length=10000)), 
   db.Column('InitialSamplesSize', db.Text(length=10000)), 
   db.Column('TreePositions', db.Text(length=10000)),
)

metadata.create_all(engine)


# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'training_behaviour', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   db.Column('TrainingStartTime', db.Text(length=10000)), 
   db.Column('TrainingFinishTime', db.Text(length=10000)), 
   db.Column('SumPassed', db.Text(length=10000)), 
   db.Column('ChoicesSize', db.Text(length=10000)), 
   db.Column('InitialSamplesSize', db.Text(length=10000)), 
   db.Column('ChoicesCorrect', db.Text(length=10000)), 
   db.Column('ReactionTimes', db.Text(length=10000)), 
   db.Column('Chosen', db.Text(length=10000)), 
   db.Column('CorrectAns', db.Text(length=10000)), 
   db.Column('NumTraining', db.Text(length=10000)), 
)

metadata.create_all(engine)


# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'questions_behaviour', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   db.Column('InstructionsStartTime', db.Text(length=10000)), 
   db.Column('QuestionsStartTime', db.Text(length=10000)), 
   db.Column('QuestionsFinishTime', db.Text(length=10000)), 
   db.Column('SumPassed', db.Text(length=10000)), 
   db.Column('PressedKeys', db.Text(length=10000)), 
   db.Column('PercentagePassed', db.Text(length=10000)), 
   db.Column('ReactionTimes', db.Text(length=10000)), 
   db.Column('Correct', db.Text(length=10000)),
)

metadata.create_all(engine)



# Establish the connection with the DB: 
engine     = db.create_engine('mysql+pymysql://root:123456??@localhost/MF', echo = True)
metadata   = db.MetaData()
connection = engine.connect()

db.Table(
    'questionnaires_behaviour', metadata, 
    
   db.Column('id', db.Integer, primary_key = True), 
   db.Column('UserNo', db.Integer), 
   
   db.Column('Date', db.Text(length=10000)), 
   db.Column('StartTime', db.Text(length=10000)), 
   db.Column('FinishTime', db.Text(length=10000)), 
   
   db.Column('PageNo0', db.Text(length=10000)), 
   db.Column('PageNo1', db.Text(length=10000)),
   db.Column('PageNo2', db.Text(length=10000)),
   db.Column('PageNo3', db.Text(length=10000)),
   db.Column('PageNo4', db.Text(length=10000)),
   db.Column('PageNo5', db.Text(length=10000)),
   
   db.Column('IQ_1', db.Text(length=10000)),
   db.Column('IQ_2', db.Text(length=10000)),
   db.Column('IQ_3', db.Text(length=10000)),
   db.Column('IQ_4', db.Text(length=10000)),
   db.Column('IQ_5', db.Text(length=10000)),
   db.Column('IQ_6', db.Text(length=10000)),
   db.Column('IQ_7', db.Text(length=10000)),
   db.Column('IQ_8', db.Text(length=10000)),
   
   db.Column('IQimage_1', db.Text(length=10000)),
   db.Column('IQimage_2', db.Text(length=10000)),
   db.Column('IQimage_3', db.Text(length=10000)),
   db.Column('IQimage_4', db.Text(length=10000)),
   db.Column('IQimage_5', db.Text(length=10000)),
   db.Column('IQimage_6', db.Text(length=10000)),
   db.Column('IQimage_7', db.Text(length=10000)),
   db.Column('IQimage_8', db.Text(length=10000)),
   
   db.Column('ASRS', db.Text(length=10000)),
   db.Column('BIS11', db.Text(length=10000)),
   db.Column('IUS', db.Text(length=10000)),

)

metadata.create_all(engine)