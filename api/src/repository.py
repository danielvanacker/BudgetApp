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

def getAllPeople(userId):
    (conn, cursor) = openConnection()
    cursor.execute('SELECT name FROM people WHERE user_id=?;', (userId,))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def insertIncome(date, amount, comment, category, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO income (date, amount, comment, category, user_id) VALUES (?, ?, ?, ?, ?)", (date, amount, comment, category, userId))
    closeConnection(conn, cursor)
    return 'Success'

def insertExpense(date, amount, comment, category, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO expense (date, amount, comment, category, user_id) VALUES (?, ?, ?, ?, ?)", (date, amount, comment, category, userId))
    rowId = cursor.lastrowid
    closeConnection(conn, cursor)
    return rowId

def insertMoneyOwed(date, amount, comment, splitWith, expenseId, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO money_owed (date, amount, comment, person, expense_id, user_id) VALUES (?, ?, ?, ?, ?, ?)", (date, amount, comment, splitWith, expenseId, userId))
    rowId = cursor.lastrowid
    closeConnection(conn, cursor)
    return rowId

def getAllTransactions(userId):
    (conn, cursor) = openConnection()
    result = cursor.execute(
        "SELECT category, amount, date, comment, 'Expense' as transactionGroup, '' as person FROM expense WHERE user_id=:userId " +
        "UNION SELECT category, amount, date, comment, 'Income' as transactionGroup, '' as peron FROM income WHERE user_id=:userId " +
        "UNION SELECT e.category, m.amount, e.date, e.comment, 'Money Lent' as transactionGroup, m.person FROM money_owed AS m, expense AS e WHERE e.id = m.expense_id AND e.user_id=:userId AND m.user_id=:userId;",
        {"userId": userId})
    
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
    closeConnection(conn, cursor)
    return {'transactions': items}

def getAllCategories(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT name, is_income FROM category WHERE user_id=?", (userId,))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAllExpenseCategories(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT name FROM category WHERE is_income=false AND user_id=?", (userId,))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAllIncomeCategories(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT name FROM category WHERE is_income=true AND user_id=?", (userId,))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def getAggregateSpendByCategory(category, userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM expense WHERE category=:category AND user_id=:userId GROUP BY strftime(\"%m-%Y\", date)", {"category": category, "userId": userId})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getAggregateIncomeByCategory(category, userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM income WHERE category=:category AND user_id=:userId GROUP BY strftime(\"%m-%Y\", date)", {"category": category, "userId": userId})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTransactionMonths(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: row[0]
    cursor.execute("SELECT DISTINCT strftime(\"%m-%Y\", date) FROM (SELECT DISTINCT date FROM income WHERE user_id=:userId UNION SELECT DISTINCT date FROM expense WHERE user_id=:userId)", {"userId": userId})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTotalIncomeByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM income WHERE user_id=? GROUP BY strftime(\"%m-%Y\", date)", (userId,))
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getTotalExpensesByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: row[0]}
    cursor.execute("SELECT SUM(amount), strftime(\"%m-%Y\", date) FROM expense WHERE user_id=? GROUP BY strftime(\"%m-%Y\", date)", (userId,))
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getNetIncomeByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.row_factory = lambda cursor, row: {row[1]: (row[2] or 0)-(row[0] or 0)}
    cursor.execute("WITH agg_expenses AS ("
            + " SELECT SUM(amount) as amt, strftime(\"%m-%Y\", date) as date"
            + " FROM expense"
            + " WHERE user_id=:userId"
            + " GROUP BY strftime(\"%m-%Y\", date)),"
            + " agg_income AS (" 
            + " SELECT SUM(amount) as amt, strftime(\"%m-%Y\", date) as date"
            + " FROM income WHERE user_id=:userId GROUP BY strftime(\"%m-%Y\", date))"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_expenses AS e"
            + " LEFT JOIN agg_income AS i USING(date)"
            + " UNION ALL"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_income AS i"
            + " LEFT JOIN agg_expenses AS e USING(date)"
            + " WHERE e.date IS NULL;", {"userId": userId})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def getUser(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT id from user WHERE id=?", (userId,))
    result = cursor.fetchall()
    print(result)
    closeConnection(conn, cursor)
    return result

def addUser(userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO user (id) VALUES (?)", (userId,))
    rowId = cursor.lastrowid
    print(rowId)
    closeConnection(conn, cursor)
    return rowId