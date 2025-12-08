# Importar bibliotecas
import docx
import os
import sys
from google import genai
from google.genai import types
from datetime import timedelta
from datetime import datetime

# Input para inserir chave de API da IA
def obter_chave_api() -> str:
    chave_api = input("Por favor, insira a chave da API do Gemini: ")
    if not chave_api:
        print("Chave da API não fornecida! O programa será encerrado.")
        sys.exit(1)
    return chave_api

# Input para inserir idiomas de origem e destino
def obter_idiomas() -> tuple[str, str]:
    """Solicita ao usuário os idiomas de origem e destino em uma única entrada, separados por vírgula."""
    idiomas = input("Por favor, insira o idioma de origem e o idioma de destino separados por vírgula (Ex: Galês, Limburguês): ")
    
    # Verifica se o usuário inseriu algo
    if not idiomas:
        print("Nenhuma entrada fornecida! O programa será encerrado.")
        sys.exit(1)
    
    # Divide a entrada pelo delimitador vírgula e remove espaços extras
    idiomas_divididos = [idioma.strip() for idioma in idiomas.split(",")]

    # Verifica se a entrada contém exatamente dois idiomas
    if len(idiomas_divididos) != 2:
        print("Erro: Por favor, forneça exatamente dois idiomas, separados por vírgula.")
        sys.exit(1)
    
    return idiomas_divididos[0], idiomas_divididos[1]

# Formata formato de horário retornado
def hora_atual() -> str:
    return datetime.now().strftime('%H:%M:%S:%f')[:-3]

# Manuseio de Arquivos
def extrair_texto_docx(caminho_arquivo: str) -> str:
    """Extrai todo o texto de um arquivo .docx."""
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        return ""

    documento = docx.Document(caminho_arquivo)

    # Juntar o texto de todos os parágrafos em uma única string
    # separar com quebras de linha.
    paragrafos = [p.text for p in documento.paragraphs]
    texto_completo = "\n".join(paragrafos)

    return texto_completo


def salvar_texto_txt(texto: str, caminho_saida: str) -> None:
    """Salva o texto fornecido em um novo arquivo .txt."""
    try:
        with open(caminho_saida, "w", encoding="utf-8") as arquivo_txt:
            print(f"Salvando em {caminho_saida}")
            arquivo_txt.write(texto)
        print(f"Sucesso: Arquivo salvo em {caminho_saida}\n")

    except Exception as e:
        print(f"Erro ao salvar o arquivo TXT: {e}")


# Motor de Tradução Gemini
def traduzir_texto_com_gemini(
    texto_original: str, idioma_origem: str, idioma_destino: str, chave_api: str
) -> str:
    """
    Traduz um bloco de texto usando o modelo Gemini 2.5 Flash.
    Assume que a GEMINI_API_KEY está definida como variável de ambiente.
    """
    try:
        # Ler a chave de API da variável de ambiente GEMINI_API_KEY
        client = genai.Client(api_key=chave_api)

        # Criar um prompt robusto e estruturado para garantir uma boa tradução
        prompt = (
            f"Traduza o seguinte texto de **{idioma_origem}** para **{idioma_destino}**. "
            "A tradução deve ter a **fluidez e naturalidade** de um falante nativo do **{idioma_destino}**. "
            "Mantenha a formatação original de parágrafos e pontuação. "
            "Não adicione comentários, introduções ou conclusões, apenas o texto traduzido.\n\n"
            f"TEXTO ORIGINAL:\n---\n{texto_original}"
        )

        # Configurações para a geração
        config = types.GenerateContentConfig(
            temperature=0.3  # Temperatura mais baixa para tradução literal
        )

        # Chamada à API
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt, config=config
        )

        print("Sucesso: O texto foi traduzido\n")

        return response.text.strip()

    except Exception as e:
        # Adicionar verificação mais clara do erro de API Key
        if "Missing key inputs argument" in str(e):
            print(
                "\nERRO DE CHAVE DE API: A variável GEMINI_API_KEY não foi carregada no ambiente."
            )
            print(
                "Verifique se você a definiu corretamente na sessão do terminal antes de executar o script."
            )
        else:
            print(f"Ocorreu um erro ao chamar a API do Gemini: {e}")
        return "Erro de tradução."


# Fluxo Principal
if __name__ == "__main__":
    # Inputs de inicio
    chave_api = obter_chave_api()
    idioma_origem, idioma_destino = obter_idiomas()

    # Registrar o horário de início do processo completo
    print("\n\n----------------------------------------\n")
    print(f"--- Início da execução: {hora_atual()} ---\n")
    print("----------------------------------------\n\n")

    # Definir o diretório onde os arquivos .docx estão localizados
    DIRETORIO_ENTRADA = "./"
    DIRETORIO_SAIDA = "./"

    # Listar todos os arquivos .docx no diretório de entrada
    arquivos_docx = [f for f in os.listdir(DIRETORIO_ENTRADA) if f.endswith(".docx")]

    if not arquivos_docx:
        print("Nenhum arquivo .docx encontrado no diretório especificado.")

    # Processar cada arquivo .docx encontrado
    for arquivo in arquivos_docx:
        print(f"--- Início da manipulação do arquivo: {hora_atual()} ---\n")

        caminho_arquivo_entrada = os.path.join(DIRETORIO_ENTRADA, arquivo)
        nome_arquivo_saida = arquivo.replace(".docx", ".txt")
        caminho_arquivo_txt = os.path.join(DIRETORIO_SAIDA, nome_arquivo_saida)
        
        print(f"=== PROCESSANDO: {arquivo} ===")
        
        # Extrair o texto do arquivo .docx
        texto_extraido = extrair_texto_docx(caminho_arquivo_entrada)

        print("Sucesso: O texto foi extraído\n")
        
        if not texto_extraido:
            print(f"Não foi possível extrair texto do arquivo {arquivo}. Pulando...\n")
            continue
        
        # Traduzir o texto extraído
        print(f"=== TRADUZINDO: De {idioma_origem} para {idioma_destino} ===")
        texto_traduzido = traduzir_texto_com_gemini(texto_extraido, idioma_origem, idioma_destino, chave_api)
        
        # Se a tradução for bem-sucedida, salvar no arquivo .txt
        if texto_traduzido != "Erro de tradução.":
            salvar_texto_txt(texto_traduzido, caminho_arquivo_txt)
        else:
            print(f"Erro de tradução no arquivo {arquivo}. Pulando...\n")

        print(f"--- Término da manipulação do arquivo: {hora_atual()} ---\n")
    
    print("-----------------------------------------\n")
    print(f"--- Término da execução: {hora_atual()} ---\n")
    print("-----------------------------------------\n\n")
