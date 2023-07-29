import box
import timeit
import yaml
from dotenv import find_dotenv, load_dotenv
from src.utils import setup_dbqa
from colorama import Fore, Back

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Import config vars
with open('config/config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


if __name__ == "__main__":
    # Setup DBQA
    start = timeit.default_timer()
    dbqa = setup_dbqa()
    mid = timeit.default_timer()
    print(f"{Fore.CYAN}Time to setup model: {mid - start}{Fore.RESET}")

    while (query := input("> ")) not in ["end", "quit", "exit"]:
      mid = timeit.default_timer()
      response = dbqa({'query': query})
      end = timeit.default_timer()

      print(f'{Back.LIGHTWHITE_EX}{Fore.BLACK}Answer: {response["result"]}{Back.RESET}')
      print(f'{Fore.BLACK}{"="*100}')

      # Process source documents
      source_docs = response['source_documents']
      for i, doc in enumerate(source_docs):
          print(f'{Back.WHITE}{Fore.LIGHTBLACK_EX}Source Document {i+1} ({doc.metadata["source"]}#page={doc.metadata["page"]})')
          print(f'{Fore.BLACK}{doc.page_content}')
          print(f'{Back.RESET}{Fore.BLACK}{"="*100}')
      print(f"{Fore.CYAN}Time to generate response: {end - mid}{Fore.RESET}")

    
    
