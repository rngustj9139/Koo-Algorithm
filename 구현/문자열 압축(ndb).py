'''
[입출력 예시]
aabbaccc, 2a2ba3c (1개 단위), 7개
ababcdcdababcdcd, 2ababcdcd (8개 단위), 9개
abcabcdede, 2abcdede (3개 단위), 8개

===========

abababcdcdcd

a b a b a b c d c d c d

ab ab ab cd cd cd

3ab3cd
'''

def solution(s):
    answer = len(s)

    for step in range(1, (len(s) // 2) + 1):
        prev = s[0:step]
        cnt = 1
        compressed = ""
        for i in range(step, len(s), step):
            if (prev == s[i:i + step]): # 만약 이전의 값과 똑같은 경우
                cnt += 1
            else: # 만약 이전의 값과 다른 경우
                if (cnt >= 2):
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                cnt = 1
                prev = s[i:i + step]

        # 남은 값 처리
        if (cnt >= 2):
            compressed += str(cnt) + prev
        else: # cnt가 1이면
            compressed += prev

        answer = min(answer, len(compressed))

    return answer

s = input()

print(solution(s))