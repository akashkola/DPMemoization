def all_sum(target: int, choices: list[int], mem: dict[int, list[list[int]]] = None) -> list[list[int]]:
    if mem is None:
        mem = {}
    if target in mem:
        return mem[target]
    if target == 0:
        return [[]]
    if target < 0:
        return []

    target_ways = []

    for choice in choices:
        next_target = target - choice
        if next_target not in mem:  # Ensure we only calculate if not already in mem
            mem[next_target] = all_sum(next_target, choices, mem)
        next_target_ways = mem[next_target]
        next_target_ways_with_choice = [[choice] + way for way in next_target_ways]
        target_ways.extend(next_target_ways_with_choice)

    mem[target] = target_ways
    return target_ways


print(all_sum(7, [5, 3, 4, 7]))
print(all([sum(way) == 7 for way in all_sum(7, [5, 3, 4, 7])]))
print(all_sum(8, [2, 3, 5]))
print(all([sum(way) == 8 for way in all_sum(8, [2, 3, 5])]))
print(all_sum(8, [1, 4, 5]))
print(all([sum(way) == 8 for way in all_sum(8, [1, 4, 5])]))
print(all_sum(100, [1, 2, 5, 25]))
print(all([sum(way) == 100 for way in all_sum(100, [1, 2, 5, 25])]))
