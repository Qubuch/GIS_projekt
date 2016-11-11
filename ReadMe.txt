Temat projektu dotyczy znajdowania wszystkich silnie spójnych sk³adowych grafu skierowanego.
Grafem silnie spójnym nazywamy graf, w którym dla kazdej pary wierzcho³ków i oraz j
istnieje droga z i do j oraz z droga z j do i. Sk³adowa silnie spójna pewnego grafu (w skrócie
SSS) nazywamy maksymalny podgraf tego grafu, który jednoczesnie jest silnie spójny. Nie
beda rozpatrywane grafy nieskierowane. Zak³adamy, ze wszystkie grafy, o których mowa w
dalszej czesci pracy sa skierowane.
Celem projektu jest implementacja dwóch algorytmów znajdowania wszystkich SSS zadanego
grafu, przetestowanie ich, wyznaczenie ich z³oznosci obliczeniowej i przeprowadzenie
eksperymentów majacych potwierdzic wyznaczona z³oznosc obilczeniowa.

Niech n okresla liczbe wierzcho³ków w zadanym grafie, a m liczbe krawedzi. Graf w programie
bedzie reprezentowany za pomoca listy sasiedztwa, dzieki czemu z³ozonosc przejscia
grafu w g³ab to O(n + m) (jest liniowa). W ramach projektu zrealizowane beda dwa algorytmy,
których pseudokod przedstawiono ponizej. Ich implementacja zostanie wykonana w
jezyku Python z wykorzystaniem standardowych struktur danych dostepnych w tym jezyku.
Do reprezentacji grafu wystarczy lista zbiorów liczb ca³kowitych (tzn. typ ”list” zawierajacy
elementy typu ”set”, z których kazdy zawiera elementy typu ”int”). Do realizacji stosu
zostanie wykorzystany typ ”list”.