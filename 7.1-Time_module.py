import time

# Pauses the program for 3 seconds, then prints "Time's Up"
time.sleep(3)
print("Time's Up")

my_time = int(input("Enter the time in second :"))

# Will count up from 0 to the number the user entered, one per second
for x in range(0, my_time + 1):
    print(x)
    time.sleep(1)
print("Ok Ok") 

# Reserve cout down
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

# Will count down again, but this time showing it in MM:SS format
for x in range(my_time, 0, -1):
    seconds = x % 60  # Gets the remaining seconds
    minutes = int(x / 60) % 60  # Gets the remaining minutes
    print(f"00:{minutes:02}:{seconds:02}")  # Displays in 00:MM:SS format
    time.sleep(1)
