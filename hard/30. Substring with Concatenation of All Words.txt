class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        check_dict = {}
        for word in words:
            if word not in check_dict:
                check_dict[word] = 1
            else:
                check_dict[word] += 1
        
        len_words = len(words)
        l_word = len(words[0])
        l_total = l_word * len_words
        result = []
        for i in range(len(words[0])):
            words_dict = {}

            idx = i
            
            if idx + l_total > len(s):
                break
            
            for j in range(len_words):
                if s[idx: idx + l_word] in check_dict:
                    if s[idx: idx + l_word] in words_dict:
                        words_dict[s[idx: idx + l_word]] += 1
                    else:
                        words_dict[s[idx: idx + l_word]] = 1
                idx += l_word
            print(words_dict)
            if words_dict == check_dict:
                result.append(idx - l_total)
            # print(words_dict, idx - l_total, idx - l_total + l_word, s[idx - l_total: idx - l_total + l_word])
            while idx + l_word <= len(s):
                # print(idx, s[idx - l_total: idx - l_total + l_word])
                if s[idx - l_total: idx - l_total + l_word] in check_dict:
                    words_dict[s[idx - l_total: idx - l_total + l_word]] -= 1
                if s[idx: idx + l_word] in check_dict:
                    if s[idx: idx + l_word] not in words_dict:
                        words_dict[s[idx: idx + l_word]] = 1
                    else:
                        words_dict[s[idx: idx + l_word]] += 1

                idx += l_word
                if words_dict == check_dict:
                    result.append(idx - l_total)
                
                print(i, words_dict)
        return result

