def unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    # Create a set to track seen elements
    seen = set()
    
    # Iterate through the original list
    for element in input_list:
        # Check if the element is not in the seen set
        if element not in seen:
            # Add it to the unique list and mark it as seen
            unique_list.append(element)
            seen.add(element)
    
    return unique_list

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", result)
