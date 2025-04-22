stud_score = [50,100,95,84,55,63,78,90]

max = 0 
for score in stud_score:
    if score > max:
        max = score
print(max)
  
sum = 0            
for i in range(1,101):
    sum = sum + i
print(sum)

# Fizz buzz program 
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: 
        print(num)



