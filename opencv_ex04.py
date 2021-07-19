import cv2
import numpy as np

org = cv2.imread('./image/iu.jpeg')
dst = cv2.resize(org, dsize=(640, 480))

cv2.imshow("origin", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()