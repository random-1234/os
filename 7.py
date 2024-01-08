def bankers_algorithm(allocation, max_claim, available):
    n_processes = len(allocation)
    n_resources = len(available)

    def is_safe_state(process, work, finish):
        for i in range(n_resources):
            if max_claim[process][i] - allocation[process][i] > work[i]:
                return False
        return True

    work = available[:]
    finish = [False] * n_processes
    safe_sequence = []

    while True:
        found = False
        for i in range(n_processes):
            if not finish[i] and is_safe_state(i, work, finish):
                for j in range(n_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        if not found:
            break

    if all(finish):
        print("Safe Sequence:", safe_sequence)
    else:
        print("Unsafe state. System is in deadlock.")

if __name__ == "__main__":
    allocation_matrix = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    max_claim_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    available_resources = [3, 3, 2]

    bankers_algorithm(allocation_matrix, max_claim_matrix, available_resources)
