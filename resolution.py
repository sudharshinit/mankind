nums = [-1,2,1,-4]
target = 1
l = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
     for k in range(j+1,len(nums)):
        if nums[i]+nums[j]+nums[k]==target :
            l.append([i,j,k])
        elif nums[i]+nums[j]+nums[k]==target+1:
         l.append([i,j,k])          
        elif nums[i]+nums[j]+nums[k]==target-1:
            l.append([i,j,k])
        else:
            False 


phone = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ"
}


digit = input('enter a number from 2-9 : ')
l = []
for x in digit :
      l.append(x)
k = []
j = []
for y in l :
   for z in phone[y] :
    k.append(z)  