#예제5, 평균을 구하는 함수를 작성한 후 세 과목의 점수를 입력받아 평균을 구하여 소수 둘째자리까지 반올림하여
#출력하는 프로그램을 작성하시오.
#입력예 세 과목의 점수를 입력하세요. 80 65 95
#평균 : 80.00

# def p(x,y,z):
#     sum_= x+y+z
#     return sum_/3

# a,b,c = map(int,input('세 과목의 점수를 입력하세요.').split())
# avg=p(a,b,c)
# print(("평균 : %.2f") % avg)

#자가진단5, 10 이하의 두 정수 m과 n을 입력 받아서 m을 n만큼 거듭제곱하여 나온 값(m의 n승)을 리턴하는 함수를
#작성하여 다음과 같이 출력하는 프로그램을 작성하시오. (거듭제곱 연산자 m**n을 리턴하면 편하나, 연습을 위해
# 거듭제곱 연산자를 사용하지 않고 작성하시오.)

def su(x,y):
    sum_=1
    for i in range(y):
        sum_*=x
    return print(sum_)

a,b = map(int,input().split()) 
su(a,b)