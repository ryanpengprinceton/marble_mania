from collections import deque

def winning_score(P, M):
    s = [0] * P
    q = deque()
    for i in range(M + 1):
        if i % 23 == 0 and i != 0:
            q.rotate(-7)
            s[i % P] += (i + q.popleft())
            q.rotate(1)
        else:
            q.rotate(1)
            q.appendleft(i)
    return max(s)
