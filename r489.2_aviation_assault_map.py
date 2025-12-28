
#矩陣轉置90度
def turn(list1):              #zip取出00 01矩陣各自的第一位                     #*解包成[[...],[...],...]的形式
    rotate=[list(row) for row in zip(*list1[::-1])]
            #放進list裡
    return rotate


def similarity(R,C,roate1,roate2):
    if len(roate2) !=R or len(roate2[0]) !=C:
        return int(0)
    count=0
    for i in range(int(R)):
        for j in range(int(C)):
            if roate1[i][j]==roate2[i][j]:
                count+=1
    anser=count*100//(int(R)*int(C))#無條件捨去先*100
    return int(anser)
    

if __name__ == "__main__":
    R,C=input().split()
    R=int(R)
    C=int(C)
    a=4
    list1=[]
    list2=[]
    anser=[]

#第一圖片
    for i in range(int(R)):
        row=list(map(int,input().split()))
        list1.append(row)

#第二圖片
    for i in range(int(R)):
        row=list(map(int,input().split()))
        list2.append(row)

    while a>0:
        anser.append(similarity(R,C,list1,list2))
        list2=turn(list2)
        a-=1

    print(f"{max(anser)}%")