#!/usr/bin/python
# -*- coding: UTF-8 -*-


N = int(input())
n = []
for i in range(N-1):
    n.append(int(input()))
teams = [x + 1 for x in range(N)]

tour = 2

while tour <= N:
    for i in range(int(N/tour)):
        if n[i] == 1:
            teams[i*2 + 1] = 0
        elif n[i] == 2:
            teams[i*2] = 0

    teams = [x for x in teams if x != 0]
    n = n[int(N/tour):]
    tour *= 2

print(teams[0])
