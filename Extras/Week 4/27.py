def run_length_encode(text):
    if not text:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1  # Reset count for new character

    # Add the last character group
    encoded += text[-1] + str(count)
    return encoded

input_string = "aaabbbbccddddd"
encoded_string = run_length_encode(input_string)

print("Original String :", input_string)
print("Encoded String  :", encoded_string)