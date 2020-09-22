import sqlite3
import json

def openConnection():
    conn = sqlite3.connect('/Users/danielvanacker/Documents/dev/BudgetApp/db/budgetdb')
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
    result = cursor.execute(
        "SELECT category, amount, date, comment, 'Expense' as transactionGroup, '' as person FROM expense " +
        "UNION SELECT category, amount, date, comment, 'Income' as transactionGroup, '' as peron FROM income " +
        "UNION SELECT e.category, m.amount, e.date, e.comment, 'Money Lent' as transactionGroup, m.person FROM money_owed AS m, expense AS e WHERE e.id = m.expense_id;"
        )
    
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
    closeConnection(conn, cursor)
    return {'transactions': items}

def getAllCategories():
    (conn, cursor) = openConnection()
    #cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT name, is_income FROM category")
    toReturn = cursor.fetchall()
    print(toReturn)
    closeConnection(conn, cursor)
    return toReturn

def getAllExpenseCategories():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT name FROM category WHERE is_income=false")
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAllIncomeCategories():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT name FROM category WHERE is_income=true")
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAggregateSpendByCategory(category):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM expense WHERE category=:category GROUP BY strftime(\"%m-%Y\", date)", {"category": category})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getAggregateIncomeByCategory(category):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM income WHERE category=:category GROUP BY strftime(\"%m-%Y\", date)", {"category": category})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTransactionMonths():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT DISTINCT strftime(\"%m-%Y\", date) FROM (SELECT DISTINCT date FROM income UNION SELECT DISTINCT date FROM expense)")
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTotalIncomeByMonth():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM income GROUP BY strftime(\"%m-%Y\", date)")
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTotalExpensesByMonth():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM expense GROUP BY strftime(\"%m-%Y\", date)")
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getNetIncomeByMonth():
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: (row[2] or 0)-(row[0] or 0)}
    cursor.execute("WITH agg_expenses AS ("
            + " SELECT SUM(amount) as amt, strftime(\"%m-%Y\", date) as date"
            + " FROM expense"
            + " GROUP BY strftime(\"%m-%Y\", date)),"
            + " agg_income AS (" 
            + " SELECT SUM(amount) as amt, strftime(\"%m-%Y\", date) as date"
            + " FROM income GROUP BY strftime(\"%m-%Y\", date))"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_expenses AS e"
            + " LEFT JOIN agg_income AS i USING(date)"
            + " UNION ALL"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_income AS i"
            + " LEFT JOIN agg_expenses AS e USING(date)"
            + " WHERE e.date IS NULL;")
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result