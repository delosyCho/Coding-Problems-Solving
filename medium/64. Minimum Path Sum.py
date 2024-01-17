import heapq

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        costs = {}
        heap = []
        
        heapq.heappush(heap, ((0, 0), 0))

        while heap:
            pos, cost = heapq.heappop(heap)

            if pos in costs:
                continue
            
            x, y = pos

            costs[pos] = cost + grid[x][y]
            if x + 1 < len(grid):
                heapq.heappush(heap, ((x + 1, y), costs[pos]))
            if y + 1 < len(grid[0]):
                heapq.heappush(heap, ((x, y + 1), costs[pos]))

        return costs[(len(grid) - 1, len(grid[0]) - 1)]
    


