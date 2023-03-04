num1 = 42 #var declaration, initialize int
num2 = 2.3 #var declaration, initialize float
boolean = True #var declaration, initialize bool
string = 'Hello World' #var declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #var declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #var declaration, initialize dict
fruit = ('blueberry', 'strawberry', 'banana') #var declaration, initialize tuple
print(type(fruit)) #log the data type of the fruit var
print(pizza_toppings[1]) #log the value of pizza_toppings at idx 1
pizza_toppings.append('Mushrooms') #add Mushrooms to pizza_toppings as the last idx
print(person['name']) #log the value of the key name in the person dict
person['name'] = 'George' #update the value of the name key in person dict to George
person['eye_color'] = 'blue'  #update the value of the eye_color key in person dic to George
print(fruit[2]) #print the value of fruit tuple at idx 2

if num1 > 45: #conditional checking if the var num1 is > 45
    print("It's greater") #if conditional is true, then log It's greater
else: #if the conditional is false, do the next part instead
    print("It's lower") #log It's lower

if len(string) < 5: #conditional checking if the length of the var string is <5
    print("It's a short word!") #if above is true, log It's a short word!
elif len(string) > 15: #if the if condition is false, check if the length is > 15 (if above is true, skip this)
    print("It's a long word!") #log It's a long word!
else: #if all other conditionals above are false, do this instead
    print("Just right!") #log Just right! (okay, Goldilocks)

for x in range(5): #for loop with 5 iterations (0-4)
    print(x) #prints 0, 1, 2, 3, 4
for x in range(2,5): #for loop with 3 iterations (2-4)
    print(x) #prints 2, 3, 4
for x in range(2,10,3): #for loop with 3 iterations (2, 5, 8)
    print(x) #prints 2, 5, 8
x = 0 #var declaration initialize int
while(x < 5): #while loop that keeps going as long as x<5
    print(x) #prints x each iteration (0, 1, 2, 3, 4)
    x += 1 #increments x by 1 each iteration

pizza_toppings.pop() #removes the last idx of pizza_toppings
pizza_toppings.pop(1) #removes the item at idx 1 from pizza_toppings

print(person) #prints the entire person dict
person.pop('eye_color') #removes the eye_color key (& value) from person dict
print(person) #prints the entire person dict with the eye_color key now removed

for topping in pizza_toppings: #for loop that iterates through pizza_toppings list (5 times)
    if topping == 'Pepperoni': #checks current idx, true if the value is the str 'Pepperoni'
        continue #continues the loop 
    print('After 1st if statement') #prints After 1st if statement if the if was true
    if topping == 'Olives': #check current idx, true if the value is the str 'Olives'
        break #force quits the loop

def print_hello_ten_times(): #defines the function called print_hello_ten_times with no params
    for num in range(10): #for loop with 9 iterations
        print('Hello') #prints Hello every loop (9) times

print_hello_ten_times() #calls the function and passes no arguments, which will log Hello 9 times

def print_hello_x_times(x): #def function called print_hello_x_times with a single param
    for num in range(x): #for loop with a variable amount of iterations, taken from the function argument
        print('Hello') #print hello x times, range(x) has x values to iterate through

print_hello_x_times(4) #call function and pass 4, this will print Hello 4 times (range(x) has 0-3)

def print_hello_x_or_ten_times(x = 10): #defines a function with a default as 10
    for num in range(x): #ceates a for loop with x iterations
        print('Hello') #prints Hello each iteration

print_hello_x_or_ten_times() #calls function with default argument of 10
print_hello_x_or_ten_times(4) #calls function with argument of 4


"""
Bonus section
"""

# print(num3) #this will fail because num3 is not defined
# num3 = 72 #define var num3 and intialize an int
# fruit[0] = 'cranberry' #this assigns cranberry to fruit idx 0
# print(person['favorite_team']) #this won't print anything because that key does not exist
# print(pizza_toppings[7]) #this fails because the idx is out of range 
#   print(boolean) #indent error
# fruit.append('raspberry') #add raspberry to the fruit list
# fruit.pop(1) #removes the item at idx 1 from fruit list