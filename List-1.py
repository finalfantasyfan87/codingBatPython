
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False
  
  def same_first_last(nums):
  if len(nums) >=1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

  def make_pi():
  return [3,1,4]

def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  else:
    return False

def sum3(nums):
  return nums[0]+nums[1]+nums[2]

def rotate_left3(nums):
  newNums = [nums[1],nums[2], nums[0]]
  return newNums

def reverse3(nums):
  return nums[::-1]

