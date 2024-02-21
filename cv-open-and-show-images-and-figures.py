import cv2 as cv

# Abrir uma imagem chamada bolachas.png
img = cv.imread('./assets/bolachas.png')

# Criar uma cópia da imagem e desenhar algumas figuras
# geométricas em cima
img_copy = img.copy()
cv.rectangle(img_copy, (150, 100), (400, 220), (0, 255, 0), 2)
cv.circle(img_copy, (220, 280), 50, (0, 0, 255), 2)
cv.line(img_copy, (400, 400), (500, 500), (255, 0, 0), 2)

# Mostrar as duas imagens lado a lado
cv.imshow('Original', img)
cv.imshow('Com figuras', img_copy)
# Ajustas as janelas para que fiquem lado a lado
cv.moveWindow('Original', 0, 0)
cv.moveWindow('Com figuras', img.shape[1]+80, 0)

# Aplicar um filtro de detecção de bordas na primeira
# imagem e mostrar o resultado
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_edges = cv.Canny(img_gray, 100, 200)
cv.imshow('Bordas', img_edges)
cv.moveWindow('Bordas', 0, img.shape[0]+120)

# fecha as janelas ao pressionar qualquer tecla
cv.waitKey(0)
cv.destroyAllWindows()









