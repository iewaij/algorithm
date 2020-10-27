import re


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.sentence_dict = dict(zip(sentences, times))
        self.input_str = ""

    def search(self, s):
        result = [(key, value)
                  for key, value in self.sentence_dict.items()
                  if key.startswith(s)]
        sorted_result = sorted(result, key=lambda x: (-x[1], x[0]))
        top_keys = [key for key, value in sorted_result[:3]]
        return top_keys

    def input(self, c):
        if c == "#":
            input_times = self.sentence_dict.setdefault(self.input_str, 0) + 1
            self.sentence_dict[self.input_str] = input_times
            return []
        else:
            self.input_str += c
            return self.search(self.input_str)


auto = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
assert auto.input("i") == ["i love you", "island","i love leetcode"]
assert auto.input(" ") == ["i love you", "i love leetcode"]
assert auto.input("a") == []
assert auto.input("#") == []
