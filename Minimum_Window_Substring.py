class Solution:   
    def contains(self, s_set: dict, t_set: dict):
        if (len(s_set) == len(t_set)):
            for key in t_set.keys():
                if key not in s_set:
                    return False
                elif not (len(s_set[key]) >= t_set[key]):
                    return False
            
            return True
        else:
            return False
        
    def strToMap(self, t:str) -> dict:
        t_set = {}
        for char in t:
            if char in t_set:
                t_set[char] += 1
            else:
                t_set[char] = 1

        return t_set
        
    def minWindow(self, s: str, t: str) -> str:
        t_set = self.strToMap(t)

        min_window_size = len(s)
        min_left = 0
        min_right = -1

        for i in range(0, len(s)):
            s_set = {}
            for j in range(i, len(s)):
                if s[j] in t_set:
                    if s[j] in s_set:
                        s_set[s[j]].add(j)
                    else:
                        s_set[s[j]] = set([j])

                if self.contains(s_set, t_set):
                    if (j - i + 1 <= min_window_size):
                        min_left = i
                        min_right = j
                        min_window_size = j - i + 1

                    break
        
        print(f'Found new min substring: {s[min_left:min_right + 1]}, Left: {min_left}, Right: {min_right}')
        return s[min_left:min_right+1]

            


    def minWindowLinear(self, s: str, t: str) -> str:
        t_set = self.strToMap(t)

        print(t_set)

        cur_set = {}

        left = 0
        right = -1

        min_window_size = len(s)

        minLeft = 0
        minRight = -1

        while (left < len(s)):
            # Find left bound
            for i in range (left, len(s) - 1):
                if s[i] in t_set:
                    left = i
                    break

            print('Find left bound: ', left)
            
            # Find right bound
            for i in range (left, len(s)):
                print(f'left: {left}, right: {right}, i: {i}')

                if s[i] in t_set:
                    if s[i] in cur_set:
                        cur_set[s[i]].add(i)
                    else:
                        cur_set[s[i]] = set([i])

                    print('s map: ', cur_set)

                    if self.contains(cur_set, t_set):
                        right = i
                        if (i - left + 1 <= min_window_size):
                            minLeft = left
                            minRight = i
                            min_window_size = i - left + 1
                            print(f'Found new min substring after expanding right: {s[minLeft:minRight + 1]}, Left: {minLeft}, Right: {minRight}')
                        else:
                            print(f'Found new substring after expanding right: {s[left:right+1]}, Left: {left}, Right: {right}')

                        break
            
            # Shrink left bound
            print('Shrink left bound')
            if (right > left and self.contains(cur_set, t_set)):   
                foundSmaller = False         
                for i in range (left, right):
                    print(f'left: {left}, right: {right}, i: {i}')
                    if s[i] in t_set:
                        if len(cur_set[s[i]]) > 1:
                            cur_set[s[i]].remove(i)
                            foundSmaller = True
                            left = i + 1
                        else:
                            del cur_set[s[i]]
                            break
                    else:
                        foundSmaller = True
                        left = i + 1

                if foundSmaller:
                    minLeft = left
                    minRight = right
                    min_window_size = right - i
                    print(f'Found new min substring after shrinking left: {s[minLeft:minRight + 1]}, Left: {minLeft}, Right: {minRight}')

                left += 1
            else:
                break
        
        
        print(f'Found new min substring: {s[minLeft:minRight + 1]}, Left: {minLeft}, Right: {minRight}')
        return s[minLeft:minRight + 1]
    

sol = Solution()
sol.minWindow('ADOBECODEBANC', 'ABC')