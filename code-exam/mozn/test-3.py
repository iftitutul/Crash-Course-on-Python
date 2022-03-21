
def solution(S,C):
    n = len(S)
    ans = 0
    for i in range(0, n - 1):
        if(S[i] != S[i + 1]):
            continue
        if(C[i] > C[i + 1]):
            swap(C[i], C[i + 1])
        ans += C[i]

    return ans

S='abccbd'
C=[0,1,2,3,4,5]


print(solution(S,C))

