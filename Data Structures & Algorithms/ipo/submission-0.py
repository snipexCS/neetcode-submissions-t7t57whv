class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(cap, prof) for cap, prof in zip(capital, profits)]
        maxHeap = []
        heapq.heapify(minHeap)

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                cap, prof = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -prof)
            
            if not maxHeap:
                break
            
            w += -heapq.heappop(maxHeap)
        
        return w