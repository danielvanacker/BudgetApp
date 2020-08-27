import sqlite3
import json

def openConnection():
    conn = sqlite3.connect('C:/Users/grano/Desktop/Budget/BudgetApp/db/budgetdb')
    cursor = conn.cursor()
    return (conn, cursor)

def closeConnection(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()

def getAllPeople():
    (conn, cursor) = openConnection()
    cursor.execute('SELECT * FROM people;')
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAllCategories():
    (conn, cursor) = openConnection()
    cursor.execute('SELECT * FROM category;')
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAllBudget():
    conn = sqlite3.connect('C:/Users/grano/Desktop/Budget/BudgetApp/db/budgetdb')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM budget;')
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def insertIncome(date, amount, comment, category):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO income (date, amount, comment, category) VALUES (?, ?, ?, ?)", (date, amount, comment, category))
    closeConnection(conn, cursor)
    return 'Success'

def insertExpense(date, amount, comment, category):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO expense (date, amount, comment, category) VALUES (?, ?, ?, ?)", (date, amount, comment, category))
    rowId = cursor.lastrowid
    closeConnection(conn, cursor)
    return rowId

def insertMoneyOwed(date, amount, comment, splitWith, expenseId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO money_owed (date, amount, comment, person, expense_id) VALUES (?, ?, ?, ?, ?)", (date, amount, comment, splitWith, expenseId))
    rowId = cursor.lastrowid
    closeConnection(conn, cursor)
    return rowId

def getAllTransactions():
    (conn, cursor) = openConnection()
    result = cursor.execute("SELECT category, amount, date, comment, 'Expense' as transactionGroup FROM expense UNION SELECT category, amount, date, comment, 'Income' as transactionGroup FROM income;")
    
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
    print(json.dumps({'items': items}))
    closeConnection(conn, cursor)
    return {'transactions': items}
