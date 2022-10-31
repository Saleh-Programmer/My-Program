# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c174f2
mainList = []
day = []
num_case = int(input())
if (num_case <= 100 and num_case >= 1):
    required_step = 0
    for item in range(num_case):
        m, n, p = input().split()
        if (int(n) >= 1 and int(n) <= 31) and (int(p) >= 1 and int(p) <= int(m)) and (int(m) >= 2 and int(m) <= 1000):
            for i in range(int(m)):
                mainList.append(input().split())
            for j in range(int(n)):
                for i in range(int(m)):
                    if i == int(p)-1:
                        continue
                    day.append(
                        int(mainList[int(int(p))-1][j])-int(mainList[i][j]))
            result = max([abs(item) for item in day if item < 0])
            mainList = []
            day = []
            print(result)
