#The ADT PriorityQueue is implemented as a heap.

class priorityQueue:
    def __init__(self):
        self.heap=[]                # an array of integers
        self.size = 0               # the size of heap

    def __len__(self):
        return self.size

    def parent(self,index):
        # index is between 1 and self.size
        # It returns the value of the parent of heap[index]
        if index<=1 or index>self.size:
            return None
        else:
            return self.heap[index//2-1]
        
    def leftChild(self,index):
        # It returns the value of the left child
        if index<1 or 2*index>self.size:
            return None
        else:
            return self.heap[index*2-1]
        
    def rightChild(self,index):
        # It returns the value of the right child
        if index<1 or 2*index+1>self.size:
            return None
        else:
            return self.heap[index*2]
        
    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
        
    def insert(self,x):
        # the funciton inserts x into the heap, satisfying the heap property
        self.size+=1
        self.heap.append(x)
        index = self.size
        while index>1 and x>self.parent(index):
            parentIndex = index//2
            self.swap(index, parentIndex)
            index = parentIndex
            


    def deleteMax(self):
        # The function returns the largest integer in self.heap if exists,
        #   otherwise None
        # After the maximum is deleted from self.heap,
        #   it must satisfy the heap property.
        if self.size<=0:
            return None
        elif self.size==1:
            self.size=0
            return self.heap[0]
        #--- code the remaining -----
        maxint = self.heap[0]
        self.swap(1, self.size)
        self.heap.pop()
        self.size-=1
        index = 1
        while True:
            if index*2+1>self.size and index*2>self.size:
                break
            elif index*2+1>self.size and index*2<=self.size:
                if self.size==2 and self.heap[0]>self.heap[1]:
                    break
                self.swap(index, index*2)
                index = index*2
                break
            elif self.heap[index-1]<self.leftChild(index) or self.heap[index-1]<self.rightChild(index):
                if self.leftChild(index)>self.rightChild(index):
                    self.swap(index, index*2)
                    index = index*2
                else:
                    self.swap(index, index*2+1)
                    index = index*2+1
            else:
                break
        return maxint

def heapSort(intList):
    # Sort intList into out, and return out
    out = []
    h = priorityQueue()
    for i in intList:
        h.insert(i)
        out.append(i)
    x = h.deleteMax()
    i=-1
    while x!=None:
        out[i]=x
        x = h.deleteMax()
        i-=1
    return out


       

#Test code
h = priorityQueue()
h.insert(10)
h.insert(5)
h.insert(14)
h.insert(9)
h.insert(2)
h.insert(11)
h.insert(6)
print(set(h.heap[0:h.size]))
x = h.deleteMax()
print(set(h.heap[0:h.size]))
x = h.deleteMax()
print(set(h.heap[0:h.size]))
x = h.deleteMax()
print(set(h.heap[0:h.size]))
### This should print out
#{2, 5, 6, 9, 10, 11, 14}
#{2, 5, 6, 9, 10, 11}
#{2, 5, 6, 9, 10}
#{9, 2, 5, 6}
# maximums are deleted one by one
print(heapSort([13, 4, 15, 9, 17, 6, 1, 8, 16, 3, 7]))
### The output should be
#[1, 3, 4, 6, 7, 8, 9, 13, 15, 16, 17]
