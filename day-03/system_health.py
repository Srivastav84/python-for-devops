import psutil

# apko kamm karna hai ki user se CPU threshold lo
# current cpu usage pata karo
# agar cpu usage threshold se zyada hua , email kar do

# added ram details as well as beattery percentage

# 🧠 Simple Analogy

# CPU percent → How fast your brain is working right now ?

# Virtual memory → How full is your brain’s memory ?

def check_cpu_threshold():
    print("CPU_Usage :\n")
    if True:
        try : 
            cpu_threshold = float(input ("enter the cpu threshold:")) #done 1. ValueError
            current_cpu = psutil.cpu_percent(interval=1)
            if current_cpu> cpu_threshold :
               print (f"Current CPU usage : {current_cpu} ,  Since more than safe limits, a security protocol ALERT Email has been sent ....")
            else:
              print("CPU in Safe state ....")
            print("")
        except ValueError as e: 
             print(f"Please enter valid input, {e} . Please provide cpu_threshold in a numerical value.")

def get_RAM_details():
    print ("Ram_details :\n")
    ram = psutil.virtual_memory()
    for key, value in ram._asdict().items(): # here ram is a namedtuple so is converible into a dictionery and named values can be printed as key vale pairs.
        if key=="percent" :
            print(f"{key} : {value} %")
        else:
            print(f"{key} : {value / (1024**3):.2f} GB")
    print("")

def get_battery_percentage():
    print ("Battery_details :\n")
    battery = psutil.sensors_battery()
    for key, value in battery._asdict().items():
        if key=="percent" :
            print(f"{key} : {value} %")
        elif key=="secsleft" :
            print(f"remaining time : {value/(60*60)} hr")
        else:
            print(f"{key} : {value}")
    print("")
         
         
check_cpu_threshold()

# get_RAM_details()

# get_battery_percentage()
