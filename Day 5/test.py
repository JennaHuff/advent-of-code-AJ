def is_palindrome(x):
    x = list(str(x))
    for i in range(len(x)):
        if not x[i] == x[-(i+1)]:
            return(False)
    return('hi')


print(is_palindrome(121))

# nums = list(str(1234567654321))

# for i in range(len(nums)):
#     if not nums[i] == nums[-(i+1)]:
#         print('
# # print([x for x in nums if x == nums[-x]])

