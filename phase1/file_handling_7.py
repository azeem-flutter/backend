import os

data_file = os.path.join(os.path.dirname(__file__), "data.txt")

file = open(data_file, "r", encoding="utf-8")
content = file.read()
print(content)
file.close()
# if you forget to close the file, it can lead to memory leaks and other issues.

with open(data_file, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# using 'with' statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
# write in the file using r+ (read and write without truncating existing data)
with open(data_file, "r+", encoding="utf-8") as file:
    file.seek(0, 2)
    content = file.write("\nHello, World!")
    print(content)
