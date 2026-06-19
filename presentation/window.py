from domain.repositories import CurrencyRepository
import customtkinter as ctk

class App(ctk.CTk):
    PALETTE = {
        "bg":          "#7a7c83",
        "card":        "#1a1d27",
        "card2":       "#21253a",
        "accent":      "#4f8ef7",
        "accent2":     "#7c5cbf",
        "text":        "#e8eaf6",
        "fg":          "#e8eaf6",
        "text_dim":    "#7b82a6",
        "success":     "#4caf7d",
        "warning":     "#f5a623",
        "error":       "#e05c5c",
        "border":      "#2d3154",
    }
    
    def __init__(self, repo : CurrencyRepository):
        
        super().__init__()
        self.title("Currency Dashboard")
        self.geometry("900x700")
        self.configure(bg=self.PALETTE["bg"])

        self.repo = repo
        self.currency_list: dict[str, float] = {}
        self.currency_list_frame = None

        self.base_currency_var = ctk.StringVar(value=self.repo.get_base_currency())
        self.converter_amount = ctk.StringVar(value="1")
        self.converter_source = ctk.StringVar()
        self.converter_target = ctk.StringVar()
        self.converter_result = ctk.StringVar(value="")
        self.converter_error = ctk.StringVar(value="")

        self.BaseCurrencyInput(self)
        self.CurrencyCalculator(self)

        self.ShowCurrencyList()
        self._update_converter_options()

    def BaseCurrencyInput(self, parent):
        frame = ctk.CTkFrame(parent, bg_color=self.PALETTE["card"], fg_color=self.PALETTE["card"])
        frame.pack(fill="x", padx=20, pady=10)

        label = ctk.CTkLabel(frame, text="Base Currency:", fg_color=self.PALETTE["card"], text_color=self.PALETTE["text"])
        label.pack(side="left", padx=10)

        self.base_currency_menu = ctk.CTkComboBox(
            frame,
            values=sorted(self.repo.get_list()),
            variable=self.base_currency_var,
            fg_color=self.PALETTE["card2"],
            button_color=self.PALETTE["accent"],
            text_color=self.PALETTE["text"],
            width=120,
        )
        self.base_currency_menu.pack(side="left", padx=10)
        
        self.base_currency_error = ctk.CTkLabel(
            frame,
            text="",
            fg_color=self.PALETTE["card"],
            text_color=self.PALETTE["error"]
        )

        button = ctk.CTkButton(
            frame,
            text="Load",
            fg_color=self.PALETTE["accent"],
            command=self._ChangeBaseCurrency,
        )
        button.pack(side="left", padx=10)

        self.base_currency_label = ctk.CTkLabel(
            frame,
            text=f"Current base: {self.repo.get_base_currency()}",
            fg_color=self.PALETTE["card"],
            text_color=self.PALETTE["text"],
        )
        self.base_currency_label.pack(side="right", padx=10)

    def CurrencyCalculator(self, parent):
        frame = ctk.CTkFrame(parent, bg_color=self.PALETTE["card"], fg_color=self.PALETTE["card"])
        frame.pack(fill="x", padx=20, pady=(0, 10))

        title = ctk.CTkLabel(frame, text="Kalkulator walut", fg_color=self.PALETTE["card"], text_color=self.PALETTE["text"], font=ctk.CTkFont(size=16, weight="bold"))
        title.grid(row=0, column=0, columnspan=5, sticky="w", padx=10, pady=(10, 5))

        amount_entry = ctk.CTkEntry(frame, width=120, fg_color=self.PALETTE["card2"], text_color=self.PALETTE["text"], textvariable=self.converter_amount)
        amount_entry.grid(row=1, column=0, padx=5, pady=5)

        self.source_menu = ctk.CTkOptionMenu(frame, values=sorted(self.currency_list.keys()), variable=self.converter_source, fg_color=self.PALETTE["card2"], button_color=self.PALETTE["accent"], text_color=self.PALETTE["text"])
        self.source_menu.grid(row=1, column=1, padx=5, pady=5)

        arrow_label = ctk.CTkLabel(frame, text="→", fg_color=self.PALETTE["card"], text_color=self.PALETTE["text"], font=ctk.CTkFont(size=18))
        arrow_label.grid(row=1, column=2, padx=5)

        self.target_menu = ctk.CTkOptionMenu(frame, values=sorted(self.currency_list.keys()), variable=self.converter_target, fg_color=self.PALETTE["card2"], button_color=self.PALETTE["accent"], text_color=self.PALETTE["text"])
        self.target_menu.grid(row=1, column=3, padx=5, pady=5)

        convert_button = ctk.CTkButton(frame, text="Przelicz", fg_color=self.PALETTE["success"], command=self._ConvertCurrency)
        convert_button.grid(row=1, column=4, padx=10, pady=5)

        self.result_label = ctk.CTkLabel(frame, textvariable=self.converter_result, fg_color=self.PALETTE["card"], text_color=self.PALETTE["text"])
        self.result_label.grid(row=2, column=0, columnspan=5, sticky="w", padx=10, pady=(5, 5))

        self.error_label = ctk.CTkLabel(frame, textvariable=self.converter_error, fg_color=self.PALETTE["card"], text_color=self.PALETTE["error"])
        self.error_label.grid(row=3, column=0, columnspan=5, sticky="w", padx=10, pady=(0, 10))

    def _update_converter_options(self):
        values = sorted(self.currency_list.keys())
        if not values:
            return

        if self.converter_source.get() not in values:
            self.converter_source.set(values[0])
        if self.converter_target.get() not in values:
            self.converter_target.set(values[1] if len(values) > 1 else values[0])

        self.source_menu.configure(values=values)
        self.target_menu.configure(values=values)

    def ShowCurrencyList(self):
        if self.currency_list_frame is None:
            frame = ctk.CTkScrollableFrame(self, bg_color=self.PALETTE["card"])
            frame.pack(fill="both", expand=True, padx=20, pady=20)
            self.currency_list_frame = frame
        else:
            for child in self.currency_list_frame.winfo_children():
                child.destroy()
            frame = self.currency_list_frame

        rates = self.repo.get_currencies_list()
        self.currency_list = rates or {}

        for code, rate in sorted(self.currency_list.items()):
            item_frame = ctk.CTkFrame(frame, bg_color=self.PALETTE["card2"], fg_color=self.PALETTE["card2"])
            item_frame.pack(fill="x", pady=5, padx=10)
            text_label = ctk.CTkLabel(
                item_frame,
                text=f"{code} : {rate}",
                padx=10,
                pady=5,
                fg_color=self.PALETTE["card2"],
                text_color=self.PALETTE["text"],
            )
            text_label.pack(side="left", padx=10)
            
    def _ConvertCurrency(self):
        self.converter_error.set("")
        try:
            amount = float(self.converter_amount.get().replace(",", "."))
        except ValueError:
            self.converter_error.set("Podaj prawidłową kwotę.")
            self.converter_result.set("")
            return

        source = self.converter_source.get()
        target = self.converter_target.get()

        if source not in self.currency_list or target not in self.currency_list:
            self.converter_error.set("Wybierz poprawne waluty.")
            self.converter_result.set("")
            return

        source_rate = float(self.currency_list.get(source, 0))
        target_rate = float(self.currency_list.get(target, 0))

        if source_rate == 0:
            self.converter_error.set("Nie można przeliczyć dla wybranej waluty.")
            self.converter_result.set("")
            return

        converted = amount / source_rate * target_rate
        self.converter_result.set(f"{amount:.2f} {source} = {converted:.2f} {target}")

    def _ChangeBaseCurrency(self):
        new_base = self.base_currency_var.get().strip().upper()
        if not new_base or new_base not in self.repo.get_list():
            self.base_currency_error.configure(text="Podaj kod waluty. np: PLN")
            return

        #self.repo.change_base_currency(new_base)
        self.base_currency_var.set(new_base)
        self.base_currency_menu.set(new_base)
        self.base_currency_error.configure(text="")
        self._UpdateCurrencyList()
        
    def _UpdateCurrencyList(self):
        self.base_currency_label.configure(text=f"Current base: {self.repo.get_base_currency()}")
        self._update_converter_options()
        self.ShowCurrencyList()
        self.converter_result.set("")
        self.converter_error.set("")