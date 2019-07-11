# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        AC:
        二分法解题
        1.设置头尾两个指针
        2.mid = （l+r）// 2；判断mid的情况，从而决定l或r指针哪一个移动
        """
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            cur_res = isBadVersion(mid)
            if cur_res:
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1  # 注意要减1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    l = mid + 1  # 注意要加1