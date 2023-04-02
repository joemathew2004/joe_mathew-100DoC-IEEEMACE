#replacing letter  with position values
def a(text):
    
    text = text.lower()
    string=''
    for i in text:
        if i.isalpha():
            string=string+str(ord(i)-96)
            string=string+" "
    return string.rstrip()


#square
def square():
    num=float(input('ENTERA NUMBER : '))
    return num**2

#array
number=[1,2,3]
while True:
    n=input("Enter the number to be stored : ")
    
    number.append(int(n))
    break
print(number)

#sum of array
def sum(a):
    total=0
    for i in a:
        total=total+i
    return total

#square sum
def sum_of_squares(a):
    total=0
    for i in a:
        total=total+i**2
    return total

