def count_evens(nums):
  count =0
  for i in nums:
    if i % 2 == 0:
      count =count+1
    
  return count  
  

  def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2:
      if nums[i+1] == 2:
        return True
        
  return False      
