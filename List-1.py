
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

def max_end3(nums):
  if nums[0] > nums[2]:
      first = [nums[0], nums[0], nums[0]]
      return first
  else:
      last = [nums[2], nums[2], nums[2]]
      return last

def sum2(nums):
  if len(nums) >=2:
    return nums[0] +nums[1]
  if len(nums) <1:
    return 0
  else:
    return nums[0]

 def middle_way(a, b):
  middle = [a[1],b[1]]
  return middle

def make_ends(nums):
  if len(nums) >= 1:
      makeEnds = [nums[0],nums[len(nums)-1]]
      return makeEnds
    
def has23(nums):
  if nums >=2:
    if nums[0] ==2 or nums[1] ==2:
      return True
    if nums[0] == 3 or nums[1]==3:
      return True
  return False




