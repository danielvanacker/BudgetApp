import sqlite3

def openConnection():
    conn = sqlite3.connect('C:/Users/grano/Desktop/Budget/BudgetApp/db/budgetdb')
    cursor = conn.cursor()
    return (conn, cursor)

def closeConnection(conn, cursor):
    cursor.close()
    conn.close()

def getAllTransactions():
    (conn, cursor) = openConnection()
    cursor.execute('SELECT * FROM expense UNION SELECT * FROM income;')
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

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