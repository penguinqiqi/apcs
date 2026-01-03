from collections import Counter
a=int(input())
place=[]

for i in range(a):
    Seven,Sodd=0,0
    product_char=input()
    product=[int(x) for x in product_char]
    for j in range(len(product)-1):
        if j%2==0:
            Sodd+=product[j]
        else:
            Seven+=product[j]
        
    if (Sodd+3*Seven)%10+product[12]==0 or (Sodd+3*Seven)%10+product[12]==10:
        place.append(product_char[0:3])

most=Counter(place).most_common(1)[0][0]
ans=place.count(most)
print(f"%s %d"%(most,ans))


