def word_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def char_valid(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def redundant_symbol(name):
    if " " in name:
        return False
    return True


def username_is_valid(name):
    if word_length(name) and char_valid(name) and redundant_symbol(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)