import tabula

# Extrair tabelas de uma imagem
df = tabula.read_pdf('output.pdf', pages='all')[0]
# salva a tabela como um arquivo Excel
df.to_excel("arquivo.xlsx", index=False)