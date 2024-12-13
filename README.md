![logo](/assets/imagem/codigo-binario.png)


# 🕵️‍♂️ ShadowHide 🔒


---

**ShadowHide** é uma ferramenta de esteganografia que permite ocultar mensagens dentro de imagens, utilizando a técnica de LSB (Least Significant Bit) para esconder dados sem alterar visivelmente a imagem original.

---

## 📋 Requisitos

- Python 3.x
- Biblioteca `stegano` (para manipulação de esteganografia)
  - Instalar via pip:

    ```bash
    pip install stegano
    ```

    - Instalar via requirements:

        ```bash
        pip install -r requirements.txt
        ```

---

## 🔥 Funcionalidades

1. **💬 Ocultar uma mensagem em uma imagem**  
   A ferramenta permite ocultar uma mensagem em uma imagem. A imagem resultante pode ser compartilhada normalmente, sem que a mensagem oculta seja percebida.

2. **🔎 Extrair a mensagem oculta**  
   A ferramenta também permite extrair a mensagem oculta de uma imagem que foi modificada.

---

## 🚀 Como usar

### 1. 🌟 Ocultar a mensagem

Esse código oculta a mensagem em uma imagem e gera uma nova imagem com a mensagem embutida.

```python
from stegano import lsb

# Mensagem a ser oculta
message = "A DEDSEC esta revelando a verdade."
image_path = "perfil.jpg"
output_path = "output_image.png"

# Ocultar mensagem
secret_image = lsb.hide(image_path, message)
secret_image.save(output_path)

# Exibir imagem com a mensagem oculta
print(f"Imagem com mensagem oculta salva em: {output_path}")

```


### Parâmetros

* `message`: A mensagem que será oculta na imagem.

* `image_path`: O caminho da imagem original(deve ser um arquivo de imagem válido).

* `output_path`: O caminho de saída onde a imagem com a mensagem oculta será salva.

### 2. 🧩 Extrair a mensagem

```python
from stegano import lsb

#caminho da imagem com a mensagem oculta
output_path = "output_image.png"


# Extrair a mensagem
extracted_message = lsb.reveal(output_path)

print(f"Mensagem extraída: {extracted_message}")
```

### Parâmetros

* `output_path`: O caminho da imagem que contém a mesagem oculta.

O código exibirá a mensagem estraída, caso a imagem que contém a mensagem oculta.

---

## 🧑‍💻 Exemplo de Uso

1. Para ocultar uma mensagem em uma imagem:

    ```bash
    python ocultar_mensagem.py
    ```

2. Para extrair a mensagem da imagem modificada:

    ```bash
    python extrair_mensagem.py
    ```

---

# AVISO 

*A Dedsec está revelando a verdade, faça dela oque quiser. Porem não seremos responsaveis pelos seus atos.*