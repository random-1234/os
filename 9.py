
def best_fit(memory_blocks, process_sizes):
    allocated_blocks = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if best_fit_index == -1 or memory_blocks[j] < memory_blocks[best_fit_index]:
                    best_fit_index = j

        if best_fit_index != -1:
            allocated_blocks[i] = best_fit_index
            memory_blocks[best_fit_index] -= process_sizes[i]

    return allocated_blocks

# Example usage:
memory_blocks_bf = [100, 500, 200, 300, 600]
process_sizes_bf = [212, 417, 112, 426]

allocated_blocks_bf = best_fit(memory_blocks_bf, page_size_bf, process_sizes_bf)
print("Best Fit Allocation:", allocated_blocks_bf)
