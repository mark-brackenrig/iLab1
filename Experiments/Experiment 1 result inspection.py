# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:17:21 2018

@author: mbrackenrig
"""
import os
os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository')

from setup import Subjects, subjectfaculty

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository/Experiments/Results')

import pandas
Experiment_1_Results = pandas.read_csv("Experiment_1_Results.csv")


Resultsbyfac = Experiment_1_Results.merge(subjectfaculty, "inner", left_on ="UTS_code", right_on="subject")

print(Resultsbyfac.groupby(["faculty"]).agg(["count"]))

print(Resultsbyfac.groupby(["faculty"]).agg(["count"]))

print(subjectfaculty.groupby(["faculty"]).agg(["count"]))



Resultsbyfac.groupby(["UTS_code"]).agg(["count"]).to_csv("Most_common.csv")
