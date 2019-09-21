def string_times(str, n):
    bigger =''
    for num in range(n):
        bigger +=str
    return bigger

def front_times(str, n):
    newbie = ''
    for i in range(n):
        if len(str)>3:
            newbie += str[:3]
        else:
            newbie += str[:n]
    return newbie

def string_bits(str):
    return str[::2]


def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i + 1]
    return result

def array_count9(nums):
    count = 0;
    for num in nums:
        if num == 9:
            count = count + 1
    return count

def array_front9(nums):
    contains_Nine = False
    limit =0
    if len(nums) >=4:
        limit = 4
        for i in range(1, limit):
            if nums[i] == 9:
                contains_Nine = True

    else:
          limit = len(nums)
          for i in range(len(nums)):
              if nums[i] == 9:
                  contains_Nine = True
                  #returning results to early
    if contains_Nine == True:
        return True
    else:
        return False


def array123(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


