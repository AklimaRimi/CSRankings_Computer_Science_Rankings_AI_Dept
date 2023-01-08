path = r'https://csrankings.org/'
import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def Scrapper():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(path)


    time.sleep(10)
    button1 = driver.find_element(By.XPATH,'//select[@id="regions"]')
    action = ActionChains(driver)
    action.click(button1).perform()

    button2 = driver.find_element(By.XPATH,'//*[@id="regions"]/optgroup[2]/option[7]').click()
    button3 = driver.find_element(By.XPATH,'//*[@id="fromyear"]/option[31]').click()


    off_button1 = driver.find_element(By.XPATH,'//a[@id="systems_areas_off"]')
    action = ActionChains(driver)
    action.click(off_button1).perform()
    off_button2 = driver.find_element(By.XPATH,'//a[@id="theory_areas_off"]')
    action = ActionChains(driver)
    action.click(off_button2).perform()


    off_button3 = driver.find_element(By.XPATH,'//a[@id="other_areas_off"]')
    action = ActionChains(driver)
    action.click(off_button3).perform()




    down=driver.find_element(By.XPATH,'//*[@id="ranking"]/tbody')
    # driver.execute_script("arguments[0].scrollIntoView();", down)


    actions = ActionChains(driver)
    actions.move_to_element(down).perform()

    rows = driver.find_elements(By.XPATH,'//*[@id="ranking"]/tbody/tr')

    rank = []
    name = []
    data = []
    count = []
    faculty = []
    n = ''
    faculty_details =[]
    actions = ActionChains(driver)
    for ind,i in enumerate(rows):
        if len(i.text.split()) > 0 and i.text.split()[0] != 'Faculty':
            print(ind)
            split = i.text.split()
            n = ''
            rank.append(split[0])
            count.append(split[-2])
            faculty.append(split[-1])
            
            for j in split[2:-2]:
                n += j+' '
            name.append(n)
        
            x = i.find_elements(By.TAG_NAME,'span')[0]
            actions.click(x).perform()
            actions = ActionChains(driver)

        

    whole_table = driver.find_elements(By.XPATH,'//*[@id="ranking"]/tbody/tr')
    n =''
    for ind,i in enumerate(whole_table):
        # print(i.text.split(),ind)
        if (ind%3) == 0:
            split = i.text.split()
            print(split)
            for j in split[2:-2]:
                n += j+' '
        elif (ind%3) == 2:
            split = i.text.split('\n')
            # print(split)
            for k in split[1:]:
                list = ['ml','nlp','vision','ai','theory','db','security','robotics','network','eda','se']
                for li in list:
                    if li in k:
                        div = k.split()
                        # print(div)
                        faculty_details.append([n,' '.join(div[:-3]),div[-3],div[-2],div[-1]])
            n=''
                
                

    cols = ['University Name','Name','Subject','Publications', 'Avg Co-Author']

    import pandas as pd

    dataf = pd.DataFrame(faculty_details,columns=cols)

    dataf.to_csv('Faculty_info.csv',index=False)
            
        

            
    datas = []
    for i in range(len(name)):
        datas.append([rank[i],name[i],count[i],faculty[i]])    
            
    import pandas as pd

    dataf = pd.DataFrame(datas,columns=['Rank','University Name','Mean','Faculty'])

    print(dataf.head())

    dataf.to_csv('University_ranks.csv',index=False)


    time.sleep(2)

    driver.close()
    
    return

