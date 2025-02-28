from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsDict = {}
        results = []
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
                
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        
        for i in range(word_len):
            left = i
            right = i
            temp_dict = {}
            while right + word_len <= n:
                cur_word = s[right:right+word_len]
                right += word_len
                if cur_word in wordsDict:
                    if cur_word not in temp_dict:
                        temp_dict[cur_word] = 1
                    else:
                        temp_dict[cur_word] += 1

                    while temp_dict[cur_word] > wordsDict[cur_word]:
                        left_word = s[left:left+word_len]
                        temp_dict[left_word] -= 1
                        left += word_len
                        
                    if right - left == total_len:
                        results.append(left)
                else:
                    temp_dict.clear()
                    left = right
        
        return results
        
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
sol = Solution()
result = sol.findSubstring(s, words)
print(result)
