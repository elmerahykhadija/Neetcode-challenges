"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination."""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        both=[]
        for i in range(0,len(position)):
            t=[position[i],speed[i]]
            both.append(t)
        both.sort(reverse=True)
        for i in both:
            if i[1]!=0:
                time=(target-i[0])/i[1]
            if stack and stack[-1]<time:
                stack.append(time)
            if not stack:
                stack.append(time)
        return len(stack)

#-------------------------------------------------
#------Method 2----------------------
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)
        stack=[]
        count=0
        for i in range(len(cars)):
            if not stack:
                stack.append(cars[i])
            else :
                t=(target-cars[i][0])/cars[i][1]
                h=(target-stack[-1][0])/stack[-1][1]
                if t >h:
                    stack.append(cars[i])
        return len(stack)    
        