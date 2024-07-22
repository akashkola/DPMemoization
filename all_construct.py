def all_construct(target_string: str, word_bank: list[str], mem: dict[str, list[list[int]]] = None) -> list[list[int]]:
    if mem is None:
        mem = {}

    if target_string in mem: return mem[target_string]
    if target_string == '': return [[]]

    results = []

    for word in word_bank:
        if not target_string.startswith(word):
            continue
        next_string = target_string[len(word)::]
        ways = all_construct(next_string, word_bank, mem)
        mem[next_string] = ways
        result = [ [word] + [way_word for way_word in way] for way in ways]
        results.extend(result)

    mem[target_string] = results
    return results

print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
