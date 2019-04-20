ROWS = 2
COLS = 12
def main():
    monthlyrain = [["January","February","March","April","May","June","July","August","September","October","November","December"],
                  [0.0] * COLS]
    
    calculate_rain(monthlyrain)

def calculate_rain(rain_list):
    total_rain = 0
    avg_rain = 0
    min_rain = 0
    max_rain = 0
    size = len(rain_list[0])
    for c in range(COLS):
        print("Please enter the rainfall for ", rain_list[0][c], ": ", sep='', end='') 
        rain_amount = input()

        while not isValid(rain_amount):
            print("Invalid rainfall value.")
            print("Please enter the rainfall for ", rain_list[0][c], ": ", sep='', end='')
            rain_amount = input()
        rain_list[1][c] = float(rain_amount)
        total_rain += rain_list[1][c]
    avg_rain = total_rain / size
    min_rain = min(rain_list[1])
    max_rain = max(rain_list[1])
    min_location = rain_list[1].index(min_rain)
    max_location = rain_list[1].index(max_rain)
    print("Total rainfall: ", format(total_rain, ".2f"), sep='')
    print("Average rainfall: ", format(avg_rain, ".2f"), sep='')
    print("Minimum rainfall: ", format(min_rain, ".2f"),  " in the month of ", rain_list[0][min_location], sep='')
    print("Maximum rainfall: ", format(max_rain, ".2f"),  " in the month of ", rain_list[0][max_location], sep='')

def isValid(num):
    try:
        num = float(num)
        if num > 0:
            return True
    except ValueError:
        return False
    
main()
