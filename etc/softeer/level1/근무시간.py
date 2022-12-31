from sys import stdin

tot_time = 0
for i in range(5):
    start, end = stdin.readline().split()
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    tot_time += (end_h - start_h) * 60 + (end_m - start_m)
print(tot_time)
