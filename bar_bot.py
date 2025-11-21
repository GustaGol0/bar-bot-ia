import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich import box
from rich.live import Live

# Carregando variáveis de ambiente do arquivo .env
load_dotenv()

# Criando o console do Rich
console = Console()

# ======================================================
# 1. CONFIGURAÇÃO DO GARÇOM (API)
# ======================================================
# IMPORTANTE: Sua chave está aqui. Quando subir pro GitHub, apague ela!
MINHA_CHAVE = os.getenv("GEMINI_API_KEY")

if not MINHA_CHAVE:
    console.print("[bold red]ERRO CRÍTICO: Chave de API não encontrada![/]")
    console.print("Verifique se você criou o arquivo [yellow].env[/] com a chave.")
    exit()

genai.configure(api_key=MINHA_CHAVE)
model = genai.GenerativeModel('gemini-2.5-flash')

# ======================================================
# 2. DADOS DO BAR (PARA A IA LER)
# ======================================================
cardapio_texto = """
1. CAIPIRINHA CLÁSSICA (R$ 20): Cachaça Prata, limão taiti, açúcar e gelo.
2. RABO DE GALO (R$ 18): Cachaça envelhecida, Vermouth Rosso e casca de laranja.
3. BOMBEIRINHO (R$ 15): Cachaça, groselha e suco de limão.
4. CAJU AMIGO (R$ 22): Cachaça, compota de caju e suco da fruta.
5. NEGRONI (R$ 35): Gin, Campari, Vermouth Rosso.
6. MOSCOW MULE (R$ 28): Vodka, xarope de gengibre, limão e espuma.
7. WHISKY SOUR (R$ 30): Bourbon, limão, açúcar e clara de ovo.
8. APEROL SPRITZ (R$ 26): Aperol, Espumante, Água com gás.
9. LONG ISLAND ICED TEA (R$ 40): Vodka, Rum, Gin, Tequila, Licor de Laranja e Cola.
10. PYTHON SOUR (R$ 25): Licor de menta (verde), Vodka e Limão.
11. BLUE SCREEN OF DEATH (R$ 32): Curaçau Blue, Gin e Tônica.
12. BUG FIX (R$ 12): Shot de café expresso com Cachaça.
13. SODA ITALIANA (R$ 18): Xarope de maçã verde ou morango com água com gás.
14. VIRGIN MOJITO (R$ 20): Hortelã, limão, açúcar e água com gás.
15. PINA COLADA VIRGIN (R$ 22): Abacaxi, leite de coco e gelo.
"""


# ======================================================
# 2.1. DICIONÁRIO DOS PREÇOS
# ======================================================
dados_precos = {
    "1": {"nome": "Caipirinha", "preco": 20},
    "2": {"nome": "Rabo de Galo", "preco": 18},
    "3": {"nome": "Bombeirinho", "preco": 15},
    "4": {"nome": "Caju Amigo", "preco": 22},
    "5": {"nome": "Negroni", "preco": 35},
    "6": {"nome": "Moscow Mule", "preco": 30},
    "7": {"nome": "Whisky Sour", "preco": 28},
    "8": {"nome": "Aperol Spritz", "preco": 26},
    "9": {"nome": "Long Island", "preco": 40},
    "10": {"nome": "Python Sour", "preco": 25},
    "11": {"nome": "Blue Screen", "preco": 32},
    "12": {"nome": "Bug Fix", "preco": 12},
    "13": {"nome": "Soda Italiana", "preco": 18},
    "14": {"nome": "Virgin Mojito", "preco": 20},
    "15": {"nome": "Pina Colada Virgin", "preco": 22},
    }

total_conta = 0
# ======================================================
# 2.2. CRIAÇÃO DA TABELA BONITA (PARA O HUMANO VER)
# ======================================================
# Aqui montamos o visual. box.DOUBLE faz a borda dupla.
tabela_visual = Table(title="🍸 CARDÁPIO DO BAR 🍸", box=box.DOUBLE, style="gold1")

# Criando as colunas
tabela_visual.add_column("Item", justify="center", style="cyan", no_wrap=True)
tabela_visual.add_column("Nome", style="magenta")
tabela_visual.add_column("Preço", justify="right", style="green")
tabela_visual.add_column("Vibe", style="white")

# Adicionando as linhas (Tem que bater com o texto da IA)
tabela_visual.add_row("1", "Caipirinha", "R$ 20", "Clássica")
tabela_visual.add_row("2", "Rabo de Galo", "R$ 18", "Forte e Raiz")
tabela_visual.add_row("3", "Bombeirinho", "R$ 15", "Doce e Perigoso")
tabela_visual.add_row("4", "Caju Amigo", "R$ 22", "Nordestino")
tabela_visual.add_row("5", "Negroni", "R$ 35", "Amargo e Chique")
tabela_visual.add_row("6", "Moscow Mule", "R$ 30", "Canequinha")
tabela_visual.add_row("7", "Whisky Mule", "R$ 28", "Cremoso e Azedo")
tabela_visual.add_row("8", "Aperol Spritz", "R$ 26", "Leve, para dias de sol")
tabela_visual.add_row("9", "Long Island", "R$ 40", "Pra apagar")
tabela_visual.add_row("10", "Python Sour", "R$ 25", "Geek & Verde")
tabela_visual.add_row("11", "Blue Screen", "R$ 32", "Azul Neon")
tabela_visual.add_row("12", "Bug Fix", "R$ 12", "Café + Cachaça")
tabela_visual.add_row("13", "Soda Italiana", "R$ 18", "Doce e Refrescante")
tabela_visual.add_row("14", "Virgin Mojito", "R$ 20", "Sem Álcool e Refrescante")
tabela_visual.add_row("15", "Pina Colada Virgin", "R$ 22", "Sem Álcool. Tropical")

# ======================================================
# 3. FUNÇÃO QUE CHAMA A IA
# ======================================================
def pedir_recomendacao(gosto_do_cliente):
    prompt = f"""
    Aja como uma Bartender muito descolada e gente boa chamada 'JadeBot'.
    
    CARDÁPIO DISPONÍVEL:
    {cardapio_texto}

    INSTRUÇÕES DE RACIONÍCIO:
    1. Analise o pedido: "{gosto_do_cliente}"
    2. CRUZE com o cardápio (Geek com Geek, Forte com Forte, Cor com Cor).
    3. Escolha a MELHOR opção ou as MELHORES opções que combinem.
    
    SUA MISSÃO:
    1. Recomende APENAS uma opção.
    2. Explique o porquê de forma curta e divertida, com piadas e um pouco fofa, mas sem deixar forçado.
    3. Você deve se comportar como uma pessoa do sexo feminino (Jade).
    4. Se não tiver o item, ofereça alternativas.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro técnico: {e}"
    
#======================================================
# 3.1 FUNÇÕES AUXILIARES
##======================================================
def escrever_com_delay(texto, delay=0.03):
    """Escreve o texto no console com um efeito de digitação."""
    for char in texto:
        console.print(char, end='', style="bold white")
        time.sleep(delay)
    console.print()


# ======================================================
# 4. INTERFACE NO TERMINAL
# ======================================================
while True:
    # 1. LIMPA A TELA E MOSTRA O CARDÁPIO
    console.clear()
    # Cabeçalho mostrando o TOTAL DA CONTA atualizado no topo
    console.print(Panel(f"====== BAR DA JADEBOT | 💰 CONTA: R$ {total_conta:.2f} ======", style="bold purple"))
    console.print(tabela_visual) 
    console.print("\nPeça uma recomendação de drink baseado no seu humor ou gosto!", style="italic green")

    # 2. INPUT DO USUÁRIO
    pedido = console.input("\n[bold gold1]O que você manda hoje?[/] 🍸 > ")
        
    # 3. CONDIÇÃO DE SAÍDA
    if pedido.lower() == "sair":
        console.print(Panel(f"💸 CONTA FECHADA: R$ {total_conta:.2f}\nObrigado pela preferência!", style="bold green"))
        break
        
    try:
        # 4. ANIMAÇÃO ENQUANTO A IA PENSA
        with console.status("[bold green]Pensando para dar a melhor resposta![/]", spinner="bouncingBall"):
            resposta = pedir_recomendacao(pedido)
        
        # 5. EFEITO TYPEWRITER (DIGITAÇÃO)
        texto_acumulado = ""
        with Live(Panel("", title="🤖 JadeBot", border_style="bold magenta"), refresh_per_second=15) as painel_vivo:
            for letra in resposta:
                texto_acumulado += letra
                painel_vivo.update(Panel(texto_acumulado, title="🤖 JadeBot", border_style="bold magenta"))
                time.sleep(0.02)

        console.print("-" * 40, style="dim")
        
        # 6. LÓGICA DE COMPRA (A COMANDA)
        decisao = console.input("Curtiu? Digite o [bold cyan]NÚMERO[/] do drink para adicionar à conta (ou Enter para pular): ")

        if decisao in dados_precos:
            item_escolhido = dados_precos[decisao]
            total_conta += item_escolhido["preco"] # Soma no total
            
            # Feedback visual da compra
            console.print(f"\n✅ [bold green]Adicionado: {item_escolhido['nome']} (+ R$ {item_escolhido['preco']})[/]")
            console.print(f"💰 [bold yellow]NOVO TOTAL: R$ {total_conta:.2f}[/]")
            
            # O PAUSE IMPORTANTE (Para você ler o saldo antes de limpar a tela)
            console.input("\nPressione [bold]ENTER[/] para continuar...")
        
        elif decisao != "":
            console.print("[red]Número inválido! Nada foi cobrado.[/]")
            time.sleep(1.5)

    except Exception as e:
        console.print(f"[bold red]Deu ruim na cozinha: {e}[/]")
        console.input("Pressione [bold cyan]Enter[/] para tentar de novo...")