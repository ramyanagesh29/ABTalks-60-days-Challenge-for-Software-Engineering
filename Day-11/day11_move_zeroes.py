numbers = [0, 1, 0, 3, 12]
position = 0
for index, number in enumerate(numbers):
  if number!=0:
    numbers[position]=number
    position+=1
for index in range(position, len(numbers)):
      numbers[index] = 0
print(numbers)

//output

[1, 3, 12, 0, 0]
