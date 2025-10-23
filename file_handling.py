# with open("demo.txt", "w") as file:
#     file.write("Where's the Danger?\n")
#     file.write("I'm the Danger\n")
#     file.write("Wassup Danger")
# print("File Written Successfully!")

# def count_lines_in_file(file_path):
#     try:
#         with open(file_path, "r") as f:
#             lines = f.readlines()
#             return len(lines)
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#     except Exception as e:
#         print(f"An exception occurred: {e}")
#         return 0
# file_path = "demo.txt"
# line_count = count_lines_in_file(file_path)
# print(f"Number of Lines: {line_count}")


# def write_lines_in_file(file_path):
#     try:
#         user_input = input("Enter text to write to the file: ")
#         with open(file_path, "w") as f:
#             f.write(user_input)
#         print(f"Text successfully written to {file_path}")
#     except Exception as e:
#         print(f"An exception occurred: {e}")
# file_path = "output.txt"
# write_lines_in_file(file_path)



import csv

def read_csv_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "info.csv"
read_csv_file(file_path)