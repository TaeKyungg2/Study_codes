from deepface import DeepFace
import cv2

img = cv2.imread(r"'/Users/Taery/Study_Codes/2025_07_~15/Images/화면 캡처 2025-07-11 135600.png'")  # ← 사진 파일명으로 바꿔줘!

result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
print(result)

for face in result:
    x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
    emotion = max(face['emotion'], key=face['emotion'].get)
    cv2.putText(img, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

cv2.imshow("Emotion Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
