def priority_scheduling(processes):
    # Sort processes based on priority; if priorities are the same, sort by burst time
    processes.sort(key=lambda x: (x[0], x[1]))

    completion_time = 0
    turnaround_time_sum = 0
    waiting_time_sum = 0

    for process in processes:
        burst_time, priority = process

        # Waiting time is the completion time of the last process
        waiting_time = max(0, completion_time)

        # Calculate completion time
        completion_time += burst_time

        # Calculate turnaround time
        turnaround_time = waiting_time + burst_time

        # Update sums for average calculation
        turnaround_time_sum += turnaround_time
        waiting_time_sum += waiting_time

        # Print information for each process
        print(f"Process | Burst Time: {burst_time} | Priority: {priority} | Waiting Time: {waiting_time} | Turnaround Time: {turnaround_time}")

    # Calculate and print average waiting time and turnaround time
    avg_waiting_time = waiting_time_sum / len(processes)
    avg_turnaround_time = turnaround_time_sum / len(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Example usage
if __name__ == "__main__":
    processes = [
        (6, 2),  # (Burst Time, Priority)
        (8, 1),
        (7, 3),
        (3, 4)
    ]

    priority_scheduling(processes)
