class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        arr_lists = []
        for n in range(numRows):
            arr = ''
            arr_lists.append('')

        step = 0
        i = 0
        
        while True:
            if step == numRows - 1:
                step = 0

            if step == 0:
                for k in range(numRows):
                    arr_lists[k] += s[i]
                    i += 1
                    
                    if i == len(s):
                        break
            else:
                # print(step, s[i])
                arr_lists[numRows - 1 - step] += s[i]
                i += 1
            
            step += 1

            if i == len(s):
                break

        result = ''.join(arr_lists)
        
        return result