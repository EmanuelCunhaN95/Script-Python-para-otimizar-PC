# 🧹 Otimizador de Windows

O algoritmo é uma ferramenta de automação simples , desenvolvida em Python, para realizar tarefas de limpeza e manutenção no sistema Windows. O projeto foca em uma interface de linha de comando (CLI) amigável, permitindo que usuários executem comandos complexos do sistema de forma fácil e segura.

## ✨ Funcionalidades

O projeto conta com as seguintes opções no menu:
1. **Limpar arquivos temporários:** Remove o "lixo" da pasta TEMP do Windows, liberando espaço em disco.
2. **Resetar driver de vídeo:** Simula o atalho `Win + Ctrl + Shift + B` para reiniciar a placa de vídeo sem causar instabilidade.
3. **Verificar e Reparar Sistema (SFC):** Roda o clássico `sfc /scannow` para encontrar e corrigir arquivos corrompidos do sistema.
4. **Reparo da Imagem do Sistema (DISM):** Executa a ferramenta DISM para reparar a base de componentes do Windows.
5. **Esvaziar Lixeira:** Esvazia permanentemente os arquivos deletados da lixeira.

## 🛠️ Tecnologias Utilizadas

*   **Python 3:** Linguagem base do projeto.
*   **Bibliotecas Padrão:** `os`, `shutil`, `subprocess`, `ctypes` (nativas do Python, não precisam de instalação).
*   **Biblioteca Externa:** `keyboard` (usada para simular o atalho de teclado do driver de vídeo).
*   **Comandos Nativos do Windows:** PowerShell e Prompt de Comando.

* NOTA: usar o VsCode como administrador para usar maior parte das funções.