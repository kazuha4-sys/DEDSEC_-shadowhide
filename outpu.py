from stegano import lsb

# Caminho da imagem com a mensagem oculta
output_path = "c:/xampp/htdocs/DEDSEC/Dedsec-(ShadowHide/output_image.png"

# Extrair a mensagem
extracted_message = lsb.reveal(output_path)

print(f"Mensagem extraída: {extracted_message}")
