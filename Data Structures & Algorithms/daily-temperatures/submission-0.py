class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output=[0]*len(temperatures)
        for i in range(len(temperatures)):
            counter=0
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    output[i]=counter
                    break
                else:
                    counter+=1
        return output
