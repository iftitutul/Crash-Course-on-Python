def solution(S):
    b_flag = 0
    ans = True
    for c in S:
        if c == 'b':
            b_flag = 1
        elif b_flag and c == 'a':
            ans = False
    
    return ans

print(solution("aabbb"))

print(solution("abba"))