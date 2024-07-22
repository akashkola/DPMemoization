def grid_traveler(m: int, n: int, mem = {}) -> int:
    if (m, n) in mem:
        return mem[(m, n)]
    if (n, m) in mem:
        return mem[(n, m)]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    mem[(m, n)] = grid_traveler(m - 1, n, mem) + grid_traveler(m, n - 1, mem)

    return mem[(m, n)]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(0, 3))
print(grid_traveler(3, 0))
print(grid_traveler(0, 0))
print(grid_traveler(18, 18))
