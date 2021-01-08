import os
import random

pos = []
neg = []

# static path to current directory - for cmd purposes downstairs
static = r"C:/Users/andrew/Desktop/home/uni/ml"

# static path to opencv create_samples.exe - also for downstairs
opencv = r"D:/apps/opencv/build/x64/vc15/bin/opencv_createsamples.exe"

def split_and_write(L, s):
    random.shuffle(L)
    c = int(len(L) * 0.7)

    train = L[:c]
    test = L[c:]

    with open(f"{s}.txt", "w") as f:
        for e in train:
            f.write(e + "\n")
    
    with open(f"test_{s}.txt", "w") as f:
        for e in test:
            f.write(e + "\n")

def gen_neg():
    for subdir, dirs, files in os.walk("neg"):
        for file in files:
            path = subdir + os.sep + file
            neg.append(path)

    split_and_write(neg, "neg")

def gen_pos():
    for subdir, dirs, files in os.walk("pos"):
        for file in files:
            path = subdir + os.sep + file
            path.replace(r"\\", r"/")
            meta = " 1 0 0 64 64"
            pos.append(path + meta)
    
    split_and_write(pos, "pos")
    os.system(f"{opencv} -info {static}\pos.txt -w  24 -h 24 -num 14000 -vec {static}\pos.vec")


gen_pos()
gen_neg()    