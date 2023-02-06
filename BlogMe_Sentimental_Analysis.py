# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 10:53:55 2023

@author: Ashutosh Bhatt
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#reading excel or xlsx file

data = pd.read_excel('articles.xlsx')

#describing the data

data.describe()

#describing the columns 

data.info()

#counting the number of article per source 

data.groupby(['source_id'])['article_id'].count()

#number of reaction by publishers'

data.groupby(['source_id'])['engagement_reaction_count'].sum()


#dropping a column 

data = data.drop('engagement_comment_plugin_count' , axis =1)

#creating keyword flag

keyword = 'crash'

#creating  a for loop for to isolate each title row 

# length = len(data)
# keyword_flag =[]
# for x in range (0,length):
#     heading = data['title'][x]
#     if keyword in heading :
#         flag = 1
#     else :
#         flag = 0
#     keyword_flag.append(flag)
    
    #defining function 
    
def keywordflag(keyword):
        length = len(data)
        keyword_flag =[]
        for x in range (0,length):
            heading = data['title'][x]
            try:
                if keyword in heading :
                        flag = 1
                else :
                        flag = 0
            except:
                   flag =0
            keyword_flag.append(flag)
        return keyword_flag
    
keywordflag = keywordflag("murder") 

#creating a new column in data dataframe 

data['keywordflag'] = keywordflag;

#SENTIMENT INTENSITY ANALYZER

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]

sent = sent_int.polarity_scores(text) 

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop for adding sentiment per title 

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
    
title_pos_sentiment = pd.Series(title_pos_sentiment)
   
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment

data['title_pos_sentiment'] = title_pos_sentiment

data['title_neu_sentiment'] = title_neu_sentiment


data.to_excel('BlogMe_Sentimental_Analysis_Organised.xlsx' , sheet_name = 'BlogMedata' , index=False)









    
    
    
    
    
    
    
    
    
    
    
    

























































