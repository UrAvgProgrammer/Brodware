from wand.image import Image as wi
from PIL import Image as pi
import os
import fitz

img_folder = r"D:\Work\Brodware\img_folder\\"
imgs = r"D:\Work\Brodware\img\\"

def pdftoImage():
	for root, dirs, files in os.walk(r"D:\Work\Brodware\pdf\\"):
		for file in files:
			# pdf = wi(filename = r"D:\Work\Brodware\pdf\\" + file, resolution = 61)
			pdf = wi(filename = r"D:\Work\Brodware\pdf\\" + file, resolution = 150)
			pdfImage = pdf.convert("jpeg")
			pdfImage.compression_quality = 99
			for img in pdfImage.sequence:
				page = wi(image = img)
				file = file.replace('.pdf', '')
				page.save(filename = img_folder + file + ".jpg")

def image_cropper():
	for root, dirs, files in os.walk(r"D:\Work\Brodware\img_folder\\"):
		for file in files:
			img = pi.open(img_folder + file)
			area = (0, 170, 2480, 3000)
			cropped_image = img.crop(area)
			cropped_image.save(imgs + file, "JPEG", quality=80, optimize=True, progressive=True)

# def ex_img():
# 	doc = fitz.open("1.6700.00.2.XX.pdf")
# 	for i in range(len(doc)):
# 		for img in doc.getPageImageList(i):
# 			xref = img[0]
# 			pix = fitz.Pixmap(doc, xref)
# 			if pix.n < 5:       # this is GRAY or RGB
# 				pix.writePNG("p%s-%s.png" % (i, xref))
# 			else:               # CMYK: convert to RGB first
# 				pix1 = fitz.Pixmap(fitz.csRGB, pix)
# 				pix1.writePNG("p%s-%s.png" % (i, xref))
# 				pix1 = None
# 			pix = None

def resizer():
	new_width = 1000
	new_height = 1000
	for root, dirs, files in os.walk(r"D:\Work\Brodware\img\\"):
		for file in files:
			img = pi.open(imgs + file)
			# w, h = img.size
			w = (new_width)
			# w = (new_width/float(w))
			h = (new_height)
			# h = (new_height/float(h))
			img = img.convert('RGB')
			img = img.resize((w, h), pi.LANCZOS)
			img.save(imgs + file, "JPEG", quality=80, optimize=True, progressive=True)

def pdfresizer():
	new_width = 2481
	new_height = 3508
	for root, dirs, files in os.walk(r"D:\Work\Brodware\img_folder\\"):
		for file in files:
			img = pi.open(img_folder + file)
			# w, h = img.size
			w = (new_width)
			# w = (new_width/float(w))
			h = (new_height)
			# h = (new_height/float(h))
			img = img.convert('RGB')
			img = img.resize((w, h), pi.LANCZOS)
			img.save(img_folder + file, "JPEG", quality=80, optimize=True, progressive=True)



if __name__ == "__main__":
	# pdftoImage()
	# image_cropper()
	# pdfresizer()
	resizer()
