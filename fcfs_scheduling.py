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

if __name__ == '__main__':
    N = 5
    at = [0, 1, 2, 3, 4]  # arrival time
    bt = [4, 3, 1, 2, 5]  # burst time

    print("\nFCFS Scheduling:")
    fcfs_scheduling(at, bt, N)
