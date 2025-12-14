"""
Solution Pt. 2 
TODO: Adding counters for each time dial crosses over at 0.
"""
file = open("ex.txt")
list = []

for line in file:
    list.append(line)
    print(line)

dial_min = 0
dial_max = 99
dial_current = 50
count_dial_at_0 = 0


for line in list:
    if line[0] == "L":
        print("rotating left")
        dial_current = dial_current - int(line[1:])
        count = 0
        while dial_current < 0:
            dial_current = dial_current + 100
            if count >= 0:
                count_dial_at_0 = count_dial_at_0 + 1
            count = count + 1
            print(dial_current)
    if line[0] == "R":
        print("rotating right")
        dial_current = dial_current + int(line[1:])
        count = 0
        while dial_current > 99:
            dial_current = dial_current - 100
            if count >= 0:
                count_dial_at_0 = count_dial_at_0 + 1
            count = count + 1
            print(dial_current)

print(count_dial_at_0)

# def main():

# if __name__ == "__main__":
    # main()
