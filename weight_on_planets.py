w = float(input('Enter your weight '))

option = float(input('Enter planet 1 - moon, 2-mars, 3 jupiter '))


mass = w / 9.8

if option == 1:
   g = 1.625
   result = mass * g
   print('your weight on moon is', result)

if option == 2 :
   g = 3.72076 
   result = mass * g
   print('your weight on moon is', result)

if option == 3 :
   g = 24.79 
   result = mass * g
   print('your weight on moon is', result)



