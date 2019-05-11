# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:01:47 2019

pcode region,province,muncicity,pov 2006,2009,2012
wht is avg pov for all yers
avg pov  2012 each region
find outlier in each column replce with avg
replce any missng value or na with avg

@author: puPpy
"""

import numpy as np
import pandas as pd
povertyestimatesimport=pd.read_csv('C:\\Users\puPpy\Downloads\povertyestimates.csv',header=0)
#print(povertyestimatesimport)
povertyestimates=povertyestimatesimport.loc[:,['PCODE','Region','Province','Municipality_City','Pov_2006','Pov_2009','Pov_2012',]]
povertyestimatesClean=povertyestimates.convert_objects(convert_dates='coerce', convert_numeric=True)
#df.convert_objects(convert_dates='coerce', convert_numeric=True)
#test=povertyestimatesClean.loc[1467:,'Pov_2006']
povertyestimatesClean2=povertyestimatesClean.fillna(povertyestimatesClean.mean())
test=povertyestimatesClean2.loc[1467:,'Pov_2006']
print("@@@@@@@@@@@@@@@@@@@@@@@===================================")
print("@@@@@@@@@@@@@@@@@@@@@@@@@=")
print(test)
povertyestimatesTransposePovyear=povertyestimatesClean2.melt(id_vars=['PCODE','Region','Province','Municipality_City'])
print(povertyestimatesTransposePovyear)
newcust=povertyestimatesTransposePovyear.loc[:,['variable','value']]
print(newcust.value.dtype)
##print(newcust)
povertyestimatesTransposePovyearAvg=povertyestimatesTransposePovyear.groupby('variable')
##print(povertyestimatesTransposePovyearAvg)
povertyestimatesTransposePovyearAvgY=povertyestimatesTransposePovyearAvg.aggregate({'value':np.mean})
##povertyestimatesTransposePovyearAvgYear=povertyestimatesTransposePovyearAvg.aggregate({'value':np.mean})
print(povertyestimatesTransposePovyearAvgY)
#
print("===================================")
print("===================================")
print(povertyestimates['Pov_2012'].mean())
povertyestimates2012group=povertyestimates.groupby('Region')
povertyestimates2012=povertyestimates2012group.aggregate({'Pov_2012':np.mean})
print("===================================")
print(povertyestimates2012)
