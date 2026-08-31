num = int(input("Enter a number: "))

file = open("fizzbuzz_output.txt", "w")

for i in range(1, num + 1):

    if i % 3 == 0 and i % 5 == 0:
        result = "FizzBuzz"

    elif i % 3 == 0:
        result = "Fizz"

    elif i % 5 == 0:
        result = "Buzz"

    else:
        result = i

    print(result)
    file.write(str(result) + "\n")

file.close()

print("FizzBuzz output saved to fizzbuzz_output.txt")