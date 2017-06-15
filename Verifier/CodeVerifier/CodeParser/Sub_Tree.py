class HeapQueue:
    def __init__(self,key):
        self.heapList = [key]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if(isinstance(self.heapList[i,Sub])):
                if self.heapList[i].get_priority < self.heapList[i // 2].get_priority:
                    tmp = self.heapList[i // 2]
                    self.heapList[i // 2] = self.heapList[i]
                    self.heapList[i] = tmp
            i = i // 2

    def enqueue(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].get_priority > self.heapList[mc].get_priority:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].get_priority < self.heapList[i*2+1].get_priority:
                return i * 2
            else:
                return i * 2 + 1

    @property
    def dequeue(self):
        retval = self.heapList[1]
        self.heapList[1].get_priority = self.heapList[self.currentSize].get_priority
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    @property
    def isEmpty(self):
        return (self.currentSize == 0)

    @property
    def peak(self):
        return self.heapList[1]

    def heapfy(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

class Sub:
    def __init__(self,val,priority=0):
        self.p = priority
        self.val = val
        self.children = HeapQueue(self)
    
    @property
    def set_priority(self,p):
        self.p = p

    @property
    def get_priority(self):
        return self.p

    @property
    def get_value(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def add_sub(self,k,p):
        al = Sub(k,p)
        self.children.enqueue(al)

    def add_sub_tree(self,list_):
        self.children.heapfy(list_)

    def get_Head(self):
        return self.children.dequeue