# https://codingbat.com/prob/p181624

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False


print(first_last6([1, 2, 3, 4]))
print(first_last6([1, 2, 6]))
print(first_last6([13, 6, 1, 2, 3]))
print(first_last6([6,1,2,3]))
