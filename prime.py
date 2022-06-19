# This is Prime Code  
def prime_composite(num_list):
  prime =[]
  composite =[]
  output = []
  for i in num_list:
    
    flag=0
    for j in range(2,i):
      
      if(i%j==0):
        flag =1
        composite.append(i)
        break
        
    if(flag==0):
        prime.append(i)


  if flag==0:
      print(0)
  else:
      print(1)
  output.append([prime] + [composite])
  return output





if __name__=="__main__":
  
  num_list = []
  count = int(input())
  
  for i in range(count):
    num_list.append(int(input()))
    
  result = prime_composite(num_list)
  
  if result!=0:
    for i in result:
      print(i)
