import heapq

class Solution(object):
    def findRelativeRanks(self, score):
        heap = []
        rank = [None] * len(score)
        r = 1
        
        # maxheap
        for i, s in enumerate(score):
            # heappush -> [(-score, 원본 index)]
            heapq.heappush(heap, (-s, i))

        while heap:
            _, i = heapq.heappop(heap)
            if r == 1:
                rank[i] = "Gold Medal"
            elif r == 2:
                rank[i] = "Silver Medal"
            elif r == 3:
                rank[i] = "Bronze Medal"
            else:
                rank[i] = str(r)
                
            r += 1

        return rank