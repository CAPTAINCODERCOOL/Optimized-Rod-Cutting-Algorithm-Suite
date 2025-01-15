import sys
import subprocess
import time
import matplotlib.pyplot as plt


def measure_time_and_output(command):
    """Measures the execution time of a command and captures its output."""
    start = time.time()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    end = time.time()
    return end - start, result.stdout.strip()


def read_input_file(file_path):
    """Reads the input file to extract rod length and prices."""
    with open(file_path, "r") as file:
        lines = file.readlines()
        rod_length = int(lines[0].strip())
        prices = list(map(int, lines[1].strip().split()))
    return rod_length, prices


def execute_and_display(command):
    """Executes a script and displays its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())
    print(f"Execution completed successfully for {command}")


if __name__ == "__main__":
    # Check if a command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python comp_analysis.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Take the input file from the command-line argument

    # Step 1: Execute and display outputs of standalone scripts
    print("Executing standalone scripts...")
    execute_and_display(f"python CUT_ROD.py {input_file}")
    execute_and_display(f"python BOTTOM_UP_CUT_ROD.py {input_file}")
    execute_and_display(f"python EXTENDED_BOTTOM_UP_CUT_ROD.py {input_file}")

    # Step 2: Read input file for analysis
    rod_length, prices = read_input_file(input_file)

    # Initialize parameters
    n_values = []
    times_cut_rod = []
    times_bottom_up = []
    times_extended_bottom_up = []
    time_differences = []
    time_difference = 0
    current_rod_length = 1  # Start with a rod length of 1
    cuts = None
    max_revenue = None

    while True:  # Use an infinite loop with a break condition
        # Generate temporary input file with the current rod length
        with open("temp_input.txt", "w") as temp_file:
            temp_file.write(f"{current_rod_length}\n")
            temp_file.write(" ".join(map(str, prices[:current_rod_length])))

        # Measure execution times for each algorithm and capture outputs
        time_cut_rod, cut_rod_output = measure_time_and_output(f"python CUT_ROD.py temp_input.txt")
        time_bottom_up, bottom_up_output = measure_time_and_output(f"python BOTTOM_UP_CUT_ROD.py temp_input.txt")
        time_extended_bottom_up, extended_bottom_up_output = measure_time_and_output(
            f"python EXTENDED_BOTTOM_UP_CUT_ROD.py temp_input.txt"
        )

        # Extract cuts and revenue from the output of EXTENDED_BOTTOM_UP_CUT_ROD
        extended_bottom_up_output_lines = extended_bottom_up_output.split("\n")
        if len(extended_bottom_up_output_lines) >= 2:  # Ensure there are enough lines in the output
            cuts = extended_bottom_up_output_lines[0].strip()  # Assuming the first line gives cuts
            max_revenue = extended_bottom_up_output_lines[1].strip()  # Assuming the second line gives max revenue
        else:
            cuts = "N/A"
            max_revenue = "N/A"

        # Debug prints
        print(f"Current Rod Length: {current_rod_length}, Time Difference: {time_difference}")
        print(f"Debug: Cuts - {cuts}, Max Revenue - {max_revenue}")

        # Record the results
        n_values.append(current_rod_length)
        times_cut_rod.append(time_cut_rod)
        times_bottom_up.append(time_bottom_up)
        times_extended_bottom_up.append(time_extended_bottom_up)

        # Calculate time difference between CUT_ROD and BOTTOM_UP_CUT_ROD
        time_difference = abs(time_cut_rod - time_bottom_up)
        time_differences.append(time_difference)

        # Break the loop if the time difference exceeds 60 seconds
        if time_difference > 60:
            print(f"Time difference between CUT_ROD and BOTTOM_UP_CUT_ROD exceeded 60 seconds at rod length {current_rod_length}.")
            print(f"Cuts: {cuts}")
            print(f"Maximum Revenue: {max_revenue}")
            break

        # Increment rod length for the next iteration
        current_rod_length += 1

        # Dynamically extend prices for larger rod lengths
        if current_rod_length > len(prices):
            prices.append(prices[-1] + 100)  # Add a large increment for new prices

    # Plot the performance comparison graph (CUT_ROD, BOTTOM_UP_CUT_ROD, EXTENDED_BOTTOM_UP_CUT_ROD)
    plt.figure()
    plt.plot(n_values, times_cut_rod, label='CUT_ROD')
    plt.plot(n_values, times_bottom_up, label='BOTTOM_UP_CUT_ROD')
    plt.plot(n_values, times_extended_bottom_up, label='EXTENDED_BOTTOM_UP_CUT_ROD', linestyle='-.')  # Dashed-dotted line
    plt.xlabel('Rod Length')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time of Rod Cutting Algorithms')
    plt.legend()
    plt.savefig('execution_comparison_all_algorithms.png')
    plt.show()

    # Plot the time difference graph
    plt.figure()
    plt.plot(n_values, time_differences, label='Time Difference (CUT_ROD - BOTTOM_UP_CUT_ROD)', color='red')
    plt.axhline(y=60, color='blue', linestyle='--', label='60-second threshold')
    plt.xlabel('Rod Length')
    plt.ylabel('Time Difference (s)')
    plt.title('Time Difference Between CUT_ROD and BOTTOM_UP_CUT_ROD')
    plt.legend()
    plt.savefig('time_difference_graph.png')
    plt.show()