numbers = [1, 7 ,3 ,6 ,8 , -7, 4, 2]

odd_numbers = []
even_numbers = []

for number in numbers:
    if number%2 == 0:       
        even_numbers.append (number)
    else:
        odd_numbers.append(number)



print(odd_numbers)
print(even_numbers)