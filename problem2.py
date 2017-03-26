fibSeq = [1,2]

while fibSeq[-1] < 4000000:
    fibSeq.append(fibSeq[-2] + fibSeq[-1])

total = 0
for i in fibSeq:
    if i%2 == 0:
        total += i

print total
