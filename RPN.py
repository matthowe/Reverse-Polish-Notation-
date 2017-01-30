class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def open(self):
         print(self.items())
         return
      


def isInt(value): #to test if input is an integer or operator
  try:
    int(value)
    return True
  except:
    return False

text = input("Input Postfix String: ")

postfix = Stack()

for i in text:
     postfix.push(i) #Stack for postfix list of instructions now complete





#for i in text:
#    if isInt(i)==False:
#      operator.append(i)
