# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 12:52:35 2018

@author: mbrackenrig
"""

#Firstly change the wording directory to the codebase
import os

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab')
#Lets see whats in the directory

Ontology = os.listdir("Ontology")

#read CSVs into environment
import pandas

broaderRelationsOccPillar = pandas.read_csv("Ontology/broaderRelationsOccPillar.csv")

broaderRelationsSkillPillar = pandas.read_csv("Ontology/broaderRelationsSkillPillar.csv")

ISCOGroups = pandas.read_csv("Ontology/ISCOGroups_en.csv")

occupationSkillRelations = pandas.read_csv("Ontology/occupationSkillRelations.csv")

occupations = pandas.read_csv("Ontology/occupations_en.csv")

skillGroups = pandas.read_csv("Ontology/skillGroups_en.csv")

skills = pandas.read_csv("Ontology/skills_en.csv")

#Inspect Columns
#broaderRelationsOccPillar[0:6]
#broaderRelationsSkillPillar[0:6] 
#ISCOGroups[0:6]
#occupationSkillRelations[0:6]
#occupations[0:6]
#skillGroups[0:6]
#skills[0:6]


#See unique Values of concept type
#set(skills.conceptType)
#set(skillGroups.conceptType)
#set(occupations.conceptType)
#set(broaderRelationsOccPillar.conceptType)

#Lets read the SLOs and CILOs

CILOs = pandas.read_csv("Subject Data/CILOs.csv")

SLOs = pandas.read_csv("Subject Data/SLOs.csv")

Subjects = pandas.read_csv("Subject Data/Subjects.csv")

print("hello world!")
