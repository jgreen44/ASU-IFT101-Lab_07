import random

# =============================
# Part I: write to file

log_file = open("log.txt", "w")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("Writing File ...")
log_file.write("User_ID\tTime\tDate\tDay\n")
print("User_ID\tTime\tDate\tDay")
for i in range(0, 10):
    # convert i into a string
    uid = str(i)

    # generate a random week day
    day = days[int(random.random() * 7)]

    # generate a random time of the form hh:mm:ss
    # notice the "%02d" % that forces the integer
    # to be represented using two digits:
    # 1 ==> 01
    # 9 ==> 09
    # also notice the + here is a concatenation operator.
    # it concatenates all values into one long string.
    time = "%02d" % (int(random.random() * 24)) + ":" \
           + "%02d" % (int(random.random() * 60)) + ":" \
           + "%02d" % (int(random.random() * 60))

    # generate a random date of the form mm-dd-yyyy
    date = "%02d" % (int(random.random() * 12) + 1) + "-" \
           + "%02d" % (int(random.random() * 30) + 1) + "-" \
           + "%02d" % (int(random.random() * 4) + 2012)

    # set the file entry
    entry = uid + "\t" + time + "\t" + date + "\t" + day + "\n"

    # write the file entry
    log_file.write(entry)

    print(entry, end='')

log_file.close()
print("File Write Completed.")
print("Please open the file on disk.")
print("-----------------------------")

# =============================
# Part II: read from file
print("Reading File ...")
log_file = open("log.txt", "r")
header = log_file.readline()
for line in log_file:
    # remove the end of line character from the end of the line
    line = line.rstrip()
    # split all entries in the current line, based on the "\t" delimiter
    entries = line.split("\t")
    print("User", entries[0], "accessed the system on", entries[3], entries[2], "at", entries[1])

log_file.close()
print("File Read Completed.")
print("--------------------")
