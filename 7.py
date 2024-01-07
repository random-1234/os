
class BankersAlgorithm:
    def __init__(self, allocation, max_claim, available):
        self.allocation = allocation
        self.max_claim = max_claim
        self.available = available
        self.n_processes = len(allocation)
        self.n_resources = len(available)

    def is_safe_state(self, process, work, finish):
        for i in range(self.n_resources):
            if self.max_claim[process][i] - self.allocation[process][i] > work[i]:
                return False
        return True

    def execute(self):
        work = self.available[:]
        finish = [False] * self.n_processes
        safe_sequence = []

        while True:
            found = False
            for i in range(self.n_processes):
                if not finish[i] and self.is_safe_state(i, work, finish):
                    for j in range(self.n_resources):
                        work[j] += self.allocation[i][j]
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

    banker = BankersAlgorithm(allocation_matrix, max_claim_matrix, available_resources)
    banker.execute()
