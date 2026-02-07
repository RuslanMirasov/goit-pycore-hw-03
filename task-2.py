import random

def get_numbers_ticket(min, max, quantity):
   if (
      min < 1
      or min > max
      or max > 1000
      or quantity < 1
      or quantity > (max - min + 1)
   ):
      return []

   return sorted(random.sample(range(min, max + 1), quantity)) 

#test
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#test errors
print(get_numbers_ticket(0, 10, 3)) 
print(get_numbers_ticket(20, 10, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(1, 10, 0))
print(get_numbers_ticket(1, 5, 10)) 