# ------------------------------------------------------------------------------------------------
#PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1 #PART1  
#-------------------------------------------------------------------------------------------------
# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]  = 15
print (x)

#2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0][2]  = 'Bryant'
print(students)

#3In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = 'Andres'
print(sports_directory)

#4.Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30    
print(z)

# ------------------------------------------------------------------------------------------------
#PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2 #PART2
# -------------------------------------------------------------------------------------------------
def iterateDictionary(items):
    for item in items:
        for key, value in item.items():
            print(f'{key} - {value}', end=', ')
        print()

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)
# ------------------------------------------------------------------------------------------------
#PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3 #PART3
# -------------------------------------------------------------------------------------------------
def itesrateDictionary2(key_name, some_list):
    for item in some_list:
        return(item[key_name])

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

y = itesrateDictionary2('first_name', students)
print(y)

#------------------------------------------------------------------------------------------------
#PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4 #PART4
# ------------------------------------------------------------------------------------------------
def printInfo(some_dict):
    for key, value in some_dict.items():    
        print(len(value), key)
        print(sep='/n')
        for item in value:
            print(item,end='')
            print()
         

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)