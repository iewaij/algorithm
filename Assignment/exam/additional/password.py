import re


def is_lengthy(password):
    return 6 <= len(password) <= 20


def is_complex(password):
    has_number = re.search(r"[0-9]", password) != None
    has_lower = re.search(r"[a-z]", password) != None
    has_upper = re.search(r"[A-Z]", password) != None
    return has_number and has_lower and has_upper


def not_repetitive(password):
    return re.search(r"(\w)\1{2,}", password) == None


def password_checker(password):
    status_dict = {"length": is_lengthy(password),
                   "complexity": is_complex(password),
                   "no_repetition": not_repetitive(password)}
    msg_dict = {"length": "Password must have at least 6 characters and at most 20 characters.",
                "complexity": "Password must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.",
                "no_repetition": "Password must not contain three repeating characters in a row."}
    msg_list = []
    for key in status_dict.keys():
        if status_dict[key] == False:
            msg_list.append(msg_dict[key])
    if msg_list != []:
        print("\n".join(msg_list))
    else:
        return 0


assert password_checker("Password") != 0
assert password_checker("123Password") == 0
