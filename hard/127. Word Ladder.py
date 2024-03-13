from collections import deque

def is_one_letter_different(str1, str2):
    # 두 문자열의 길이가 다르면 바로 False를 반환
    if len(str1) != len(str2):
        return False
    
    # 서로 다른 문자의 수를 세기
    diff_count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diff_count += 1
            # 서로 다른 문자가 두 개 이상이면 바로 False를 반환
            if diff_count > 1:
                return False
    
    # 정확히 한 문자만 다른 경우 True를 반환
    return diff_count == 1

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        end_i = wordList.index(endWord)

        edge = {}
        
        visited = set()
        visited.add(beginWord)        
        
        nodes = deque()
        nodes.append([beginWord, 1])

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        while nodes:
            node, distance = nodes.popleft()

            for i in range(len(node)):
                intermediate_word = node[:i] + '*' + node[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return distance + 1

                    if word not in visited:
                        visited.add(word)
                        nodes.append([word, distance + 1])

        return 0
 
                



