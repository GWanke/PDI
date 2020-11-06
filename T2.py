import numpy as np
import cv2 as ocv

faces = { 
	1: (255,0,0),         #vermelho(contrario=ciano)
	2: (0,255,0),         #verde(contrario=magenta)
	3: (0,0,255),         #azul(contrario=amarelo)
	4: (255,255,0),       #amarelo 
	5: (255,0,255),       #magenta 
	6: (0,255,255),       #ciano
}

def readInput():
	face = int(input("Entre com uma face para o cubo(valor entre 1 a 6): "))
	while face <1 or face>6:
		print("Face invalida. Por favor, entre com um valor de 1 a 6.")
		face = int(input())
	ind = int(input("Entre com uma fatia para o corte no cubo(valor entre 0 a 255) :"))
	while ind <0 or ind>255:		
		print("Face invalida. Por favor, entre com um valor de 0 a 255.")
		ind = int(input())
	return face,ind


def geraFace(face,index):
	#colore uma face,apenas.
	absIndex=abs(index-255)
	if face == 1:
		MatFace = np.array([[(red,green,index) for green in range(0,256)] for red in range(0,256)],np.uint8)
	elif face == 2:
		MatFace = np.array([[(blue,index,red) for red in range(0,256)] for blue in range(0,256)],np.uint8)
	elif face == 3:
		MatFace = np.array([[(index,green,blue) for green in range(0,256)] for blue in range(0,256)],np.uint8)
	elif face == 4:
		MatFace = np.array([[(absIndex,green,blue) for green in range(0,256)] for blue in range(0,256)],np.uint8)
	elif face == 5:
		MatFace = np.array([[(blue,absIndex,red) for red in range(0,256)] for blue in range(0,256)],np.uint8)
	elif face == 6:
		MatFace = np.array([[(red,green,absIndex) for green in range(0,256)] for red in range(0,256)],np.uint8)
	return MatFace


def main():
	face,index=readInput()
	img = geraFace(face,index)
	ocv.imshow('Cubo cortado',img)
	ocv.waitKey(0)
	ocv.destroyAllWindows()
if __name__ == '__main__':
    main()