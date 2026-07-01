from datetime import datetime

def reformat_date(date_str, input_format, output_format):
    date_obj = datetime.strptime(date_str, input_format)
    return date_obj.strftime(output_format)

input_date = "2025-09-29"
input_fmt = "%Y-%m-%d"
output_fmt = "%d/%m/%Y"

formatted_date = reformat_date(input_date, input_fmt, output_fmt)
print("Original Date: ", input_date)
print("Formatted Date: ", formatted_date)