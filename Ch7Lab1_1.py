ROWS = 2
COLS = 7
def main():
    week_sales = [["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                  [0.0] * COLS]
    
    calculate_sales(week_sales)

def calculate_sales(sales_list):
    total_sales = 0
    avg_sales = 0
    size = len(sales_list[0])
    for c in range(COLS):
        print("Please enter sales for ", sales_list[0][c], ": ", sep='', end='') 
        sale_price = input()

        while not isValid(sale_price):
            print("Invalid sales value.")
            print("Please enter sales for ", sales_list[0][c], ": ", sep='', end='')
            sale_price = input()
        sales_list[1][c] = float(sale_price)
        total_sales += sales_list[1][c]
    avg_sales = total_sales / size
    print("Total sales: ", "$", format(total_sales, ".2f"), sep='')
    print("Average sales: ", "$", format(avg_sales, ".2f"), sep='')

def isValid(num):
        valid = True
        if not num.isdigit():
            valid = False
            return valid
        
        new_num = int(num)

        if new_num < 0:
            valid = False 
            return valid
        else:
            valid = True
            return valid
main()
