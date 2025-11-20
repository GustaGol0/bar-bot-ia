# 🍸 Bar da JadeBot

Um bartender virtual inteligente que roda no terminal! A JadeBot usa IA (Google Gemini) para recomendar drinks personalizados baseados no seu humor, gosto ou vibe do momento.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- **Recomendações inteligentes** — A IA analisa seu pedido e cruza com o cardápio para sugerir o drink perfeito
- **Interface rica no terminal** — Visual bonito com tabelas, painéis e cores usando Rich
- **Efeito de digitação** — Respostas aparecem letra por letra, simulando uma conversa real
- **Sistema de comanda** — Adicione drinks à conta e acompanhe o total em tempo real
- **15 drinks no cardápio** — De clássicos como Caipirinha a temáticos como "Blue Screen of Death"

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chave de API do Google Gemini

## 🚀 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/bar-jadebot.git
   cd bar-jadebot
   ```

2. **Instale as dependências**
   ```bash
   pip install google-generativeai python-dotenv rich
   ```

3. **Configure a chave de API**
   
   Crie um arquivo `.env` na raiz do projeto:
   ```env
   GEMINI_API_KEY=sua_chave_aqui
   ```
   
   > 💡 Obtenha sua chave gratuita em [Google AI Studio](https://aistudio.google.com/app/apikey)

4. **Execute o programa**
   ```bash
   python main.py
   ```

## 🎮 Como Usar

1. Ao iniciar, você verá o cardápio completo do bar
2. Digite seu humor, gosto ou o que está sentindo (ex: "algo refrescante", "to querendo esquecer os problemas", "drink de programador")
3. A JadeBot vai recomendar o drink ideal com uma explicação divertida
4. Digite o **número** do drink para adicionar à sua conta
5. Digite `sair` para fechar a conta e encerrar

## 🍹 Cardápio

| # | Drink | Preço | Vibe |
|---|-------|-------|------|
| 1 | Caipirinha | R$ 20 | Clássica |
| 2 | Rabo de Galo | R$ 18 | Forte e Raiz |
| 3 | Bombeirinho | R$ 15 | Doce e Perigoso |
| 4 | Caju Amigo | R$ 22 | Nordestino |
| 5 | Negroni | R$ 35 | Amargo e Chique |
| 6 | Moscow Mule | R$ 30 | Canequinha |
| 7 | Whisky Sour | R$ 28 | Cremoso e Azedo |
| 8 | Aperol Spritz | R$ 26 | Leve, para dias de sol |
| 9 | Long Island | R$ 40 | Pra apagar |
| 10 | Python Sour | R$ 25 | Geek & Verde |
| 11 | Blue Screen of Death | R$ 32 | Azul Neon |
| 12 | Bug Fix | R$ 12 | Café + Cachaça |
| 13 | Soda Italiana | R$ 18 | Doce e Refrescante |
| 14 | Virgin Mojito | R$ 20 | Sem Álcool |
| 15 | Pina Colada Virgin | R$ 22 | Tropical Sem Álcool |

## 🛠️ Tecnologias

- **[Google Gemini](https://ai.google.dev/)** — Modelo de IA para gerar recomendações
- **[Rich](https://rich.readthedocs.io/)** — Formatação e visual no terminal
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Gerenciamento de variáveis de ambiente

## 📁 Estrutura

```
bar-jadebot/
├── main.py          # Código principal
├── .env             # Chave de API (não committar!)
├── .gitignore       # Ignorar .env
└── README.md
```

## ⚠️ Importante

**Nunca commite sua chave de API!** Adicione `.env` ao seu `.gitignore`:

```gitignore
.env
```

## 📝 Licença

Este projeto está sob a licença MIT.

---

Feito com 🍸 e Python