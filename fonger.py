import cv2
import os
import numpy as np

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("brak kamery!")

Y1=100
Y2=200
X1=50
X2=150
ALPHA=1.5
BETA=75

def getCurrentFrame():
    ret, frame = cap.read()
    if ret:
        return np.uint8(cv2.add(cv2.multiply(np.float32(frame[Y1:Y2,X1:X2]),np.array([ALPHA])),BETA))
    else:
        return None


def addFingerprint(owner):
    frame=getCurrentFrame()
    if frame is None:
        return None
    filename=f"./data/{owner}_{hash(frame.tobytes())}.bmp"
    cv2.imwrite(filename, frame)
    return filename



THRESHOLD=0
SENSITIVITY=0.3

def findOwner(path):
    if path is None:
        sample=getCurrentFrame()
        if sample is None:
            raise OSError()
    else:
        sample=cv2.imread(path)
        if sample is None or sample.size == 0:
            raise FileNotFoundError()
    bestScore=0
    bestMatch=None
    for file in os.listdir("./data"):
        fingerprint=cv2.imread(f"./data/{file}")
        sift=cv2.SIFT_create()
        keypoints_1,descriptors_1=sift.detectAndCompute(sample,None)
        keypoints_2,descriptors_2=sift.detectAndCompute(fingerprint,None)
        matches=cv2.FlannBasedMatcher({"algorithm":1,"trees":10},{}).knnMatch(descriptors_1,descriptors_2,k=2)
        matchPoints=[]
        for p,q in matches:
            #print(p.distance,q.distance)
            if p.distance<SENSITIVITY*q.distance:
                matchPoints.append(p)
        keypoints=min([len(keypoints_1),len(keypoints_2)])
        score=len(matchPoints)/keypoints*100
        #print(score)
        if score>bestScore:
            bestScore=score
            bestMatch=file
    if bestScore>=THRESHOLD:
        if bestMatch is None:
            return (None,None)
        return (bestMatch.split('_')[0],bestScore)
    else:
        return (None,None)
