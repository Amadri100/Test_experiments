def get_num(num: float, porcent: float):
     'This function gives the value of a porcentage of a number (num, por)'
     try:
          n_num = num / 100 #The result of this operation will be 1% of the 100%
          return n_num * porcent
     except TypeError:
          print("Only use float or int values")
          print('Type error ocurred try again')
          return None

    
def get_por(num1: float, num2: float, roun = 5):
     'This function gives the porcentage that num 2 represent of num1, roun is the amount of numbers the round is going to be (num1, num2, roun).\n Output (Unrounded, rounded, and string(from round)'
     try:
          base = num1 / 100
          por = num2 / base
          por_round = round(por, roun)
          por_string = f"{por_round}%"
          return por, por_round, por_string
     except TypeError:
          print("Only use float or int values")
          print('Type error ocurred try again')
          return None
def check_por(base_num: float, num1: float, por: float):
     '''This function gets the value of the porcentage that represents num1 in base_num
     and compares it to the por parameter that is the porcentage that the number is supposed to represent.
     Return True or False.
     Don't use "%" in por only numbers'''
     try:
          porcent = 100 / base_num
          num1_porcentage = num1 * porcent
          g = por == num1_porcentage
          return g
     except TypeError:
          print("Only use float or int values")
          print('Type error ocurred try again')
          return None
f = check_por(10, 100, 1000)  
print(f)
