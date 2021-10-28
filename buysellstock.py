n=int(input())
ele=[]
for i in range(n):
    num=int(input())
    ele.append(num)
maxi=profit=0
for j in range(len(ele)-1,0,-1):
    if(maxi<ele[j]):
        maxi=ele[j]
    if maxi-ele[j]>profit:
        profit=maxi-ele[j]
print(profit)