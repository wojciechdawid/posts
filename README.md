Utworzyc nowy projekt z aplikacją posts W aplikacji utworzyc model (Djangowy) Post (wpis na bloga)

title: CharField(max_length=255)
content: TextField()
created_at: DateTimeField(auto_now_add=True)
updated_at: DateTimeField(auto_now=True)
Utworzyc stron z lista postow

GET /posts -> lista postow (plus formularz do tworzenia nowego postu) POST /posts -> dodanie nowego Postu

GET /posts/1

Wyświetlenie szczegółw postu

Szokujaca wiadomosc (utworzono: 2023-11-18 12:21)

Programiści nie napisali serwisów w swoich aplikacjach

dodatkowo: repo na github dodatkowo: wprowadzenie Serwisu - analogicznie do tego co mamy wczesniej (oparty o faker)