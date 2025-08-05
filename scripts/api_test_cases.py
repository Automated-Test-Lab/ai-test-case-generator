import os
from dotenv import load_dotenv
import sys
# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.main_utils import get_page_content, generate_content, create_feature_file, create_spec_file

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê variáveis de ambiente
url_API = os.getenv("URL_API")

def main():
    """
    Função principal para gerar arquivos .feature e .spec.ts a partir de uma URL.
    """
    prompt_feature = os.getenv("PROMPT_FEATURE", "Considerando que você é um Engenheiro de Automação Software especializado em testes de API, gere um arquivo .feature (Gherkin) com os cenários básicos, alternativos e de exceção dos endpoints.")
    prompt_spec = os.getenv("PROMPT_SPEC", "Considerando que você é um Engenheiro de Automação Software especializado em testes de API, gere um arquivo Playwright .spec.ts com testes bem estrututrados de API.")

    if not url_API:
        raise ValueError("A variável de ambiente URL_API deve estar definida.")

    print(f"Buscando conteúdo da URL: {url_API}...")
    conteudo_da_url = get_page_content(url_API)

    if not conteudo_da_url:
        print("Não foi possível obter o conteúdo da URL. Encerrando.")
        return

    print("Gerando cenários em Gherkin para o arquivo .feature...")
    feature_content = generate_content(prompt_feature, conteudo_da_url)
    create_feature_file("api_test_cases.feature", feature_content)

    print("\n---")

    print("Gerando casos de testes em Playwright para o arquivo .spec.ts...")
    spec_content = generate_content(prompt_spec, conteudo_da_url)
    create_spec_file("api_test_cases.spec.ts", spec_content)

if __name__ == "__main__":
    main()