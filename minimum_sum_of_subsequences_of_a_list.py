def combinations(a_list,n,k):
    result=[]
    if k>1:
        for i in range(n):
            for j in range(i+1,n):
                if(len(a_list[j:j+k-1]))<k-1:
                    break
                temp=[a_list[i]]
                temp.extend(a_list[j:j+k-1])
                result.append(temp)
        return result
    else:
        return a_list



#----------------------------------------

t = int(input())
if 1<=t<=10:
    for i in range(t):
        good = True
        n,k = map(int,input().split())
        if k<1 or k>50 or n<1 or n>50:
            good = False
            break
        a_list = list(map(int,input().split()))
        for i in a_list:
            if i<1 or i>100:
                good = False
                break
        main_list = list(combinations(a_list,n,k))
        sums = [sum(i) for i in main_list]
        if good:
            print(min(sums))
