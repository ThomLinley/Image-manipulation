from PIL import Image
import webbrowser

path = str("C://Users//Thomas//Dropbox//Python_working_drive//")
img1 = Image.open(str(path + "IMG_0001.JPG"))
angle = 45
size = 100, 100

#rotate counterclockwise 'angle' deg
img2 = img1.rotate(angle, expand = 1)

#save
img2.save(str(path + 'test.jpg'))

#view
webbrowser.open(str(path + 'test.jpg'))
