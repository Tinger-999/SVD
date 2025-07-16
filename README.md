# SVD

這是一個使用 Python 搭配 NumPy 與 OpenCV ，並透過奇異值分解（SVD），在保留圖像的主要特徵的條件下，對圖像進行壓縮。

---

## 專案功能說明

- 讀取圖像檔（JPEG / PNG）
- 使用 NumPy 套件進行對 R、G、B 三通道做 SVD 分解
- 使用前 k 個奇異值來重建圖像（壓縮效果）
- 顯示原圖與壓縮後圖像的比較
- 使用 OpenCV cv2.imshow() 及 cv2.imwrite() 顯示與儲存結果

---

## 執行環境

- Python 3.x
- OpenCV (cv2)
- NumPy

### 安裝方式（建議使用虛擬環境）

```bash
pip install numpy opencv-python
SVD
