#loops.py
# Using the for loop;

vowels = ["a","e","i","o"]
for vowel in vowels:
  print( vowel +" is vowel")
print( "This is done" )  

#To find the cube of number list using the for loop
numbers=[1,2,3,4,5]
for number in numbers:
  print(number **3)
#method2
numbers=[1,2,3,4,5]
for number in numbers:
  print(number*number*number)
  # method3
  numbers= range(1,6)
  for number in numbers:
    print(f"The cube of {number} is {number ** 3}")
  print("This is done")

  # The while loop
  order=5
  while order>0:
    print(str(order)+ "has been fulfilled")
    order= order -1
  
















