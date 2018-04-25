ROWS = 2
COLS = 7

def main():
    week_sales = [["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                  [0.0,0.0,0.0,0.0,0.0,0.0,0.0]]

    filename = ask_sales(week_sales)
    sales_price = ask_sales_again()

    if filename.upper() != "QUIT":
        readContents(filename)

def ask_sales_again():
    new_sale = float(input("Invalid sales value.\n"))
    return new_sale

def ask_sales(sales_list):
    total = 0
    for c in range(COLS):
        print("Please enter sales for", sales_list[0][c], ":")
        sales_list[1][c] = float(input())
        if sales_list[1][c] < 0:
            ask_sales_again()
        else:
            total += sales_list[1][c]
    # need to add input validation in here
    return sales_list

def file_exists(filename):
    try:
        file = open(filename)
        file.close()
    except FileNotFoundError:
        file_ok = False
    else:
        file_ok = True
        
    return file_ok

def readContents(filename):
    file = open(filename, 'r')
    count = 0
    totalSum = 0
    # count amount of lines extracted from file
    line = file.readline()
    if line == '':
        print("File", filename, "is empty.")
        return
    else:
        while line != '':
            file_info = float(line)
            totalSum += file_info
            count += 1
            
            line = file.readline()

    average = totalSum / count
    print("Total:", format(totalSum, "2.3f"))
    print("Average:", format(average, "2.3f"))
    file.close()
    
main()
