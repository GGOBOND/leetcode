class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        AC：
        1.先将列表排序
        2.定义三个指针，一个从头遍历，第二个紧跟着第一个之后，第三个从后往前
        3.如果i==0或者当前数比其前一个大，那么赋值第二个指针在第一个指针的后一位（防止三元指针重复）
        4.如果三数之和为0-->判断其最大最小是否在字典d中，（防止cur_res重复）
        '''

        res = []
        len_nums = len(nums)
        d = {}
        nums.sort()
        for i in range(len_nums):
            if i == 0 or nums[i] > nums[i - 1]:  # 此处i，left，right相当于三个指针
                left = i + 1
                right = len_nums - 1
                while right > left:
                    s = nums[i] + nums[left] + nums[right]
                    if s == 0:
                        cur_res = [nums[i], nums[left], nums[right]]
                        max_cur_res = max(cur_res)  # 判断cur_res中最大最小值是否在字典中，---> 排除重复
                        min_cur_res = min(cur_res)
                        if (min_cur_res, max_cur_res) not in d:
                            d[(min_cur_res, max_cur_res)] = 1
                            res.append(cur_res)

                        left += 1
                        right -= 1

                    elif s < 0:  # 如果三数之和小于0.证明中间指针left还可以向右移，因为nums之前已排序
                        left += 1
                    else:  # 如果三数之和大于0.证明中间指针right还可以向左移
                        right -= 1

        return res


'''
此方法还是超出时间限制，看来不能使用三重循环！！！

TIP: 如果res中有相同的元素，为了避免重复，可以使用字典，因为字典的键具有唯一性，另外集合也具有唯一性
'''
# num_l = len(nums)
#         if num_l==0:
#             return []
#         res = []
#         d = {}
#         for i in range(num_l-2):
#             for j in range(i+1, num_l-1):
#                 for k in range(i+2, num_l):
#                     if i==j or j==k or i==k:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         a = [nums[i], nums[j], nums[k]]
#                         max_a,min_a = max(a),min(a)
#                         if (max_a, min_a) not in d:

#                             d[(max_a,min_a)] = 1   # 字典的键具有唯一性
#                             res.append(a)
#         del d


#         return res


''' 超时 '''
#         num_l = len(nums)
#         if num_l==0:
#             return []
#         res = []
#         for i in range(num_l-2):
#             for j in range(i+1, num_l-1):
#                 for k in range(i+2, num_l):
#                     # if i==j==k:
#                     #     continue
#                     if i !=j !=k and nums[i] + nums[j] + nums[k] == 0:
#                         a = sorted([nums[i], nums[j], nums[k]])
#                         res.append(a)

#         if res != None:
#             result = []
#             for lst_nums in res:
#                 if lst_nums not in result:
#                     result.append(lst_nums)


#         return result