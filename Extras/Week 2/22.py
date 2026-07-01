def is_anagram(str1, str2):

    str1_clean = str1.replace(" ", "").lower()
    str2_clean = str2.replace(" ", "").lower()

    return sorted(str1_clean) == sorted(str2_clean)


print(is_anagram("listen", "silent"))