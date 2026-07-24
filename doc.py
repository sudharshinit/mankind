l1 = [2,4,3]
l2 = [5,6,4]
l3 = []
l4 = []
for i in l1 :
    l3.insert(0,i)
    a=''.join(str(x) for x in l3)
for j in l2 :
    l4.insert(0,j)
    b=''.join(str(x) for x in l4)
def add(a,b):
    return a+b
print(add(int(a),int(b)))

nums =[3,3]
target = 6
for i in nums :
    for j in nums:
        if j==i:
            continue
        elif i+j==target:
             a = [nums.index(i),nums.index(j)]
             a.sort()
print(a)

nums = [1,1]
max1 = 1
max2=1
for num1 in nums:
  if num1 > max1  :
      max1 = num1
for num2 in reversed(nums):
  if num2 > max2 and nums.index(num2)>nums.index(max2) :
      max2 = num2
tiny = min(max1,max2)
def area(a,b):
    return a*b
print(area(tiny,max2))