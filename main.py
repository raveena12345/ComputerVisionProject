import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap=cv2.VideoCapture(0)

while(True):
    key, img=cap.read()

    # Convert color format
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            for point in landmarks.landmark:
                x, y = int(point.x * img.shape[1]), int(point.y * img.shape[0])
                cv2.circle(img, (x, y), 1, (0, 255, 0), -1)

    cv2.imshow("my_video", img)
    cv2.waitKey(1)

