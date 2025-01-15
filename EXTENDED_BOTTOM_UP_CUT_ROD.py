import time

def extended_bottom_up_cut_rod(p, n):
    """Extended Bottom-Up Rod Cutting Algorithm"""
    r = [0] * (n + 1)  # Revenue for each rod length
    s = [0] * (n + 1)  # Sizes where cuts are made
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    """Prints the sizes of cuts and the maximum revenue."""
    r, s = extended_bottom_up_cut_rod(p, n)
    cuts = []
    while n > 0:
        cuts.append(s[n])
        n -= s[n]
    return cuts, r[-1]  # Return cuts and the maximum revenue

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  # Rod length
        p = list(map(int, lines[1].strip().split()))  # Prices for each length

    # Measure execution time
    start_time = time.time()
    cuts, max_revenue = print_cut_rod_solution(p, n)
    end_time = time.time()

    # Output results
    print("Cut sizes that maximize revenue:", cuts)
    print("Maximum Revenue:", max_revenue)
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print("Execution completed successfully.")