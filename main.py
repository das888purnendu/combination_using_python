#a_list = list(map(int,input().split()))   #Space separated numbers -> 1 2 3 4 5

a_list = [1,2,3,4,5] # Given list
n = len(a_list)  # items of the list
k = 3        # lenght of subsequence
print("Main List :",a_list)
print("All Possible Combinations are :")
if k>1:
    for i in range(n):
        for j in range(i+1,n):
            if(len(a_list[j:j+k-1]))<k-1:
                break
            temp=[a_list[i]]
            temp.extend(a_list[j:j+k-1])
            print(*temp,sep=",")
else:
    print(*a_list,sep="\n")
