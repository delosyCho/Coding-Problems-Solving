class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_register = {}
        word_positions = {}
        word_positions_ = {}

        for w in range(len(words)):
            words_register[w] = -1
            word_positions[words[w]] = []
            word_positions_[words[w]] = []
            
        for i in range(len(s)):
            for w in range(len(words)):
                if words_register[w] == -1:
                    if s[i] == words[w][0]:
                        # print('@@@@', words[w][0], i)
                        words_register[w] = 0

                        if words_register[w] + 1 == len(words[w]):
                            word_positions[words[w]].append(i + 1 - len(words[w]))
                            word_positions_[words[w]].append(i)
                            
                            words_register[w] = -1
                            # print('####')

                else:
                    # print('!!!!', words[w][0], i)
                    j = words_register[w]
                    if s[i] == words[w][j + 1]:
                        # print('!!!!', words[w][j + 1])
                        words_register[w] += 1

                        if words_register[w] + 1 == len(words[w]):
                            word_positions[words[w]].append(i + 1 - len(words[w]))
                            word_positions_[words[w]].append(i)

                            words_register[w] = -1
                    else:
                        words_register[w] = -1

        tuples_list = []
        for w in range(len(words)):
            for word_position in word_positions[words[w]]:
                if (word_position, w) not in tuples_list:
                    tuples_list.append((word_position, w))
        
        sorted_list = sorted(tuples_list, key=lambda x: x[0])
        print(sorted_list)
        result = []

        for i in range(len(sorted_list)):
            if len(words) == 1:
                if sorted_list[i][0] not in result:
                    result.append(sorted_list[i][0])
                continue

            con_words = {}
            position = sorted_list[i][0] + len(words[sorted_list[i][1]])
            # print(position)
            con_words[sorted_list[i][1]] = 1

            for j in range(i + 1, len(sorted_list)):
                if sorted_list[j][0] > position:
                    break
                
                if sorted_list[j][0] == position:
                    if sorted_list[j][1] not in con_words:
                        con_words[sorted_list[j][1]] = 1
                        position = sorted_list[j][0] + len(words[sorted_list[j][1]])

                        if len(con_words) == len(words):
                            if sorted_list[i][0] not in result:
                                result.append(sorted_list[i][0])
                            break

        return result
