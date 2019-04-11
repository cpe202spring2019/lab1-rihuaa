
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) > 0:
      maxNumber = int_list[0]
      for i in range (len(int_list)):
         if int_list[i] > maxNumber:
            maxNumber = int_list[i]
      return maxNumber
   else:
      return 'None'

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   else:
      if len(int_list) == 0:
         return []
      else:
         return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   elif int_list == []:
      return None
   else:
      mid = (low + high)//2
      if int_list[mid] == target:
         return mid
      else:
         if int_list[mid] < target and mid < high:
            return bin_search(target, mid+1, high, int_list)
         elif int_list[mid]> target and mid > low:
            return bin_search(target, low, mid-1, int_list)
         else:
            return None
