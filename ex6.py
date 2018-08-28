img=np.zeros((512,512,3),np.uint8)
pts=np.array([[10,50],[400,50],[90,200],[50,500]],np.int32)

cv2.imshow("original image",img)
cv2.polylines(img,[pts],True,(0,255,0),10)
cv2.imshow("polygon",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
