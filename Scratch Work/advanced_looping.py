# 14.2.1. Problem 1
# for i in range(10):
#     print("*", end=" ")


# 14.2.2. Problem 14.2
# for i in range(10):
#     print("*", end=" ")
# print()
# for i in range(5):
#     print("*", end=" ")
# print()
# for i in range(20):
#     print("*", end=" ")


# 14.2.3. Problem 3
# for i in range(10):
#     for j in range(10):
#         print("*", end=" ")
#     print()


# 14.2.4. Problem 4
# for i in range(10):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# 14.2.5. Problem 5
# for i in range(5):
#     for j in range(20):
#         print("*", end=" ")
#     print()


# 14.2.6. Problem 6
# for i in range(10):
#     for j in range(10):
#         print(j, end=" ")
#     print()


# 14.2.7. Problem 7
# for i in range(10):
#     for j in range(10):
#         print(i, end=" ")
#     print()


# 14.2.8. Problem 8
# for i in range(11):
#     for j in range(i):
#         print(j, end=" ")
#     print()


# 14.2.9. Problem 9
# for i in range(10):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(10 - i):
#         print(k, end=" ")
#     print()


# 14.2.10. Problem 10
# for i in range(1, 10):
#     for j in range(1, 10):
#         # Extra space?
#         if i * j < 10:
#             print(" ", end="")
#         print(i * j, end=" ")
#     print()


# 14.2.11. Problem 11
# for i in range(1, 10):
#     for j in range(10 - i):
#         print(" ", end=" ")
#     # Count up
#     for k in range(1, i):
#         print(k, end=" ")
#     # Count down
#     for l in range(i, 0, -1):
#         print(l, end=" ")
#     print()


# 14.2.12. Problem 12
# for i in range(1, 10):
#     for j in range(10 - i):
#         print(" ", end=" ")
#     # Count up
#     for k in range(1, i):
#         print(k, end=" ")
#     # Count down
#     for l in range(i, 0, -1):
#         print(l, end=" ")
#     print()
#
# for m in range(10):
#     for n in range(m + 2):
#         print(" ", end=" ")
#     for o in range(1, 9 - m):
#         print(o, end=" ")
#     print()


# 14.2.13. Problem 13
for i in range(1, 10):
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for k in range(1, i):
        print(k, end=" ")
    # Count down
    for l in range(i, 0, -1):
        print(l, end=" ")
    print()

for m in range(10):
    for n in range(m + 2):
        print(" ", end=" ")
    for o in range(1, 9 - m):
        print(o, end=" ")
    for p in range(7 - m, 0, -1):
        print(p, end=" ")
    print()
