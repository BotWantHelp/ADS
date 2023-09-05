# Esse codigo transforma qualquer pdf na pasta em arquivos MP3
# Para funcionar execute no terminal pip install PyPDF2 pyttsx3
import os
import PyPDF2
import pyttsx3

files_in_directory = os.listdir()
pdf_files = [file for file in files_in_directory if file.endswith(".pdf")]
output_dir = "Arquivos MP3"
os.makedirs(output_dir, exist_ok=True)
engine = pyttsx3.init()
for pdf_filename in pdf_files:
    with open(pdf_filename, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        for start_page in range(0, num_pages, 10):
            end_page = min(start_page + 10, num_pages)
            text = ""
            for page_num in range(start_page, end_page):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            mp3_filename = os.path.join(output_dir, 
                f"{pdf_filename}_parte_{start_page + 1}-{end_page}.mp3")
            engine.save_to_file(text, mp3_filename)
            print(f"Criado o arquivo {mp3_filename}")            
            engine.runAndWait()
print("Concluído!")

