print("It#s a trap")
import qrcode

def make_qr(filename, msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()

def eingabe():
    filename = str(input("Dateiname: "))
    filename = filename + ".png"
    msg = str(input("Inhalt des QR Codes: "))
    return filename, msg

def run():
    filename, msg = eingabe()
    make_qr(filename, msg)

run()
exit()

