import sys
num = int(input())
lst = []
for i in range(num):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    sys.stdout.write(str(i)+'\n')
