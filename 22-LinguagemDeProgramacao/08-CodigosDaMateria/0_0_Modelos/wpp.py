import pywhatkit as kit
import openpyxl
import datetime
import pyautogui
import time
import locale
import keyboard
import os

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def enviar_mensagem_whatsapp(numero, mensagem):
    kit.sendwhatmsg_instantly(numero, mensagem) 

# Obtém o caminho completo para o arquivo "dados.xlsx" na mesma pasta que o script
caminho_arquivo_excel = os.path.join(os.path.dirname(__file__), 'dados.xlsx')

wb = openpyxl.load_workbook(caminho_arquivo_excel)
planilha = wb.active

try:
    for row in planilha.iter_rows(min_row=2, values_only=True):
        nome = row[0]
        numero = "+55" + row[1]
        vencimento = row[2]
        chave_pix = row[3]
        mes_atual = datetime.datetime.now().strftime('%B - %Y')
        mes_atual_ptbr = datetime.datetime.now().strftime('%B de %Y')
        favorecido = row[4]
        
        if vencimento == "0" or vencimento == 0:
            pyautogui.hotkey("ctrl", "w")
            print(f"Pulando {nome} porque não possui data de vencimento")
        else:
            mensagem_personalizada = f'Bom dia {nome}, seu boleto de: {vencimento}, por gentileza, nos envie o comprovante de pagamento feito com a Chave Pix: {chave_pix}\n\n[ ( Mês de {mes_atual_ptbr} ) ]\n\nFavorecido: {favorecido}'
            pyautogui.press("esc")
            enviar_mensagem_whatsapp(numero, mensagem_personalizada)
            time.sleep(2)
            pyautogui.hotkey("ctrl", "w")
            print(f"Mensagem Enviada com sucesso para: {nome}")
        
        if keyboard.is_pressed('q'):
            print("Encerramento manual detectado, parando scripts...")
            break
except Exception as e:
    
    
    print(f'Algo estranho aconteceu: {e}')
finally:
    wb.close()
