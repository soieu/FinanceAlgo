#6주차(4차시)
#1. 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

#2. 각도기
def solution(angle):
    result = 0
    if(angle==180):
        result = 4
    elif(angle > 90):
        result = 3
    elif(angle == 90):
        result = 2
    else:
        result = 1
    return result

#3. 양꼬치
def solution(n,k):
    #10인분 - 음료수1개
    #1인분 12000원, 음료수 2000원
    #양꼬치 n인분, 음료수 k개(총음료수, 따로시킨거도포함)
    return 12000*n + (k-n//10)*2000

#4. 짝수의 합
def solution(n):
    return sum([i for i in range(2,n+1,2)])

#5. 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

#6. 외계행성의 나이
def solution(age):
    age_dict = {'0':'a','1':'b','2':'c','3':'d','4':'e',
                '5':'f','6':'g','7':'h','8':'i','9':'j'}
    result = ''
    for i in str(age):
        result += age_dict[i]
    return result

#7. 진료순서 정하기
def solution(emergency):
    result = []
    for i in emergency:
        result.append(sorted(emergency)[::-1].index(i)+1)
    return result


#8. 순서쌍의 개수
def solution(n):
    #흠 딱 절반까지 알아보면.. 됨
    #짝수면 n/2까지, 홀수라도 걍 n/2까지 아닌가
    cnt = 0
    for i in range(1,int(n**(1/2))+1):
        if(i==n**(1/2)):
            cnt += 1
        elif(n%i==0):
            cnt += 2
    return cnt