
from presentation.window import App
from data.currency_freaks_repo import CurrencyRepo

def load_config():
    import json
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except Exception:
        return {}

def build_repository():
    config = load_config()
    repo = CurrencyRepo(host=config.get("api-host"), key=config.get("api-key"), def_list_cur=config.get("default_list"), base_currency=str(config.get("default_base")))
    return repo, config

if __name__ == "__main__":
    repo, config = build_repository()
    app = App(repo=repo)
    app.mainloop()
    
# pyinstaller --onefile main.py // do produkcji jednego pliku exe