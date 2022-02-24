from columnar import columnar


class PRIORITY:
    def processData(self, no_of_processes):
        process_data = []
        # process_data = [
        #     [0, 0, 8, 0, 3],
        #     [1, 1, 2, 0, 4],
        #     [2, 3, 4, 0, 4],
        #     [3, 4, 1, 0, 5],
        #     [4, 5, 6, 0, 2],
        #     [5, 6, 5, 0, 6],
        #     [6, 10, 1, 0, 1]
        # ]

        for i in range(no_of_processes):
            temporary = []

            arrival_time = int(input("Enter Arrival Time: "))

            burst_time = int(input(f"Enter Burst Time: "))

            priority = int(input("Priority: "))

            temporary.extend([i, arrival_time, burst_time, 0, priority])
            process_data.append(temporary)

        PRIORITY.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []

            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    temp.extend(
                        [process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend(
                        [process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][4]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3])
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
        t_time = PRIORITY.calculateTurnaroundTime(self, process_data)
        w_time = PRIORITY.calculateWaitingTime(self, process_data)
        PRIORITY.printData(self, process_data, t_time, w_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]

            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)

        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        headers = ['Process Id', 'Arrival Time', 'Burst Time', 'Completed', 'Priority',
                   'Completion Time', 'Turn Around Time', 'Waiting Time']

        table = columnar(process_data, headers)
        print(table)

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')


if __name__ == "__main__":

    no_of_processes = int(input("Enter number of processes: "))

    priority = PRIORITY()
    priority.processData(no_of_processes)
