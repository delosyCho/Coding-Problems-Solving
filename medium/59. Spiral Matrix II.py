class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for _ in range(n):
            line = [-1] * n
            result.append(line)

        direction = 0

        add_x = 1
        add_y = 0
        
        x, y = 0, 0
        count = 1
        result[y][x] = count

        while True:
            if add_x == 1:
                if x == n - 1 or result[y][x + 1] != -1:
                    add_x = 0
                    add_y = 1

                    if y == n - 1 or result[y + 1][x] != -1:
                        break
                    continue
            if add_x == -1:
                if x == 0 or result[y][x - 1] != -1:
                    add_x = 0
                    add_y = -1

                    if y == 0 or result[y - 1][x] != -1:
                        break
                    continue
            
            if add_y == 1:
                if y == n - 1 or result[y + 1][x] != -1:
                    add_x = -1
                    add_y = 0

                    if x == 0 or result[y][x - 1] != -1:
                        break
                    continue
            if add_y == -1:
                if y == 0 or result[y - 1][x] != -1:
                    add_x = 1
                    add_y = 0

                    if x == n - 1 or result[y][x + 1] != -1:
                        break
                    continue
            
            x += add_x
            y += add_y
            result[y][x] = count + 1
            
            # print(x, y, '|', add_x, add_y)
            
            count += 1
        return result
