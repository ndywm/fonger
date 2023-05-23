import cv2
import os
import numpy as np

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

Y1=100
Y2=200
X1=50
X2=150
ALPHA=1.5
BETA=75


def addFingerprint(owner):
    ret, frame = cap.read()
    frame=np.uint8(cv2.add(cv2.multiply(np.float32(frame[Y1:Y2,X1:X2]),np.array([ALPHA])),BETA))
    filename=None
    if ret:
        filename=f"./data/{owner}_{hash(frame.tobytes())}.bmp"
        cv2.imwrite(filename, frame)
    else:
        raise Exception()
    return filename



THRESHOLD=0

def findOwner():
    ret, sample=cap.read()
    if not ret:
        raise Exception()
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
            if p.distance<0.1*q.distance:
                matchPoints.append(p)
        keypoints=min([len(keypoints_1),len(keypoints_2)])
        score=len(matchPoints)/keypoints*100
        if score>bestScore:
            bestScore=score
            bestMatch=file
    if bestScore>=THRESHOLD:
        if bestMatch is None:
            return None
        return bestMatch.split('_')[0]
    else:
        return None
