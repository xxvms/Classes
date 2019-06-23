from classes import *
# another way is to do this
# import classes
# then fran = classes.HighSchoolStudent("frank")
# or we can use from classes import [then name of class or method or * for all

frank = HighSchoolStudent("frank")
print("Printing from Classes file")
print(frank.get_name_capitalize())
