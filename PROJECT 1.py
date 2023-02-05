# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:13:19 2023

@author: Ashutosh Bhatt
"""

import pandas as pd

# file_name=pd.read_csv('file.csv')
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

#summary of the data 
data.info()

# working with calculation
# defining variables 

CostPerItem=11.73

SellingPricePerItem = 21.11

NumberOfItemPurchased = 6

#mathematical operation on tableau

ProfitPerItem = 21.11 - 11.73

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to the dataframe 

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per transaction

data['SalesPerTransaction'] =  data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation
 #     sales -cost
 
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


#markup = (sales-cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup'] = (data['SalesPerTransaction']) / data['CostPerTransaction']

#rounding markup 
roundmarkup = round(data['Markup'] , 2)
data['Markup'] = round(data['Markup'], 2)

#combining data field

my_name = 'ASHUTOSH' + 'BHATT'

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

print(data['Day'].dtype)

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)





my_date = day + '-' + data['Month'] + '-' + year
data['date'] = my_date

#using iloc for specific column or rows 

data.iloc[0] #view the row with number 0

data.iloc[0:3] #views first three rows 
data.loc[-5:] #views the last five rows 

data.head(5) #brings in first five rows 


data.iloc[:,2] #it brings all rows but specific column 

data.iloc[4,2] #it will bring fourth row and second column 

#this time we are going to do data spliting and replacing 

#new_var =column.str.split('sep' , expand =true)

split_col = data['ClientKeywords'].str.split(',' , expand=True)


#creating neww column for the split column in the column variable 
data['ClientAge'] = split_col[0]
data['Clienttype'] = split_col[1]
data['LengthofContract'] = split_col[2]


#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthofContract'] =data['LengthofContract'].str.replace(']', '')

#using the lowercase function to change the item to lowercse

data['ItemDescription'] = data['ItemDescription'].str.lower()

#joining the data set together two different files or it is called merging in python 

seasons= pd.read_csv ('value_inc_seasons.csv', sep=';')

data = pd.merge(data , seasons , on ='Month')

#dropping  the column in python 

data = data.drop('ClientKeywords' , axis =1 )
data = data.drop('Day' , axis= 1)

data = data.drop(['Year' , 'Month'], axis =1)


#exporting into csv file 

data.to_csv('ValueInc_organised.csv', index = False)



































































