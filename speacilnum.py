# while(num >0)
# 1.find the digits
# 2.squre of degit and add
# result 
def solution(num):
    rem = 0
    count = 0
    s = 0
    while(num > 0):
        rem = num%10
        s = s + (rem*rem)
        num = num//10
        count = count +1
    return sum

num = 28
result = num
while(result!= 1 and result !=4 ):
    result = solution(result)

if(result == 1):
    print(count)
else:
    print("-1")
