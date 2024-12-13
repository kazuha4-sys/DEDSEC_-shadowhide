from stegano import lsb

# Mensagem a ser oculta
message = "A DEDSEC esta revelando a verdade."
image_path = "perfil.jpg"
output_path = "output_image.png"

# Ocultar mensagem
secret_image = lsb.hide(image_path, message)
secret_image.save(output_path)

# Extrair a mensagem
extracted_message = lsb.reveal(output_path)

print(f"Mensagem extraída: {extracted_message}")
