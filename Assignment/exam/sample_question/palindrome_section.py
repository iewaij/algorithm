"""
A palindrome is a sequence that reads the same backwards as forwards. “Anna”, for example is a palindrome. The task is to find all palindromic sequences within any given string.
"""
def palindrome_section(a_string: str) -> list:
    palindrome_list = []
    n = len(a_string)
    for i in range(1, n-1):
        section_list = []
        for j in range(min(i, n-i)):
            if a_string[i-j] == a_string[i+j+1]:
                if not section_list:
                    palindrome_string = a_string[i-j] + a_string[i+j+1]
                else:
                    palindrome_string = a_string[i-j] + section_list[-1] + a_string[i+j+1]
                section_list.append(palindrome_string)
            else:
                break
        palindrome_list.extend(section_list)
    return palindrome_list
