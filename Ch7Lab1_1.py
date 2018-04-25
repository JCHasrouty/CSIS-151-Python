ROWS = 2
COLS = 7
def main():
    week_sales = [["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                  [0.0] * COLS]
    
    calculate_sales(week_sales)


    
def calculate_sales(sales_list):
    for c in range(COLS):
        print("Please enter sales for ", sales_list[0][c], ": ", sep='', end='') 
        sale_price = float(input())
        if isValid(sale_price):
            sales_list[1][c] = sale_price
        else:
            sale_price = ask_sale_again()
def isValid(num):
        try:
            if num < 0:
                print("Invalid sales value.\n")
                return False
        except ValueError:
            print("Invalid sales value. Not a number\n")
            return False
        else:
            return True

def ask_sale_again():
    sale_price = float(input("Invalid sales value.\n"))
    return sale_price

main()
