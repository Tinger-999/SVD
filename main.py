import numpy as np
import cv2

scale = 0.5

img_org = cv2.imread('judagemeisi.jpg')
print('image shape is', img_org.shape)


def svd_compression(img, k):
    res_image = np.zeros_like(img)
    for i in range(img.shape[2]):
        U, Sigma, VT = np.linalg.svd(img[:, :, i])
        res_image[:, :, i] = U[:, :k].dot(np.diag(Sigma[:k])).dot(VT[:k, :])
    return res_image

res1 = svd_compression(img_org, k = 306)
res2 = svd_compression(img_org, k = 100)
res3 = svd_compression(img_org, k = 50)
res4 = svd_compression(img_org, k = 25)

row11 = np.hstack((res1, res2))
row22 = np.hstack((res3, res4))
res = np.vstack((row11, row22))

cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()



