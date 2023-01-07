# Name 
  Data Analysis on CSRankings: Computer Science Rankings AI Department.
  
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
  3. Unzip file. You can change folder name. 
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
      cd Scripts
      ```
      ```
      python run.py
      ```
  5. After finishing all the prompts, press enter, wait for 5 minutes. 
      ***After 5 minutes, user will get 3 outputs in csv formate***
          
            Uncleaned Data:
            1. `University_ranks.csv`
            2. `Faculty_info.csv`

            Transformed Data:
            1. `CSRanking_Universities_Ai_Area.csv`
  
  
     
   
  
  
  
