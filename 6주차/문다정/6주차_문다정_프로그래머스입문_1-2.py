#6주차(2차시)
#1. 나머지 구하기
def solution(num1, num2):
    return num1 % num2
    
#2. 중앙값 구하기
def solution(array):
    #제한사항에서 array의 길이는 항상 홀수 = 걍 중간값 출력
    return sorted(array)[int(len(array)/2)]
    
    #짝수 길이의 array도 주어졌다면 중간의 2개 값의 평균이 중앙값

#3. 최빈값 구하기
import collections
def solution(array):
    num =  collections.Counter(array)
    result = []
    for i in list(num.keys()):
        if(num[i] == max(list(num.values()))):
            result.append(i)
    return -1 if(len(result)>=2) else result[0]


#4. 짝수는 싫어요
#옛날에 풀었을때
# def solution(n):
#     return sorted([i for i in range(1,n+1) if(i%2!=0)])

#이번풀이(더 간단하게)
def solution(n):
    return [i for i in range(1,n+1,2)]


#5. 피자 나눠먹기(1)
def solution(n):
    if(n<=7):
        return 1
    elif(n%7==0):
        return n//7
    else:
        return n//7+1


#6. 피자 나눠먹기(2)
import math    
def solution(n):
    #피자한판 = 6조각
    #n명이 피자를 남기지 않고, 모두 같은 수의 피자조각을 먹어야함 - 최소 몇판?
    #결국 n명과 6조각의 최소공배수를 구하고, 이를 명수로 나눈값
    
    # mingong = math.lcm(n,6)
    # return mingong//n
    #그런데 버전이 안맞아서 lcm은 써지지 않음 
    #>> 유클리드 호제법 적용 - 최소공배수 == (두수의곲)/(두수의최대공약수)
    return ((n*6)/(math.gcd(n,6)))/6

#7. 피자 나눠먹기(3)
def solution(slice,n):
    #각 slice에 따라서 n명일때 최소 몇 판을 시켜야하는지
    if(n<slice):
        return 1
    elif(n%slice==0):
        return n//slice
    else:
        return n//slice+1

#8. 배열의 평균값
def solution(numbers):
    #엥 왜 mean은 안되지?
    return sum(numbers)/len(numbers)


