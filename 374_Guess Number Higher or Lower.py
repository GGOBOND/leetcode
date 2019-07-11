# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        AC:
        与278. 第一个错误的版本这道题作对比！！！（同样是二分法）
        1.创建头尾两指针l，r
        2.mid，判断mid对应情况，从而决定l和r指针向哪个方向移动
        NOTE: 3. while l <= r: (此处应该考虑等号)-->考虑当n==1时的情况，即l==r==1
        """

        l, r = 1, n
        while l <= r:  # 考虑等号
            mid = (l + r) // 2
            cur_res = guess(mid)
            print(mid, cur_res)
            if cur_res == -1:
                if guess(mid - 1) == 0:
                    return mid - 1
                r = mid - 1
            elif cur_res == 1:
                if guess(mid + 1) == 0:
                    return mid + 1
                l = mid + 1
            elif cur_res == 0:
                return mid
