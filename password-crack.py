password = input("giv password: ")
crack = ""
count = 0

def cracker(size, attempt= ""):
    global count
    if size == 0:
        print(attempt)
        if attempt== password:
            crack= attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            cracker(size - 1, newTry)

for i in range(1, 99):
    cracker(i)
