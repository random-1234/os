import os

def main():
    print("Main process ID:", os.getpid())

    # Fork the process
    child_pid = os.fork()

    if child_pid == 0:
        # This code will be executed by the child process
        print("Child process ID:", os.getpid())
        print("Parent process ID:", os.getppid())

        # The child process exits with status 0
        os._exit(0)
    else:
        # This code will be executed by the parent process
        print("Parent process ID:", os.getpid())

        # Wait for the child process to complete
        _, status = os.waitpid(child_pid, 0)
        print(f"Child process {child_pid} exited with status {status >> 8}")

if __name__ == "__main__":
    main()
