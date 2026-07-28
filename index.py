head = [1,2,3,4]
for i in head :
  if head.index(i)%2==0:
    head[i], head[i - 1] = head[i - 1], head[i]
print(head)


head = [1,2,3,4]
a = len(head)
print(a)
u1 = int(input("enter a num from 1-6 : "))
for x in head :
  if head.index(i)%2==0:
      head[i], head[i - 1] = head[i - 1], head[i]
  if u1==3:
    if head.index(x)%u1 == 0 :
     head[x],head[x-1],head[x-2] = head[x-2] ,head[x-1], head[x]
  if u1==4:
      if head.index(x)%u1 == 0 :
       head[x],head[x-1],head[x-2],head[x-3] =head[x-3],head[x-2] ,head[x-1], head[x]
print(head)
