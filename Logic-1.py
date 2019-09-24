def cigar_party(cigars, is_weekend):
  if cigars >=40 and cigars <=60 and is_weekend == False:
      return True
  elif cigars >=40 and is_weekend == True:
      return True
  else:
      return False
    
def date_fashion(you, date):
  if you <=2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
if is_summer == True and temp>=60 and temp <=100:
  return True
if is_summer == False and temp>=60 and temp <=90:
  return True
else:
  return False

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed -=5
  if speed <=60:
    return 0
  if speed >61 and speed<=80:
    return 1
  else:
    return 2
  
def sorta_sum(a, b):
  sum = a+b
  if sum >=10 and sum <=19:
    return 20
  else:
    return sum
  
def alarm_clock(day, vacation):
  if vacation == True and (day == 0 or day == 6):
    return 'off'
  elif vacation == False and (day == 0 or day == 6):
    return '10:00'
  elif vacation == True and  not (day == 0 or day == 6):
    return '10:00'
  else:
    return '7:00'
    
def love6(a, b):
  sum = a + b
  diff = abs(a-b)
  if a == 6 or b == 6:
    return True
  if sum == 6 or diff == 6:
    return True
  return False

def in1to10(n, outside_mode):
    if not outside_mode:
      return n>=1 and n<11
    return n<=1 or n >=10
    
def near_ten(num):
 return (num+2) % 10 <=4
