def fibonacci(a,b,c,n):
    if(c!=n-1):
        print(a+b,",",end='')
        fibonacci(b,a+b,c+1,n)
    else:
        print(a+b)
        return
        

n=int(input("Enter the number of terms in the series: "))
print("0, 1, ",end='')
fibonacci(0,1,2,n)
