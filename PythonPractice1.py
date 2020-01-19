def hello_name(name):
    return "Hello {}!".format(name)

def make_abba(a, b):
    return "{}{}{}{}".format(a,b,b,a)

def make_tags(tag, word):
    return "<{}>{}</{}>".format(tag,word,tag)

 def make_out_word(out, word):
  s= ""
  for a in out[0:len(out)/2]:
    s = s + a
  s= s + word
  for a in out[len(out)/2:len(out)]:
    s = s + a
  return s

def extra_end(str):
  if len(str) < 2:
    return None
  
  end  = str[len(str)-2:len(str)]
  
  final = ""
  
  x=0
  while x < 3:
    final = final + end
    x=x+1
    
  return final  

def first_two(str):
  return str[0:2]

def first_half(str):
  return str[0:len(str)/2]

def without_end(str):
  return str[1:len(str)-1]

def combo_string(a, b):
  if len(a) > len(b):
    return "{}{}{}".format(b,a,b)
    
  return "{}{}{}".format(a,b,a)   
  def non_start(a, b):
 
  return "{}{}".format(a[1:len(a)],b[1:len(b)])

def left2(str):
    if len(str) <3:
      return str
    
  return "{}{}".format(str[2:len(str)],str[0:2])  

def double_char(str):
    s = ""
    for i in str:
      s = s + i +i
  
    return s 

def count_hi(str):
      x=0
  count =0
  while x < len(str):
    if str[x:x+2] == "hi":
      count = count + 1
    x=x+1  
      
    return count  

 def cat_dog(str):
  x =0
  cat = 0
  dog =0
  while x<len(str):
    if str[x:x+3] == "cat":
      cat = cat +1
    if str[x:x+3] == "dog":
      dog = dog +1
    x=x+1
    
  if cat == dog:
    return True
  else:
    return False        

def count_code(str):
  x =0
  count =0
  while x < len(str):
    if str[x:x+2] == "co" and str[x+3:x+4] == "e":
      count = count +1
    x=x+1  
  return count    

def end_other(a, b):
  temp=""
  if len(a) < len(b):
      temp = b
      b = a
      a = temp
  a = a.lower()
  b=b.lower()
  if a[len(a)-len(b):len(a)] == b:
    return True
    
  return False  
def xyz_there(str):
  x=0
  while x < len(str):
    if str[x:x+3] == "xyz":
      if x != 0:
        if  str[x-1:x+3] != ".xyz":
          return True
      elif x == 0:
        return True
    x = x+1    
  return False 