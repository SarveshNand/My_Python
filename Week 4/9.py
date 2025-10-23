def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if both strings have the same length
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")