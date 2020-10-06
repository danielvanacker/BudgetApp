import psycopg2
import json
import os
from flask import g
import sqlalchemy.pool as pool

def getConn():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PW']
    )

def createPool():
    g.pool = pool.QueuePool(getConn, max_overflow=10, pool_size=5)

def openConnection():
    if not hasattr(g, 'pool'):
        createPool()
    conn = g.pool.connect()
    cursor = conn.cursor()
    return (conn, cursor)

def closeConnection(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()

def repGetAllPeople(userId):
    (conn, cursor) = openConnection()
    cursor.execute('SELECT id, name FROM people WHERE user_id=%s;', (str(userId),))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn


def repInsertIncome(date, amount, comment, categoryId, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO income (date, amount, comment, category_id, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", (date, amount, comment, categoryId, str(userId)))
    rowId = cursor.fetchone()[0]
    closeConnection(conn, cursor)
    return rowId

def repInsertExpense(date, amount, comment, category, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO expense (date, amount, comment, category_id, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", (date, amount, comment, category, str(userId)))
    rowId = cursor.fetchone()[0]
    closeConnection(conn, cursor)
    return rowId

def repInsertMoneyOwed(date, amount, comment, splitWithId, expenseId, userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO money_owed (date, amount, comment, person_id, expense_id, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id", (date, amount, comment, splitWithId, expenseId, str(userId)))
    rowId = cursor.fetchone()[0]
    closeConnection(conn, cursor)
    return rowId

def repGetAllTransactions(userId):
    (conn, cursor) = openConnection()
    result = cursor.execute(
        "WITH transactions AS (SELECT category_id, amount, date, comment, 'Expense' as transactionGroup, '' as person FROM expense WHERE user_id=%(userId)s "
        + "UNION ALL SELECT category_id, amount, date, comment, 'Income' as transactionGroup, '' as person FROM income WHERE user_id=%(userId)s "
        + "UNION ALL SELECT e.category_id, m.amount, e.date, e.comment, 'Money Lent' as transactionGroup, p.name FROM money_owed AS m, expense AS e, people AS p WHERE e.id = m.expense_id AND e.user_id = p.user_id AND p.user_id = m.user_id AND p.id = m.person_id AND p.user_id=%(userId)s) "
        + "SELECT c.name, t.amount, t.date, t.comment, t.transactionGroup, t.person FROM transactions AS t, category AS c WHERE t.category_id = c.id AND c.user_id=%(userId)s;",
        {"userId": userId})

    columns = [desc[0] for desc in cursor.description]
    real_dict = [dict(zip(columns, row)) for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return {'transactions': real_dict}

def repGetAllCategories(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT id, name, is_income FROM category WHERE user_id=%s", (str(userId),))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def repGetAllExpenseCategories(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT id, name FROM category WHERE is_income=false AND user_id=%s", (str(userId),))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def repGetAllIncomeCategories(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT id, name FROM category WHERE is_income=true AND user_id=%s", (str(userId),))
    toReturn = cursor.fetchall()
    closeConnection(conn, cursor)
    return toReturn

def repGetAggregateSpendByCategory(categoryId, userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT SUM(amount), to_char(date, 'Mon-YYYY') FROM expense WHERE user_id=%(userId)s AND category_id=%(categoryId)s GROUP BY to_char(date, 'Mon-YYYY');", {"categoryId": categoryId, "userId": str(userId)})
    result = [{row[1]: row[0]} for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return result

def repGetAggregateIncomeByCategory(categoryId, userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT SUM(amount), to_char(date, 'Mon-YYYY') FROM income WHERE category_id=%(categoryId)s AND user_id=%(userId)s GROUP BY to_char(date, 'Mon-YYYY');", {"categoryId": categoryId, "userId": str(userId)})
    result = [{row[1]: row[0]} for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return result

def repGetTransactionMonths(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT DISTINCT to_char(date, 'Mon-YYYY') FROM (SELECT DISTINCT date FROM income WHERE user_id=%(userId)s UNION SELECT DISTINCT date FROM expense WHERE user_id=%(userId)s) AS e;", {"userId": str(userId)})
    result = cursor.fetchall()
    closeConnection(conn, cursor)
    return result

def repGetTotalIncomeByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT SUM(amount), to_char(date, 'Mon-YYYY') FROM income WHERE user_id=%s GROUP BY to_char(date, 'Mon-YYYY');", (userId,))
    result = [{row[1]: row[0]} for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return result

def repGetTotalExpensesByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT SUM(amount), to_char(date, 'Mon-YYYY') FROM expense WHERE user_id=%s GROUP BY to_char(date, 'Mon-YYYY');", (userId,))
    result = [{row[1]: row[0]} for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return result

def repGetNetIncomeByMonth(userId):
    (conn, cursor) = openConnection()
    cursor.execute("WITH agg_expenses AS ("
            + " SELECT SUM(amount) as amt, to_char(date, 'Mon-YYYY') as date"
            + " FROM expense"
            + " WHERE user_id=%(userId)s"
            + " GROUP BY to_char(date, 'Mon-YYYY')),"
            + " agg_income AS (" 
            + " SELECT SUM(amount) as amt, to_char(date, 'Mon-YYYY') as date"
            + " FROM income WHERE user_id=%(userId)s"
            + " GROUP BY to_char(date, 'Mon-YYYY'))"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_expenses AS e"
            + " LEFT JOIN agg_income AS i USING(date)"
            + " UNION ALL"
            + " SELECT e.amt, e.date, i.amt, i.date"
            + " FROM agg_income AS i"
            + " LEFT JOIN agg_expenses AS e USING(date)"
            + " WHERE e.date IS NULL;", {"userId": userId})
    result = [{(row[1] or row[3]): (row[2] or 0)-(row[0] or 0)} for row in cursor.fetchall()]
    closeConnection(conn, cursor)
    return result

def repGetUser(userId):
    (conn, cursor) = openConnection()
    cursor.execute("SELECT id from active_user WHERE id=%s", (str(userId),))
    result = cursor.fetchall()
    print(result)
    closeConnection(conn, cursor)
    return result

def repAddUser(userId):
    (conn, cursor) = openConnection()
    cursor.execute("INSERT INTO user (id) VALUES (%s) RETURNING id", (str(userId),))
    rowId = cursor.fetchone()[0]
    print(rowId)
    closeConnection(conn, cursor)
    return rowId