import time
import csv

with open('rows_300.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    data = ['№', 'Секунда', 'Микросекунда']
    writer.writerow(data)
    for i in range(1,301):
        TimeNow = time.time()
        sec = int(TimeNow)
        microsec = int((TimeNow - sec) * 10000000)
        writer.writerow([i, sec, microsec])
        time.sleep(0.01)

with open('rows_300.csv') as file:
    print(file.read())