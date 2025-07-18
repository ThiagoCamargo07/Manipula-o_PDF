from time import sleep
import pyautogui




Nome = input(str("Olá \nqual é seu nome ?")).strip()

resposta1 = "sim".strip().lower().upper()
senha_adm = [123,"%TGB7181*UHB"]

while True:
    if Nome == Nome:
        print(f"Olá {Nome}")
        pergunta1 = input(str("Deseja abrir este sistema ?"))
        if pergunta1 == resposta1:
            senha = input(int("Digite a senha de adiministrador:"))
            if senha in senha_adm:
                print("Acesso autorizado !!")
                sleep(1)
                print("Abrindo Manipulador de PDF`S...")
                sleep(1)
                print("*" * 20)
                sleep(1.3)
                
                print("*" * 10,"Relátorio de atividades", "*" * 10) 
                print("Opção 1: Gerar PDF.")
                print("Opção 2: Mesclar PDF`S.")
                print("Opção 3: Transformar PDF`S em arquivo Word.")
                print("Opção 4: Criar cópia dd PDF")
                
                sleep(1.3)
                
                pergunta2 = input(str("Escolha uma opção para continuar"))
                
                if pergunta2 == "1":
                    Gerar_PDF() 
                    pass
                elif pergunta2 == "2":
                    Mesclar_PDFS()
                    pass
                elif pergunta2 == "3":
                    Transformar_PDF()
                    pass
                elif pergunta2 == "4":
                    Criar_cópia()
                    pass
                else:
                    print("Opção invalida, tente novamente. ")
                    sleep(0.3)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            else:
                print("Senha incorrete !!\nTente novamente.")
        else:
            print("Sistema interrompido.")
            break
    else:
        print("Nome não identificado !!\nPor favor tente novamente.")
            
            
            
        
    