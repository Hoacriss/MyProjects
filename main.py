import time
import os
import random


# This is the function that generates random arrays of given sizes
def generate_random_arrays(sizes):
    arrays = {}
    for size in sizes:
        arrays[size] = [random.randint(0, 10000) for _ in range(size)]
    return arrays

# This is the function that generates sorted arrays of given sizes
def generate_sorted_arrays(sizes):
    arrays = {}
    for size in sizes:
        arrays[size] = list(range(size))
    return arrays

# This is the function that generates sorted arrays in descending order of given sizes
def generate_reverse_sorted_arrays(sizes):
    arrays = {}
    for size in sizes:
        arrays[size] = list(range(size, 0, -1))
    return arrays
# This is the function that handles the type of array that will be generated
def generate_arrays(array_type, sizes):
    array_generators = {
        'sorted': generate_sorted_arrays,
        'random': generate_random_arrays,
        'reverse_sorted': generate_reverse_sorted_arrays
    }

    if array_type in array_generators:
        return array_generators[array_type](sizes)
    else:
        raise ValueError("Invalid array_type. Expected 'sorted', 'random', 'reverse_sorted'.")

# The function that checks if an array is sorted or not
def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))

# Bubble sort implementation
def BubbleSort(array):
    # At the start of each sorting algorithm the array is copied so the original does not change
    array = array.copy()
    # The time is recorded at the start of each algorithm
    start_time = time.time()
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    #The end time is recorded after the end of each algorithm
    end_time = time.time()
    #The elapsed time is computed from the start time and end time
    elapsed_time = end_time - start_time
    print("BubbleSort")
    print("Time: ", elapsed_time, "seconds")
    # The array is checked if it is sorted or not
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# Selection sort implementation
def SelectionSort(array):
    array = array.copy()
    start_time = time.time()
    for i in range(len(array)):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
    end_time = time.time()
    #The elapsed time is calculated from the start time and end time
    elapsed_time = end_time - start_time
    print("SelectionSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# Insertion sort implementation
def InsertionSort(array):
    array = array.copy()
    start_time = time.time()
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("InsertionSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# Helper function for QuickSort for partitioning the array
def partition(array, low, high):
    # Median-of-three pivot selection
    mid = (low + high) // 2
    pivot_candidates = [array[low], array[mid], array[high]]
    pivot_candidates.sort()
    pivot = pivot_candidates[1]

    # Move pivot to end
    pivot_index = array.index(pivot)
    array[pivot_index], array[high] = array[high], array[pivot_index]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Recursive QuickSort implementation
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


# The main QuickSort function that measures the execution time
def QuickSort(array, low, high):
    array = array.copy()
    start_time = time.time()
    quicksort(array, low, high)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("QuickSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# Recursive MergeSort implementation
def mergesort(array):
    if len(array) > 1:
        # Finds the middle point of the array
        mid = len(array)//2
        # Divides the array elements into 2 halves
        L = array[:mid]
        R = array[mid:]
        # Sorts the first half
        mergesort(L)
        # Sorts the second half
        mergesort(R)
        i = j = k = 0
        # Merges the sorted halves
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i = i + 1
            else:
                array[k] = R[j]
                j = j + 1
            k = k + 1
        # Copies the remaining elements of L[], if any
        while i < len(L):
            array[k] = L[i]
            i = i + 1
            k = k + 1
        # Copies the remaining elements of R[], if any
        while j < len(R):
            array[k] = R[j]
            j = j + 1
            k = k + 1

# The main MergeSort function that also measures the execution time
def MergeSort(array):
    array = array.copy()
    start_time = time.time()
    mergesort(array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("MergeSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# Counting Sort implementation
def CountingSort(array, k):
    array = array.copy()
    start_time = time.time()

    # Initialize count array
    Carray = [0] * (k + 1)
    Barray = [0] * len(array)

    # Store the count of each element
    for j in range(len(array)):
        Carray[array[j]] += 1

    # Update the count array to have the actual positions of elements
    for i in range(1, k + 1):
        Carray[i] += Carray[i - 1]

    # Build the sorted array
    for j in range(len(array) - 1, -1, -1):
        Barray[Carray[array[j]] - 1] = array[j]
        Carray[array[j]] -= 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("CountingSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(Barray))
    print("")
    return elapsed_time

# BogoSort implementation
def BogoSort(array):
    array = array.copy()

    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    start_time = time.time()
    attempts = 0
    while not is_sorted(array):
        # Shuffles the array randomly
        random.shuffle(array)
        attempts += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("BogoSort")
    print("Time: ", elapsed_time, "seconds")
    print("Sorted: ", is_sorted(array))
    print("")
    return elapsed_time

# The function that runs the tests and stores the results
def StartTest(array, k):
    if k == 0:
        # The run for the first element
        L = len(array.copy())
        bubblesort_times.append(BubbleSort(array))
        selectionsort_times.append(SelectionSort(array))
        insertionsort_times.append(InsertionSort(array))
        quicksort_times.append(QuickSort(array, 0, L - 1))
        mergesort_times.append(MergeSort(array))
        countingsort_times.append(CountingSort(array, max(array)))
        bogosort_times.append(BogoSort(array))
        detailed_results.append(f"BubbleSort - Size: {L}, Time: {bubblesort_times[-1]} seconds")
        detailed_results.append(f"SelectionSort - Size: {L}, Time: {selectionsort_times[-1]} seconds")
        detailed_results.append(f"InsertionSort - Size: {L}, Time: {insertionsort_times[-1]} seconds")
        detailed_results.append(f"QuickSort - Size: {L}, Time: {quicksort_times[-1]} seconds")
        detailed_results.append(f"MergeSort - Size: {L}, Time: {mergesort_times[-1]} seconds")
        detailed_results.append(f"CountingSort - Size: {L}, Time: {countingsort_times[-1]} seconds")
        detailed_results.append(f"BogoSort - Size: {L}, Time: {bogosort_times[-1]} seconds\n")
        print("")
    else:
        L = len(array.copy())
        # This part checks if each algorithm has taken more than 30 seconds to compute
        # If the algorithm did take more than 30 seconds it will be skipped until the end of the program and
        # the next recorded time will be recorded as -1
        if bubblesort_times[-1] <= 30 and bubblesort_times[-1] >= 0:
            bubblesort_times.append(BubbleSort(array))
            detailed_results.append(f"BubbleSort - Size: {L}, Time: {bubblesort_times[-1]} seconds")
        else:
            bubblesort_times.append(-1)
            detailed_results.append(f"BubbleSort - Size: {L}, Skipped due to previous timeout")
            print("BubbleSort")
            print("TIME LIMIT EXCEEDED \n")
        if selectionsort_times[-1] <= 30 and selectionsort_times[-1] >= 0:
            selectionsort_times.append(SelectionSort(array))
            detailed_results.append(f"SelectionSort - Size: {L}, Time: {selectionsort_times[-1]} seconds")
        else:
            selectionsort_times.append(-1)
            detailed_results.append(f"SelectionSort - Size: {L}, Skipped due to previous timeout")
            print("SelectionSort")
            print("TIME LIMIT EXCEEDED\n")
        if insertionsort_times[-1] <= 30 and insertionsort_times[-1] >= 0:
            insertionsort_times.append(InsertionSort(array))
            detailed_results.append(f"InsertionSort - Size: {L}, Time: {insertionsort_times[-1]} seconds")
        else:
            insertionsort_times.append(-1)
            detailed_results.append(f"InsertionSort - Size: {L}, Skipped due to previous timeout")
            print("InsertionSort")
            print("TIME LIMIT EXCEEDED\n")
        if quicksort_times[-1] <= 30 and quicksort_times[-1] >= 0:
            quicksort_times.append(QuickSort(array, 0, L - 1))
            detailed_results.append(f"QuickSort - Size: {L}, Time: {quicksort_times[-1]} seconds")
        else:
            quicksort_times.append(-1)
            detailed_results.append(f"QuickSort - Size: {L}, Skipped due to previous timeout")
            print("QuickSort")
            print("TIME LIMIT EXCEEDED\n")
        if mergesort_times[-1] <= 30 and mergesort_times[-1] >= 0:
            mergesort_times.append(MergeSort(array))
            detailed_results.append(f"MergeSort - Size: {L}, Time: {mergesort_times[-1]} seconds")
        else:
            mergesort_times.append(-1)
            detailed_results.append(f"MergeSort - Size: {L}, Skipped due to previous timeout")
            print("MergeSort")
            print("TIME LIMIT EXCEEDED\n")
        if countingsort_times[-1] <= 30 and countingsort_times[-1] >= 0:
            countingsort_times.append(CountingSort(array, max(array)))
            detailed_results.append(f"CountingSort - Size: {L}, Time: {countingsort_times[-1]} seconds")
        else:
            countingsort_times.append(-1)
            detailed_results.append(f"CountingSort - Size: {L}, Skipped due to previous timeout")
            print("CountingSort")
            print("TIME LIMIT EXCEEDED\n")
        if is_sorted(array):
            if bogosort_times[-1] <= 30 and bogosort_times[-1] >= 0:
                bogosort_times.append(BogoSort(array))
                detailed_results.append(f"BogoSort - Size: {L}, Time: {bogosort_times[-1]} seconds\n")
            else:
                bogosort_times.append(-1)
                detailed_results.append(f"BogoSort - Size: {L}, Skipped due to previous timeout\n")
                print("BogoSort")
                print("TIME LIMIT EXCEEDED\n")
        else:
            bogosort_times.append(-1)
            detailed_results.append(f"BogoSort - Size: {L}, Skipped due to previous timeout\n")
            print("BogoSort")
            print("TIME LIMIT EXCEEDED\n")
    print(f"Test Completed size {L} arrays")

# Function that creates the detailedResults file and writes the information in it
def write_detailed_results(filename, results):
    with open(filename, 'w') as f:
        f.write("Here are the detailed results of the test:\n\n")
        f.write("WARNING: CLOSE FILE BEFORE RUNNING ANOTHER TEST\n\n")
        for line in results:
            f.write(line + '\n')

# Function that creates the simpleResults file and writes the information in it
def write_simple_results(filename):
    with open(filename, 'w') as f:
        f.write("Here are the simplified results such that are stored in a list:\n\n")
        f.write("WARNING: CLOSE FILE BEFORE RUNNING ANOTHER TEST\n\n")
        f.write("BubbleSort Times: " + str(bubblesort_times) + '\n')
        f.write("SelectionSort Times: " + str(selectionsort_times) + '\n')
        f.write("InsertionSort Times: " + str(insertionsort_times) + '\n')
        f.write("QuickSort Times: " + str(quicksort_times) + '\n')
        f.write("MergeSort Times: " + str(mergesort_times) + '\n')
        f.write("CountingSort Times: " + str(countingsort_times) + '\n')
        f.write("BogoSort Times: " + str(bogosort_times) + '\n')

# The function that creates the arraysUsed file and writes the arrays used in the test in it
def write_arrays_used(filename, arrays):
    with open(filename, 'w') as f:
        f.write("Here are the arrays used for te test:\n\n")
        f.write("WARNING: CLOSE FILE BEFORE RUNNING ANOTHER TEST\n\n")
        for size, array in arrays.items():
            f.write(f"Number of elements: {size} = {array}\n\n")

# This function clears the previous results from all the files
def clear_previous_results(filenames):
    for filename in filenames:
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except PermissionError:
            print("Error: Unable to start the program because there is an open file that can't be deleted. Make sure to close all open files and retry.")

# Here are the specified sizes for the arrays that will be generated
sizes = [10, 20, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 500000, 10000000, 5000000]

# The first run counter
k = 0

# The lists where the times will be stored for each algorithm
bubblesort_times = []
selectionsort_times = []
insertionsort_times = []
quicksort_times = []
mergesort_times = []
countingsort_times = []
bogosort_times = []
detailed_results = []

array_type = input("Enter the type of array to generate (sorted, random, reverse_sorted): ").strip().lower()
print("PLEASE WAIT!!")
clear_previous_results(["detailedResults.txt", "simpleResults.txt", "arraysUsed.txt"])

try:
    generated_arrays = generate_arrays(array_type, sizes)
# Error handling in case the user input is not expected
except ValueError as e:
    print(e)
else:
    write_arrays_used("arraysUsed.txt", generated_arrays)
    for size, array in generated_arrays.items():
        print("Testing array of size: ", size, "\n")
        StartTest(array, k)
        k = 1
write_detailed_results("detailedResults.txt", detailed_results)
write_simple_results("simpleResults.txt")

print("BubbleSort Times: ", bubblesort_times, "\nSelectionSort Times: ", selectionsort_times, "\nInsertionSort Times", insertionsort_times, "\nQuickSort Times: ", quicksort_times, "\nMergeSort Times: ", mergesort_times, "\nCountingSort Times: ", countingsort_times, "\nBogoSort Times: ", bogosort_times)


