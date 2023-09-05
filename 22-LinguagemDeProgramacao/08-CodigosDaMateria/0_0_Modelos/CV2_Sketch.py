import cv2 as cv #Importando o Módulo Necessário = pip install opencv-python

imagem = cv.imread("E:/MDIR/1000201.jpg")
imagem_cinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
imagem_invertida = cv.bitwise_not(imagem_cinza)                          # Invertendo a Imagem
imagem_borrada = cv.GaussianBlur(imagem_invertida, (21, 21), 0)          # Imagem borrada
imagem_borrada_invertida = cv.bitwise_not(imagem_borrada)                # Invertendo a Imagem Borada
desenho = cv.divide(imagem_cinza, imagem_borrada_invertida, scale=256.0) # Convertendo a Imagem em Desenho
cv.imwrite("imagem.png", desenho)                                        # Gerando a Imagem e Salvando como imagem.png

