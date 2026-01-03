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
                                         #Counter(place)將列表轉換為一個計數字典:Counter({'471': 2, '030': 1, '300': 1})
most=Counter(place).most_common(1)[0][0] #.most_common(1)統計結果中，找出出現次數前 1 名的資料
ans=place.count(most)                    #[0] (第一個索引)列表中取出第一個元素('471', 2) [0] (第二個索引)從元組 ('471', 2) 中取出索引為 0 的值。
print(f"%s %d"%(most,ans))


