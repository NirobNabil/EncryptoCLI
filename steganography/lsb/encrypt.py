from stegano import lsb


def encrypt_text(input_image_path, secret, output_dir="./"):
    encrypted = lsb.hide(input_image_path, secret)
    encrypted.save( output_dir + "encrypto.png")

