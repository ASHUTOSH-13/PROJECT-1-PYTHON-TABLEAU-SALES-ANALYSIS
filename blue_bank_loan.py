# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 21:42:23 2023

@author: Ashutosh Bhatt
"""

#THIS PROJECT BASICALLY BASED ON A BANK NAMED BLUE BANK THAT GIVES LOAN TO THE COSTOMERS 
#AND KEEPS THE RECORD IN A JSON FILE SO WHAT WE WILL BE DOING IS THAT, SINCE WE KNOW THAT 
#PYTHON HAS A LIBRARY THAT CAN READ THIS TYPE OF FILE ...

import json

import pandas as pd

import numpy as num

import matplotlib.pyplot as plt

#METHOD 1 TO READ JSON FILE 

json_file = open('loan_data_json.json')
data = json.load(json_file)

#METHOD 2 TO READ JSON FILE 

with open('loan_data_json.json') as json_file :
    
    data = json.load(json_file)

#transform to dataframe 
loandata = pd.DataFrame(data)

#finding unique value for the purpose of loan 

loandata['purpose'].unique()

#discribing the data 

loandata.describe()

#describe the data for a specific column

loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using exp to get the annual income 

income =num.exp(loandata['log.annual.inc'])

loandata['annual income'] = income 






length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    if category>=300 and category < 400 :
      cat = 'very poor'
    elif category>=400 and category< 600 :
      cat = 'poor'
    elif category>=600 and category< 668 :
     cat = 'fair'

    elif category>=668 and category< 700 :
     cat = 'good'
    elif category>=700 :
        cat = 'excellent'
    else:
        cat ='unknown'
    ficocat.append(cat) 

    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat




#df.loc for conditional statement 

# a new column is needed for interest rate if int. rate>.12 then high else low 

loandata.loc[loandata['int.rate']>0.12, 'interest rate type'] = 'High'
loandata.loc[loandata['int.rate']<0.12, 'interest rate type'] = 'Low'


# number of loan rows by fico.category 

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'red', width = 0.3)
plt.show()
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.3)
plt.show()

#scattered plot 

ypoint = loandata['annual income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

# writing to csv 

loandata.to_csv('blue_bank_loan_cleaned.csv', index = True)




















































































