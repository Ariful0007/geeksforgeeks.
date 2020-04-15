def check(k):
    sum1=0
    while k > 0:
        rem= k % 10
        sum1= sum1*10 +rem
        k =k //10
    return  sum1




for _ in range(int(input())):
    n = int(input())
    temp = n
    sum=0
    while n !=0:
        rem = n % 10
        sum += rem
        n=n//10
    if  sum==check(sum):
        print("YES")
    else :
        print("NO")

    #print(sum)


    if __name__ == '__main__':
        pass


