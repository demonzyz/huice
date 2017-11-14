class Stack(object):

    def __init__(self, size):
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
        return self.__size

    def push(self, x):
        if self.__isfull():
            raise Exception('Stack is full')
        self.__stack.append(x)

    def pop(self):
        if self.__isempty():
            raise Exception('Stack is empty')
        self.__stack.pop(-1)

if __name__ == '__main__':
    stackTest = Stack(10)
    stackTest.push(1)
    stackTest.push(2)
    stackTest.push(3)
    print stackTest.getsize()
    print stackTest
    stackTest.pop()
    print stackTest
