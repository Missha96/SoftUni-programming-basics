from math import ceil

people = int(input())
capacity = int(input())
courses = 0

courses = people / capacity
print(ceil(courses))