import random


class tickets:
    "self.num = is the amount of tickets"
    def __init__(self, num):
        self.num = num
    def get_ticket(self):
        my_num = random.randint(1, self.num)
        print(f"Your ticket number is {my_num}.")
        return my_num
    def winner(self):
        win_num = random.randint(1, self.num)
        print(f"Winner number is {win_num}.")
        return win_num
def plai(balance):
    #Istanciate the class for getting the winner and ticket numbers
    balance = balance - 4
    while True:
        maxNum = input("Select the amount of lottery numbers: ")
        #manages possible exceptions
        try: 
            if int(maxNum) <= 0:
                print('Number most be higher than 0')
                continue
            tick = tickets(int(maxNum))
            break
        except ValueError:
            print("That is not a number")
        except TypeError:
            print("Number error")
    f = tick.get_ticket()
    h = tick.winner()
    prize = int(maxNum) *3
    if f == h:
        balance = balance + prize       
        print("Won")
        print(f"Price is {prize}.")
        print("Current balance is " + str(balance) + ".")
    else:
        print('Not won')
        print("Current balance is " + str(balance) + ".")
    return balance
print("""
This is a lottery.
each ticket adds $3 to the price
tickets value $4. You can select how much tickets were sold.
""")
balance = plai(12)
while True:
    #To play again
    print("Want to play again(y or n)")
    ns = input(': ')
    if ns.lower() == 'y':
        balance = plai(balance)
    elif ns.lower() == 'n':
        print(f"Final balance {balance}...")
        break
    else:
        print("error try again")

