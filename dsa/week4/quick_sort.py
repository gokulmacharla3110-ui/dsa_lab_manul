def quick_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Create three lists for partitioning the elements
    left = [x for x in arr if x < pivot]      # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot
    
    # Recursively sort the left and right parts, then combine everything
    return quick_sort(left) + middle + quick_sort(right)


# --- Main Program Execution ---
if __name__ == "__main__":
    print("--- Quick Sort Program ---")
    
    # 1. Ask the user for inputs separated by spaces
    user_input = input("Enter numbers separated by spaces (e.g., 5 2 9 1 7): ")
    
    # 2. Convert the input string into a list of integers
    # .split() breaks the text by spaces, and int(x) converts each piece to a number
    try:
        numbers = [int(x) for x in user_input.split()]
        
        # Check if the user actually entered any numbers
        if not numbers:
            print("You didn't enter any numbers!")
        else:
            # 3. Sort the numbers and print the final result
            sorted_numbers = quick_sort(numbers)
            print("\nOriginal array:", numbers)
            print("Sorted array:  ", sorted_numbers)
            
    except ValueError:
        print("\n[Error]: Please enter only valid integers separated by spaces.")
