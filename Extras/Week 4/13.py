def count_substring_occurrences(main_string, substring):
    return main_string.count(substring)

main_string = "The quick brown fox jumps over the lazy fox."
substring = "fox"

result = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' appears {result} times in the main string.")