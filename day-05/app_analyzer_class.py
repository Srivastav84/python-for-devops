import os
import json
import pdb

class log_analyze :
    def __init__(self,log_file):
        self.log_file=log_file

    def read_logs(self):
          self.base_dir = os.path.dirname(os.path.abspath(__file__))
          self.file_path = os.path.join(self.base_dir, self.log_file)
   
          with open (self.file_path, "r") as file:
            return file.readlines()

    def log_analyze(self):
      self.log_count = {
         "ERROR": 0,
         "INFO": 0,
         "WARNING": 0
        }
      lines=self.read_logs()

      for line in lines:
          if "ERROR" in line:
            self.log_count["ERROR"] += 1
          elif "WARNING" in line:
            self.log_count["WARNING"] += 1
          elif "INFO" in line:
            self.log_count["INFO"] += 1

      else : pass

      return self.log_count
    
    def write_logs_summary(self):
      self.base_dir = os.path.dirname(os.path.abspath(__file__))
      self.file_path2 = os.path.join(self.base_dir, f"{self.log_file}_output.json")
      with open(self.file_path2, "w") as file2:
          json.dump(self.log_count, file2, indent=4)
      print(f"\n✅ Data successfully saved to {self.log_file}_output.json\n")

def main():
    analyzer = log_analyze("app.log")

    analyzer.read_logs()          # Step 1: read file
    counts = analyzer.log_analyze()  # Step 2: analyze
    analyzer.write_logs_summary() # Step 3: save result

    print("Log Summary:")
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    main()