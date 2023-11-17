import qrcode

def generate_qr_code(data, file_name='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_name)

if __name__ == "__main__":
    url_data = "https://catabolic-neuron.github.io/BlendAndTrend/index.html"
    generate_qr_code(url_data, file_name='example_qrcode.png')
    print("QR code generated successfully.")
