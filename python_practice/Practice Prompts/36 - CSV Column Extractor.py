# Without using pandas, read a CSV and:
#   Extract a chosen column by name.
#   Count unique values in that column.

def csv_column_display(col):

    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(BASE_DIR, "sample.csv")

    with open(csv_file, 'r', encoding="utf8") as file:

        col_index = 0
        for first_line in file:

            if col in first_line:
                header_index = first_line.strip().split(",").index(col)
                col_index = header_index
                break

        column_values = []
        for line in file:
            value = line.strip().split(",")[col_index]
            column_values.append(value)

        unique_col_value_count = len(set(column_values))

        return column_values, unique_col_value_count
        
colvals, uniquecnt = csv_column_display("department")
print("Column values:")
for x in colvals:
    print(x)            
print(f"Unique values: {uniquecnt}")