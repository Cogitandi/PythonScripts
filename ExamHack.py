import pyperclip
import tkinter as tk
import keyboard

odp = {
'Proszę precyzyjnie opisać związek pomiędzy encjami ORDER i ORDER_ITEM:' : 'Zamówienie (ORDER) musi zawierać co najmniej jedną pozycję (ORDER_ITEM), a każda pozycja zamówienia musi należeć dokładnie do jednego zamówienia.',
'Proszę wskazać cechy charakterystyczne dla podzapytania zwykłego:' : 'Wykonuje się dokładnie jeden raz,Wykonuje się jako pierwsze, dostarczając danych do zapytania nadrzędnego',
'Proszę dokładnie opisać związek między encją OBYWATEL i encją PASZPORT:'	:	'Obywatel może posiadać (ale nie musi) jeden paszport, natomiast paszport musi należeć tylko do jednego obywatela.',
'Co obejmuje spójność bazy danych?'	:	'1.	Poprawność danych w przypadku awarii sprzętowo-programowych 2.	Poprawność danych z punktu widzenia pewnych przyjętych kryteriów 3.	Odporność na przypadkowe błędy użytkowników',
'Proszę wskazać funkcje Systemu Zarządzania Bazą Danych:'	:	'''1.	Autoryzacja dostępu do danych
2.	Zapewnienie bezpieczeństwa danych w przypadku awarii sprzętowo-programowej,
Optymalizacja dostępu do danych,
6.	Zapewnienie współbieżnego dostępu do danych,
7.	Zapewnienie efektywnego składowania i przetwarzania dużych wolumenów danych,
8.	Wsparcie dla języka bazy danych, umożliwiającego m.in. wstawianie, modyfikowanie, usuwanie i wyszukiwanie danych oraz tworzenie, modyfikowanie i usuwanie struktur danych''',
'Wskaż poprawne, z punktu widzenia składni, polecenie (zakładamy, że podane kolumny istnieją we wskazanej tabeli):'	:	'1.	SELECT kolumna1, COUNT(*) FROM tabela GROUP BY kolumna1,2.	SELECT DISTINCT kolumna1 FROM tabela ORDER BY kolumna2 ;3.  SELECT MIN(kolumna2), MAX(kolumna2) FROM tabela GROUP BY kolumna1;4.  SELECT COUNT(*) FROM tabela GROUP BY kolumna1, kolumna2 ;',
'Proszę wskazać systemy klasy OLTP:'	:	'''5.	System obsługi zamówień
6.	System obsługi klienta
7.	System prognozowania sprzedaży
8.	System ewidencji czasu pracy''',
'''System Zarządzania Bazą Danych to:'''	:	'''Jest to oprogramowanie, którego zadaniem jest zarządzanie całą bazą danych oraz realizowanie żądań aplikacji użytkowników.''',
'''Proszę wskazać cechy charakterystyczne transformacji związku M:N do postaci modelu relacyjnego:'''	:	'''2.	Związek M:N jest reprezentowany w modelu relacyjnym poprzez dodatkową relację
3.	Dodatkowa relacja zawiera klucze obce wskazujące na klucze podstawowe relacji powstałych z powiązanych encji
Klucze obce w dodatkowej relacji tworzą klucz podstawowy tej relacji
''',
'''Co przechowuje tabela faktu w hurtowni danych?'''	:	'''Dane opisujące analizowany obszar rzeczywistości''',
'''Na czym polega operacja projekcji?'''	:	'''Jest to wyodrębnienie wybranych atrybutów relacji''',
'''Wskaż poprawne, z punktu widzenia składni, polecenie (zakładamy, że podane kolumny istnieją
we wskazanej tabeli):'''	:	'''SELECT kolumna1, COUNT(*) FROM tabela GROUP BY kolumna1 ;
wszystkie''',
'''System Zarządzania Bazą Danych to:'''	:	'''Jest to oprogramowanie, którego zadaniem jest zarządzanie całą bazą danych oraz realizowanie żądań aplikacji użytkowników.''',
'''Wskaż poprawne reguły transformacji encji:'''	:	'''2.	Atrybut encji jest odwzorowywany w atrybut relacji
3.	Unikalny identyfikator encji jest transformowany w klucz podstawowy relacji
4.	Encja jest odwzorowywana w relację
5.	Obowiązkowość atrybutów encji jest reprezentowana w relacji w postaci ograniczenia NOT NULL zdefiniowanego na atrybucie relacji odpowiadającym atrybutowi encji
6.	Nazwy atrybutów encji są odwzorowywane w nazwy atrybutów relacji.
''',
'''Proszę wskazać cechy charakterystyczne dla tabeli wymiaru:'''	:	'''Posiada kolumny umożliwiające opis poszczególnych poziomów hierarchii wymiaru''',
'''Na czym polega operacja selekcji?'''	:	'''Jest to wyodrębnienie podzbioru krotek relacji, które spełniają warunek selekcji''',
'''Jakie cechy posiada klucz obcy (FOREIGN KEY)?'''	:	'''1.	Jest pojedynczym atrybutem (lub zbiorem atrybutów), który wskazuje na klucz podstawowy w innej relacji
2.	Dziedziną wartości klucza obcego jest dziedzina wartości klucza podstawowego, na który ten klucz obcy wskazuje
''',
'''Proszę wskazać systemy klasy OLAP:'''	:	'''System analizy efektywności szkoleń
3.	System wspomagania decyzji sprzedażowych
4.	System oceny jakości obsługi klienta
''',
'''Proszę wskazać rodzaje modeli danych, możliwe do wykorzystania w modelowaniu baz danych:'''	:	'''1.	Relacyjno-obiektowy
2.	Hierarchiczny
3.	Sieciowy
Relacyjny''',
'''Proszę wskazać te modele danych, które wykorzystuje się najczęściej w modelowaniu współczesnych baz danych:'''	:	'''2.	Obiektowo-relacyjny
3.	Obiektowy
Relacyjny''',
'''Proszę wskazać cechy relacji:'''	:	'''2.	Relacja nie zawiera powtarzających się krotek
3.	Kolejność atrybutów relacji nie ma znaczenia
4.	Nazwy atrybutów relacji są unikalne
7.	Kolejność krotek relacji nie ma znaczenia
8.	Wartości atrybutów relacji mają charakter niepodzielny
''',
'''Hurtownia danych to:'''	:	'''Baza danych wspomagająca procesy decyzyjne''',
'''Proszę wskazać elementy, które definiowane są w ramach modelu związków-encji:'''	:	''' Encje,6.	Atrybuty encji
7.	Związki między encjami
''',
'''Jakie cechy posiada klucz podstawowy relacji?'''	:	'''Przyjmuje wartości określone (NOT NULL),
Przyjmuje unikalne wartości''',
'''Proszę wskazać cechy charakterystyczne dla podzapytania skorelowanego:'''	:	'''Zawiera odwołanie do kolumny z zapytania nadrzędnego,Wykonuje się wiele razy''',
'''Co można umieścić po klauzuli ORDER BY w poleceniu SELECT jako kryterium sortowania:'''	:	'''Dowolną kolumnę tabeli, wykorzystanej w poleceniu SELECT
3.	Alias wyrażenia, zdefiniowanego na liście kolumn po słowie SELECT
4.	Liczbę wskazującą na pozycję kolumny na liście kolumn po słowie SELECT
''',
'''Proszę wskazać cechy charakterystyczne transformacji związku 1:M:'''	:	'''1.	Klucz obcy dodany do relacji po stronie "wiele" musi przyjmować wartość różną od NULL w przypadku wystąpienia obowiązkowości związku po stronie "wiele"
2.	Klucz obcy jest dodawany do relacji po stronie "wiele"
3.	Klucz obcy dodany do relacji po stronie "wiele" może przyjmować wartość NULL w przypadku wystąpienia opcjonalności związku po stronie "wiele"
''',
'''Co składa się na definicję schematu relacji?'''	:	'''.  Definicja atrybutów, ich dziedzin oraz ograniczeń integralnościowych nałożonych na atrybuty''',
'''Czym jest deskryptor encji?'''	:	'''Jest to atrybut (różny od identyfikatora encji) opisujący cechę encji.''',
'''Wskaż cechy związku między encjami:'''	:	'''Klasa przynależności
3.	Typ asocjacji
4.	Stopień związku
''',
'''Które ograniczenia integralnościowe można definiować TYLKO na poziomie pojedynczego atrybutu?'''	:	'''NOT NULL''',
'''Proszę wskazać cechy charakterystyczne dla tabeli faktu:'''	:	'''Posiada kolumny będące kluczami obcymi do tabel wymiarów
Posiada kolumny przechowujące wartości dla poszczególnych miar''',
'''Proszę wskazać poprawne polecenie SELECT, które dla każdego produktu wyznaczy liczbę zamówionych sztuk:'''	:	'''SELECT PRODUKT_NAZWA, (SELECT SUM(ILOSC) FROM SZCZEGOLY_ZAMOWIENIA WHERE PRODUKT_ID = P.PRODUKT_ID) AS RAZEM_ILOSC FROM PRODUKTY P;''',
'''Schemat bazy danych to:'''	:	'''Struktura danych i powiązania między nimi.''',
'''Czym jest identyfikator encji?'''	:	'''.  Jest to pojedynczy atrybut (lub zbiór atrybutów) umożliwiający jednoznaczną identyfikację encji.''',
'''Proszę wskazać miejsca w instrukcji SELECT, w których może wystąpić podzapytanie:'''	:	'''1.	Warunek w klauzuli WHERE
2.	Warunek w klauzuli HAVING
4.	Jako źródło danych po słowie JOIN
5.	Jako kolumna na liście kolumn po słowie SELECT
Jako źródło danych po słowie FROM''',
'''Co to jest encja?'''	:	''' Jest to zbiór obiektów opisany tymi samymi cechami''',
'''Proszę wskazać cechy charakterystyczne transformacji binarnego związku 1:1 do postaci relacyjnej:'''	:	'''1.	Dla związku jednostronnie obowiązkowego klucz obcy dodawany jest w relacji po stronie związku obowiązkowego
2.	Dla związku jednostronnie obowiązkowego klucz obcy nie może przyjmować wartości równych NULL
3.	Klucz obcy jest dodawany do jednej lub obydwu relacji po stronie "jeden"
''',
'''Transakcja to:'''	:	'''Zbiór akcji wykonywanych wszystkie albo żadna''',
'''Warunki integralności danych to:'''	:	'''Warunki jakie muszą spełniać dane wprowadzane do bazy danych''',
'''Normalizacja bazy danych to proces, który prowadzi do:'''	:	'''Uproszczenia struktury tabel i eliminacji redundancji danych''',
'''Integralność danych to:'''	:	'''Poprawność wartości danych w bazie danych z ich wartościami występującymi w rzeczywistości.''',
'''Integralność referencyjna oznacza:'''	:	'''Istnienie dokładnie jednej wartości klucza głównego dla każdej wartości klucza obcego''',
'''Do czego służy klauzula HAVING w poleceniu SELECT:'''	:	'''Do definiowania warunku dla grup rekordów''',
'''Co przechowuje tabela wymiaru w hurtowni danych:'''	:	'''1.	Dane umożliwiające opis analizowanego obszaru z wybranego punktu widzenia
2.	Dane opisujące poziomy hierarchii wymiaru
''',
'''Do czego wykorzystuje się hierarchię wymiaru:'''	:	'''1.	Do analizowania faktu z różnym stopniem szczegółowości w ramach danego wymiaru
''',
'''Co może zawierać warunek, zdefiniowany po klauzuli HAVING?'''	:	'''Funkcje agregacji np. COUNT, MIN, MAX
Dowolną kolumnę wymienioną po klauzuli GROUP BY''',
'''Wymich operacje wykonywane na rekordach w relacyjnych bazach danych'''	:	'''Selekcja
3.	Złączenie
4.	Projekcja
''',
'''Która cecha dotyczy klucza unikalnego w tabeli relacyjnej:'''	:	'''.  Unikalność wartości
.  Określoność wartości''',
'''Co jest potrzebne do odtworzenia stanu spójnego po awarii systemowej?'''	:	'''Baza danych i dziennik''',
'''Co jest potrzebne do odtwarzania stanu spójnego po awarii sprzętowej?'''	:	'''Kopia bazy danych''',
'''Co mówi o ilości powiązanych tabel (relacji)?'''	:	'''Stopien''',
'''Jakie mogą być rodzaje kluczy w RBD?'''	:	'''1.	Klucz podstawowy (primary key)
2.	Klucz obcy
3.	Klucz unikalny
''',
'''Jakie sa cech transakcji'''	:	'''1.	Atomowość
2.	Trwałość
3.	Spójność
4.	Izolacja
''',
'''Zadania DDL'''	:	'''1.	Definiowanie i nazywanie klas obiektów oraz określanie powiązań między nimi
2.	Tworzenie, modyfikacja schematu wewnętrznego, pojęciowego i schematów zewnętrznych
''',
'''Proszę wskazać niemożliwą do wykonania kombinację operacji bazodanowych:'''	:	'''Projekcja, Złączenie''',
'''Co rozumiesz pod pojęciem „Encja”:'''	:	''' Indywidualny, rozpoznawalny w rzeczywistości obiekt''',
'''W jakim celu definiuje się warunki integralności:'''	:	'''Zapewnienia zgodności danych w bazie danych ze stanem faktycznym istniejącym w rzeczywistości''',
'Czym jest baza danych'	:	'Czym jest baza danych',
'Która z niżej wymienionych operacji nie jest wykonywana w bd'	:	'iniekcja',
'''Jakie podstawowe operacje algebry relacji wykonuje się na relacjach?''' : '''1. Część wspólna zbiorów
3. Suma zbiorów
4. Projekcja
5. Połączenie
6. Selekcja
7. Różnica zbiorów''',
}


def show(text):
    root = tk.Tk()
    root.overrideredirect(1);
    tk.Label(root, text=text).pack()
    root.after(3000, lambda: root.destroy())     # time in ms
    root.attributes('-topmost', True) # note - before topmost
    root.mainloop()
    
def findAnswer(question):
    for element in odp:
        if keyboard.is_pressed('q'):
            break
        if(element.find(question) != -1):
            show(odp.get(element));
        


pquestion = pyperclip.paste(); 
while True:
    question = pyperclip.paste();
    if question != pquestion:
        answser = findAnswer(question);
        pquestion = question;
        

