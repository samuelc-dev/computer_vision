import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

#ativar a webcam através do index, caso dê algum erro basta trocar o valor entre parênteses para 1,2,3...;
video = cv2.VideoCapture(0)

#resolução para a imagem da webcam
video.set(3,1280)
video.set(4,720)

#killboard
kb = Controller()

#configuração
detector = HandDetector(detectionCon=0.8)

#vetor dos dedinhos
estadoAtual = [0,0,0,0,0]

while True:
        _,img = video.read()
        hands, img = detector.findHands(img)

         # Ajeitar câmera como espelho caso esteja invertida
        img = cv2.flip(img, 1)

        if hands:
                estado = detector.fingersUp(hands[0])
                
                if estado!=estadoAtual and estado == [0,1,0,0,0]:
                        print('passar slide')
                        kb.press(Key.right)
                        kb.release(Key.right)

                if estado!=estadoAtual and estado == [0,1,1,0,0]:
                        print('voltar slide')
                        kb.press(Key.left)
                        kb.release(Key.left)

                estadoAtual = estado

        cv2.imshow('img',cv2.resize(img,(640,420)))
        cv2.waitKey(1)