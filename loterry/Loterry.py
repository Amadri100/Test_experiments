import random

class tickets:
    #self.num = is the amount of tickets
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
def plai():      
    while True:
        maxNum = input("Select the amount of lottery numbers: ")
        try:
            tick = tickets(int(maxNum))
            break
        except ValueError:
            print("That is not a number")
    f = tick.get_ticket()
    h = tick.winner()

    if f == h:
        print("Won")
    else:
        print('Not won')
plai()
while True:
    print("Want to play again(y or n)")
    ns = input(': ')
    if ns.lower() == 'y':
        plai()
    elif ns.lower() == 'n':
        break
    else:
        print("error try again")

