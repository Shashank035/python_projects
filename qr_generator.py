import qrcode
import cv2
from pyzbar.pyzbar import decode

def generate_qr():
    """Generate a QR code from user input."""
    data = input("Enter text or URL to generate QR code: ")
    filename = "qrcode.png"

    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def scan_qr():
    """Scan a QR code from an image file or webcam."""
    choice = input("Scan QR from (1) Image or (2) Webcam? ")

    if choice == "1":
        image_path = input("Enter image file path: ")
        img = cv2.imread(image_path)
        decoded_objects = decode(img)
        for obj in decoded_objects:
            print("QR Code Data:", obj.data.decode("utf-8"))
            return
        print("No QR code found in the image.")

    elif choice == "2":
        print("Opening webcam for QR scanning. Press 'q' to exit.")
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                print("QR Code Data:", obj.data.decode("utf-8"))
                cap.release()
                cv2.destroyAllWindows()
                return
            cv2.imshow("QR Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Generate QR Code")
    print("2. Scan QR Code")
    
    option = input("Enter your choice (1 or 2): ")
    
    if option == "1":
        generate_qr()
    elif option == "2":
        scan_qr()
    else:
        print("Invalid option. Please choose 1 or 2.")
