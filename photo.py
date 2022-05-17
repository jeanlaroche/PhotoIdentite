from imageio import imread,imwrite
from matplotlib import pyplot as pl
import numpy as np

# Normes Francaise pour les photos d'dentite.
hauteurCm = 4.5
largeurCm = 3.5
# Le visage doit occuper environ 74% de l'image, du bas du menton au haut du front.
visageRatio = 0.74


cmParInch = 2.54

def doit(args):
    mentonY = None
    frontY = None
    centreXPix = None
    def on_click(event):
        nonlocal mentonY,frontY,centreXPix
        if mentonY is None:
            mentonY = int(event.ydata)
            print("Maintenant clickez sur le haut du front")
        elif frontY is None:
            frontY = int(event.ydata)
            print("Maintenant clickez exactement entre les yeux")
        else:
            centreXPix = int(event.xdata)

    imageOrig = imread(args.ImageOriginale)
    pl.connect('button_press_event', on_click)
    while 1:
        pl.imshow(imageOrig)
        pl.axis('off')
        print("Clickez sur le bas du menton")
        while frontY is None or mentonY is None or centreXPix is None:
            pl.pause(.1)

        # Calcul de la hauteur de l'image, proportionelle a la hauteur du visage.
        hauteurVisagePix = (abs(frontY-mentonY))
        hauteurImagePix = int(round(hauteurVisagePix / visageRatio))
        # La largeur de l'image est proportionelle a sa hauteur
        largeurImagePix = int(round(hauteurImagePix / hauteurCm * largeurCm))
        # Le haut de l'image correspond a y = 0!
        basYPix = max(mentonY,frontY) + (hauteurImagePix-hauteurVisagePix)//2
        gaucheXPix = centreXPix - largeurImagePix//2
        # Extraction de l'image
        imageModifiee = imageOrig[basYPix-hauteurImagePix:basYPix,gaucheXPix:gaucheXPix+largeurImagePix]
        pl.imshow(imageModifiee)
        pl.pause(.1)
        break
        # if input('La photo est bonne? -> [o/n]') == 'o': break
        # print("OK on recommence")
    # Pixels par inch.
    dpi_f = largeurImagePix/largeurCm*cmParInch
    dpi = int(round(dpi_f))
    
    if args.repliquer:
        # Cree une image en replicant imageModifiee autant de fois possible dans une image de taille
        # largeurInch hauteurInch
        largeurInch = 4
        hauteurInch = 6
        X = int(round(largeurInch*dpi_f))
        Y = int(round(hauteurInch*dpi_f))
        C = 255*np.ones((Y,X,imageModifiee.shape[2])).astype(np.uint8)
        margePix = 10
        coordX,coordY = (margePix,margePix)
        while 1:
            while 1:
                C[coordY:coordY+hauteurImagePix,coordX:coordX+largeurImagePix,] = imageModifiee
                coordX += largeurImagePix + margePix
                if coordX + largeurImagePix > X:
                    coordX = margePix
                    break
            coordY += hauteurImagePix + margePix
            if coordY + hauteurImagePix > Y: break
        pl.imshow(C)
        pl.pause(.1)
        imageModifiee=C

    imwrite(args.ImageFinale,imageModifiee,dpi=[dpi,dpi])
    print(f"Image sauvee sur {args.ImageFinale}")

if __name__ == '__main__':
    import argparse
    desc='''Cree un photo d'identitee aux normes francaises. 3.5 cm par 4.5 cm, le visage occupant 74% de l'image'''
    parser = argparse.ArgumentParser('photo', description=desc)
    parser.add_argument('ImageOriginale', help='Image originale')
    parser.add_argument('ImageFinale', help='Image finale')
    parser.add_argument('-t', dest='repliquer', action='store_true', help = 'Repliquer l\'image au format 6x4')
    args = parser.parse_args()

    doit(args)