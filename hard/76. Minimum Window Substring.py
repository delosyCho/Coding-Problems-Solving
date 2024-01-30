class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pos_dict = {}
        count_dict = {}
        ref_count_dict = {}
        for j in range(len(t)):
            if t[j] not in count_dict:
                count_dict[t[j]] = 0
                pos_dict[t[j]] = -1
            
            if t[j] not in ref_count_dict:
                ref_count_dict[t[j]] = 1
            else:
                ref_count_dict[t[j]] += 1
        
        start = 0
        start_char = ''
        matched_num = 1        

        while start < len(s):
            if s[start] in count_dict:
                count_dict[s[start]] += 1
                if len(t) == 1:
                    return t

                break
            else:
                start += 1

        if start >= len(s):
            return ""

        selected_start = -1
        selected_end = len(s)
        cur_c = ''

        p = start + 1 # point
        while p < len(s):
            print(start, p)
            
            if s[p] in count_dict:
                    cur_c = s[p]
                    count_dict[s[p]] += 1
                    if count_dict[s[p]] <= ref_count_dict[s[p]]:
                        matched_num += 1

            if matched_num == len(t):
                while start < p:
                    if s[start] not in count_dict:
                        start += 1
                    else:
                        if count_dict[s[start]] - 1 >= ref_count_dict[s[start]]:
                            count_dict[s[start]] -= 1
                            start += 1

                        else:
                            break

                if p - start < selected_end - selected_start:
                    selected_start = start
                    selected_end = p

                while start < p:
                    if s[start] in count_dict:
                        count_dict[s[start]] -= 1
                        if count_dict[s[start]] < ref_count_dict[s[start]]:
                            matched_num -= 1
                            start += 1
                            break
                        start += 1

            p += 1

        if selected_start == -1:
            return ""
        
        return s[selected_start: selected_end + 1]
                
