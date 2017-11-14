class Stackzyz(int):

    def __init__(self,size):
        self.__size = size
        self.__stack = []

    def __str__(self):
        return str(self.__stack)

    def __isfull(self):
        if len(self.__stack) == self.__size:
            return True
        else:
            return False

    def __isempty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def getsize(self):
        return len(self.__stack)

    def push(self,x):
        if self.__isfull():
            raise Exception("Stack is full")
        else:
            self.__stack.append(x)

    def pop(self):
        if self.__isempty():
            raise Exception("Stack is empty")
        else:
            self.__stack.pop(-1)

if __name__ == '__main__':
        TestZyzStack = Stackzyz(10)
        TestZyzStack.push(1)
        TestZyzStack.push(2)
        TestZyzStack.push(3)
        print TestZyzStack.getsize()
        print TestZyzStack
        TestZyzStack.pop()
        TestZyzStack.pop()
        TestZyzStack.pop()
        print TestZyzStack
