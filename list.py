""" import random
american_states = ['Washington','Virginia','West Virginia','Massacheusetts']
print(american_states[2])
american_states[0] = "Ohio"
print(american_states[0:-1])
print(american_states[-1])
num_length = len(american_states)
print(num_length)

friends = ["Alice","Bob","Cassandra","Monica"] 
rand = random.choice(friends)
print(rand)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) """

# Initialize a list
my_list = [1, 2, 3, 4, 5]

""" # Interchange first and last elements
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list
print("List after swapping first and last elements:", my_list) """

my_list[0] = my_list[1]
print(my_list)