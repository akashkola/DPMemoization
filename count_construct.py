def count_construct(target_string: str, word_bank: list[str], mem: dict[str, int] = None) -> int:
    if mem is None:
        mem = {}

    if target_string in mem: return mem[target_string]

    if target_string == '': return 1

    count = 0

    for word in word_bank:
        if not target_string.startswith(word):
            continue
        next_string = target_string[len(word)::]
        result = count_construct(next_string, word_bank, mem)
        mem[next_string] = result
        if result:
            count += result
    
    mem[target_string] = count
    return count

print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"])) # 0
# print(can_construct("", ["ate", "ab", "ac"])) # 
