import cv2
from kraken import binarization
from kraken import pageseg
from PIL import Image
from kraken.lib import models

input_image_path = './documento.jpg'
input_image = cv2.imread(input_image_path)

input_image = Image.fromarray(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)) 
input_image.save('test_test.jpeg')

bw_im = binarization.nlbin(input_image)



seg_result = pageseg.segment(bw_im
                            
                             )
segT = seg_result['boxes']

image = cv2.imread(input_image_path) 

for points in segT:
    (x, y, w, h) = points
    cv2.rectangle(image, (x, y), (w, y), (0, 0, 0), 2) 

cv2.imwrite("output_marked.png", image)

cv2.imshow("Output Marked Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
