![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FAklimaRimi%2FCSRankings_Computer_Science_Rankings_AI_Dept&label=Reads&countColor=%23263759)

# Data Analysis on CSRankings: Computer Science Rankings AI Department.

![](https://github.com/AklimaRimi/CSRankings_Computer_Science_Rankings_AI_Dept/blob/main/tableau_dashboard/viz.png)
  
# Goal of this Project
  1. Collecting data from [Website](https://csrankings.org/#/fromyear/2000/toyear/2022/index?ai&vision&mlmining&nlp&inforet&world).
  2. Data Cleaning, Transform.
  3. Data Visualization using Tableau.
  4. Find story from Tableau Dashboard.
  
# Data Collection
  Using the website several data can be collected such as Rank, Institute name, Count, Faculty, Faculty Name, Subject, Number of Publications, Number of Co-authors.
    
  ## **Steps**
  1. Install Python on your device from [Here](https://www.python.org/downloads/). 
  2. Click [Zip_File](https://github.com/AklimaRimi/CSRankings_Computer_Science_Rankings_AI_Dept/archive/refs/heads/main.zip) to download all files.
  3. Unzip file. You can change the folder name. 
  4. Create an environment where downloaded files are staying. To do this `Click Right Mouse Button` and Click on `Open in Terminal` and write code one by one :
    
      ```
      Set-ExecutionPlicy Unrestricted
      ```
      
      ```
      pip install virtualenv
      or 
      pip3 install virtualenv
      ```
      ```
      virtualenv env
      ```
      ```
      env\Scripts\Activate.ps1
      ```
      ```
      pip install -r requirements.txt
      or 
      pip3 install -r requirements.txt
      ```
      ```
      cd scripts
      ```
      ```
      python run.py
      ```
  5. After finishing all the prompts, press enter, wait for 5 minutes. 
      ***After 5 minutes, user will get 3 outputs in csv format***
          
      Uncleaned Data:
        1. `University_ranks.csv`
        2. `Faculty_info.csv`
 
      Transformed Data:
        1. `CSRanking_Universities_Ai_Area.csv`
        
     
# Data Transform
If you did everything according to the above instructions then Data Transformation has already been done already.
In the data transformation a few things were completed..
  
  1. Dropped Duplicate values.
  2. Created new columns/ features.
  3. Created a new Dataframe.
  4. Merge 2 DataFrames.
  5. Dropped 2 Columns.
  
# Visualization/ Dashboard
  1. Using '[CSRanking_Universities_Ai_Area.csv](https://github.com/AklimaRimi/CSRankings_Computer_Science_Rankings_AI_Dept/blob/main/outputs/CSRanking_Universities_Ai_Area.csv)' Dataset I've created [This Dashboard](https://public.tableau.com/app/profile/aklima.akter.rimi/viz/VisualizationsonCSRankingsUniversitiesinAIDepartment/Dashboard1)
  ![](https://github.com/AklimaRimi/CSRankings_Computer_Science_Rankings_AI_Dept/blob/main/tableau_dashboard/viz.png)
  
# Story or Findings
   1. At Westlake University, each faculty published on average 59 papers which is the highest value.
    
   2. At Carnegie Mellon University, faculties published the highest number of papers from 2000-2022.
    
   3. In the fields of AI, ML, NLP, Vision, Peking University has published the most papers, including 35 papers on AI, 11 papers on ML, 16 on NLP, and 33 papers on computer vision.
    
  4. An average of 107 papers are published from each department at Carnegie Mellon University which is the maximum.
    
  5. In 2000-2022, the top 3 fields are AI(1520), ML(1124), NLP(737). Most of the papers in the world are related to these 3 areas.
  
  6. Most faculties have published 2-18 research papers from their university. About 214 faculties published 4 papers which is the maximum.
 
 
# Caution
1. About 5-7 minutes take to complete the whole process. It depends on your device performance.
 
2. Do not touch, minimize or close any pop up Google Chrome.
 
3. Data might be changed over time.
  
  
# Conclusion
This entire project is for Data Analysis. It's suitable for beginners. This project can be executed by anyone. 
 
 

