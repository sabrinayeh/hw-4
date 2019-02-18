#reverse a string manually

reverse = "reverse"
reverse_manually = "serever"

print(reverse_manually)


#reverse a string using an empty string

user_entry = input('Please enter your favorite number: ')
reverse_user_entry = ""


for each_word in user_entry:
	reverse_user_entry = each_word + reverse_user_entry

print(reverse_user_entry)

