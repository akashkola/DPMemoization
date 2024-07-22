def best_sum(target_sum: int, options: list[int], mem: dict[int, list[int] | None] = None) -> list[int] | None:
    if mem is None:
        mem = {}

    if target_sum in mem: return mem[target_sum]

    if target_sum == 0: return []
    if target_sum < 0: return None

    best_combination: list[int] | None = None

    for option in options:
        result = best_sum(target_sum - option, options, mem)
        if result is not None:
            result.append(option)
            if best_combination is None or len(best_combination) > len(result):
                best_combination = result
    
    mem[target_sum] = best_combination
    return best_combination

print(best_sum(7, [5, 3, 4, 7])) # [7]
print(best_sum(8, [2, 3, 5])) # [5, 3]
print(best_sum(8, [1, 4, 5])) # [4, 4]
print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
