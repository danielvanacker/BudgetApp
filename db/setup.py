import sqlite3
conn = sqlite3.connect('budgetdb')
cursor = conn.cursor()

def createTables():
    cursor.execute('CREATE TABLE category(name VARCHAR(55) PRIMARY KEY, is_income boolean NOT NULL)')
    cursor.execute('CREATE TABLE expense(id INTEGER PRIMARY KEY, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, FOREIGN KEY(category) REFERENCES category(name))')
    cursor.execute('CREATE TABLE budget(month TINYINT, year TINYINT, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, PRIMARY KEY(month, year, category), FOREIGN KEY(category) REFERENCES category(name))')
    cursor.execute('CREATE TABLE income(id INTEGER PRIMARY KEY, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, FOREIGN KEY(category) REFERENCES category(name))')
    cursor.execute('CREATE TABLE people(name VARCHAR(55) PRIMARY KEY)')
    cursor.execute('CREATE TABLE money_owed(id INTEGER PRIMARY KEY, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), person VARCHAR(55) NOT NULL, FOREIGN KEY(person) REFERENCES person(name))')

def insertMockData():
    cursor.execute('INSERT INTO category (name, is_income) VALUES ("Groceries", true), ("Travel", true), ("Work Income", false)')
    cursor.execute('INSERT INTO budget (month, year, amount, comment, category) VALUES ("July", 2020, 500, "mock data", "Travel"), ("July", 2020, 100, "mock data 2", "Groceries"), ("August", 2020, 2000, "work income", "Work Income")')

def test():
    cursor.execute('SELECT * FROM category;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM budget;')
    print(cursor.fetchall())

def commitAndClose():
    conn.commit()
    cursor.close()
    conn.close()

createTables()
insertMockData()
commitAndClose()
