It is a project of Negative Message Blocker 
Which will help to remove messages from any social media and also any type of data it can remove .
Main working with uniqueness is:-
 * It will work from server side.
 * We will add this feature directly in social media app and whenever client will update its app it will automatically install in client app  as a
   normal feature and work automatically no need of client is there to delete negative messages it will delete whenever it will detect.
 * No matter it is  a video,audio,image and text  it will work for all.

   
 ##Build with

 The prototype is made using follows as:-
  - Python
  - Nltk

##Libraries Installation
  import os
  import nltk
  import vader.sentiment
  import better_profanity

#### It is a code for  text messages only #####

import os
import time
from datetime import datetime as dt
import nltk.data
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from better_profanity import profanity
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8):
        dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16)
        print("working")
            
        with open("C:/Users/Vivek Agrawal/OneDrive/Documents/file1.txt",'r+') as file :
            if __name__=="__main__":
                list1=input("enter any  negative sentence");		

                custom_badwords=['rascal','Apathetic','bastard','asshole','bitch','brother fucker','bullshit','bollocks','wanker','dickhead','nigra','damn it','hell','bloody hell','shit as','farted']
                profanity.add_censor_words(custom_badwords)
                profanity.censor(custom_badwords)
                s=profanity.censor(list1)
                print(profanity.censor(s))                    
                file.write(s)  
                content=file.readline()                              
                analyzer=SentimentIntensityAnalyzer()
                polarity_scores=analyzer.polarity_scores(content)
                positive_score=polarity_scores['pos']
                negative_score=polarity_scores['neg']
                compound_score=polarity_scores['compound']           
    
    if compound_score>0.5:
        print("positive message")
        break
    elif compound_score< -0.5:
        print("negative message")        
        break
    else:
        print("Thanku ")
        break
            


  
    
