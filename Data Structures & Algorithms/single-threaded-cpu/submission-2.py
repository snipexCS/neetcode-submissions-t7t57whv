class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        minHeap = []
        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda t:t[0])
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i += 1 
            if not minHeap:
                time = tasks[i][0]
            else:
                enq , process = heapq.heappop(minHeap)
                time+= enq
                res.append(process)
        return res
            