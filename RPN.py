class Stack:
    """Implement a simple stack"""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
         return self.items.pop()

def isInt(value):
    """to test if input is an integer or operator"""
    try:
        int(value)
        return True
    except:
        return False

stack = Stack() #Initialise a simple stack to pop operands and results to

text = input("Input Postfix String: ")

for i in text: #Read each character of the string
     if isInt(i): #If it is a number
          i = int(i)
          stack.push(i) #Push to stack for postfix
     elif i == '+': #If operator, pop last two item from stack and carry out operation
          b = stack.pop()
          a = stack.pop()
          stack.push(a+b)
     elif i == '-':
          b = stack.pop()
          a = stack.pop()
          stack.push(a-b)
     elif i == '*':
          b = stack.pop()
          a = stack.pop()
          stack.push(a*b)
     elif i == '/':
          b = stack.pop()
          a = stack.pop()
          stack.push(a/b)
     elif i == '^':
          b = stack.pop()
          a = stack.pop()
          stack.push(a**b)
     else:
          pass

print ("Answer = ",stack.pop()) #Final pop should be answer
