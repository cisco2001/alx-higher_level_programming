#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j:
            if int(f"{i}{j}")  < int(f"{j}{i}"):
                print("{}{}".format(i, j))
