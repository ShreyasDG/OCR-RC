# OCR-RC
BMSCE Hackathon 
The Debug Thugs

Email IDs :

Rajeev : rajeevbhat27@gmail.com
Rohit : rohit.b.r1998@gmail.com
Shreyas : shreyas19971121@gmail.com
Sumanth : vsk21098@gmail.com



text_recogition.py
  - What the text_recogition.py does is that it searches for text in the image wherever it occurs. It does so by doing a pixel by pixel search across the whole image and putting a textbox around the text wherever it occurs in the image. Then this textbox co-ordinates are sent to the tesseract api which then processes the image(partial image whose coordinates are specified) sent to it and gives the corresponding text as the output.

Dependancies : 

-Tesseract
-Open-CV
-Python
-Numpy
-pytesseract
-imutils






