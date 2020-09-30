import sqlite3
conn = sqlite3.connect('budgetdb')
cursor = conn.cursor()

def createTables():
    cursor.execute('CREATE TABLE category(name VARCHAR(55), is_income boolean NOT NULL, user_id BIGINT NOT NULL, FOREIGN KEY(user_id) REFERENCES user(name), PRIMARY KEY(name, user_id))')
    cursor.execute('CREATE TABLE expense(id INTEGER, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, user_id BIGINT NOT NULL, FOREIGN KEY(category) REFERENCES category(name), FOREIGN KEY(user_id) REFERENCES user(name), PRIMARY KEY(id))')
    cursor.execute('CREATE TABLE budget(month TINYINT, year TINYINT, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, user_id BIGINT NOT NULL, PRIMARY KEY(month, year, category, user_id), FOREIGN KEY(category) REFERENCES category(name), FOREIGN KEY(user_id) REFERENCES user(name))')
    cursor.execute('CREATE TABLE income(id INTEGER, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), category VARCHAR(55) NOT NULL, user_id BIGINT NOT NULL, FOREIGN KEY(category) REFERENCES category(name), FOREIGN KEY(user_id) REFERENCES user(name), PRIMARY KEY (id))')
    cursor.execute('CREATE TABLE people(name VARCHAR(55), user_id BIGINT NOT NULL, FOREIGN KEY(user_id) REFERENCES user(name), PRIMARY KEY (name, user_id))')
    cursor.execute('CREATE TABLE money_owed(id INTEGER PRIMARY KEY, date DATE NOT NULL, amount FLOAT NOT NULL, comment VARCHAR(255), person VARCHAR(55) NOT NULL, expense_id INTEGER, user_id BIGINT NOT NULL, FOREIGN KEY(person) REFERENCES person(name), FOREIGN KEY(expense_id) REFERENCES expense(id), FOREIGN KEY(user_id) REFERENCES user(name))')
    cursor.execute('CREATE TABLE user(id BIGINT PRIMARY KEY)')

def insertMockData():
    #Insert Danvan values
    cursor.execute('INSERT INTO user (id) VALUES (114127949071419358649)')
    cursor.execute('INSERT INTO category (name, is_income, user_id) VALUES ("Groceries", false, 114127949071419358649), ("Travel", false, 114127949071419358649), ("Work Income", true, 114127949071419358649)')
    cursor.execute('INSERT INTO budget (month, year, amount, comment, category, user_id) VALUES ("July", 2020, 500, "mock data", "Travel", 114127949071419358649), ("July", 2020, 100, "mock data 2", "Groceries", 114127949071419358649), ("August", 2020, 2000, "work income", "Work Income", 114127949071419358649)')
    cursor.execute('INSERT INTO people (name, user_id) VALUES ("John Doe", 114127949071419358649), ("Foo Bar", 114127949071419358649), ("Tony Stark", 114127949071419358649)')

    #Insert local values
    cursor.execute('INSERT INTO user (id) VALUES (0)')
    cursor.execute('INSERT INTO category (name, is_income, user_id) VALUES ("Groceries", false, 0), ("Travel", false, 0), ("Work Income", true, 0)')
    cursor.execute('INSERT INTO budget (month, year, amount, comment, category, user_id) VALUES ("July", 2020, 500, "mock data", "Travel", 0), ("July", 2020, 100, "mock data 2", "Groceries", 0), ("August", 2020, 2000, "work income", "Work Income", 0)')
    cursor.execute('INSERT INTO people (name, user_id) VALUES ("John Doe", 0), ("Foo Bar", 0), ("Tony Stark", 0)')
    cursor.execute('INSERT INTO money_owed (date, amount, person, expense_id, user_id) VALUES ("2020-01-01", 50, "Toney Stark", 0, 0)')

def test():
    cursor.execute('SELECT * FROM category;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM budget;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM people;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM income;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM expense;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM money_owed;')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM user;')
    print(cursor.fetchall())

def commitAndClose():
    conn.commit()
    cursor.close()
    conn.close()

createTables()
insertMockData()
test()
commitAndClose()
