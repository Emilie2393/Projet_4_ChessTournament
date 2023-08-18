# Projet_4_ChessTournament

# 1- Install venv and copy requirements.txt
On terminal enter :  
python -m venv "name of your choice"  
For Windows terminal : "name of your choice"\Scripts\activate.bat  
Powershell terminal : "name of your choice"\Scripts\activate  
Then enter : pip install -r requirements.txt  
python main.py

# 2- You can start by players menu or tournament menu

## Players menu --
1- Create some players  
2- Add players to your tournament players list (8 minimum) : they will play in tournament you'll create  
3- Check your players list or your tournament players list, add some players or delete your tournament players list  

## Tournament menu --
1- Create one or several tournaments  
2- Associate your tournament with tournament players list (or change players if you wish)  
3- Get tournament you just created, or an old tournament to continue it  
4- Begin to play 

## Reports menu --
1- Once you have data in chess.json you can check them here  
2- Check details about all players by alphabetical order of their first name  
3- Check details about tournament  
4- Once you found the tournament of your choice, check details about their rounds or their players  

## Important to play --
1- You will see this "!--" if you forget to do something : associate message will guide you  
2- After each round, tournament players will be sorted by highest score. They will be associated for next match if they never played together before.  
3- Round number is automatically set to 4  

## Flake8
To generate a new repport, enter " flake8 --format=html --htmldir=flake-report " in terminal and check it directly in the file
