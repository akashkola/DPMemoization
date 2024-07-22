def how_sum(n: int, options: list[int], mem: dict[int, list[int] | None] = None) -> list[int] | None:
    if mem is None:
        mem = {}
    if n in mem:
        return mem[n]
    if n == 0:
        return []
    if n < 0:
        return None
    
    for option in options:
        result = how_sum(n - option, options, mem)
        if result is not None:
            result.append(option)
            mem[n - option] = result
            return result

    mem[n] = None
    return None

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
