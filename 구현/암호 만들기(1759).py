'''
[완전탐색(브루트포스)]
암호는 L자리의 소문자 알파벳 오름차순으로 이루어짐
최소 1개의 모음과 (a, i, e, o, u)
최소 2개의 자음을 사용해야함
'''
from itertools import combinations

L, C = map(int, input().split())
alphabets = list(map(str, input().split()))
alphabets.sort() # 오름차순 정렬
vowels = ['a', 'i', 'e', 'o', 'u']
results = []

passwordList = combinations(alphabets, L)

for password in passwordList:
    vowelCnt = 0
    consonantCnt = 0

    for onePassword in password:
        if (onePassword in vowels):
            vowelCnt += 1
        else:
            consonantCnt += 1

    if (vowelCnt >= 1 and consonantCnt >= 2):
        results.append(password)

for result in results:
    print(''.join(result))

