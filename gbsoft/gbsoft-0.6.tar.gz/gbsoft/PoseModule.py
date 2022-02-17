import cv2
import mediapipe as mp
import time
import math

class PoseDetector():

    def __init__(self,mode=False, upBody = False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upperBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        #self.pose = self.mpPose.Pose(self.mode,self.upperBody,self.smooth,self.detectionCon,self.trackCon)
        self.pose = self.mpPose.Pose()

    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img
    def findPosition(self,img,draw=True):
        self.lmlist = []
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                #print(id, lm)
                cx,cy = int(lm.x*w), int(lm.y*h)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
        return self.lmlist
    def findAngle(self,img,p1,p2,p3,draw=True):
        #Get the Landmarks
        x1,y1 = self.lmlist[p1][1:]
        x2,y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]
        # calculate Angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2))

        if angle < 0:
            angle += 360
        #print(angle)
        # Draw
        if draw:
            cv2.line(img,(x1, y1),(x2, y2),(255,0,0),3)
            cv2.line(img, (x2, y2), (x3, y3), (255, 0, 0), 3)
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img,str(round(angle,2)),(x2-50,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        return angle

def main():
    cap = cv2.VideoCapture(1)
    pTime = 0
    detector = PoseDetector()
    while True:
        ret, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.findPosition(img,draw=True)
        if lmlist:
            print(lmlist[14])
            cx,cy = lmlist[14][1],lmlist[14][2]
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            cv2.putText(img, 'cx=' + str(cx) + " cy=" + str(cy), (800, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cTime = time.time()
        fps = int(1 / (cTime - pTime))
        pTime = cTime
        print(fps)
        cv2.putText(img, "Fps = " + str(fps), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow('Frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
