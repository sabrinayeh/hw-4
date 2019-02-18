# <Input Prompt:> What calculation would you like to do? (add, sub, mult, div)
# <User Input:> add
# <Input Prompt:> What is number 1?
# <User Input:> 3
# <Input Prompt:> What is number 2?
# <User Input:> 6

# Your expected program output:
#"Your result is 9. Calc U later!""


calculation = input("What calculation would you like to do? (add, sub, mult, div)")
number_1 = int(input("Please enter a number. "))
number_2 = int(input("Please enter a second number. "))

res = 0 

if calculation == "add":
	res = number_1 + number_2
elif calculation == "sub":
	res = number_1 - number_2
elif calculation == "mult":
	res = number_1 * number_2
elif calculation == "div":
	res = number_1 / number_2

print(res)