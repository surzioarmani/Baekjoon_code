import sys

def greedy(meeting):
    answer = 0
    endTime = 0
    for i in range(len(meeting)):
        if endTime <= meeting[i][0]:
            endTime = meeting[i][1]
            answer += 1
    return answer
 
 
N = int(sys.stdin.readline())
meeting = []
 
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    meeting.append([A, B])
 
meeting.sort(key=lambda x: (x[1], x[0]))
print(greedy(meeting))
