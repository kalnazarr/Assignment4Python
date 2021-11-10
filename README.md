# Assignment 4 SE-2001 Sayat Kalnazar
Writing program to input a coin name into text field, displaying a list of paragraphs and storing parsed news & blogs in the database (almost like how we did with Assignment 2, but now connected with SQL).
# Installation
Before starting to use the code you must install required packages and modules. All packages and libraries will be provided in requirements.txt file, that is uploaded in the repository. Basically, you'll need the packages that are provided below:
```
flask (https://flask.palletsprojects.com/en/2.0.x/)
flask_sqlalchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
requests  (https://pypi.org/project/requests/)
beautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
```
# Usage
At first we need to create a database in DBMS application(SQL server,Pgadmin) or other database management system. After that, you need to successfully connect your server with the database. We called our database "assignment4" as it is shown in the code. Also, it's important to know the login and password of your database, ours is postgres and 5432.
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/flask'
```
The next step is to create a table in your new database, the database name is assignment4.
```
CREATE TABLE Paragraphs (
id INTEGER PRIMARY KEY,
coin_name VARCHAR,
title VARCHAR,
body VARCHAR, 
link VARCHAR
)
```
Further step is to run main.py file, you'll get the IP-address in the terminal that you need to follow, after following it, you need to add /coin after this address. 
```
http://127.0.0.1:5000/coin
```
Then you will see the page with the input field and one button, here you need to input the existing coin from the coin market, for example Bitcoin. It will afterwards output some articles, news, paragraphs regarding this coin. Also, all the parsed information will be stored in the database.

# Examples
### At the beggining you will have an empty page, except the input field and the check button. You need to enter the coin.
![1](https://user-images.githubusercontent.com/82859085/141158434-d9e2920f-cc20-4ec9-9b7b-e022bbcef0b7.PNG)

![2](https://user-images.githubusercontent.com/82859085/141158683-93e8dedd-91a8-4661-87b5-e1612212dd79.PNG)

### After entering the coin and pressing the check button, you will get many articles as an output.

![3](https://user-images.githubusercontent.com/82859085/141158847-073a2866-aa4d-49f7-9e26-6eaa075fdaab.PNG)

### Also, here you can see how this data is stored in the database.


![4](https://user-images.githubusercontent.com/82859085/141159166-f7105955-7309-4790-816c-f1f89d9ede23.PNG)

![5](https://user-images.githubusercontent.com/82859085/141159315-e02333b7-bc2c-48e7-ba1c-2815df71337e.PNG)





