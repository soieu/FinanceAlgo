#주사위의 개수
def solution(box, n):
    answer = 0
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n) 
    return answer

#합성수 찾기
def solution(n):
    answer = 0
    count = 0
    for i in range(n+1):
        measure = 0
        for j in range(2, i):
            if i % j == 0:
                measure += 1
        if measure >= 1:
            count += 1
    answer = count
    return answer

#최댓값 만들기(1)
def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]
    return answer

#팩토리얼
def solution(n):
    answer = 0

    i = 1
    factorial = 1
    
    while(True):
        for num in range(1, i+1):
            factorial *= num
        
        print(factorial)
        
        if factorial > n:
            answer = i - 1
            break
        if factorial == n:
            answer = i
            break
            
        i += 1
        factorial = 1
        
        
        
    return answer

#모음 제거
def solution(my_string):
    answer = ''
    vowels = ['a','e','i','o','u']
    my_list = list(my_string)
    for vowel in vowels:
        cnt = my_string.count(vowel)
        for _ in range(cnt):
            my_list.remove(vowel)
    answer = "".join(my_list)
    return answer

#문자열 정렬하기 (1)
# #include <string>
# #include <vector>
# #include <algorithm>

# using namespace std;

# vector<int> solution(string my_string) {
#     vector<int> answer;
#     for(int i = 0; i < my_string.length(); i++)
#     {
#         if(my_string[i] >= '0' && my_string[i] <= '9')
#             answer.push_back(my_string[i]-'0');
#     }
#     sort(answer.begin(), answer.end());
    
#     return answer;
# }


#숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for s in my_string:
        if s >= '0' and s <= '9':
            answer += int(s)
    return answer

#소인수분해
def solution(n):
    answer = []

    for i in range(2, n+1):
        # i가 소수인지 체크
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break;
        if flag == 0:
            if n % i == 0:
                answer.append(i)
    return answer


