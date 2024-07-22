def can_construct(target_string: str, word_bank: list[str], mem: dict[str, bool] = None) -> bool:
    if mem is None:
        mem = {}

    if target_string in mem: return mem[target_string]

    if target_string == '': return True

    for word in word_bank:
        if not target_string.startswith(word):
            continue
        next_string = target_string[len(word)::]
        result = can_construct(next_string, word_bank, mem)
        mem[next_string] = result
        if result:
            return result
            
    mem[target_string] = False
    return False
        

# abcdef
# ab

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"])) # False
print(can_construct("", ["ate", "ab", "ac"])) # True
