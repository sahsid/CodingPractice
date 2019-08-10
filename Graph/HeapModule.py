class MinHeap:

    def __init__(self, arr):
        self.heap_arr = []
        for item in arr:
            self.insert(item)

    def insert(self, item):
        self.heap_arr.append(item)
        self.__floatup(len(self.heap_arr) - 1)

    def pop(self):
        if not self.heap_arr:
            return
    
        self.__swap(0,-1)
        item = self.heap_arr.pop()
        if self.heap_arr:
            self.__sink(0)
        
        return item    

    def decreaseKey(self, key, newValue):
        try:
            keyIndex = self.heap_arr.index(key)
            self.heap_arr[keyIndex] = newValue
            self.__floatup(keyIndex)
        except ValueError:
            print("Error: key not found in heap")
            return
    
    def __sink(self, index):
        parent = index
        lChild = 2*index + 1
        rchild = lChild + 1

        smallerChild = None

        if lChild > len(self.heap_arr) - 1:
            return
        elif rchild > len(self.heap_arr) - 1:
            smallerChild = lChild
        else:
            if self.heap_arr[lChild] < self.heap_arr[rchild]:
                smallerChild = lChild
            else:
                smallerChild = rchild
        
        if self.heap_arr[parent] > self.heap_arr[smallerChild]:
            self.__swap(smallerChild, parent)
            self.__sink(smallerChild)

    def __floatup(self, index):

        parent = (index - 1)//2

        if parent < 0:
            return

        if self.heap_arr[parent] > self.heap_arr[index]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def __swap(self, i,j):
        self.heap_arr[i], self.heap_arr[j] = self.heap_arr[j], self.heap_arr[i]

    def len(self):
        return len(self.heap_arr)

class MaxHeap:

    def __init__(self, arr):
        self.heap_arr = []
        for item in arr:
            self.insert(item)

    def insert(self, item):
        self.heap_arr.append(item)
        self.__floatup(len(self.heap_arr) - 1)

    def pop(self):
        if not self.heap_arr:
            return

        self.__swap(0,-1)
        item = self.heap_arr.pop()
        if self.heap_arr:
            self.__sink(0)
        
        return item

    def increaseKey(self, key, newValue):
        try:
            keyIndex = self.heap_arr.index(key)
            self.heap_arr[keyIndex] = newValue
            self.__floatup(keyIndex)
        except ValueError:
            print("Error: key not found in heap")
            return
    
    def __sink(self, index):
        parent = index
        lChild = 2*index + 1
        rchild = lChild + 1

        largerChild = None

        if lChild > len(self.heap_arr) - 1:
            return
        elif rchild > len(self.heap_arr) - 1:
            largerChild = lChild
        else:
            if self.heap_arr[lChild] > self.heap_arr[rchild]:
                largerChild = lChild
            else:
                largerChild = rchild
        
        if self.heap_arr[parent] < self.heap_arr[largerChild]:
            self.__swap(largerChild, parent)
            self.__sink(largerChild)

    def __floatup(self, index):

        parent = (index - 1)//2

        if parent < 0:
            return
        
        if self.heap_arr[parent] < self.heap_arr[index]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def __swap(self, i,j):
        self.heap_arr[i], self.heap_arr[j] = self.heap_arr[j], self.heap_arr[i]
        
    def len(self):
        return len(self.heap_arr)