
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1]))  # Sort processes based on burst time
    completion_time = 0
    turnaround_time_sum = 0
    waiting_time_sum = 0

    for process in processes:
        id, burst_time = process

        # Calculate waiting time
        waiting_time = max(0, completion_time)

        # Calculate completion time
        completion_time += burst_time

        # Calculate turnaround time
        turnaround_time = waiting_time + burst_time

        # Update sums for average calculation
        turnaround_time_sum += turnaround_time
        waiting_time_sum += waiting_time

        # Print information for each process
        print(f"Process {id}| Burst Time: {burst_time} | Waiting Time: {waiting_time} | Turnaround Time: {turnaround_time}")

    # Calculate and print average waiting time and turnaround time
    avg_waiting_time = waiting_time_sum / len(processes)
    avg_turnaround_time = turnaround_time_sum / len(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

processes = [
        (1, 6),
        (2, 8),
        (3, 7),
        (4, 3)
    ]

sjf_scheduling(processes)

