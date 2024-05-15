def round_robin_scheduling(at, bt, quantum, N):
    remaining_bt = bt[:]
    wt = [0]*N
    tat = [0]*N
    ft = [0]*N
    total_wt = 0
    total_tat = 0
    total_ft = 0
    time = 0

    while True:
        done = True
        for i in range(N):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > quantum:
                    time += quantum
                    remaining_bt[i] -= quantum
                else:
                    time += remaining_bt[i]
                    wt[i] = time - bt[i] - at[i]
                    remaining_bt[i] = 0
                    ft[i] = time

        if done:
            break

    for i in range(N):
        tat[i] = bt[i] + wt[i]

    total_wt = sum(wt)
    total_tat = sum(tat)
    total_ft = sum(ft)
    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N

    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tFinish Time")
    for i in range(N):
        print(i+1, "\t\t", at[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i], "\t\t", ft[i])
    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)
    print("Average finish time =", average_ft)

if __name__ == '__main__':
    N = 5
    at = [0, 1, 2, 3, 4]  # arrival time
    bt = [4, 3, 1, 2, 5]  # burst time
    quantum = 2  # time quantum

    print("\nRound Robin Scheduling:")
    round_robin_scheduling(at, bt, quantum, N)
