numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum=numbers[0]
max_sum=numbers[0]
for number in numbers[1:]:
   current_sum = max(current_sum + number, number)
   max_sum = max(max_sum, current_sum)
print("Current_sum:",current_sum)
print("Max_sum:",max_sum)

//Ouput:
Current_sum: 5
Max_sum: 6
