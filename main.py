
class Stack:
    stack = []
    def init(self):
        pass
    
    def isEmpty(self):
        return len(self.stack)==0
        
    def push(self, item):
       self.stack.append(item)
    
    def pop(self):
        self.stack.pop()
        if self.isEmpty() == True:
            res = None
        else:
            res = self.stack[-1]
        return res

    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
def check_balance(check_list): 
    symbols = {')':'(',']':'[','}':'{'}
    symbols_open = ['(', '[', '{']
    check_symb = list(check_list)
    stack_list = Stack() 
    for i in check_symb:
        if i not in symbols_open and stack_list.isEmpty() == True:
            result = 'Unbalanced'
            break
        else:
            if i in symbols_open:
                stack_list.push(i)
            elif i not in symbols_open:
                if stack_list.peek() == symbols[i]:
                    stack_list.pop()
                else:
                    result = 'Unbalanced'
                    break              
        if stack_list.isEmpty() == True:
            result = 'Balanced'
        else:
            result = 'Unbalanced'
    return result
        
        
if __name__ == '__main__':
    check_list = '[]{}()'
    print(check_balance(check_list))
   
        