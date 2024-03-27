from itertools import permutations

def partition(n, m=1):
    yield (n, )
    for i in range(m, n // 2 + 1):
        for p in partition(n - i, i):
            yield (i, ) + p


N = int(input("Number N is: "))

print("\nGenerated partitions:\n")
for k in partition(N):
    print(k)
print("\n")
print("Generated compositions:\n")
for k in partition(N):
    print("\n".join([str(x) for x in sorted([e for e in set(permutations(k))])]))

