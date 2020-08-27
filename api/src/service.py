import repository
from models import constants as c

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