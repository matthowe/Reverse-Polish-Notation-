import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow}

class Stack:
    def __init__(self):
        self.content = []

    def push(self,thing):
        self.content.append(thing)

    def isEmpty(self):
        if len(self.content) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty() == False:
            return(self.content.pop())
        else:
            print('cannot pop from an empty list')

class Rpn:
    def __init__(self,expression):
        self.expression = expression
        self.stack = Stack()

        self.getElement()
        print(self.answer())

    def getElement(self):

        for i in self.expression.split(" "):
            try:
                int(i)
                self.isInt(i)
                
            except ValueError:
                self.isOp(i)
                
    def isInt(self,i):
        self.stack.push(int(i))
        

    def isOp(self,i):
        
        a = self.stack.pop()
        b = self.stack.pop()

        self.stack.push(ops[i](b,a)) # push the result of the calculation on the stack


    def answer(self):
        return self.stack.pop() # pop final item from list which is answer
    


test = Rpn("2 8 2 2 + / ^")
