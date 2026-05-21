class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n=len(self.arr)//2
        if len(self.arr) ==1:
            return self.arr[0]
        return float(self.arr[n]+self.arr[n-1])/2 if len(self.arr)%2 == 0 else self.arr[n]
        
        