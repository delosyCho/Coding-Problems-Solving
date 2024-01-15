def convert_digit(word):
    word = word.replace('222', 'a')
    word = word.replace('22', 'b')
    word = word.replace('2', 'c')
    
    word = word.replace('333', 'd')
    word = word.replace('33', 'e')
    word = word.replace('3', 'f')

    word = word.replace('444', 'g')
    word = word.replace('44', 'h')
    word = word.replace('4', 'i')
    
    word = word.replace('555', 'j')
    word = word.replace('55', 'k')
    word = word.replace('5', 'l')

    word = word.replace('666', 'm')
    word = word.replace('66', 'n')
    word = word.replace('6', 'o')

    word = word.replace('7777', 'p')
    word = word.replace('777', 'q')
    word = word.replace('77', 'r')
    word = word.replace('7', 's')

    word = word.replace('888', 't')
    word = word.replace('88', 'u')
    word = word.replace('8', 'v')

    word = word.replace('9999', 'w')
    word = word.replace('999', 'x')
    word = word.replace('99', 'y')
    word = word.replace('9', 'z')
    return word.replace(' ', '')

class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return []

        start = int(digits[0])
        end = int(digits[-1])
        result = []
        def backtracking(arr, index, acc):
            if index >= len(digits):
                word = ''.join(arr)
                word = convert_digit(word)

                result.append(word)
                return
            
            if digits[index] == '7' or digits[index] == '9':
                if acc < 4:
                    arr.append(digits[index])
                    backtracking(arr, index, acc + 1)
                    arr.pop()
            else:
                if acc < 3:
                    arr.append(digits[index])
                    backtracking(arr, index, acc + 1)
                    arr.pop()
            
            if acc > 0:
                arr.append(' ')
                backtracking(arr, index + 1, 0)
                arr.pop()
        backtracking([], 0, 0)
        return result