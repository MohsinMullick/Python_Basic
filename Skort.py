"""Sort a list permanently with the sort() method """
cars=["BMW","AUDI","FORD","TOYOTA","SUBARU"]#create a list with car brand name
print(f"Here the orginal list: {cars}")#print all list elements
cars.sort()#cars brand name alphabatically sorted
print(f"Here the sorted list: {cars}")#print all sorted list
cars.reverse()#all sorted list reverse
print(f"Reverse: {cars}")#print reverse
print(len(cars))#print total elements with length function