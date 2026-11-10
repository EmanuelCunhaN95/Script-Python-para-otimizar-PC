import os
import shutil
import subprocess
import ctypes
import keyboard
import time

def is_admin():
    """Verifica se o script está sendo executado como Administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def limpar_temporarios():
    """Função que varre a pasta TEMP do Windows e apaga os arquivos."""
    print("\n--- Iniciando Limpeza de Temporários ---")
    
    # Pega o caminho da pasta Temp do usuário atual
    caminho_temp = os.environ.get('TEMP')
    
    if not caminho_temp:
        print("❌ Não foi possível localizar a pasta TEMP.")
        return

    print(f"Varrendo a pasta: {caminho_temp}")
    
    arquivos_apagados = 0
    erros = 0

    # os.walk navega por todas as subpastas dentro da TEMP
    for raiz, pastas, arquivos in os.walk(caminho_temp):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            try:
                os.remove(caminho_completo) # Tenta apagar o arquivo
                arquivos_apagados += 1
            except Exception:
                # Se o arquivo estiver em uso pelo Windows, ele cai aqui e ignoramos
                erros += 1 
                
    print(f"✅ Limpeza concluída!")
    print(f"🗑️ Arquivos removidos: {arquivos_apagados}")
    if erros > 0:
        print(f"⚠️ {erros} arquivos foram ignorados (provavelmente estavam em uso).")

def resetar_driver_video():
    """Reinicia o driver de vídeo simulando o atalho Win + Ctrl + Shift + B."""
    print("\n--- Resetando Driver de Vídeo ---")
    print("⚠️ A tela pode piscar por um segundo. Isso é normal.")
    
    try:
        print("Enviando comando de reinicialização...")
        
        # A função send() aperta e solta as teclas na ordem correta
        keyboard.send('windows+ctrl+shift+b')
        
        print("✅ Comando enviado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao tentar reiniciar o driver: {e}")

def verificar_sistema_sfc():
    
    print("\n--- Verificação de Arquivos do Sistema (SFC) ---")
    print("⚠️ Este processo pode levar de 5 a 15 minutos.")
    print("⚠️ Não feche esta janela. O Windows mostrará o progresso abaixo.")
    
    time.sleep(2)
    
    try:
        
        comando = ["sfc", "/scannow"]
        
        print("\nIniciando verificação...\n")
        
        subprocess.run(comando, check=True)
        
        print("\n✅ Processo concluído.")
        print("Verifique as mensagens acima para saber se o Windows encontrou algum erro.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Ocorreu um erro ao executar o SFC. Código do erro: {e}")
    except FileNotFoundError:
        print("\n❌ O comando SFC não foi encontrado. Isso não deveria acontecer no Windows.")

def exibir_menu():
    """Função que desenha o menu na tela."""
    print("\n" + "="*35)
    print("         Otimize seu pc com Link Ocean")
    print("="*35)
    print("1. Limpar arquivos temporários")
    print("2. Resetar driver de vídeo")
    print("3. Verificar e Reparar Sistema (SFC)")
    print("0. Sair")
    print("="*35)

# --- INÍCIO DO PROGRAMA ---
def main():
    # Checa admin logo na inicialização e avisa o usuário
    if not is_admin():
        print("\n⚠️ AVISO: Você não está rodando como Administrador.")
        print("Algumas funções (como o reset de vídeo) podem falhar.")

    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            confirmacao = input("Isso apagará arquivos temporários. Continuar? (s/n): ")
            if confirmacao.lower() == 's':
                limpar_temporarios()
            else:
                print("Operação cancelada.")
                
        elif opcao == '2':
            if not is_admin():
                print("❌ Você precisa abrir o VS Code como Administrador para usar esta função.")
                continue # Volta para o início do menu
                
            confirmacao = input("A tela vai piscar. Continuar? (s/n): ")
            if confirmacao.lower() == 's':
                resetar_driver_video()
            else:
                print("Operação cancelada.")

        elif opcao == '3':
            if not is_admin():
                print("❌ Você precisa abrir o VS Code como Administrador para usar esta função.")
                continue
                
            confirmacao = input("Isso pode demorar. Continuar? (s/n): ")
            if confirmacao.lower() == 's':
                verificar_sistema_sfc()
            else:
                print("Operação cancelada.")

        elif opcao == '0':
            print("Saindo do Programa... Até logo!")
            break
            
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()