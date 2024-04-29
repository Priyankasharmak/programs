# n = 5
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f)


# n = 7
# p = True
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         p = False
#         break
# print(p)

# n = 10
# f = [0, 1]
# for i in range(2, n):
#     f.append(f[-1] + f[-2])
# print(f)

# def g(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# r = g(24, 36)
# print(r)

# s = "radar"
# p = True
# for i in range(len(s) // 2):
#     if s[i] != s[-i - 1]:
#         p = False
#         break
# print(p)

# l1 = [1, 3, 5]
# l2 = [2, 4, 6]
# m = []
# i = j = 0
# while i < len(l1) and j < len(l2):
#     if l1[i] < l2[j]:
#         m.append(l1[i])
#         i += 1
#     else:
#         m.append(l2[j])
#         j += 1
# m += l1[i:] + l2[j:]
# print(m)

# def p(b, e):
#     if e == 0:
#         return 1
#     else:
#         return b * p(b, e - 1)

# r = p(2, 3)
# print(r)

s = "This is a sample sentence"
w = s.split()
l = ""
for word in w:
    if len(word) > len(l):
        l = word
print(l)

# import itertools
# n = [1, 2, 3]
# p = list(itertools.permutations(n))
# print(p)

# s = "This is a sample sentence is is"
# w = s.split()
# c = {}
# for word in w:
#     if word in c:
#         c[word] += 1
#     else:
#         c[word] = 1
# print(c)