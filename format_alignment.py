col1 = 10
col2 = 50
col3 = 12
col32 = 2
# 50s is spacing for strings
# 10d is for numbers
# sep = "   " to separate by 3 spaces
# col1 = "10s" - could use this 
print(format("ID", "10s"), format("Name", "50s"), format("Salary", "10s"), sep="   ")
print("-" * 10, "-" * 50, "-" * 10, sep="   ")
print(format(100, "10d"), format("Michael Jackson", "50s"), format(500.45, "10.2f"), sep="   ")
print(format(200345, "10d"), format("Wesley So", "50s"), format(600000.01, "10.2f"), sep="   ")
print(format(5, "10d"), format("A very long line that we dont know right now", "50s"), format(1.10, "10.2f"), sep="   ")
