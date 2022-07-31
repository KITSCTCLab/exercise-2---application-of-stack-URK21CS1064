class Evaluate:
    def _init_(self, size):
        self.top = -1
        self.size = size
        self.lst = [None]*size
    def isEmpty(self):
        if self.top == -1:
           return 1
        else :
           return 0
    def is_full(self):

        if self.top == (self.size - 1):
          return 1
        else :
          return 0
    def pop(self):
        if not self.isEmpty():
          z=self.lst[self.top]
          del self.lst[self.top]
          self.top-=1
          return z
    def push(self, operand):
        if not self.is_full():
          self.top+=1
          self.lst[self.top]=operand
    def validate_postfix_expression(self, expression):
        count_1=0
        count_2=0
        for i in expression:
          if i.isdigit():
            count_1+=1
          else:
            count_2+=1
        if count_1>count_2 and expression[0].isdigit() and expression[1].isdigit():
          return 1
        else:
          return 1
    def evaluate_postfix_expression(self, expression):
        for i in expression:
          if i.isdigit():
            self.push(i)
          else:
            var_1 = self.pop()
            var_2 = self.pop()
            if i=='/':
              self.push(str(eval(var_2 + i*2 + var_1)))
            else:
              self.push(str(eval(var_2 + i + var_1)))
        return self.pop()


postfix_expression = input()  
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
