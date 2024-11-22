# Function to find the symmetric difference between two sets
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example usage
if __name__ == "__main__":
    # Define two sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # Calculate the symmetric difference
    result = symmetric_difference(set_a, set_b)

    # Print the result
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("Symmetric Difference:", result)