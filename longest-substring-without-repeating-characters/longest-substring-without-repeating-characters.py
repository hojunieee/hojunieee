class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s_list = list(s)
        max_len = 0
        for i in range(len(s_list)):
            curr_list = [s_list[i]]
            for j in range(i+1, len(s_list)):
                if s_list[j] in curr_list:
                    break
                else:
                    curr_list.append(s_list[j])
            max_len = max(max_len, len(curr_list))

        return max_len
