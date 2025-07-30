"""
2. Climate Change Data Tracker

Scientists track daily temperatures as a string of values separated by spaces (e.g.,
"30.5 32.1 29.8"). Write a python program that extracts the temperatures, converts
them into float values, and finds the highest, lowest, and average temperature.

Rules & Constraints:
* Input is a string of space-separated float values (e.g., "30.5 31.2").
* All values must be valid floating-point numbers.
* The list must have at least two values.
* Temperatures must be within a realistic range: -100.0C to 60.0C.
* The program should round the average to two decimal places.
* If the input is invalid (non-numeric, empty, out-of-range), return an error
  message.

Input Format:
A single string with space-separated temperature readings (e.g., "25.4 27.8 26.5")

Output Format:
Highest:
Lowest:
Average :

"""

temps = str(input("Enter space separated temperature values : ")).split()

if len(temps) >= 2:
    for i in range(0, len(temps)):
        try:
            temps[i] = float(temps[i])

            if temps[i] < -100 or temps[i] > 60:
                print("Temperature values should be within -100C and 60C!")
                exit(0)

        except ValueError:
            print(f"The value at index \"{i}\" is not a valid temperature\n {temps}")
            exit(0)

    # MIN MAX AVG LOGIC USING LIBRARY FUNCTIONS

    print(f"Highest : {max(temps):.2f}")
    print(f"Lowest : {min(temps):.2f}")
    print(f"Average : {sum(temps) / len(temps):.2f}")

    # MIN MAX AVG LOGIC WITHOUT LIBRARY FUNCTIONS
    
    """
    temps_sum = max_temp = min_temp = temps[0]
    for i in range(1, len(temps)):
        if temps[i] > max_temp:
            max_temp = temps[i]
        if temps[i] < min_temp:
            min_temp = temps[i]
        temps_sum += temps[i]
    print(f"Highest : {max_temp:.2f}")
    print(f"Lowest : {min_temp:.2f}")
    print(f"Average : {temps_sum / len(temps):.2f}")
    
    """


else:
    print("Please enter at least 2 values!")