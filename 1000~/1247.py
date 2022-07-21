for _ in range(3) :
  t = int(input())
  data = []
  for _ in range(t) :
    data.append(int(input()))
  
  if sum(data) == 0 :
    print(0)
  elif sum(data) > 0 :
    print("+")
  else :
    print("-")