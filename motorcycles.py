motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

# Appending elements means adding elements to the list 
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
#Inserting elements into a list 

motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#removing elements from a list

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#removing items using pop method

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles=['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f" The last motorcycle I owned was a {last_owned.title()}.")