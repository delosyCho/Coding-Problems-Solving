class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        results = []

        lines_w = []
        lines_l = []

        w_ids = []
        l_ids = []
        

        c_len = 0
        for w, word in enumerate(words):
            if c_len + len(word) <= maxWidth:
                w_ids.append(w)
                l_ids.append(len(word))
                c_len += len(word) + 1 
            else:
                lines_w.append(w_ids[:])
                lines_l.append(l_ids[:])

                w_ids = [w]
                l_ids = [len(word)]
                c_len = len(word) + 1
        lines_w.append(w_ids[:])
        lines_l.append(l_ids[:])

        for l in lines_w:
            print(l)

        for l in range(len(lines_w)):
            line_w = lines_w[l]
            line_l = lines_l[l]

            if l == len(lines_w) - 1:
                line = ''

                for w in line_w:
                    line += words[w] + ' '
                line = line.strip()
                line += ' ' * (maxWidth - len(line))
                results.append(line)
                continue

            pad_l = len(line_l) - 1
            if pad_l <= 0:
                pads_num = maxWidth - sum(line_l)
                line = words[line_w[0]] + ' ' * pads_num    
                results.append(line)
                continue
            pads_num = maxWidth - sum(line_l)
            each_pad = pads_num // pad_l
            pads = [each_pad] * pad_l
            print(l, pads)
            pad_rest = pads_num % pad_l
            for p in range(pad_rest):
                pads[p] += 1
            for p in range(pad_l):
                pads[p] = ' ' * pads[p]
            

            line = ''

            p = 0
            for w in line_w:
                line += words[w]
                if p < len(pads):
                    line += pads[p]
                p += 1
            
            results.append(line)

        return results