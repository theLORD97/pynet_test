f = open("file.txt")

for line in f:
    print(line.strip())

#### WRITE ####
print("\nWriting file.")
f = open("new_file.txt", "w")
f.write('Leon is 2nd best\n')
f.close()

#### APPEND ####
print("\nAppending file.")
with open("new_file.txt", "a") as f:
    f.write('Oilers rule\n')

print ("Script Completed")

