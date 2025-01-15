import time

def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)  # This array will store the optimal first cut for each rod length
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i  # Store the first cut at rod length j
        r[j] = q
    return r[n], s  # Return the maximum revenue and the cuts array

def print_cut_rod_solution(s, n):
    cuts = []
    while n > 0:
        cuts.append(s[n])  # Get the next cut
        n -= s[n]  # Reduce the remaining rod length
    return cuts

if __name__ == "__main__":
    # Read input file
    import sys
    filename = sys.argv[1]

    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        p = list(map(int, lines[1].strip().split()))

    # Measure the execution time
    start_time = time.time()
    max_revenue, s = bottom_up_cut_rod(p, n)
    end_time = time.time()

    # Print the results
    cuts = print_cut_rod_solution(s, n)
    execution_time = end_time - start_time

    print(f"Maximum Revenue: {max_revenue}")
    print(f"Cuts: {cuts}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print("Execution completed successfully.")