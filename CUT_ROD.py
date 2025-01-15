import time

def cut_rod_with_cuts(p, n):
    """Returns the maximum revenue and the cuts that achieve it."""
    if n == 0:
        return 0, []
    
    q = float('-inf')
    cuts = []
    
    for i in range(1, n + 1):
        sub_revenue, sub_cuts = cut_rod_with_cuts(p, n - i)
        current_revenue = p[i - 1] + sub_revenue
        if current_revenue > q:
            q = current_revenue
            cuts = [i] + sub_cuts  # Add the current cut to the list of cuts
    
    return q, cuts

if __name__ == "__main__":
    import sys
    
    # Measure time
    start_time = time.time()
    
    # Read input file
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        p = list(map(int, lines[1].strip().split()))
    
    # Calculate maximum revenue and cuts
    max_revenue, cuts = cut_rod_with_cuts(p, n)
    
    # Measure execution time
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Output results
    print(f"Maximum Revenue: {max_revenue}")
    print(f"Rod Cuts: {cuts}")
    print(f"Execution Time: {execution_time:.6f} seconds")
    print("Execution completed successfully.")