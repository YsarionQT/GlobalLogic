# GlobalLogic
Vytvorte program, ktory bude spracuvat elementy na prikazovom riadku az po znak '.' Spracuva ich tak, ze vzdy porovna prvy a posledny element a ak su rovnake, oba elementy odstrani. Toto pravidlo sa opakuje, kym je mozne odstranit elementy. Inak program konci.
Uvazujme, ze 1 element je prave 1 znak.

Priklady:
$ program a b c .
$ a b c

$ program a b a .
$ a

$ program a b c b a .
$ c

$ program a b b a .
$ 
(^^^ prazdny riadok)


Poziadavky pri vypracovani: 

    pouzite python3, venv, dogygen, pytest
    vypracujte riesenie, aby pylint mal hodnotenie aspon 8.00
    vytvorte modul pre logovanie 'spravania sa programu' do log suboru
    riesenie ulozene na github.com



