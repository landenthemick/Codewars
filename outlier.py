def find_outlier(integers):
  odd = 0
  odd_list = []
  even = 0
  even_list = []
  if len(integers) == 0:
    return None
  else:
    for item in integers:
      if item%2==0:
        even +=1
        even_list.append(item)
      else:
        odd +=1
        odd_list.append(item)
  if even > odd:
    return odd_list[0]
  else:
    return even_list[0]



print(find_outlier([2,4,6,8,10,3]))