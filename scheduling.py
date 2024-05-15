def fcfs_scheduling(at, bt, N):
    wt = [0]*N
    tat = [0]*N
    ft = [0]*N
    wt[0] = 0
    
    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tFinish Time")
    print("1\t\t" , at[0] , "\t\t" , bt[0] , "\t\t" , wt[0], "\t\t" , bt[0], "\t\t" , bt[0])

    total_wt = 0
    total_tat = bt[0]
    total_ft = bt[0]

    for i in range(1, N):
        wt[i] = (ft[i - 1] - at[i]) if (ft[i - 1] > at[i]) else 0
        tat[i] = wt[i] + bt[i]
        ft[i] = at[i] + tat[i]
        total_wt += wt[i]
        total_tat += tat[i]
        total_ft += ft[i]
        print(i + 1 , "\t\t" , at[i] , "\t\t" , bt[i] , "\t\t" , wt[i], "\t\t" , tat[i], "\t\t" , ft[i])

    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N
    print("Average waiting time = " , average_wt)
    print("Average turnaround time = " , average_tat)
    print("Average finish time = " , average_ft)

def sjf_preemptive_scheduling(at, bt, N):
    processes = []
    for i in range(N):
        processes.append((i+1, at[i], bt[i]))
    processes.sort(key=lambda x: x[1])

    wt = [0]*N
    tat = [0]*N
    ft = [0]*N
    remaining_bt = bt[:]
    total_bt = sum(bt)
    time = 0

    while time < total_bt:
        min_bt = float('inf')
        next_process = -1
        for i in range(N):
            if at[i] <= time and remaining_bt[i] < min_bt and remaining_bt[i] > 0:
                min_bt = remaining_bt[i]
                next_process = i
        if next_process == -1:
            time += 1
            continue
        remaining_bt[next_process] -= 1
        time += 1
        if remaining_bt[next_process] == 0:
            wt[next_process] = time - at[next_process] - bt[next_process]
            tat[next_process] = wt[next_process] + bt[next_process]
            ft[next_process] = time

    total_wt = sum(wt)
    total_tat = sum(tat)
    total_ft = sum(ft)
    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N

    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tFinish Time")
    for i in range(N):
        print(processes[i][0], "\t\t", processes[i][1], "\t\t", processes[i][2], "\t\t", wt[i], "\t\t", tat[i], "\t\t", ft[i])
    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)
    print("Average finish time =", average_ft)

def sjf_non_preemptive_scheduling(at, bt, N):
    processes = []
    for i in range(N):
        processes.append((i+1, at[i], bt[i]))
    processes.sort(key=lambda x: x[1])

    wt = [0]*N
    tat = [0]*N
    ft = [0]*N

    wt[0] = 0
    for i in range(1, N):
        wt[i] = wt[i - 1] + processes[i - 1][2]

    for i in range(N):
        tat[i] = wt[i] + processes[i][2]
        ft[i] = at[i] + tat[i]

    total_wt = sum(wt)
    total_tat = sum(tat)
    total_ft = sum(ft)
    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N

    print("P.No.\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tFinish Time")
    for i in range(N):
        print(processes[i][0], "\t\t", processes[i][1], "\t\t", processes[i][2], "\t\t", wt[i], "\t\t", tat[i], "\t\t", ft[i])
    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)
    print("Average finish time =", average_ft)



def priority_scheduling(at, bt, priority, N):
    processes = []
    for i in range(N):
        processes.append((i+1, at[i], bt[i], priority[i]))
    processes.sort(key=lambda x: x[3])

    wt = [0]*N
    tat = [0]*N
    ft = [0]*N

    wt[0] = 0
    for i in range(1, N):
        wt[i] = wt[i - 1] + processes[i - 1][2]

    for i in range(N):
        tat[i] = wt[i] + processes[i][2]
        ft[i] = at[i] + tat[i]

    total_wt = sum(wt)
    total_tat = sum(tat)
    total_ft = sum(ft)
    average_wt = total_wt / N
    average_tat = total_tat / N
    average_ft = total_ft / N

    print("P.No.\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time\tFinish Time")
    for i in range(N):
        print(processes[i][0], "\t\t", processes[i][1], "\t\t", processes[i][2], "\t\t", processes[i][3], "\t\t", wt[i], "\t\t", tat[i], "\t\t", ft[i])
    print("Average waiting time =", average_wt)
    print("Average turnaround time =", average_tat)
    print("Average finish time =", average_ft)

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
    priority = [2, 1, 3, 4, 5]  # priority
    quantum = 2  # time quantum

    print("\nFCFS Scheduling:")
    fcfs_scheduling(at, bt, N)

    print("\nSJF Scheduling (Preemptive):")
    sjf_preemptive_scheduling(at, bt, N)

    print("\nSJF Scheduling (Non-Preemptive):")
    sjf_non_preemptive_scheduling(at, bt, N)

    print("\nPriority Scheduling:")
    priority_scheduling(at, bt, priority, N)

    print("\nRound Robin Scheduling:")
    round_robin_scheduling(at, bt, quantum, N)
