def expand_hex_code(short_code, length=6):
    """Expand a short hex code to a full hex code of the specified length."""
    if length == 6:
        expanded = ''.join([ch * 2 for ch in short_code[:3]])
    elif length == 8:
        expanded = ''.join([ch * 2 for ch in short_code[:4]])
    else:
        expanded = ''.join([ch * length for ch in short_code])
    return expanded.upper()

def parse_dfpi_with_custom_prefix(dfpi_str):
    # Check for the presence of '#!' in the string
    if '#!' not in dfpi_str:
        raise ValueError("Error: invalid syntax, did you mean 'X#!'?")

    # Split the input string at the '#!' to separate the prefix
    prefix, dfpi = dfpi_str.split('#!')

    # Validate the prefix
    if not prefix:
        prefix = 'X'
    elif prefix.lower() == '3a':
        prefix = '3A'
    elif not prefix.isdigit() and prefix != 'X':
        raise ValueError(f"Error: invalid syntax, did you mean '{prefix.upper()}#!'?")

    # Validate characters
    if not all(ch.isalnum() or ch == '.' for ch in dfpi):
        raise ValueError("Error: special character(s) detected where letter or number was expected")

    # Remove the decimal point for length checking
    dfpi_no_decimal = dfpi.replace('.', '')

    # Expected length checks
    expected_length = 12
    if prefix in ['1', '3A', 'X']:
        expected_length = 12
    
    if len(dfpi_no_decimal) != expected_length:
        raise ValueError(f"Error: {expected_length} characters expected for dynamic floating point integer")

    # Process based on prefix
    if prefix == '1':
        print(dfpi[:6])
    elif prefix == '2':
        parts = dfpi.split('.')
        print(parts[0])
        print(parts[1])
    elif prefix == '3A':
        for i in range(3):
            print(expand_hex_code(dfpi_no_decimal[i*4:(i+1)*4], 8))
    elif prefix == '4':
        for i in range(4):
            print(expand_hex_code(dfpi_no_decimal[i*3:(i+1)*3], 6))
    elif prefix == '6':
        for i in range(6):
            print(expand_hex_code(dfpi_no_decimal[i*2:(i+1)*2], 6))
    elif prefix == '12':
        for ch in dfpi_no_decimal:
            print(expand_hex_code(ch, 6))
    elif prefix == 'X':
        print(dfpi_no_decimal)
    else:
        raise ValueError(f"Error: invalid division, did you mean '6#!'?")

# Testing the function with different inputs
test_cases = [
    "1#!00fgbb.fg00fp",
    "2#!00fg00.fg00fp",
    "3A#!00fg00.fg00fp",
    "4#!00fg00.fg00fp",
    "6#!00fg00.fg00fp",
    "12#!00fg00.fg00fp",
    "X#!00fg00.fg00fp",
    "4#!00ff00.ff00f",
    "3a#!00ff00.ff00ff",
    "3A#!00ppp00.ppp00pp",
    "3A#[]{}#%.=+*^><",
    "#!00ff00.ff00ff",
    ""
]

for test in test_cases:
    print(f"Testing: {test}")
    try:
        parse_dfpi_with_custom_prefix(test)
    except ValueError as e:
        print(e)
    print()
