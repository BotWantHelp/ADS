import win32com.client # pip install pywin32
import re
from PyPDF2 import PdfWriter

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 representa a pasta de entrada (inbox)
keywords = ['palavra-chave1', 'palavra-chave2']  # Adicione as palavras-chave desejadas
output_pdf = 'output.pdf'
pdf_writer = PdfWriter()

for message in inbox.Items:    # Encontre palavras-chave
    if message.UnRead:  # Verificar se o email está marcado como não lido
        if "Assunto desejado" in message.Subject:
            email_text = message.Body       
            found_keywords = [word for word in keywords if re.search(r'\b' + re.escape(word) + r'\b', email_text, re.IGNORECASE)]

            if found_keywords: # Encontra e copia as linhas contendo as palavras-chave        
                lines_with_keywords = []
                for line in email_text.split('\n'):
                    if any(re.search(r'\b' + re.escape(keyword) + r'\b', line, re.IGNORECASE) for keyword in found_keywords):
                        lines_with_keywords.append(line)

                if lines_with_keywords:
                    pdf_writer.add_page() # Adiciona as linhas ao PDF
                    pdf_writer.addBookmark('\n'.join(lines_with_keywords), pagenum=pdf_writer.page_number - 1)

with open(output_pdf, 'wb') as pdf_file:
    pdf_writer.write(pdf_file) # Salvar PDF

print(f'PDF salvo em: {output_pdf}')
