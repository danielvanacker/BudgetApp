import repository

def getAllPeople():
    return repository.getAllPeople()

def getAllCategories():
    return repository.getAllCategories()

def insertTransaction(transaction):
    print(transaction)
    print(transaction['comment'])
    return 'Success'