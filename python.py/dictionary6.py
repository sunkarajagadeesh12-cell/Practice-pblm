"""
info = {
    "key" : "value",
    "name" : "apnacollege",
    "learner" : "Sai",
    "age" : "18",
    "is_adult" : "True",
    "marks" : "94.3",
    "subjects" : ["python", "c", "java"],
    12 : 29 #we can change our key value into integer 
}
info["name"] = "SaiJaggu"   #we can change the value 
info["surname"] = "khapra"  #we can add the value
print(info["name"])
print(info["age"])
print(info["marks"])
print(info)

#dictionary is a mutable because it store all types of data in it
#dictionary are unordered(no index in dictionary),mutable,don't allow duplicate keys
#no repetation of keys
#we ca also create an empty dictionary 
dict = {}
dict["name"] = "Sai"  #we can add the values in the empty dictionary
print(dict)

#nested dictionary

student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}
print(student)
print(student["Subjects"]["eng"]) #we can print a certain value in the dictionary
"""
"""
#dictionary methods
 #mydict.keys()
student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}
print(list(student.keys())) #typecasting into list
print(len(list(student.keys()))) #typecasting into list
print(student.keys())
"""

#mydict.values()
"""
student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}
print(list(student.values())) #typecasting into list
print(len(list(student.values()))) #typecasting into list
print(student) 
"""
"""
student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}

print(student.items())  #it converts in tuple where there are two tuples in the above program
pairs = list(student.items())  #in this we print the first tuple
print(pairs[0])

"""
"""
#mydict.get()
student = {

    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}
print(student["Subjects"]["phy"])
print(student["Subjects"].get("phy"))
print(student["name"])
print(student.get("name"))
"""
"""
print(student["name2"])  #it will print error
print(student.get("name2")) #it will not print error but it print none
"""

"""
#mydict.update()
#we can update or add a value in the dictionary
student = {
    "name" : "Sai",
    "Subjects" : {
       "phy" : 94,
        "math" : 99,
        "eng" : 90
}
}

#method1

student.update({"city" : "vizag"})
print(student)

#method2
new_dict = {"city" : "vizag", "age" : "16", "name" : "Jaggu"} #we can add multiple values in the dictionary
student.update(new_dict) #we can change the name in the dictionary
print(student)

"""
