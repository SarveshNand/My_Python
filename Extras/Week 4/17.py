def end_with(string, suffix):
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False

print(end_with("hello", "lo"))