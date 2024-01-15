class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_dict = {}
        word_dict = {}

        for word in strs:
            word_sorted = sorted(word)
            word_sorted = ''.join(word_sorted)

            if word_sorted not in group_dict:
                group_dict[word_sorted] = []
            group_dict[word_sorted].append(word)

        keys = list(group_dict.keys())
        result = []

        for key in keys:
            result.append(group_dict[key])

        return result