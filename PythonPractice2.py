def make_pi():
  a = [3,1,4]
  return a

def common_end(a, b):
  if len(a) < 1 or len(b) < 1:
    return False
  
  if (a[0] == b[0]) or (a[-1] == b[-1]):
    return True
    
return False  

def sum3(nums):
  sum =0
  for i in nums:
    sum = sum + i
  
  return sum

 def rotate_left3(nums):
  if len(nums) != 3:
    return nums
  
  o1 = nums[0]
  o2 = nums[1]
  
  nums[0] = o2
  nums[1] =nums[2]
  nums[2] = o1
  
  return nums

  def max_end3(nums):
   
  if nums[0] > nums[-1]:
    max  = nums[0]
  else:
    max  = nums[-1]
    
  x =0 
  while x < len(nums):
    nums[x] = max
    x =x+1
    
  return nums 

  def middle_way(a, b):
    a = [a[1],b[1]]
    return a

 def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
    
  if nums[1] == 2 or nums[1] == 3:
    return True   

  return False   
 