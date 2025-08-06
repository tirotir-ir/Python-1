#pip install pyscreenshot
#pip install pillow

import pyscreenshot 

image = pyscreenshot.grab(bbox=(10, 10, 500, 500)) 

image.show() 

image.save("tirotir.png") 
