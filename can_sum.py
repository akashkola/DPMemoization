def can_sum(target_sum: int, numbers: list[int], mem: dict[int, bool] = None) -> bool:
    if mem is None:
        mem = {}
    
    if target_sum in mem:
        return mem[target_sum]

    if target_sum == 0:
        return True
    
    if target_sum < 0:
        return False
    
    for choice in numbers:
        result = can_sum(target_sum - choice, numbers, mem)
        if result:
            mem[target_sum] = True
            return True

    mem[target_sum] = False
    return False

print(can_sum(7, [2, 3]))          # True
print(can_sum(7, [5, 3, 4, 7]))    # True
print(can_sum(7, [2, 4]))          # False
print(can_sum(8, [2, 3, 5]))       # True
print(can_sum(300, [7, 14]))       # False
