# Recognize faces in images and identify who they are
import face_recognition

known_pic = face_recognition.load_image_file("known_pictures/nicole.jpg")
print ("what is the face_encoding: ", face_recognition.face_encodings(known_pic))
known_face_encoding = face_recognition.face_encodings(known_pic)[0]

unknown_pic = face_recognition.load_image_file("unknown_pictures/unknown1.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_pic)[0]
res = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

if res[0] == True:
    print ("obama")
else:
    print ("This picture is unrecognized! Please try it again!")
