Aby zademonstrować podstawowe użycie weryfikacji dwuetapowej oraz jej skuteczność wobec ataków, w szczególności typu brute force, został przygotowany program w języku Python służący do zarządzania hasłami.
Implementuje on zabezpieczenie MFA oraz pozwala na przetestowanie ataku brute force przeciwko niemu.

Proces rejestracji i logowania:
 
Po otwarciu aplikacji pojawia się okno umożliwiające rejestrację nowego użytkownika lub zalogowanie się do istniejącego konta.
1.	Podczas rejestracji, jeśli użytkownik poda nazwę, która już istnieje, lub pominie wymagane pola, wyświetlany jest odpowiedni komunikat o błędzie.
2.	W przeciwnym wypadku login i hasło użytkownika zostają zapisane w odpowiednim słowniku.
3.	Przejście dalej jest możliwe dopiero po podaniu poprawnej nazwy użytkownika i hasła – aplikacja sprawdza, czy znajdują się w bazie danych.
 
Weryfikacja dwuetapowa:
Po poprawnym zalogowaniu użytkownik musi przejść weryfikację dwuetapową, która odbywa się poprzez wiadomość e-mail wysyłaną na adres podany w aplikacji. Użytkownik może wybrać długość kodu wysyłanego na maila,
a następnie decyduje, jak chce przejść weryfikację:
 
1.	Ręczne wpisanie kodu (Enter Code):
 
a.	Wysyłany jest kod o określonej długości.
b.	W aplikacji pojawia się pole do jego wpisania.
c.	Jeśli użytkownik poda poprawny kod, otwiera się właściwe okno zarządzania hasłami.
d.	Jeśli kod jest błędny, generowany jest nowy, a poprzedni traci ważność. Dzięki temu tradycyjny atak brute force jest praktycznie niemożliwy – przy każdej niepoprawnej próbie kod zmienia się, więc
algorytm brute force nie ma szans na przetestowanie wszystkich kombinacji.

2.	Atak brute force (Bruteforce Attack):
a.	Wysyłany jest kod o określonej długości, a jego wartość wyświetla się w konsoli.
b.	Uruchamiany jest stoper o wartości 30 sekund.
c.	Algorytm brute force zaczyna generować wszystkie możliwe kombinacje, próbując odgadnąć kod.
d.	Jeśli w tym czasie znajdzie poprawny kod, aplikacja przechodzi do panelu zarządzania hasłami.
e.	Jeśli kod nie zostanie znaleziony w 30 sekund, wyświetla się komunikat o niepowodzeniu i użytkownik wraca do ekranu wyboru metody weryfikacji.
f.	Limit czasu 30 sekund został zastosowany w celu skutecznego uniemożliwienia złamania kodu atakiem brute force, jednocześnie pozostawiając użytkownikowi wystarczająco dużo czasu na ręczne wpisanie kodu.
Zarządzanie hasłami
 
Po przejściu weryfikacji dwuetapowej otwiera się okno zarządzania hasłami, które umożliwia:
1.	Wpisanie nazwy strony internetowej, e-maila/nazwy użytkownika oraz hasła i dodanie ich do listy istniejących już takich zbiorów w pliku json.
2.	Wygenerowanie bezpiecznego hasła, które znacząco utrudnia atak brute force, ponieważ wymaga znacznie większej mocy obliczeniowej do jego złamania, spełniającego określone kryteria:
a.	8–10 dużych i małych liter,
b.	2–4 znaki specjalne,
c.	2–4 cyfry.
3.	Po wygenerowaniu hasło jest automatycznie kopiowane do schowka użytkownika, co ułatwia jego wpisanie.
4.	Jeśli użytkownik chce odczytać zapisane hasło, może wpisać nazwę strony i wybrać opcję Search – wtedy wyświetli się odpowiedni komunikat zawierający dane logowania.
Na każdym etapie aplikacji widoczny jest przycisk Back, umożliwiający powrót do poprzedniego okna.
