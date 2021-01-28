import os
import cv2

pos = open("test_pos.txt").read().split("\n")
neg = open("test_neg.txt").read().split("\n")

new_pos = []
new_neg = []

for subdir, dirs, files in os.walk("neg"):
    for file in files:
        new_file = subdir + os.sep + file
        if new_file in neg:
            new_neg.append(new_file)

new_neg = new_neg[:int(len(new_neg)/2)]

for file in os.listdir("pos"):
    new_file = f"pos\\{file} 1 0 0 64 64"
    if new_file in pos:
        new_pos.append(new_file)

new_pos = new_pos[:int(len(new_pos)/2)]

for n in new_neg:
    img = cv2.imread(n)
    n = n.split(f"\\")
    cv2.imwrite(f"test_neg/{n[len(n)-1]}", img)

for p in new_pos:
    p = p.split(" ")[0]
    img = cv2.imread(p)
    p = p.split(f"\\")
    cv2.imwrite(f"test_pos/{p[len(p)-1]}", img)


with open("new_test_neg.txt", "w") as f:
    for n in new_neg:
        f.write(f"{n}\n")

with open("new_test_pos.txt", "w") as f:
    for p in new_pos:
        f.write(f"{p}\n")