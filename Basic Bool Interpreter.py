def compare_dynamic_float_points(df1, df2):
    int_part1, frac_part1 = df1.split('.')
    int_part2, frac_part2 = df2.split('.')
    
    # Compare integer parts
    if int_part1 == int_part2:
        # Compare fractional parts if integer parts are equal
        if frac_part1 == frac_part2:
            return True
    return False

# Example usage
df1 = "FFF000.FFF000"
df2 = "FFF000.FFFF00"
df3 = "FFF000.FFF000"

print(compare_dynamic_float_points(df1, df2))  # Output: False
print(compare_dynamic_float_points(df1, df3))  # Output: True
