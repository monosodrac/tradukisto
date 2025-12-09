[PYTHON__BADGE]: https://img.shields.io/badge/python-D4FAFF?style=for-the-badge&logo=python

<h1 align="center" style="font-weight: bold;">Tradukisto</h1>

![typescript][PYTHON__BADGE]

<details open="open">
<summary>Sumário</summary>
 
- [📌 Sobre](#about)
- [⚙️ Arquitetura do projeto](#architecture)
- [🚀 Comece por aqui](#started)
  - [Pré-requisitos](#prerequisites)
  - [Clonando repositório](#cloning)
  - [Como executar](#executing)
- [🧠 Funcionalidades](#features)
- [🤝 Contato](#reach)
  
</details>

---

<h2 id="about">📌 Sobre</h2>

**Tradukisto** é um tradutor de textos.  
Estes scripts automatizam o processo de tradução de documentos .docx, adaptando nomes próprios e termos culturais conforme a região ou país de destino. Ele extrai o texto do arquivo, traduz utilizando a API Gemini, e salva o texto traduzido em um arquivo .txt, com ajustes na ambientação e nomes próprios específicos para a região escolhida.

---

<h2 id="architecture">⚙️ Arquitetura do projeto</h2>

```
📂src/
├── .gitignore
├── executar_automacao.bat
├── README.md
├── requirements.txt
├── traduzir_c_regiao.py
└── traduzir.py
```

---

<h2 id="started">🚀 Comece por aqui</h2>

<h3 id="prerequisites">Pré-requisitos</h3>

- [Git](https://git-scm.com/install/windows)
- [Python](https://www.python.org/downloads/)

---

<h3 id="cloning">Clonando repositório</h3>

```bash
git clone https://github.com/monosodrac/tradukisto.git
```

<h3 id="executing">Como executar</h3>

#### Instalar o Python 3.x  
Após instalar, pode verificar se o Python foi corretamente instalado com o comando:

```bash
python --version
```

Isso deve retornar a versão do Python instalada. O script exige o Python 3.x.


#### Criar o Ambiente Virtual
O próximo passo é criar um ambiente virtual. Esse ambiente isola as dependências do projeto, garantindo que elas não interfiram em outras instalações Python no sistema.  

Abrir o terminal ou prompt de comando.

Se você está utilizando Windows:
Abra o Prompt de Comando ou PowerShell.

Se você está utilizando Linux ou Mac:
Abra o Terminal.

***
	IMPORTANTE: Navegar até o diretório (pasta) do projeto (onde o código Python e os arquivos .bat e requirements.txt estão localizados).
	Exemplo no CMD do Windows:
		
        Digite o comando:  
        cd C:\Users\<Nome_Do_Usuário>\Documents\automacao
		
        Depois de executar, digite o comando:  
        dir

		E execute  

		Se estiver no diretório correto, deverá aparecer a lista com o nome dos arquivos
***

Criar o ambiente virtual com o seguinte comando:  
```bash
python -m venv .env
```

Isso vai criar um diretório chamado .env onde o ambiente virtual será armazenado.


#### Ativar o Ambiente Virtual
Agora que o ambiente virtual foi criado, você precisa ativá-lo.

---
No Windows:
```bash
.\.env\Scripts\activate
```

No Linux/Mac:
```bash
source .env/bin/activate
```
---

Quando o ambiente virtual estiver ativado, o nome do ambiente virtual (geralmente _.env_) aparecerá no início da linha do terminal, indicando que as dependências e o Python agora estão sendo gerenciados dentro deste ambiente.


#### Instalar as Dependências
No diretório do projeto, existe um arquivo chamado requirements.txt que lista todas as bibliotecas necessárias para o projeto.  
Para instalar as dependências, rode o seguinte comando enquanto o ambiente virtual estiver ativo:
```bash
pip install -r requirements.txt
```

Isso irá instalar todas as dependências necessárias para rodar o script, como o google-genai e outras bibliotecas que seu código pode precisar.

Agora pode desativar o ambiente virtual, rodando:
```bash
deactivate
```

E feche o terminal.


#### Obter a Chave da API
* Seu código requer uma chave de API para se comunicar com o serviço Gemini.  
* Crie uma conta no serviço Gemini.  
* Obtenha a chave de API do serviço, seguindo as instruções da plataforma.  
* Quando solicitado pelo script, insira a chave da API no terminal.


#### Rodar o Script Usando o Arquivo Batch
No repositório está incluído o arquivo executar_automacao.bat, que cuida da ativação do ambiente virtual e da execução do script Python.

Ao rodar o script:
O terminal pedirá a chave da API, e o script começará a processar os arquivos conforme programado.

Ele vai automaticamente:  
* Ativar o ambiente virtual.
* Rodar o script Python.
* Desativar o ambiente virtual quando o script terminar.
* Manter o terminal aberto para análise de resultados (ou qualquer erro).



--- Problemas Comuns ---

**Erro ao ativar o ambiente virtual:**  
Se houver problemas para ativar o ambiente, pode ser necessário verificar se o caminho para o ambiente virtual está correto. Tente usar o caminho absoluto para a ativação se necessário.

**Erros de instalação:**  
Se algum pacote não for instalado corretamente, tente excluir a pasta .env que foi criada para o ambiente virtual, rodar o comando de criação novamente e veja se algum erro específico aparece. Dependendo da situação, a instalação de dependências extras pode ser necessária.

**Problema com a chave da API:**  
Certifique-se de que a chave foi inserida corretamente quando o script pedir.


<h2 id="features">🧠 Funcionalidades</h2>

- 📄 Extração e Tradução de textos
- 🌍 Adaptação Cultural e Regional
- 🤖 Tradução Personalizada com a API Gemini
- ⚙️ Processamento em Lote


<h2 id="reach">🤝 Contato</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://linktr.ee/monosodrac">
        <img src="https://avatars.githubusercontent.com/u/141099551?v=4" width="100px;" alt="Mono Cardoso Profile Picture"/><br>
        <sub>
          <b>Mono</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
