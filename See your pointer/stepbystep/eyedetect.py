
import cv2
import mediapipe as mp
import os

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=2)

for im in (os.listdir(r'stepbystep\DATA')):
    try:
        a = f"stepbystep\\DATA\\{im}"
        image = cv2.imread(a)
        height, width, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_image)

        landmarks = [22,23,24,25,26,27,28,29,30,252,253,254,255,256,257,258,259,260,261]

        for facial_landmarks in result.multi_face_landmarks:
            for i in landmarks:
                pt1 = facial_landmarks.landmark[i]
                x = int(pt1.x * width)
                y = int(pt1.y * height)
                cv2.circle(image, (x, y), 5, (100, 100, 0), -1)
        cv2.imwrite(f'stepbystep\\tempdata\\{im}',image)
        print(im)
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
    except:
        print("error..")
   