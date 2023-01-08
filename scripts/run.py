import pandas as pd
import numpy as np
from scrapper import Scrapper


def Transformer():
    
    data1= pd.read_csv('University_ranks.csv')
    data2 = pd.read_csv('Faculty_info.csv')
    
    ## Remove Duplicates 
    
    data2 = data2.drop_duplicates()
    
    li = ['ml','nlp','vision','ai','theory','db','security','robotics','network','eda','se']
    def search(x,word):
        re = 0
        splits = x.split(',')

        for i in splits:
            if word == i:
                return 1
        return 0
    

    data2['ml'] = data2['Subject'].apply(lambda x: search(x,'ml'))
    data2['nlp'] = data2['Subject'].apply(lambda x: search(x,'nlp'))
    data2['vision'] = data2['Subject'].apply(lambda x: search(x,'vision'))
    data2['ai'] = data2['Subject'].apply(lambda x: search(x,'ai'))
    data2['theory'] = data2['Subject'].apply(lambda x: search(x,'theory'))
    data2['db'] = data2['Subject'].apply(lambda x: search(x,'db'))
    data2['security'] = data2['Subject'].apply(lambda x: search(x,'security'))
    data2['robotics'] = data2['Subject'].apply(lambda x: search(x,'robotics'))
    data2['network'] = data2['Subject'].apply(lambda x: search(x,'network'))
    data2['eda'] = data2['Subject'].apply(lambda x: search(x,'eda'))
    data2['se'] = data2['Subject'].apply(lambda x: search(x,'se'))
    ## Creating new data from data2 or Faculty_info
    print(data2.head(5))
    new_data = data2.groupby(['University Name'])[['Publications','ml','nlp','vision','ai','theory','db','security','robotics','network','eda','se']].sum()
    
    ## saving the new data as DataFrame
    data3 = pd.DataFrame(new_data) 
    
    ## Merge 2 dataframes
    final_data = data1.merge(data3,right_on = 'University Name',left_on = 'University Name')
    
    ## creating new column in Final_data
    final_data['publication_per_faculty'] = 0.0
    
    ## New column is per person as faculty published paper on avg. 
    def pct(data):
        for i in range(len(data)):
            final_data['publication_per_faculty'][i] = final_data['Publications'][i]/final_data['Faculty'][i]
            
            
    ## saving final_data as csv formate
    final_data.to_csv('CSRanking_Universities_Ai_Area.csv',index = False)




if __name__ == '__main__':
    Scrapper()
    Transformer()
