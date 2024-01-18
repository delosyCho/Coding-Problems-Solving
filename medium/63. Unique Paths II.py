class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        path_dict = {}
        visited_dict = {}
        
        nodes_to_visit = []
        
        nodes_to_visit.append((0, 0))
        path_dict[(0, 0)] = 1
        
        dest = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        if obstacleGrid[0][0] == 1:
                return 0
        if dest == (0, 0):
            return 1
        
        while len(nodes_to_visit) > 0:
            position = nodes_to_visit.pop(0)
            
            x, y = position
            # print(position, path_dict[position])
            if (x, y) in visited_dict:
                continue
            visited_dict[(x, y)] = 1
            
            if x + 1 < len(obstacleGrid):
                if obstacleGrid[x + 1][y] != 1:
                    if (x+1, y) not in path_dict:
                        path_dict[(x+1, y)] = 0
                    path_dict[(x+1, y)] += path_dict[(x, y)]
                    nodes_to_visit.append((x+1, y))

            if y + 1 < len(obstacleGrid[0]):
                if obstacleGrid[x][y + 1] != 1:
                    if (x, y+1) not in path_dict:
                        path_dict[(x, y+1)] = 0
                    path_dict[(x, y+1)] += path_dict[(x, y)]
                    nodes_to_visit.append((x, y+1))
        


        if dest not in path_dict:
            return 0
        return path_dict[dest]