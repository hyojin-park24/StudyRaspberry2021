#Python 함수2

m = 0
n = 1

def func():
    global m 
    global n
    m = m + 1
    n += 1

func()
print(m,n)

def counter(max):
    t = 0

    def output():   #중첩함수 , 따로 쓸 수 없음
        print('t = {0}'.format(t))
    
    while t < max:
        output()
        t += 1

counter(10)

#output

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print (factorial(9))

# lambda함수 
a = lambda x, y : x * y
print(a(2, 8))

#Closure함수
#함수 자체를 리턴해주는 형태 - C#델리게이트와 비슷한 의미
def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))
