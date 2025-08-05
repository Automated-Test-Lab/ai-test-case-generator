import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê a chave da API do Gemini do ambiente
gemini_api_key = os.getenv("GEMINI_API_KEY")

def get_page_content(url: str) -> str:
    """
    Fetches the content of a web page from a given URL.

    Args:
        url (str): The URL of the web page.

    Returns:
        str: The extracted text content of the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        page_content = soup.get_text(separator=' ', strip=True)
        return page_content

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return ""

def generate_content(prompt: str, content_to_analyze: str, model: str = "gemini-1.5-flash") -> str:
    """
    Generates content based on the provided prompt and additional content.

    Args:
        prompt (str): The base prompt.
        content_to_analyze (str): The content to be analyzed (e.g., page content).
        model (str): The name of the Gemini model to use for generation.

    Returns:
        str: The generated content.
    """
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it.")

    genai.configure(api_key=gemini_api_key)

    full_prompt = f"{prompt}\n\nAnalise o seguinte conteúdo:\n\n{content_to_analyze}"

    # Usa o modelo padrão mais recente
    model_instance = genai.GenerativeModel('gemini-2.5-flash')
    response = model_instance.generate_content(full_prompt)

    return response.text


def create_output_directory(dir_name: str = "results"):
    """
    Cria um diretório se ele não existir.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Diretório '{dir_name}' criado.")

def create_feature_file(file_name: str, feature_content: str, output_dir: str = "results"):
    """
    Creates or overwrites a .feature file in the specified directory.
    """
    create_output_directory(output_dir)
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(feature_content)
    print(f"Arquivo '{file_path}' criado com sucesso!")

def create_spec_file(file_name: str, spec_content: str, output_dir: str = "results"):
    """
    Creates or overwrites a .spec.ts file in the specified directory.
    """
    create_output_directory(output_dir)
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(spec_content)
    print(f"Arquivo '{file_path}' criado com sucesso!")