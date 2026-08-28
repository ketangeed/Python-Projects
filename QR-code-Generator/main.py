# we are going to use python library like qrcode and convert url to qr..



"""import qrcode

img = qrcode.make("....enter the data....")

type(img)

img.save("qr_name.png")"""




import qrcode
url = input("Enter your URL : ")
img_file_name = input("Enter the name of the file : ")

img = qrcode.make(url)

type(img)

img.save(f"{img_file_name}.png")
