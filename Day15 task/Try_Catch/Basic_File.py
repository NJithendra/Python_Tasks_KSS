#Basic File Logger

try:
    with open("log.txt", "a") as f:
        while True:
            log = input("Enter user action (stop to exit): ")
            if log.lower() == "stop":
                break
            f.write(log + "\n")
    print("Logs saved successfully")
except IOError:
    print("File error occurred")
