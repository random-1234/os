
def first_fit(pages, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(pages)):
            if pages[j] >= processes[i]:
                allocation[i] = j
                pages[j] -= processes[i]
                break

    print_allocation("First Fit", allocation, processes)

def print_allocation(technique, allocation, processes):
    print(f"\n{technique} Memory Allocation:")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i+1} -> Page {allocation[i]+1}")
        else:
            print(f"Process {i+1} -> Not Allocated")

# Example usage:
if __name__ == "__main__":
    pages = [100, 200, 300, 400, 500]
    processes = [212, 417, 112, 426]

    first_fit(pages, processes)
