# Verilmiş [a,b] intervaldakı Armstrong ədədlərin tapılması
def Number_Armstrong(num):
    sum=0
    temp=num
    n=len(str(num))

    while(temp>0):
        sonuncu_eded=temp % 10 # Sonuncu ədədin tapılması ->Məsələn:407->7, 1563->3
        sum +=sonuncu_eded**n
        temp //=10 # Sonuncu ədədi silir qalan ifadəni ədəd kimi götürür ->Məsələn:407->40, 1563->156

    if(num==sum):
        return True
    else:
        return False

print('[a,b] intervalını daxil edin!')
a=int(input('Birinci interval: '))
b=int(input('İkinci interval: '))

print(f'[{a},{b}] intervalındakı Armstrong ədədlər: ')
for num in range(a,b+1):
    if(Number_Armstrong(num)):
        print(num)