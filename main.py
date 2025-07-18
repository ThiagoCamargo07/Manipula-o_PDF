import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import os
import time
from fpdf import FPDF
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from pdf2docx import Converter
import threading


# ---------------------- Funções principais ---------------------- #
def gerar_pdf_interface():
    limpar_tela()
    tb.Label(root, text="Digite o conteúdo do PDF:", font=("Segoe UI", 12)).pack(pady=10)
    caixa_texto = tk.Text(root, height=15)
    caixa_texto.pack(fill=BOTH, expand=True, pady=10)

    def salvar_pdf():
        texto = caixa_texto.get("1.0", tk.END).strip()
        if texto:
            caminho = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if caminho:
                time.sleep(0.3)
                progresso = tb.Progressbar(root, mode='indeterminate')
                progresso.pack(pady=10, fill='x')
                progresso.start()
                threading.Thread(target=lambda: gerar_pdf(texto, caminho, progresso)).start()

    def gerar_pdf(texto, caminho, progresso):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, texto)
        pdf.output(caminho)
        progresso.stop()
        progresso.destroy()
        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")

    tb.Button(root, text="Gerar PDF", bootstyle=DANGER, command=salvar_pdf).pack(pady=10)
    tb.Label(root, text="").pack(expand=True)
    tb.Button(root, text="Voltar ao menu", bootstyle=SECONDARY, command=tela_menu).pack(pady=5, side=BOTTOM)

def mesclar_pdfs_interface():
    limpar_tela()
    tb.Label(root, text="Mesclar dois arquivos PDF", font=("Segoe UI", 12)).pack(pady=15)

    arquivos_selecionados = []
    progresso = None

    def selecionar_pdf():
        nonlocal progresso
        if len(arquivos_selecionados) < 2:
            arquivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
            if arquivo:
                arquivos_selecionados.append(arquivo)
                tb.Label(root, text=f"Selecionado: {os.path.basename(arquivo)}").pack()
            if len(arquivos_selecionados) == 2:
                tb.Button(root, text="Mesclar PDFs", bootstyle=SUCCESS, command=mesclar).pack(pady=15)

    def mesclar():
        nonlocal progresso
        caminho = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if caminho:
            time.sleep(0.3)
            progresso = tb.Progressbar(root, mode='indeterminate')
            progresso.pack(pady=10, fill='x')
            progresso.start()
            threading.Thread(target=processar_mesclagem, args=(arquivos_selecionados, caminho, progresso)).start()

    def processar_mesclagem(arquivos, caminho, progresso):
        merger = PdfMerger()
        for arquivo in arquivos:
            merger.append(arquivo)
        merger.write(caminho)
        merger.close()
        progresso.stop()
        progresso.destroy()
        messagebox.showinfo("Sucesso", "PDFs mesclados com sucesso!")

    tb.Button(root, text="Selecionar primeiro PDF", bootstyle=INFO, command=selecionar_pdf).pack(pady=5)
    tb.Button(root, text="Selecionar segundo PDF", bootstyle=INFO, command=selecionar_pdf).pack(pady=5)
    tb.Label(root, text="").pack(expand=True)
    tb.Button(root, text="Voltar ao menu", bootstyle=SECONDARY, command=tela_menu).pack(pady=10, side=BOTTOM)

def pdf_para_word_interface():
    limpar_tela()
    tb.Label(root, text="Converter PDF para Word", font=("Segoe UI", 12)).pack(pady=15)

    progresso = None

    def converter():
        nonlocal progresso
        entrada = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if entrada:
            saida = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
            if saida:
                time.sleep(0.3)
                progresso = tb.Progressbar(root, mode='indeterminate')
                progresso.pack(pady=10, fill='x')
                progresso.start()
                threading.Thread(target=processar_conversao, args=(entrada, saida, progresso)).start()

    def processar_conversao(entrada, saida, progresso):
        cv = Converter(entrada)
        cv.convert(saida, start=0, end=None)
        cv.close()
        progresso.stop()
        progresso.destroy()
        messagebox.showinfo("Sucesso", "PDF convertido para Word com sucesso!")

    tb.Button(root, text="Selecionar PDF para converter", bootstyle=PRIMARY, command=converter).pack(pady=15)
    tb.Label(root, text="").pack(expand=True)
    tb.Button(root, text="Voltar ao menu", bootstyle=SECONDARY, command=tela_menu).pack(pady=10, side=BOTTOM)

def copiar_pdf_interface():
    limpar_tela()
    tb.Label(root, text="Copiar PDF", font=("Segoe UI", 12)).pack(pady=15)

    progresso = None

    def copiar():
        nonlocal progresso
        arquivo = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if arquivo:
            destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if destino:
                time.sleep(0.3)
                progresso = tb.Progressbar(root, mode='indeterminate')
                progresso.pack(pady=10, fill='x')
                progresso.start()
                threading.Thread(target=processar_copia, args=(arquivo, destino, progresso)).start()

    def processar_copia(origem, destino, progresso):
        reader = PdfReader(origem)
        writer = PdfWriter()
        for pagina in reader.pages:
            writer.add_page(pagina)
        with open(destino, "wb") as f:
            writer.write(f)
        progresso.stop()
        progresso.destroy()
        messagebox.showinfo("Sucesso", "Cópia criada com sucesso!")

    tb.Button(root, text="Selecionar PDF para copiar", bootstyle=WARNING, command=copiar).pack(pady=15)
    tb.Label(root, text="").pack(expand=True)
    tb.Button(root, text="Voltar ao menu", bootstyle=SECONDARY, command=tela_menu).pack(pady=10, side=BOTTOM)

# ---------------------- Telas e Navegação ---------------------- #
def tela_menu():
    limpar_tela()
    tb.Label(root, text="Menu Principal", font=("Segoe UI", 14)).pack(pady=10)
    tb.Button(root, text="1. Gerar PDF", bootstyle=SUCCESS, width=25, command=gerar_pdf_interface).pack(pady=5)
    tb.Button(root, text="2. Mesclar PDFs", bootstyle=INFO, width=25, command=mesclar_pdfs_interface).pack(pady=5)
    tb.Button(root, text="3. PDF para Word", bootstyle=PRIMARY, width=25, command=pdf_para_word_interface).pack(pady=5)
    tb.Button(root, text="4. Copiar PDF", bootstyle=WARNING, width=25, command=copiar_pdf_interface).pack(pady=5)

def autenticar():
    senha = campo_senha.get()
    if senha in ["123", "sua senha"]:
        tela_menu()
    else:
        messagebox.showerror("Erro", "Senha incorreta!")
        campo_senha.delete(0, tk.END)

def confirmar_abertura():
    if var_confirm.get() == "sim":
        mostrar_tela_senha()
    else:
        messagebox.showinfo("Encerrado", "Sistema encerrado.")
        root.destroy()

def mostrar_tela_confirmacao():
    limpar_tela()
    global var_confirm
    tb.Label(root, text=f"Olá {usuario_nome.get()}, Deseja abrir o sistema?", font=("Segoe UI", 12)).pack(pady=25)
    var_confirm = tk.StringVar()
    tb.Radiobutton(root, text="Sim", variable=var_confirm, value="sim").pack()
    tb.Radiobutton(root, text="Não", variable=var_confirm, value="nao").pack()
    tb.Button(root, text="Confirmar", command=confirmar_abertura, bootstyle=SUCCESS).pack(pady=25)

def mostrar_tela_senha():
    limpar_tela()
    global campo_senha
    tb.Label(root, text="Digite a senha do administrador:").pack(pady=15)
    campo_senha = tb.Entry(root, show="*")
    campo_senha.pack(pady=5)
    tb.Button(root, text="Entrar", command=autenticar, bootstyle=PRIMARY).pack(pady=15)

def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------------- Tela Inicial ---------------------- #
root = tb.Window(themename="darkly")
root.title("Manipulador de PDFs")
root.geometry("500x450")
root.configure(padx=20, pady=20)

usuario_nome = tk.StringVar()
tb.Label(root, text="Bem-vindo ao Manipulador de PDFs", font=("Segoe UI", 14, "bold")).pack(pady=25)
tb.Label(root, text="Digite seu nome:").pack()
tb.Entry(root, textvariable=usuario_nome).pack(pady=5)
tb.Button(root, text="Avançar", command=mostrar_tela_confirmacao, bootstyle=DANGER).pack(pady=25)

root.mainloop()
