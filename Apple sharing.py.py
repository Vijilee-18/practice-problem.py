'''author:Vijilee george kurian
  description:program to find  How many apples will each single student get? How many apples will remain in the basket?
  if N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket'''
students=int(input("enter the number of student's:"))
apple=int(input("enter the total apple:"))
apple_for_students=apple//students
a=students*apple_for_students
remaining=apple-a
print(apple_for_students,remaining)