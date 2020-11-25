#function.py
#Declaring a function
def showdata():
    print("Today is a great day")

showdata()
#To pass in a name
def showdata(name):
    print( "Azubi " +  name + " said \" Today is a great day\"")

showdata ('Ajara')
showdata ('Ama')
showdata ('Marian')

# Returning a result
def addition(a, b):
    sum= (a+b)
    return sum
result= addition (1,2)
print("Result is " + str(result))

#passing a name and a quote
def showdata(name, quote):
    print("Azubi " + name + " said " + quote)

showdata('Ajara', 'Today is a great day')
showdata('Nana Akosua', 'Tomorrow is going to be a great day')
showdata('Nana Adjoa', 'Next month is going to be a wonderful month ')
showdata('Joseeph', 'Next year will be a year to remember') 


#Show a list containing short messages
#pass the list to a function called showmessages
#the function is supposed to print each short messages in defining our function
#within function,we can implement conditionals, loops, etc
#the messages becomes the argument that is passed in place of the texts
messages=["i love Waakye ", "I'm going to buy some","its just by the roadside"]
def showMessages(texts):
    for text in texts:
        print(text)

showMessages(messages)


def greetings(name):
    print("Hello," + name)

    



