#Generator-based Log Reader

def read_logs():
    with open("log.txt", "r") as f:
        for line in f:
            yield line
count = {}
try:
    for log in read_logs():
        if "ERROR" in log:
            print(log.strip())
            count["ERROR"] = count.get("ERROR", 0) + 1
    print("Error count:", count)
except FileNotFoundError:
    print("Log file not found")
