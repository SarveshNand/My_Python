def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substrings(text):
    palindromes = set()  # Use set to avoid duplicates

    n = len(text)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = text[i:j]
            if len(substring) > 1 and is_palindrome(substring):
                palindromes.add(substring)

    return palindromes

input_string = "madamracecar"
result = find_palindromic_substrings(input_string)

print("Palindromic Substrings:")
for p in sorted(result):
    print(p)