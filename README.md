# Picture ID

Creates a picture ID to the French norms:  
3.5cm by 4.5cm with the face occupying about 74% of the picture.

Import a jpg picture, and launch the script:  
`python photo.py originalImage.jpg finalImage.jpg`  
Click on the chin, then the top of the forehead, then the middle of the eyes.

The script crops the picture, and adjusts the dpi so the printed size will be exactly 3.5x4.5cm
If the -t option is give, tiles the cropped image on a 4x6 inch postcard, which can then be printed anywhere.

Note that if you print the 4x6 postcard, make sure you print as-is, with no margins, no cropping.

Requires numpy, imageio, matplotlib.
`pip install numpy imageio matplotlib`

_____________________________

# Photo d'Identité
Crée une photo d'identité aux normes Françaises
3.5cm par 4.5cm, le visage occupant environ 74% de l'image.

Choisissez une image originale au format jpeg par exemple et lancez le script:  
`python photo.py imageOriginale.jpg imageFinale.jpg`

Vous cliquez sur le bas du menton, puis sur le haut de front, puis exactement entre les yeux.
L'utilitaire réduit l'image en fonction des normes Française, et adjuste le paramètre dot-per-inch pour qu'après impression, la taille soit exactement 3.5x4.5 cm.

Si l'option `-t` est ajoutée, l'image est répliquée sur une photo de taille 4x6 pouces.
Lors de l'impression, ne faites aucune modification à l'image (pas de changement de taille ou d'ajout de bordure).

Nécessite l'installation de numpy, imageio, matplotlib
`pip install numpy imageio matplotlib`
