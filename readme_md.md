# 🚰 Sistema de Monitoramento de Reservatório de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ETEC](https://img.shields.io/badge/ETEC-Atividade_Escolar-red?style=for-the-badge)
![Colorama](https://img.shields.io/badge/Colorama-Terminal_UI-blue?style=for-the-badge)

> **Autor:** Lucas Fersa  
> **Instituição:** ETEC  
> **Status do Projeto:** 🟢 Concluído

---

## 📌 Sobre o Projeto

Este projeto consiste em um sistema simples de **simulação e monitoramento de níveis de água em um reservatório**, desenvolvido em Python para ser executado via terminal.

O objetivo principal é exibir mensagens formatadas com cores específicas para cada nível de água, facilitando a visualização rápida e intuitiva da situação do reservatório (de níveis críticos a alertas de transbordamento).

---

## 🎨 Tabela de Níveis e Cores

| Nível | Situação | Cor de Exibição |
| :---: | :--- | :---: |
| **1** | Muito baixo (crítico) | 🔴 Vermelho |
| **2** | Baixo | 🟡 Amarelo |
| **3** | Médio | 🟢 Verde |
| **4** | Alto | 🔵 Ciano |
| **5** | Muito alto (alerta) | 🟦 Azul |

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **[Python 3](https://www.python.org/)** — Linguagem de programação principal.
- 🎨 **[Colorama](https://pypi.org/project/colorama/)** — Biblioteca para estilização de texto com cores no terminal.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina.

### Passo a Passo

1. **Clone ou baixe o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/controle_agua.git
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd controle_agua
   ```

3. **Instale a biblioteca necessária (`colorama`):**
   ```bash
   pip install colorama
   ```

4. **Execute o arquivo Python:**
   ```bash
   python controle_agua.py
   ```

---

## 🖥️ Exemplo de Saída no Terminal

```text
--- Iniciando Monitoramento do Reservatório ---
Nível de água 1: Muito baixo (crítico)
Nível de água 2: Baixo
Nível de água 3: Médio
Nível de água 4: Alto
Nível de água 5: Muito alto (alerta)

Controle de nível de água concluído.
```

---
*Projeto desenvolvido para fins didáticos no curso da ETEC.*