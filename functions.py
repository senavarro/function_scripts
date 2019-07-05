#Create a function that doubles the number given: 

def double_value(num):
	return num*2

n=10
n=double_value(n) 
print(n)


--------------------------------------

#Create a recursive function that gets the factorial of an undetermined number:

def factorial(num):
	print ("Initial value =", num)
	if num > 1:
		num = num * factorial(num -1)
	print ("Final value =", num)
	return num

print (factorial(5))

--------------------------------------

#Create a function that makes a countdown:

def countdown(num):

	while num > 0:
		num -=1
		print(num)
	else:
		print("It's the final countdown")

countdown(5)

--------------------------------------

#Create a function that allows undetermined args and kwargs:

def indetermined_position(*args, **kwargs):
	t=0
	for arg in args:
		t+=arg
	print("the total amount of args is:", t)
	for kwarg in kwargs:
		print(kwarg, kwargs[kwarg])

indetermined_position(1,2,3,4,5,6,7,8,9, name="Sergi", age=24)

