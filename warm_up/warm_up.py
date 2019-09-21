def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True

    else:
        return False

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a+b

def diff21(n):
  if n > 21:
    return 2*abs(n-21)
  return abs(n-21)


def parrot_trouble(talking, hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False

def makes10(a, b):
    if a==10 or b == 10 or a+b==10:
      return True;
    else:
      return False;

def near_hundred(n):
    return abs(n-100) <=10 or abs(n-200) <=10

def pos_neg(a, b, negative):
    if (negative == True) and (a<0 and b<0):
            return True
    if (negative == True) and (a>0 or b>0):
            return False
    return (a<0 and b>0) or (a>0 and b<0)

def not_string(str):
    if len(str) >=3 and str[:3] == "not":
        return str
    else:
        return "not "+str

def missing_char(str, n):
    return str.replace(str[n],'')

def front_back(str):
    if len(str) <=1:
        return str
    return str[len(str)-1:] + str[1: len(str)-1]+ str[0:1]

def front3(str):
    if len(str) >=3:
        return str[:3] +str[:3] +str[:3]
    else:
        return str[:len(str)]+str[:len(str)]+str[:len(str)]