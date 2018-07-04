#wap to find the sqrt
num =8
num_sqrt =num**0.5
print('the square root of %0.3f is %0.3f'%(num,num_sqrt))
#wap to find area of the triangle
a = 5
b = 6
c = 7
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))*0.5
print('area of triangle is %0.2f'%area)
#WAP to solve quadratic quation
import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
# Write a program to print these things in each lines using fstrings and format way
my_name = 'Zed A. Shaw'
my_age=35#notalie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print(f'my name is {my_name},age is {my_age},height is {my_height},weight is {my_weight},eyes is {my_eyes},teeth is {my_teeth},hair is {my_hair}.')
print('my name is {},age is{},height is {},weight is{},eyes is{},teeth is{},hair is{}.'.format(my_name,my_age,my_height,my_weight,my_eyes,my_teeth,my_hair))