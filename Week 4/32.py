import re

def camel_to_snake(text):
    snake_case = re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()
    return snake_case

camel_string = "thisIsCamelText"
snake_string = camel_to_snake(camel_string)

print("CamelCase: ", camel_string)
print("snake_case: ", snake_string)