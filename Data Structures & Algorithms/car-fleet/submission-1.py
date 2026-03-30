

class Solution:
    def carFleet(self,target, position, speed):
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)  

        fleets = 0
        max_time = 0

        for p, time in cars:
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets

        