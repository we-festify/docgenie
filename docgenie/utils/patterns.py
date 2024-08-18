import re

def doesMatchPattern(file, patterns):
    """
        Patterns support wildcard characters * and ?
    """

    for pattern in patterns:
        if pattern == file:
            return True
        if pattern == "*":
            return True
        if pattern == "":
            continue
        pattern = pattern.replace("*", ".*")
        pattern = pattern.replace("?", ".")
        if re.match(pattern, file):
            return True
    return False
