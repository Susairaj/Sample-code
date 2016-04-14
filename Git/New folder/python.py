import random
operatorList = [ "+", "-", "*" ]
print 'Welcome To The Maths Quiz!'
s = 0
g = raw_input("Please Enter Your Full Name: ")
g = raw_input("Please Enter Your Form (A, B Or C): ")
for i in range(10): 
     term1 = random.randint(1,10) 
     term2 = random.randint(1,10)
     op = random.choice(operatorList)
     
     expression = "%d %s %d" % (term1, op, term2) 
     answer = eval(expression) 
     print expression, "= ???" 
     reply = int( raw_input("Enter your answer: ") ) 
     if (reply == answer): 
        print "Correct!"
        s=s+1
     else:  
        print "Oh No! The Correct Answer Is", answer
print "Well Done"
print "\nl Asked You 10 Questions. You Got %d Of 10" % s

----------------------------------------------------------------------------
#My first program in Python. Im still learning this programing language.

running = True 

while running:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("Addition")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first + secund
        print(first ,'+' ,secund ,'=' , result)
    elif cmd == 2:
        print("Subtraction")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first - secund
        print(first ,"-" ,secund ,"=" , result)
    elif cmd == 3:
        print("Mmltiplication")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first * secund
        print(first ,"*" ,secund ,"=" , result)
    elif cmd == 4:
        print("Division")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first / secund
        print(first ,"/" ,secund ,"=" , result)
    elif cmd == 5:
        print("Quit!")
        running = False
		----------------------------------------------------------------------------