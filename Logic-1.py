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
  
