import pytesseract
from nltk.tokenize import sent_tokenize
import cv2

# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())

imagem1 = cv2.imread("imagem1.png")

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem1)
token = sent_tokenize(texto)
print(texto)



# import os
# import pytesseract
# import cv2

# # Carrega a imagem
# imagem = cv2.imread("IMG_20230503_093527918.jpg")

# # Define o caminho completo onde o arquivo PDF será salvo
# caminho_pdf = os.path.join(os.getcwd(), "output.pdf")

# caminho = r"C:\Program Files\Tesseract-OCR"
# pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
# # Converte a imagem em PDF
# pdf = pytesseract.image_to_pdf_or_hocr(imagem, extension='pdf')

# # Cria o arquivo PDF e escreve o conteúdo dentro dele
# with open(caminho_pdf, 'wb') as arquivo_pdf:
#     arquivo_pdf.write(bytearray(pdf))
    
# print("PDF salvo com sucesso!")