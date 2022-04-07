
import pytesseract
import cv2




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



img = cv2.imread(r'C:\Users\Pc\Desktop\vsCodes\2021_3e_wa_s2_trousil\python_intro\py_tess\test2.jpg')
result = img.copy()
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_thresh = cv2.threshold(img_grey,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30,1))
detect_horizontal = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(img_thresh, [c], -1, (0,0,0), cv2.FILLED)

vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,30))
detect_vertical = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(img_thresh, [c], -1, (0,0,0), cv2.FILLED)
    



cv2.imshow("treti",img_thresh)
cv2.imshow("result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()


data = pytesseract.image_to_string(img_thresh, lang='ces')
print(data)

