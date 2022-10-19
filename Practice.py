age_classes_file='data/age_classes.txt'
print(age_classes_file, "======================")
with open(age_classes_file, "r") as f:
    for i in range(20):
        print(i, "\t", repr(f.readline()))