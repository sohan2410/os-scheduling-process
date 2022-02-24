from columnar import columnar


class FCFS:
    def processData(self, no_of_processes):
        process_data = []

        for i in range(no_of_processes):
            temporary = []

            arrival_time = int(input("Enter Arrival Time: "))

            burst_time = int(input(f"Enter Burst Time: "))

            temporary.extend([i, arrival_time, burst_time])
            process_data.append(temporary)

        FCFS.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        current_time = 0
        for i in range(len(process_data)):
            # if arrival time is greaten than current time
            if current_time < process_data[i][1]:
                current_time = process_data[i][1]
            start_time.append(current_time)
            current_time = current_time + process_data[i][2]
            end_time = current_time
            exit_time.append(end_time)
            process_data[i].append(end_time)

        turn_around_time = FCFS.calculateTurnaroundTime(self, process_data)
        waiting_time = FCFS.calculateWaitingTime(self, process_data)
        FCFS.printData(self, process_data, turn_around_time, waiting_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        headers = ['Process Id', 'Arrival Time', 'Burst Time',
                   'Completion Time', 'Turn Around Time', 'Waiting Time']

        table = columnar(process_data, headers)
        print(table)

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')


if __name__ == "__main__":

    no_of_processes = int(input("Enter number of processes: "))

    fcfs = FCFS()
    fcfs.processData(no_of_processes)
