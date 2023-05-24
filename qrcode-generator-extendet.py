print("It's a trap")
import qrcode

def make_qr(filename, msg, colorBackground, colorVorground, resulution, border_size):
    file = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=resulution,
        border=border_size,
    )
    file.add_data(msg)
    file.make(fit=True)

    image = file.make_image(fill_color=colorVorground, back_color=colorBackground)

    image.save(filename)
    image.show()

def eingabe():
    filename = str(input("Dateiname: ") or "test") + ".png"
    msg = str(input("Inhalt des QR Codes: ") or "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    colorBackground = str(input("moegliche Farben sind:\nblue\ngreen\nyellow\norange\npink\nred\nwhite\nblack\npurple\ngrey \n\nHintergrundFarbe: ") or "white")
    colorVorground = str(input("Vordergrund: ") or "black")
    resulution = int(input("Bildaufloesung(Empfohlen: 80): ") or 80)
    border_size = int(input("Groesse des Randes(Empfohlen: 2): ") or 2)
    return filename, msg, colorBackground, colorVorground, resulution, border_size

def main():
    filename, msg, colorBackground, colorVorground, resulution, border_size = eingabe()
    make_qr(filename, msg, colorBackground, colorVorground, resulution, border_size)
    print("done")
    exit()

try:
    main()
except KeyboardInterrupt:
    exit()
except ValueError:
    exit()

