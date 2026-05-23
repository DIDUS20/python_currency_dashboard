import customtkinter as ctk
from api.currency_api import get_currency_rates
from api.crypto_api import get_crypto_prices


class CryptoApp(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        super().__init__()

        self.title("Crypto & Currency Tracker")
        self.geometry("950x760")
        self.minsize(900, 700)

        self.currency_data = {}
        self.crypto_data = {}

        self.title_label = ctk.CTkLabel(
            self,
            text="Crypto & Currency Tracker",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        self.refresh_button = ctk.CTkButton(
            self,
            text="Aktualizuj dane",
            command=self.load_data
        )
        self.refresh_button.pack(pady=(0, 10))

        self.status_label = ctk.CTkLabel(
            self,
            text="Wczytywanie...",
            font=("Arial", 14),
            text_color="#B0B0B0"
        )
        self.status_label.pack(pady=(0, 10))

        self.currency_frame = ctk.CTkFrame(self)
        self.currency_frame.pack(padx=20, pady=(0, 20), fill="x")

        self.crypto_frame = ctk.CTkFrame(self)
        self.crypto_frame.pack(padx=20, pady=(0, 20), fill="x")

        self.converter_frame = ctk.CTkFrame(self)
        self.converter_frame.pack(padx=20, pady=(0, 20), fill="x")

        self.create_converter()
        self.load_data()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def load_data(self):
        self.clear_frame(self.currency_frame)
        self.clear_frame(self.crypto_frame)

        self.status_label.configure(text="Ładowanie danych...")
        self.update_idletasks()

        self.currency_data = get_currency_rates()
        self.crypto_data = get_crypto_prices()

        if not self.currency_data and not self.crypto_data:
            self.status_label.configure(text="Błąd połączenia. Sprawdź internet i spróbuj ponownie.")
            return

        self.status_label.configure(text="Dane pobrane pomyślnie.")

        currency_title = ctk.CTkLabel(
            self.currency_frame,
            text="Kursy walut",
            font=("Arial", 22, "bold")
        )
        currency_title.pack(pady=(10, 10))

        currency_table = ctk.CTkFrame(self.currency_frame)
        currency_table.pack(fill="x", padx=10, pady=(0, 10))

        header_code = ctk.CTkLabel(currency_table, text="Waluta", font=("Arial", 16, "bold"))
        header_rate = ctk.CTkLabel(currency_table, text="Kurs (PLN)", font=("Arial", 16, "bold"))
        header_code.grid(row=0, column=0, padx=10, pady=4, sticky="w")
        header_rate.grid(row=0, column=1, padx=10, pady=4, sticky="w")

        for row, (code, rate) in enumerate(self.currency_data.items(), start=1):
            label_code = ctk.CTkLabel(currency_table, text=code, font=("Arial", 14))
            label_rate = ctk.CTkLabel(currency_table, text=f"{rate:.4f}", font=("Arial", 14))
            label_code.grid(row=row, column=0, padx=10, pady=3, sticky="w")
            label_rate.grid(row=row, column=1, padx=10, pady=3, sticky="w")

        crypto_title = ctk.CTkLabel(
            self.crypto_frame,
            text="Ceny kryptowalut",
            font=("Arial", 22, "bold")
        )
        crypto_title.pack(pady=(10, 10))

        crypto_table = ctk.CTkFrame(self.crypto_frame)
        crypto_table.pack(fill="x", padx=10, pady=(0, 10))

        header_symbol = ctk.CTkLabel(crypto_table, text="Symbol", font=("Arial", 16, "bold"))
        header_price = ctk.CTkLabel(crypto_table, text="Cena (PLN)", font=("Arial", 16, "bold"))
        header_change = ctk.CTkLabel(crypto_table, text="Zmiana 24h", font=("Arial", 16, "bold"))
        header_symbol.grid(row=0, column=0, padx=10, pady=4, sticky="w")
        header_price.grid(row=0, column=1, padx=10, pady=4, sticky="w")
        header_change.grid(row=0, column=2, padx=10, pady=4, sticky="w")

        for row, (symbol, info) in enumerate(self.crypto_data.items(), start=1):
            price_text = f"{info.get('price', 0):,.2f}"
            change_value = info.get('change', 0.0)
            change_text = f"{change_value:+.2f}%"
            color = "#3BB33B" if change_value >= 0 else "#E25454"

            label_symbol = ctk.CTkLabel(crypto_table, text=symbol, font=("Arial", 14))
            label_price = ctk.CTkLabel(crypto_table, text=price_text, font=("Arial", 14))
            label_change = ctk.CTkLabel(crypto_table, text=change_text, font=("Arial", 14), text_color=color)

            label_symbol.grid(row=row, column=0, padx=10, pady=3, sticky="w")
            label_price.grid(row=row, column=1, padx=10, pady=3, sticky="w")
            label_change.grid(row=row, column=2, padx=10, pady=3, sticky="w")

    def create_converter(self):
        converter_title = ctk.CTkLabel(
            self.converter_frame,
            text="Konwerter walut",
            font=("Arial", 22, "bold")
        )
        converter_title.pack(pady=(10, 10))

        form_frame = ctk.CTkFrame(self.converter_frame)
        form_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.amount_entry = ctk.CTkEntry(form_frame, placeholder_text="Kwota")
        self.amount_entry.grid(row=0, column=0, padx=8, pady=8, sticky="ew")

        currency_options = ["PLN", "USD", "EUR", "GBP", "CHF"]
        self.from_currency = ctk.CTkOptionMenu(form_frame, values=currency_options)
        self.to_currency = ctk.CTkOptionMenu(form_frame, values=currency_options)
        self.from_currency.grid(row=0, column=1, padx=8, pady=8)
        self.to_currency.grid(row=0, column=2, padx=8, pady=8)

        self.from_currency.set("PLN")
        self.to_currency.set("USD")

        self.convert_button = ctk.CTkButton(
            form_frame,
            text="Konwertuj",
            command=self.convert_currency
        )
        self.convert_button.grid(row=0, column=3, padx=8, pady=8)

        self.result_label = ctk.CTkLabel(
            self.converter_frame,
            text="Wynik: -",
            font=("Arial", 16)
        )
        self.result_label.pack(pady=(8, 10))

        form_frame.grid_columnconfigure(0, weight=1)

    def convert_currency(self):
        amount_text = self.amount_entry.get().strip()
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        try:
            amount = float(amount_text.replace(",", "."))
        except ValueError:
            self.result_label.configure(text="Wprowadź poprawną kwotę.")
            return

        if from_curr == to_curr:
            result = amount
        else:
            if from_curr == "PLN":
                rate_from = 1.0
            else:
                rate_from = self.currency_data.get(from_curr)

            if to_curr == "PLN":
                rate_to = 1.0
            else:
                rate_to = self.currency_data.get(to_curr)

            if rate_from is None or rate_to is None:
                self.result_label.configure(text="Brak kursu dla wybranej waluty. Zaktualizuj dane.")
                return

            result = amount * (rate_from / rate_to)

        self.result_label.configure(text=f"Wynik: {result:,.4f} {to_curr}")
