Temat projektu dotyczy znajdowania wszystkich silnie sp�jnych sk�adowych grafu skierowanego.
Grafem silnie sp�jnym nazywamy graf, w kt�rym dla kazdej pary wierzcho�k�w i oraz j
istnieje droga z i do j oraz z droga z j do i. Sk�adowa silnie sp�jna pewnego grafu (w skr�cie
SSS) nazywamy maksymalny podgraf tego grafu, kt�ry jednoczesnie jest silnie sp�jny. Nie
beda rozpatrywane grafy nieskierowane. Zak�adamy, ze wszystkie grafy, o kt�rych mowa w
dalszej czesci pracy sa skierowane.
Celem projektu jest implementacja dw�ch algorytm�w znajdowania wszystkich SSS zadanego
grafu, przetestowanie ich, wyznaczenie ich z�oznosci obliczeniowej i przeprowadzenie
eksperyment�w majacych potwierdzic wyznaczona z�oznosc obilczeniowa.

Niech n okresla liczbe wierzcho�k�w w zadanym grafie, a m liczbe krawedzi. Graf w programie
bedzie reprezentowany za pomoca listy sasiedztwa, dzieki czemu z�ozonosc przejscia
grafu w g�ab to O(n + m) (jest liniowa). W ramach projektu zrealizowane beda dwa algorytmy,
kt�rych pseudokod przedstawiono ponizej. Ich implementacja zostanie wykonana w
jezyku Python z wykorzystaniem standardowych struktur danych dostepnych w tym jezyku.
Do reprezentacji grafu wystarczy lista zbior�w liczb ca�kowitych (tzn. typ �list� zawierajacy
elementy typu �set�, z kt�rych kazdy zawiera elementy typu �int�). Do realizacji stosu
zostanie wykorzystany typ �list�.