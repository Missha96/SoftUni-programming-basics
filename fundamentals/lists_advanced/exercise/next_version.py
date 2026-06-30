version = input().split(".")
version_as_int = int("".join(version))
next_version = version_as_int + 1
next_version_lst = [digit for digit in str(next_version)]

print(*next_version_lst, sep=".")