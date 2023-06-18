class Category:
    def __init__(self, name):
        self.ledger = []
        self.balance = 0
        self.catName = name
        self.withdrawals = 0

    def __str__(self):
        title = '*' * int((30 - len(self.catName))/2) + self.catName + '*' * int((30 - len(self.catName))/2) + '**' 
        ledger = ''
        for entry in self.ledger:
            description = entry['description']
            length = 29 - len(format(float(entry['amount']), '.2f'))
            ledger += description[0:length] + ' ' + format(entry['amount'], '.2f').rjust(29 - len(description)) + '\n'

        
        return title[0:30] + '\n' + ledger + 'Total: ' + str(self.balance)

    def deposit(self, amount, description = False):
        obj = dict() 
        obj["amount"] = amount
        self.balance += amount
        obj["description"] = ''
        if description != False:
            obj["description"] += description
        self.ledger.append(obj)

    def withdraw(self, amount, description = False):
        obj = dict() 

        if self.check_funds(amount):
           
            obj["amount"] = 0 - amount
            self.balance -= amount
            self.withdrawals += amount        
            obj["description"] = ''
            
            if description != False:
                obj["description"] += description
                
            self.ledger.append(obj)
            return True
            
        return False


    def transfer(self, amount, destination : 'Category'):
        
        if self.withdraw(amount, 'Transfer to ' + destination.catName) :
            destination.deposit(amount, 'Transfer from ' + self.catName)
            return True
        
        return False





    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

        

def create_spend_chart(categories : list[Category]):
    hyphens = (len(categories) * 3) + 1
    line = ('    ' + hyphens * '-') +'\n'

    chart = ''
    cat = ''

    catList = []
    withdrawsAmount = []
    
    for catItem in categories:
        catList.append(catItem.catName)
        withdrawsAmount.append(catItem.withdrawals)

    total = sum(withdrawsAmount)

    percentage = [round(amount*100/total) for amount in withdrawsAmount]
    print(percentage)
    percentage = [int(p/10)*10 for p in percentage]
    
    print(percentage)

    

    graph = ['' for i in range(11)]

    for g in range(len(graph)):
        flag = 0
        for p in percentage:    
            if p >= (g*10):
                if flag == 1:
                    graph[g] += 2*' ' + 'o'
                elif percentage.index(p) == 0:
                    graph[g] += ' ' + 'o'
                    flag = 1
                else:
                    print(percentage.index(p))
                    graph[g] += ((percentage.index(p)+1)*2) * ' ' + 'o'
                    flag = 1
        graph[g] += (10 - len(graph[g]))* ' '
            


    for i in range(100, -1, -10):
        chart += (str(i) + '|').rjust(4)
        chart += graph[int(i/10)]
        chart += '\n'

    number = max([len(i) for i in catList])

    for i in range(number):
        cat += 5*' '
        for item in catList:
            if i >= len(item):
                cat += '   '
            else:
                cat += item[i] + '  '
        if i < (number - 1):
            cat += '\n'

    return 'Percentage spent by category\n' + chart + line + cat




food = Category('food')
entertainment = Category('entertainment')
business = Category('business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([ business, food, entertainment]))






'''
test = Category('Food')



test2 = Category('Clothing')
test3 = Category('Auto')


test.deposit(2000, 'initial deposit')
test.withdraw(50, 'cold drink')
test.withdraw(700.25, 'restaurant and more food')
test.transfer(500, test2)

test2.deposit(1000, 'initial deposit')
test2.withdraw(100, 'T-shirt')
test2.withdraw(300, 'Shoes')

test3.deposit(3000, 'initial deposit')
test3.withdraw(300, 'Fuel')

#print(test, test2, test3)
#print(test2)


#create_spend_chart([test, test2, test3])


print(create_spend_chart([test, test2, test3]))
'''