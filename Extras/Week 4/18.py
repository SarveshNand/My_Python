def count_text_stats(paragraph):
    lines = paragraph.strip().split('\n')
    line_count = len(lines)
    
    words = paragraph.strip().split()
    word_count = len(words)

    char_count = len(paragraph)

    return line_count, word_count, char_count

paragraph = """
This is a sample paragraph.
It spans multiple lines,
and contains several words and characters.
"""

lines, words, characters = count_text_stats(paragraph)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)