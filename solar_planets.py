import cv2

img = cv2.imread ("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
)

cv2.putText(img,
            "Venus",
            (125,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (180,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Jupiter",
            (560,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (760,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Uranus",
            (970,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Neptune",
            (1110,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imshow ("display",img)
cv2.waitKey(0)

