import os
from dotenv import load_dotenv
import sys
# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.main_utils import get_page_content, generate_content, create_feature_file, create_spec_file

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê variáveis de ambiente
url_UI = os.getenv("URL_UI")

def main():
    """
    Função principal para gerar arquivos .feature e .spec.ts a partir de uma URL.
    """
    prompt_feature = os.getenv("PROMPT_FEATURE", "Considerando que você é um Engenheiro de Automação Software especializado em testes de UI, gere um arquivo .feature (Gherkin) com os cenários básicos, alternativos e de exceção da aplicação fornecida pela {url_UI}")
    prompt_spec = os.getenv("PROMPT_SPEC", "Considerando que você é um Engenheiro de Automação Software especializado em testes de UI, gere um arquivo Playwright .spec.ts com testes bem estrututrados E2E da aplicação fornecida pela {url_UI}")
   
    if not url_UI:
        raise ValueError("A variável de ambiente URL_UI deve estar definida.")

    print(f"Buscando conteúdo da URL: {url_UI}...")
    conteudo_da_url = get_page_content(url_UI)

    if not conteudo_da_url:
        print("Não foi possível obter o conteúdo da URL. Encerrando.")
        return
    
    formatted_prompt_feature = prompt_feature.format(url_UI=url_UI)
    print("Gerando cenários em Gherkin para o arquivo .feature...")
    feature_content = generate_content(formatted_prompt_feature, conteudo_da_url)
    create_feature_file("ui_test_cases.feature", feature_content)

    print("\n---")

    formatted_prompt_spec = prompt_spec.format(url_UI=url_UI)
    print("Gerando casos de testes em Playwright para o arquivo .spec.ts...")
    spec_content = generate_content(formatted_prompt_spec, conteudo_da_url)
    create_spec_file("ui_test_cases.spec.ts", spec_content)

if __name__ == "__main__":
    main()