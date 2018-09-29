import csv
import matplotlib.pyplot as plt
with open("filters1.tsv") as tsvfile:
    reader = csv.reader(tsvfile, delimiter="\t")

    for row in reader:
        f = row[0]
        u = row[1]
        p = row[2]
print(f,u)
# plt.plot(f,u)
# plt.show()
