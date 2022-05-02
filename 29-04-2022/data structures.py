'''************************---------ARRAY-----------********************'''

##from array import *

##arr = array('i',[1,2,3,4,5,6])  #creating an array of integer type
##print(arr)
##
##print(arr[0])
##print(arr[-1])

##arr[4] = 9
##arr[1:4] = array('i', [1,2,3])   #changing elements in an array
##print(arr)



##del arr[4]   #deleting an element from an array
##print(*arr)

##arr.append(7)        #appending an element to arr
##print(*arr)


##arr.remove(7)         #removing the first occurance of a number
##print(*arr)


##arr.index(3)          #returns index of first occurance of numbre

##print(len(arr))     #length of an array
##
##
##
##arr1 = array('d',[1.1, 2.4, 5.2, 8.3, 9.4])
##arr2 = array('d', [3.6, 1.7, 8.5, 6.9])
##arr3 = arr1 + arr2                      #combining 2 arrays
##arr4 = array('d')                      #creating an empty array of data type decimal
##print(arr3, type(arr3))



##for a in arr:
##    print(a)





'''**********************______________STACK_________________****************'''
##from queue import LifoQueue
##
##stack = LifoQueue(maxsize = 3)
##print(stack.qsize())      #getting the queue size
##
##stack.put("hi")          #pushing an element into a stack using put() func
##stack.put(2)
##print(stack.qsize())
##
##stack.put_nowait([1,2])
##print(stack.full())      #checking if the stack is full
##print(stack.get())     #popping an element out of the stack using get() func
##print(stack.qsize())
##
##print(stack.get())
##print(stack.get())
##
##print(stack.qsize())
##print(stack.empty())   #checking if the stack is empty






'''********************_____________QUEUE_____________*********************'''

##class Queue:
##    def __init__(self, maxsize):
##        self.q = []
##        self.maxsize = maxsize
##
##    def enQueue(self, val):
##        if len(self.q) < self.maxsize:
##            self.q.append(val)
##        else:
##            print("Queue is Full")
##            print(*self.q)
##
##    def deQueue(self):
##        if len(self.q) > 0:
##            rem = self.q.pop(0)
##            print("The removed element is " + str(rem))
##        else:
##            print("Queue is Empty")
##
##    def isEmpty(self):
##        return len(self.q) == 0
##
##    def isFull(self):
##        return len(self.q) == self.maxsize
##
##    def display(self):
##        print(*self.q)
##
##
##que = Queue(3)
##print(que.isEmpty())
##que.enQueue(1)
##que.enQueue(12)
##que.enQueue("hi")
##que.enQueue(4)
###que.display()




