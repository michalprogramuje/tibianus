TODO 

Done:
Stworzyć tabele z relacją (do tabeli characters): [X]
    loyality_level_points_table [X] ŁW 
    loyality_trade_points_table [X] ŁW
    Jednak tutaj będzie bez tych tabel (są niepotrzebne)
Stworzyć tabelę rang (nazwa_rangi) ŁW [X]
Stworzyć tabelę przechowującą osiągnięcia ŁW [X]    
Znaleźć sposób na dziedzieczenie szablonów ŁW [X]
Uporządkować kod [X]


ToDo:
MZ:
Musimy stworzyć tabele, która bedzie przechowywala taski. 
Uzgodnilismy ze kazde zadanie bedzie należeć do określonej grupy (bardzo łatwe, łatwe, normalne, średnie, trudne, bardzo trudne).
Ich ilość jest zgodna z ilością rang (możesz to zmienić w taki sposób jaki uznasz za stosowny, np jedna ranga => kilka poziomów trudności) 
- Tak czy inaczej, będziesz musiał stworzyć jedną tabelę (model), w której będą przechowywane poziomy trudności (wystarczy sama nazwa poziomu trudności. kolumna dla ID     generuje się automatycznie; zerknij na models.py i zobacz jak ja to robilem)
- Następnie stwórz drugą tabelę (model), który bedzie przechowywać informacje na temat zadań np.
  * nazwa_taska
  * poziom_trudności (tutaj musi być relacja z tabelą poziomów trudności)
  * minimalna_ilość_loyality_level_point (minimalna ilosc punktow do zdobycia za wykonanie taska)
  * maxymalna_ilosc_loyality_level_point (maksymalna ilosc punktow do zdobycia za wykonanie taska)
  * minimalna_ilosc_loyality_trade_point (minimalna ilosc punktow handlu do zdobycia za wykonanie taska)
  * maxymalna_ilosc_loyality_trade_point (maksymalna ilosc punktow handlu do zdobycia za wykonanie taska)

Możesz jeszcze sobie tam pododawać coś wedle uznania. Finalnie musimy zrobić tak, że wykonane taski będą dodawane na konto określonej postaci (model Character).
Najprawdopodobniej zrobimy kolejną tabelę ManyToMany w ktorej po prostu będziemy przechowywać rekordy id_character + id_task + status; w momencie jak ktos z nas wylosuje dany task to automatycznie bedzie taki rekord dodawany do bazki. Po wykonaniu bedziemy aktualizowac status w profilu np. 

Narazie skup sie na tym, pomysl czy takie cos moze byc czy jednak znasz lepszy sposob oraz masz w glowie inne rozwiazanie + koncepcje. Rob tak jak uwazasz. Ponizej wklejam wczesniejszy zamysl/sciage. 


# Założonka

1. Każdy  gracz rozpoczyna rozgrywkę od 0 ilości Loyality Level Points oraz 0 ilości Loyality Trade Points
2. Aby zdobywać Loyality Level Points oraz Loyality Trade Points, należy wykonywać tzw taski
3. Każdy task należy do określonej grupy Loyality Level Tasks: 
   Gracz zaczyna rozgrywkę od poziomu adepta. Aby awansować do pierwszej gildyjnej grupy - Rogue - musi zdobyć minimum 1 Loyality Level Point, który uzyska:
   a) Zdobycie achievementu 'Become a little hero' czyli wykonaniu questu Dawnport 
   b) Zdobycie achievementu 'Dawnport rich man' czyli przejściu na mainland z budżetem 1k gold (1000gp)
   c) Zdobycie achievementu 'Rookslayer' czyli wbicia 8 lvla na starym rookgardzie 
   d) Zdobycie achievementu 'Snapper Killer' czyli zabiciu bossa krokodyli dostępnego po wykonaniu taska na 300 krokodyli u     Grizzly Adamsa
   e) Zdobycie achievementu '7 days streaker' czyli zdobycia 7 nagród daily 
   f) Zdobycie achievementu 'Faster then furious' czyli wbiciu 20 lvla w ciągu 24h 
   !!!  Jeżeli gracz ma >= 1 Loyality Level Point, nie ma możliwości wykonania kolejnych zadań z poziomu adepta !!!

4. Gdy gracz osiągnie poziom adepta, ma możliwość zdobycia kolejnych rang: 
   a) Rogue (łotrzyk) (przedział zadań od [5-20] Loyality Level Points, Loyality Trade Points [1-10])
   b) Chaplain (kapelan) (przedział zadań [21-40] Loyality Level Points, Loyality Trade Points [11-20))
   c) Grand Admiral (wielki admirał) (przedział [41-60] Loyality Level Points, Loyality Trade Points [21-30])
   d) Herald (przedział zadań [71 - 89] Loyality Level Points, Loyality Trade Points [31-40])
   e) Warmaster (mistrz wojenny xD) (przedział zadań [90] Loyality Level Points, Loyality Trade Points [41-50])

5. Każdy item w store kosztuje określoną ilość Loyality Trade Points. Ich ilość jest zależna od poziomu unikalności przedmiotu:
   a) Worthless (brak ramki w przedmiocie) - 1-10 Loyality Trade Points 
   a) Common (szara ramka) - 11-30 Loyality Trade Points 
   b) Uncommon (zielona ramka) - 31-100 Loyality Trade Points 
   c) Semi-rare (niebieska ramka) - 101-250 Loyality Trade Points
   d) Rare (fioletowa ramka) - 251-500 Loyality Trade Points
   e) Very Rare (Żółta ramka) - 501-900 Loyality Trade Points
Jeżeli przedmiot należy do określonej grupy unikalności, generator losuje ilość wymaganej puli Loyality Trade Points aby gracz wiedział, ile LTP musi zapłacić za możliwość kupna przedmiotu na markiecie (czy też od innego gracza). Przykład:
Gracz posiada uzbieraną pulę 300 Loyality Trade Points. Chce kupić Bohy na markiecie. Bohy należą do grupy semi-rare, a więc generator ma prawo wylosować mu wymaganą pulę Loyality Trade Points z przedziału od 101 do 250. Najpierw generator weryfikuje, czy gracz ma wymaganą ilość Loyality Trade Points. Jeżeli tak - generator rozpoczyna pracę. W innym przypadku - przerywa. W ramach przykładu - gracz ma wymaganą ilość punktów.
Generator wylosował liczbę 131. Aby gracz mógł mieć możliwość kupna BOH'ów, musi zapłacić najpierw 131 Loyality Trade Points, czyli 300 - 131 = 169 (tyle punktów zostanie mu na jego koncie, jeżeli zdecyduje się na kupno bohów). 
Koszt danego przedmiotu nie jest stały. W momencie gdy gracz zechce po raz kolejny kupić bohy, musi znowu użyć generatora w celu wylosowania kosztu Loyality Trade Points. 
!Gracz nie ma możliwości rezygnacji z kupna przedmiotu po uruchomieniu generatora!
!Gdy gracz zdecyduje się na sprzedaż kupionego przedmiotu, Loyality Trade Points nie zostają mu zwrócone! 





