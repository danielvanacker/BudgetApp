from .repository import *
from .models import constants as c
from flask import jsonify

def getTransactionMonths(userId):
    return repGetTransactionMonths(userId)

def getElapsedBudget(userId):
    result = []
    expenses = getCategorySpendByMonth(userId)
    income = getCategoryIncomeByMonth(userId)
    totalIncome = getTotalIncomeByMonth(userId)
    totalExpenses = getTotalExpensesByMonth(userId)
    netIncome = getNetIncomeByMonth(userId)
    return income + totalIncome + expenses + totalExpenses + netIncome

def getTotalIncomeByMonth(userId):
    result = {'category': 'Total Income', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repGetTotalIncomeByMonth(userId)))
    return [result]

def getTotalExpensesByMonth(userId):
    result = {'category': 'Total Expenses', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repGetTotalExpensesByMonth(userId)))
    return [result]

def getNetIncomeByMonth(userId):
    result = {'category': 'Net Income (Out)', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repGetNetIncomeByMonth(userId)))
    return [result]

def getCategorySpendByMonth(userId):
    result = []
    categories = repGetAllExpenseCategories(userId)
    for category in categories:
        row = {'category': category[1], 'transactionGroup': "Expense"}
        row.update(listOfDictsToDict(repGetAggregateSpendByCategory(category[0], userId)))
        result.append(row)
    return result

def getCategoryIncomeByMonth(userId):
    result = []
    categories = repGetAllIncomeCategories(userId)
    for category in categories:
        row = {'category': category[1], 'transactionGroup': "Income"}
        row.update(listOfDictsToDict(repGetAggregateIncomeByCategory(category[0], userId)))
        result.append(row)
    return result

def getAllPeople(userId):
    return repGetAllPeople(userId)

def getAllCategories(userId):
    return repGetAllCategories(userId)

def getAllTransactions(userId):
    return repGetAllTransactions(userId)

def insertCategory(category, userId):
    name = category[c.NAME]
    isIncome = category[c.TRANSACTION_TYPE] == c.INCOME
    repInsertCategory(name, isIncome, userId)

    return 'Success'

def insertPerson(person, userId):
    name = person[c.NAME]
    repInsertPerson(name, userId)

    return 'Success'

def insertBudget(budget, userId):
    comment = budget[c.COMMENT]
    categoryId = budget[c.CATEGORY][0]
    amount = budget[c.AMOUNT]
    month = budget[c.MONTH]
    year = budget[c.YEAR]
    repInsertBudget(month, year, amount, comment, categoryId, userId)

    return 'Success'



def insertTransaction(transaction, userId):
    comment = transaction[c.COMMENT]
    date = transaction[c.DATE]
    amount = transaction[c.AMOUNT]
    categoryId = transaction[c.CATEGORY][0]
    isIncome = transaction[c.CATEGORY][2] == c.INCOME
    isSplit = transaction[c.SPLIT_WITH][c.NAME] != c.NO_SPLIT
    splitWithId = transaction[c.SPLIT_WITH][c.ID]
    myPortion = transaction[c.MY_PORTION]

    if(isIncome):
        repInsertIncome(date, amount, comment, categoryId, userId)

    elif(isSplit):
        expensePortion = amount * myPortion/100
        moneyOwed = amount - expensePortion
        expenseId = repInsertExpense(date, expensePortion, comment, categoryId, userId)
        repInsertMoneyOwed(date, moneyOwed, comment, splitWithId, expenseId, userId)

    else:
        repInsertExpense(date, amount, comment, categoryId, userId)

    return 'Success'

def listOfDictsToDict(listOfDicts):
    result = {}
    for d in listOfDicts:
        result.update(d)
    return result

def validateSession(userId):
    if(len(repGetUser(userId)) == 0):
        repAddUser(userId)
        return jsonify("Successfully added a new user.")
    else:
        return jsonify("Successfully authenticated existing user.")