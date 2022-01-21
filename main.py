class Calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def sqr(self):
        return self.a ** 2
    def sqrroot(self):
        return self.a ** 0.5
    def inverse(self):
        return 1//self.a
a = int(input('first number: '))
b = int(input('second number: '))
obj = Calculator(a,b)
choice = 1
while choice!= 0:
    print()
    print("0. exit")
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiply')
    print('4. Divion')
    print('5. Square')
    print('6. Square root')
    print('7. Inverse')
    print()
    choice = int(input('enter choice: '))
    print()
    if choice == 1:
        print('result: ',obj.add())
    elif choice == 2:
        print('result: ',obj.sub())
    elif choice == 3:
        print('result: ',obj.mul())
    elif choice == 4:
        print('result: ',obj.div())
    elif choice == 5:
        print('Square of',a,'is',obj.sqr())
    elif choice == 6:
        print('Square root of',a,'is',obj.sqrroot())
    elif choice == 7:
        print('Inverse of',a,'is',obj.inverse())
    elif choice == 0:
        print('exiting')
    else:
        print('invalid choice')
print()
