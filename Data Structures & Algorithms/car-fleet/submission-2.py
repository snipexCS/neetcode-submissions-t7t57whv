

class Solution:
    def carFleet(self,target, position, speed):
        cars = [(p, (target - p) / s) for p,s in zip(position,speed)]
        stack = []
        cars.sort(reverse=True)  


        for pos,time in cars:
            
            if not stack or time > stack[-1]:
                 stack.append(time)
            
           

        return len(stack)

        