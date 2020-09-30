import repository
from models import constants as c
from flask import jsonify

def getTransactionMonths(userId):
    return repository.getTransactionMonths(userId)

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
    result.update(listOfDictsToDict(repository.getTotalIncomeByMonth(userId)))
    return [result]

def getTotalExpensesByMonth(userId):
    result = {'category': 'Total Expenses', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repository.getTotalExpensesByMonth(userId)))
    return [result]

def getNetIncomeByMonth(userId):
    result = {'category': 'Net Income (Out)', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repository.getNetIncomeByMonth(userId)))
    return [result]

def getCategorySpendByMonth(userId):
    result = []
    categories = repository.getAllExpenseCategories(userId)
    for category in categories:
        row = {'category': category, 'transactionGroup': "Expense"}
        row.update(listOfDictsToDict(repository.getAggregateSpendByCategory(category, userId)))
        result.append(row)
    return result

def getCategoryIncomeByMonth(userId):
    result = []
    categories = repository.getAllIncomeCategories(userId)
    for category in categories:
        row = {'category': category, 'transactionGroup': "Income"}
        row.update(listOfDictsToDict(repository.getAggregateIncomeByCategory(category, userId)))
        result.append(row)
    return result

def getAllPeople(userId):
    return repository.getAllPeople(userId)

def getAllCategories(userId):
    return repository.getAllCategories(userId)

def getAllTransactions(userId):
    return repository.getAllTransactions(userId)

def insertTransaction(transaction, userId):
    comment = transaction[c.COMMENT]
    date = transaction[c.DATE]
    amount = transaction[c.AMOUNT]
    category = transaction[c.CATEGORY][0]
    isIncome = transaction[c.CATEGORY][1] == c.INCOME
    isSplit = transaction[c.SPLIT_WITH] != c.NO_SPLIT
    splitWith = transaction[c.SPLIT_WITH]
    myPortion = transaction[c.MY_PORTION]

    if(isIncome):
        repository.insertIncome(date, amount, comment, category, userId)

    elif(isSplit):
        expensePortion = amount * myPortion/100
        moneyOwed = amount - expensePortion
        expenseId = repository.insertExpense(date, expensePortion, comment, category, userId)
        repository.insertMoneyOwed(date, moneyOwed, comment, splitWith, expenseId, userId)

    else:
        repository.insertExpense(date, amount, comment, category, userId)

    return 'Success'

def listOfDictsToDict(listOfDicts):
    result = {}
    for d in listOfDicts:
        result.update(d)
    return result

def validateSession(userId):
    if(len(repository.getUser(userId)) == 0):
        repository.addUser(userId)
        return jsonify("Successfully added a new user.")
    else:
        return jsonify("Successfully authenticated existing user.")