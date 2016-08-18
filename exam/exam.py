import math
import datetime
# 'hello, {name}!'と出力してください 。
def hello(name):
    print('hello,''name'+'!')


# sentence の文字数を出力してくださいu
def length(sentence):
    print(len(sentence))


# sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
def slicing2to5(sentence):
    print(sentence[2:5])


# number の符号を出力してください。ただし、0は'0'と出力してください
def number_sign(number):
    if number == 0:
        print(str(0))

    elif number < 0:
        print('-')

    else:
        print('+')



# number が素数なら'ok',そうでないなら'ng'と出力してください
def prime_number(number):
    count = 0
    for i in range(1,number):
        if number % i == 0:
            count += 1
        else:
            count += 0

    if count == 1:
        print('ok')

    else:
        print('ng')


# 1からnumberまでの合計を出力してください
def sum_from_1_to(number):
    sum = 0
    for i in range(1,number+1):
        sum += i
        print(sum)



# numberの階乗(factorial)を出力してください
def factorial(number):
    print(math.factorial(number))


# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
def cubic_list(data):
    data = [x**3 for x in range(10)]
    return data


# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
def calc_hypotenuse(x, y):
    a = x ** 2 + y ** 2
    b = math.sqrt(a)
    return b


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
def calc_subtense(x, v):
    a = x ** 2 - v ** 2
    b = math.sqrt(a)
    return b


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
def calc_area_triangle(x, y, z):
    pass


# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
def point_two_digits(a, b, c):
    pass


# リストdataの内容を小さい順でソートした結果を返してください
def list_sort(data):
    return sorted(data)


# 文字列の並びを逆にしたものを返してください
def reverse_string(sentence):
    a = sentence
    a.reverse()
    print(" ".join(a))


# dateから2016年4月1日までの日数を返してください
def days_from_date(point):
    d = datetime.date(2016,4,1)
    a = d - point
    c = a.days
    return c