import cv2

img = cv2.imread("C:/Users/HP/OneDrive/Desktop/P-C-110/P-116/solar-system.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)  # White color

# Add text for each planet with its position
cv2.putText(img, "Mercury", (100, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Venus", (180, 90), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Earth", (280, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Mars", (380, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (490, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Saturn", (750, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Uranus", (950, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1100, 50), font, 0.7, color, 2, cv2.LINE_AA)
cv2.putText(img,"Sun",(30, 200),font,0.9,color,2,cv2.LINE_AA)

cv2.imshow("output",img)





cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg", img)
