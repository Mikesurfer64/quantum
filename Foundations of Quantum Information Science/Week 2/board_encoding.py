import numpy as np # Import numpy for array manipulation

def decimal_to_ternary(d: int) -> str:
    """
    Converts a non-negative decimal integer to its ternary (base 3) string representation.

    Args:
        d (int): The non-negative decimal integer to convert.

    Returns:
        str: The ternary string representation of the decimal number.
             Returns "0" if the input is 0.
    """
    if d == 0:
        return "0"
    t_str = ""
    while d > 0:
        t_str += str(d % 3) # Get the remainder (ternary digit)
        d = d // 3          # Integer division
    return t_str[::-1] # Reverse the string as digits are collected in reverse order

def map_list_elements(input_list: list) -> dict:
    """
    Creates a mapping from specific string elements in an input list to desired output values
    (e.g., '1' to 'X', '2' to 'O', '' to '').

    Args:
        input_list (list): The list containing the string elements to map (e.g., ['', '1', '2']).

    Returns:
        dict: A dictionary containing:
            - 'input_list': The original list.
            - 'mapping_dictionary': The internal mapping used.
            - 'mapped_list': A new list with elements mapped to their target values.
    """
    # Define the target mapping
    # This dictionary explicitly maps the values '', '1', and '2' to "", "X", and "O".
    target_map = {
        '': "",
        '0': "", # Added '0' mapping for ternary conversion context
        '1': "X",
        '2': "O"
    }

    # Create a new list by applying this mapping
    mapped_results = []
    for item in input_list:
        # Check if the item exists in our target_map to avoid KeyError
        # Convert item to string just in case it's an int from previous ops
        str_item = str(item)
        if str_item in target_map:
            mapped_results.append(target_map[str_item])
        else:
            print(f"Warning: No mapping found for input item '{str_item}'. Assigning None.")
            mapped_results.append(None)

    return {
        "input_list": input_list,
        "mapping_dictionary": target_map,
        "mapped_list": mapped_results
    }

# --- Example Usage ---
if __name__ == "__main__":
    # --- Original examples for mapping lists ---
    print("--- Original Examples for Mapping Lists ---")
    original_list_to_map = ['', '1', '2']
    mapping_info_for_query = map_list_elements(original_list_to_map)
    print(f"Original Input List: {mapping_info_for_query['input_list']}")
    print(f"Resulting Mapped List: {mapping_info_for_query['mapped_list']}")

    print("\n--- Other Examples from the Original Script ---")
    original_list = ['', '1', '2']
    mapping_info = map_list_elements(original_list)
    print(f"Original Input List: {mapping_info['input_list']}")
    print(f"Defined Mapping: {mapping_info['mapping_dictionary']}")
    print(f"Resulting Mapped List: {mapping_info['mapped_list']}")

    print("\nDemonstrating direct access using the mapping:")
    mapping = mapping_info['mapping_dictionary']
    print(f"Mapping for '': '{mapping['']}'")
    print(f"Mapping for '1': '{mapping['1']}'")
    print(f"Mapping for '2': '{mapping['2']}'")

    another_list = ['1', '', '2', '1', '0', 'X'] # '0' and 'X' are not in the map, will show warning
    another_mapping_info = map_list_elements(another_list)
    print(f"\n--- Processing Another List ---")
    print(f"Original Input List: {another_mapping_info['input_list']}")
    print(f"Resulting Mapped List: {another_mapping_info['mapped_list']}")


    # --- New Functionality: Creating a 3x3 Array with X's and O's ---
    print("\n" + "="*60)
    print("Creating a 3x3 Array with X's and O's from Ternary Conversion")
    print("="*60)

    decimal_number = 12065
    ternary_str = decimal_to_ternary(decimal_number)
    print(f"{decimal_number:,} in decimal = '{ternary_str}' in ternary")

    # Pad the ternary string with leading zeros to ensure it's 9 digits long for a 3x3 array
    # This handles cases where the ternary representation is shorter than 9 digits.
    # For 2271, '10010010' becomes '010010010'
    padded_ternary_str = ternary_str.zfill(9)
    print(f"Padded Ternary String (for 3x3 board): '{padded_ternary_str}'")

    # Slice the padded ternary string into three 3-character parts
    # Each part represents a row of the 3x3 board
    first_row_str = padded_ternary_str[0:3]
    second_row_str = padded_ternary_str[3:6]
    third_row_str = padded_ternary_str[6:9]

    print(f"Sliced Rows (as strings): {first_row_str}, {second_row_str}, {third_row_str}")

    # Convert each string part into a list of its characters (digits)
    # e.g., '010' -> ['0', '1', '0']
    first_row_list_digits = list(first_row_str)
    second_row_list_digits = list(second_row_str)
    third_row_list_digits = list(third_row_str)

    print(f"Rows as lists of digits: {first_row_list_digits}, {second_row_list_digits}, {third_row_list_digits}")

    # Map the digits ('0', '1', '2') to the board symbols ('', 'X', 'O')
    mapped_first_row = map_list_elements(first_row_list_digits)['mapped_list']
    mapped_second_row = map_list_elements(second_row_list_digits)['mapped_list']
    mapped_third_row = map_list_elements(third_row_list_digits)['mapped_list']

    print(f"Mapped Rows (with symbols): {mapped_first_row}, {mapped_second_row}, {mapped_third_row}")

    # Combine the mapped rows into a list of lists to form the 3x3 grid
    board_grid = [mapped_first_row, mapped_second_row, mapped_third_row]

    # Convert the list of lists into a NumPy array
    final_3x3_array = np.array(board_grid)

    print("\nFinal 3x3 Tic-Tac-Toe Board (X's, O's, and empty strings):")
    print(final_3x3_array)

    print("\n" + "="*60)
    print("End of 3x3 Array Generation Example.")
    print("="*60)
