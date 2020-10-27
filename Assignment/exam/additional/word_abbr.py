import re


def word_abbr(s, abbr):
    """Given a non-empty string s and an abbreviation abbr, return whether the string matches withthe given abbreviation."""
    s_list = re.findall(r"(\d+|[a-z]+)", abbr)
    pattern = ""
    for i in s_list:
        if i.isdigit():
            pattern += int(i) * "[a-z]"
        else:
            pattern += i
    return re.fullmatch(r"{}".format(pattern), s) != None


assert word_abbr(s="apple", abbr="a2e") == False
assert word_abbr(s="internationalization", abbr="i12iz4n") == True


def word_abbr_2(s, abbr):
    """Given a non-empty string s and an abbreviation abbr, return whether the string matches withthe given abbreviation."""
    return re.fullmatch(re.sub(r"\d+", r"[a-z]{\g<0>}", abbr), s) != None


assert word_abbr_2(s="apple", abbr="a2e") == False
assert word_abbr_2(s="internationalization", abbr="i12iz4n") == True
