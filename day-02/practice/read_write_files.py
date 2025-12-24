file_path = r"C:\Users\great\OneDrive\Desktop\Tutedude\python-for-devops\day-02\practice\demo.txt"

with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nHello Dosto, kya haal chaal")
    # print(file.read())