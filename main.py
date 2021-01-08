import cv2
import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import os

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

cascade = cv2.CascadeClassifier("cascade/cascade.xml")
cascade2 = cv2.CascadeClassifier("p2_cascades/haarcascade_frontalface_default.xml")
cascade3 = cv2.CascadeClassifier("p2_cascades/haarcascade_eye.xml")

results = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}

def draw(c, f, color):
    rectangles = c.detectMultiScale(f)

    for r in rectangles:
        p1 = tuple(r[:-2])
        p2 = tuple([p1[0] + r[2], p1[1] + r[3]])

        f = cv2.rectangle(f, p1, p2, color, 2) 

    return f

def video():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        # frame = draw(cascade, frame, blue)
        frame = draw(cascade2, frame, green)
        frame = draw(cascade3, frame, red)

        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def eval(s, face, c):
    imgs = open(s).read().split("\n")

    for img in imgs:
        img = img.split(" ")[0]
        img = cv2.imread(img)

        rectangles = c.detectMultiScale(img, scaleFactor=1.01, minNeighbors=6)

        if len(rectangles) > 0 and face:
            results["TP"] += 1
        elif len(rectangles) == 0 and face:
            results["FP"] += 1
        elif len(rectangles) == 0 and not face:
            results["TN"] += 1
        elif len(rectangles) > 0 and not face:
            results["FN"] += 1


def evaluate(cascade):
    eval("test_pos.txt", face=True, c=cascade)
    eval("test_neg.txt", face=False, c=cascade)

    precision = results["TP"] / (results["TP"] + results["FP"]) 
    recall = results["TP"] / (results["TP"] + results["FN"]) # true positive rate
    fallout = results["FP"] / (results["FP"] + results["TN"]) # false positive rate
    f1 = (2 * precision * recall) / (precision + recall)

    print("Results:")
    print(results)

    print(f"Precision: [{precision}] Recall: [{recall}] Fallout: [{fallout}] F1-score: [{f1}]")

# evaluate(cascade)

video()

