import os
import json
import pdb


def read_logs():
#    print("Current directory:", os.getcwd())
   base_dir = os.path.dirname(os.path.abspath(__file__))
   file_path = os.path.join(base_dir, "app.log")
   

#option 1
#    file= open("app.log", "r") # file open
#    print (file.readlines()) # file operation
#    file.close() #close

#option 2
    
   with open (file_path, "r") as file:
         lines=file.readlines()
         return lines
#       json.dump(app.log, "w",)

   

def write_logs_summary():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path2 = os.path.join(base_dir, f"logs_output.json")
    with open(file_path2, "w") as file2:
       file2.write("_______app.log Summary______\n\n")
       json.dump(counts, file2, indent=4)
    print(f"\n✅ Data successfully saved to logs_output.json\n")

         

def log_analyze(lines):
    log_count = {
        "ERROR": 0,
        "INFO": 0,
        "WARNING": 0
    }

    for line in lines:
        if "ERROR" in line:
            log_count["ERROR"] += 1
        elif "WARNING" in line:
            log_count["WARNING"] += 1
        elif "INFO" in line:
            log_count["INFO"] += 1

        
        else : pass

    return log_count
lines=read_logs()
counts=log_analyze(lines)
    
print("log counts are : ", counts)
write_logs_summary()

