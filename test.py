
data_file = "./codedata.txt"
print("Opening file: " + data_file)
csv = open(data_file, "w")
print("Writing hello")
csv.write("Hello")
print("Flusing file")
csv.flush()
print("Closing file")
csv.close()
print("Done")

