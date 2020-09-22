import repository
from models import constants as c

def getTransactionMonths():
    return repository.getTransactionMonths()

def getElapsedBudget():
    result = []
    expenses = getCategorySpendByMonth()
    income = getCategoryIncomeByMonth()
    totalIncome = getTotalIncomeByMonth()
    totalExpenses = getTotalExpensesByMonth()
    netIncome = getNetIncomeByMonth()
    return income + totalIncome + expenses + totalExpenses + netIncome

def getTotalIncomeByMonth():
    result = {'category': 'Total Income', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repository.getTotalIncomeByMonth()))
    return [result]

def getTotalExpensesByMonth():
    result = {'category': 'Total Expenses', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repository.getTotalExpensesByMonth()))
    return [result]

def getNetIncomeByMonth():
    result = {'category': 'Net Income (Out)', 'transactionGroup': 'Aggregate'}
    result.update(listOfDictsToDict(repository.getNetIncomeByMonth()))
    return [result]

def getCategorySpendByMonth():
    result = []
    categories = repository.getAllExpenseCategories()
    for category in categories:
        row = {'category': category, 'transactionGroup': "Expense"}
        row.update(listOfDictsToDict(repository.getAggregateSpendByCategory(category)))
        result.append(row)
    return result

def getCategoryIncomeByMonth():
    result = []
    categories = repository.getAllIncomeCategories()
    for category in categories:
        row = {'category': category, 'transactionGroup': "Income"}
        row.update(listOfDictsToDict(repository.getAggregateIncomeByCategory(category)))
        result.append(row)
    return result

def getAllPeople():
    return repository.getAllPeople()

def getAllCategories():
    return repository.getAllCategories()

def getAllTransactions():
    return repository.getAllTransactions()

def insertTransaction(transaction):
    comment = transaction[c.COMMENT]
    date = transaction[c.DATE]
    amount = transaction[c.AMOUNT]
    category = transaction[c.CATEGORY][0]
    isIncome = transaction[c.CATEGORY][1] == c.INCOME
    isSplit = transaction[c.SPLIT_WITH] != c.NO_SPLIT
    splitWith = transaction[c.SPLIT_WITH]
    myPortion = transaction[c.MY_PORTION]

    if(isIncome):
        repository.insertIncome(date, amount, comment, category)

    elif(isSplit):
        expensePortion = amount * myPortion/100
        moneyOwed = amount - expensePortion
        expenseId = repository.insertExpense(date, expensePortion, comment, category)
        repository.insertMoneyOwed(date, moneyOwed, comment, splitWith, expenseId)

    else:
        repository.insertExpense(date, amount, comment, category)

    return 'Success'

def listOfDictsToDict(listOfDicts):
    result = {}
    for d in listOfDicts:
        result.update(d)
    return result