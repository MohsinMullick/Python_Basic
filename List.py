"""
List:A list is a collection of items in a particula order.
You can make a list  that includes the
       letters of the alphabet,number of digit(0 to 9) and name of the people in your family.
"""
bicycle=["Trek","Cannondale"]#create a list name bicycle  with two strings elements
print("All bicycle list below:")
print(bicycle)#Print the entire list

####Accessing elements
bicycle=['trek','cannondale','redline']#create a list with three bicycle brand names
print("Specific item or elements below:")
print(bicycle[0])#print the first item in the list index[0]

###title()method list
bicycle=["trek","cannondale","redline"]#create a list with three bicycle brand name
print("Specific element with title:")
print(bicycle[2].title())#print the third item in the list index[2] with title method


####last item or elements
bicycle=["trek","cannondale","redline"]
print("Last elements:")
print(bicycle[-1])

###Using individual value from a list
fruits=['Apple','Banana','Orange','Strawberry','Cherry']
print(f"All fruits elements are: {fruits}")
print(f"My favorite fruits always {fruits[3].title()}")

####Modifying adding and removing elements
motorcycle=['Hunda','Yamaha','Suzuki']
print(motorcycle)
motorcycle[0]='Ducati'
print(motorcycle)
motorcycle.append("Ktm")
print(motorcycle)
motorcycle.insert(0,'Royal Enfield')
print(motorcycle)
pop_motorcycle=motorcycle.pop()
print(pop_motorcycle)