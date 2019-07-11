class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        AC: 循环遍历法
        1.考虑一个极端条件---当target>=letters的最后一个字符时，返回第一个字符
        2.一直遍历，直到当前letters大于target，则返回
        '''
        #         if target >= letters[-1]:
        #             return letters[0]

        #         for num, s in enumerate(letters):
        #             if letters[num] <= target:
        #                 continue
        #             else:
        #                 return letters[num]



        '''
        二分法

        1.先考虑两种极端情况：1.1：当target比首字符小时；1.2：当末尾字符比target小
        2.指定首位两指针
        3.分三种情况：
          分别是大于；小于；等于时如何处理
          尤其注意等于时不一定返回下一个字符，有可能字符串中有重复字符
          letters[mid] > target时也要注意返回的时letters[mid]，而非letters[mid-1]
        '''
        s_len = len(letters)
        l, r = 0, s_len - 1

        if target < letters[0]:
            return letters[0]
        if target >= letters[-1]:  # 注意此处有等于号
            return letters[0]

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if letters[mid] > target:
                if letters[mid - 1] < target:
                    return letters[mid]  # 注意此处当mid-1小于target时，返回mid，而非mid-1；因为求的是比目标大的字符
                r = mid - 1
            elif letters[mid] < target:
                if letters[mid + 1] > target:
                    return letters[mid + 1]
                l = mid + 1
            elif letters[mid] == target:
                if letters[mid + 1] and letters[mid + 1] > target:
                    return letters[mid + 1]
                elif letters[mid + 1] and letters[
                            mid + 1] == target:  # 肯能会有重复字符；如：["e","e","e","e","e","e","n","n","n","n"]
                    l = mid + 1
                else:
                    return letters[0]




















