from function3 import person
from function2 import calc
import function3
from function2 import add_end
import function2
from function import enroll
import function
import sys
from function import quadratic
import math
string = 'Hydrogen!'
print(string)
for index, char in enumerate(string):
    print((index, char))

c = 10**10
print('10 ^ 10 =', c)

name = input('please enter your name')
print('hello', name)

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok')
print('I\'m learning\np')
print(r'\\\\n\\\\')

print('''I
... like
... chi''')

print('''hello,\n
world''')


not (5 > 3 and 6 > 8)

a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

a = "ABC"
b = a
a = "XYZ"
print(b)

10 / 3
9 / 3

print(r'Hello,"Bart"')

print(r'''Hello
Lisa''')

print('包含中文的str')
ord('中')
chr(25991)

'\u4e2d\u6587'

':'.encode('utf-8')
'中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8', errors='ignore')


len('中文'.encode('utf-8'))

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415927)


print('growth rate: %d %%' % 7)

'Hello,{0},成绩提升了{1:.1f}%'.format('小明', 17.125)
'Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125)

'Hello,{0},{1},{2},{3}'.format('12', '22', 23, 123)

# 小明的成绩
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明的成绩提升了%.2d %%' % r)


classmate = ['Micheal', 'Bob', 'Tracy']
classmate
len(classmate)

classmate[len(classmate) - 1]

classmate[-3]

classmate.append('Adam')

classmate.insert(1, 'Jack')

classmate.pop(-4)
classmate


s = ['pthon', 'Java', ['asp', 'php'], 'scheme']


classmate = ('Micheal', 'Bob', 'Tracy')
classmate[1]

t = (1,)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


############
age = 1
if age >= 18:
    print('Your age is %d years old' % age)
elif age >= 6:
    print('Tenneager')
else:
    print('Kid')


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

zpp = 0
if zpp:
    print('True')
else:
    print('False')


birth = input('birth:')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')


# BMI Compute and adjugement
hight = input('Please enter your height:(M)')
weight = input('Please enter your weight:(KG)')
hight = float(hight)
weight = float(weight)

BMI = weight / (hight**2)
if BMI <= 18.5:
    print('过轻')
elif BMI <= 25:
    print('正常')
elif BMI <= 28:
    print('过重')
elif BMI <= 32:
    print('肥胖')
else:
    print('严重肥胖')


# circle
names = ['Micheal', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
xx = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in xx:
    sum = sum + x
print(sum)


c = range(5)

cc = list(range(5))

for x in cc:
    cc[x] = cc[x] + 1
print(cc)


hundreds = (list(range(101)))
hundreds.pop(0)

print(hundreds)

sumhu = 0
for x in hundreds:
    sumhu = sumhu + x
print(sumhu)


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,{0}'.format(x))


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 1
    if sum % 2 == 0:
        continue
    print(sum)


sum = 0
for x in range(101):
    if x % 2 != 0:
        continue
        pass
    sum = sum + x
print(sum)


sum = 0
for x in range(101):
    if sum >= 3000:
        break
        pass
    sum = sum + x
print(sum)


###############
names = ['Micheal', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
d['Micheal'] = 10


'Thomas' in d

d.get('Thomas', -1)
de
d.get("Micheal")
d.pop('Bob')


s1 = set([1, 2, 3, 2])
s1.add(6)
s1.remove(1)
s2 = set([2, 3, 5])

s1 & s2
s1 | s2

a = 'abc'
a.replace('a', 'A')
a
a = a.replace('a', 'A')
a

b = 2313
c = {'Micheal': (1, 2, 3), 'Bob': (1, [2, 3])}
c.get('Micheal')
c.get('Bob')
c['Bob'][1][0]


#####################

bool()

n1 = 255
hex(n1)
n2 = 1000
hex(n2)


n = 123
m = 234
di = {"n": n, "m": m}
for i in di.keys():
    print(i, hex(di[i]))


################

    def my_abs(x):
        if x >= 0:
            return x
        else:
            return -x
        pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Plese enter int or float')
    if x >= 0:
        return x
    else:
        return -x


my_abs(10)


def move(x, y, step=10, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    pass


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


x = quadratic(1, 23, 1)

print(quadratic(2, 3, 1))

sys.path.append('C:/Users/pdxgs/desktop/python')
print(quadratic(2, 3, 1))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


enroll('lili', 'M', city='tianjin')

del function
add_end([123123, 'dwf', 'dqwf'])

add_end()

sys.path.append('C:/Users/pdxgs/desktop/python')

nums = [1, 2, 3]
calc(*nums)
calc()

person('Bob', 12, city='beijing', job='sada')


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 231, city='sda', job='woe')


def person(name, age, *c, city, job):
    print(name, age, c, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2, 2, city='ccc')


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(123, 123, 23, d=13, hah='asd', ad='asd')



#######递归
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
    pass

fact(10000)


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(4)


def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
        return
    elif n == 2:
        print(b,'-->',c)
    return move(n-1,a,b,c)

# the question of hanoi tower
def hanoi(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')


n=1
ll=[]
while n<=99:
    ll.append(n)
    n=n+1
print(ll)


# 切片
name=['Micheal','Bob','Jack']
name[-4:]


L=list(range(199))
L[0:1000:5]


c=(0,1,2,3,4,5,6,7,8,9)
c[1:5:2]


def trim(s):
    while s.find(' ') == 0:
        s=s[1:]
        if len(s)==0:
            break
    while s.rfind(' ') == len(s)-1:
        s=s[:-2]
        if len(s)==0:
            break
        pass
    return s
    pass

trim('  hello  world  ')

trim('    ')

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


d={'a':1,'b':2,'c':3}
for value in d.items():
    print(value)

for ch in 'ABC':
    print(ch)

from    collections import Iterable
isinstance(123,Iterable)

for c,x in enumerate(['A','B','C']):
    print(x)
    print(c)

for x,y in [(1,1),(2,4),(3,9)]:
    print('x:',x,'y:',y)


def findMinAndMax(L):
    if len(L) !=0:
        Max=L[0]
        Min=L[0]
        for x in L:
            if x >= Max:
                Max=x
            if x <= Min:
                Min=x
        return (Min,Max)
    else:
        return (None,None)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


L=[]
for x in range(1,11):
        L.append(x*x)

L

[x*x for x in range(1,11)]


[x*x for x in range(1,20) if x*x%7==0]

[x+y for x in 'ABC' for y in 'XYZw']

import os
print(os.getcwd())
os.chdir('C:/Users/pdxgs/desktop/python')
[d for d in os.listdir('.')]


d={'X':'a','Y':'b','Z':'c'}
for n,m in d.items():
    print(n,'=','m')

[n+'='+m for n,m in d.items()]

L=['Hello','World','IBM','Apple']
[s.lower() for s in L]

L=['Hello','World','IBM','Apple']
isinstance(L[0],str)

L1=['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


## generator
L=[x*x for x in range(10)]
L
L1=(x*x for x in range(10))

for n in L1:
    print(n)


def fib(max):
    x1,x2=1,1
    if max == 1:
        return x1
    elif max == 2:
        return x2
    else:
        n,xna,xnb=3,x1,x2
        while n <= max:
            xna,xnb = xnb,xna+xnb
            n=n+1
        return xnb

fib(7)

def fib2(max):
    n,xb1,x1=1,0,1
    xna,xnb=xb1,x1
    while n<=max:
        yield xnb
        xna,xnb = xnb,xna+xnb
        n=n+1
    return 'done'

for x in fib2(6):
    print(x)


c=fib2(6)
next(c)

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3
    pass


c=odd()
next(c)
for n in odd():
    print(n)

c=fib2(6)
while True:
    try:
        x=next(c)
        print('c',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break



#  杨辉三角
def triangles():
    x=[1]
    yield x
    while True:
            y=[x1+x2 for n1,x1 in enumerate(x) for n2,x2 in enumerate(x) if n2-n1==1]
            # y=[x[x1]+x[x1+1] for x1 in range(len(x)-1)]
            y.insert(0,1)
            y.append(1)
            yield y
            x=y
    pass

c=triangles
c=c()
next(c)
cc=triangles()
next(cc)

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')



from collections import Iterator,Iterable
# iterator
isinstance('abc',Iterable)
isinstance('abc',Iterator)
c=iter('abc')
next(c)


# 函数指向
c=abs
c(1)

# 高阶函数
def add(a,b,f):
    return f(a)+f(b)
    pass

def square(x):
    return x**2
    pass
add(-1,10,square)


# map()函数
c=list(range(1,101))
cc=map(square,c)
list(cc)
c2=map(str,c)
list(c2)

def add(x,y):
    return  x+y
    pass

c=list(range(1,101))
from functools  import reduce
reduce(add,c)

def change(x,y):
    return  10*x+y
    pass
c=[1,3,5,7,9]
reduce(change, c)

def chr2num(str):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return  digits[str]
    pass


reduce(change,map(chr2num,'13568899'))




def str2int(str):
    return reduce(change,map(chr2num,str))
    pass

str2int('2132312')


import os
os.chdir('C:/Users/pdxgs/desktop/python')
from    str2num import str2int
str2int('2314')


# Normalize Name
def normalize(name):
    return name.capitalize()
    pass

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 求积函数
from    functools   import reduce
def prod(lis):
    return  reduce(lambda x,y:x*y,lis)
    pass


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')




def str2L(x):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'0'}
    return digits[x]
    pass
map(str2L,'1313.5')



import os
os.chdir('C:/Users/pdxgs/desktop/python')
from ChanStr import str2float

str2float('1231.231319')
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



def is_odd(n):
    return  n%2==0
    pass

list(filter(is_odd,list(range(1,10))))


def not_empty(str):
    # str.strip():remove the Space and /t at the first or last
    return  str and str.strip()
    pass

list(filter(not_empty,['A','B','C',None,'',' ']))



def _odd_iter():
    n = 1
    while True:
        n=n+2
        yield n
    pass

def _not_divisible(n):
    return  lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n=next(it)
        yield n
        it = filter(_not_divisible(n),it)
    pass


for n in primes():
    if n<4:
        print(n)
    else:
        break


def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

def is_palindrome(n):
    w=0
    L=[]
    # str(): int or float --> str
    while True:
        c=n // 10**w
        L.append(c%10)
        if c < 10:
            break
        w=w+1

    re=True
    for n1 in range(len(L)//2):
        if L[n1] != L[len(L)-n1-1]:
            re=False
            break
    return  re
    pass

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')



sorted([1.3,-23,145,1325],key=abs)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return  t[0]
    pass

L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return  -t[1]
    pass
L2 = sorted(L, key=by_score)
print(L2)


## Createcounter
def createCounter():
    n=0
    def counter():
        nonlocal    n
        n=n+1
        return n
    return counter

# lambda
list(map(lambda x: x*x,[1,2,3,4,5,6,7,8]))

list(filter(lambda x: x%2 ==1,range(1,20)))



# Decorator
def now():
    print('2015-3-25')
    pass
f=now
now.__name__
f.__name__

# Decorator: could print the diary
import  functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
        pass
    return wrapper
    pass
# @log ... def` func():    =====  func=log(func)
@log
def now():
    print('2015-3-25')

now()

def log(txt):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (txt, func.__name__))
            return  func(*args,**kw)
            pass
        return  wrapper
        pass
    return  decorator
    pass

# @log('sample') ... def func() ====== func=log('sample')(func)
@log('Hollo')
def now():
    print('2015-3-25')
    pass
now()


# time recording
import  time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        sta_time=time.time()
        func=fn(*args,**kw)
        end_time=time.time()
        dtime=end_time-sta_time
        print('%s executed in %s ms' % (fn.__name__, dtime))
        return func
    return  wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
fast.__name__
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# partial function
import functools
int2=functools.partial(int,base=4)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart=Student('Bart',59)
bart.print_score()

class Person(object):
    def __init__(self,hight,weight,age):
        self.height=hight
        self.weight=weight
        self.age=age
        pass
    def paoniu(self):
        print('you have ability to finde the girl')
        pass
    def eat(self):
        print('you can eat')
        pass

zhangsan=Person(170,50,29)
lisi=Person(175,100,30)

zhangsan.paoniu()
zhangsan.eat()


class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
        pass
    def get_grade(self):
        if self.score>=90:
            return  'A'
        elif self.score>=60:
            return  'B'
        else:
            return  'C'
            pass
        pass

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())

## the later Class don't influence the Former Class
#第一轮
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
        pass
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
        pass
#实例1
lisa = Student('Lisa',99)
lisa.name='GIM'
#第二轮
class  Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def get_grade(self):
		if self.score >= 90:
		    return 'A'
		elif self.score >= 60:
		    return 'B'
		else:
		    return 'C'
	def print_score(self):
		print ('%s: %s, Level %s' % (self.name, self.score,self.get_grade()))

#创建实例2
bart = Student('Bart',58)

#调用函数输出
lisa.print_score()
bart.print_score


class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        pass

    def print_score(self):
        print('%s : %s'% (self.__name,self.__score))
        pass

    def get_name(self):
        return  self.__name
        pass
    def get_score(self):
        return  self.__score
        pass
bart=Student('Bart',122)
bart.get_score()

# couldn't change the self's name by the new virable directly
bart.__name='GIM'
bart.get_name()


class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        pass

    def print_score(self):
        print('%s : %s'% (self.__name,self.__score))
        pass

    def get_name(self):
        return  self.__name
        pass
    def get_score(self):
        return  self.__score
        pass
    def change_socre(self,score):
        if 0 <= score <=100:
            self.__score=score
        else:
            raise   ValueError('bad score: The socre should between 0 and 100')
            pass
    def change_name(self,name):
        self.__name=name
        pass
bart=Student('Bart',122)
bart.get_name()
bart.get_score()

bart.change_name('Lisa')
bart.get_name()
bart.change_socre()

bart._Student__name='Loiza'
bart._Student__name




class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
        pass
    def get_gender(self):
        return  self.__gender
        pass

    def set_gender(self,gender):
        self.__gender=gender
        pass


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running...')
        pass

class Dog(Animal):
    def run(self):
        print('Dog is running...')
        pass
    def eat(self):
        print('Eating meat...')
        pass
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running...')
        pass
    def eat(self):
        print('Eating fish...')
        pass
    pass

def runtw(animal):
    animal.run()
    animal.run()
    pass

runtw(Dog())
