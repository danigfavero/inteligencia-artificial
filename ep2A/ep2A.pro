%%%%% Insira aqui os seus predicados.
%%%%% Use quantos predicados auxiliares julgar necessario


% Exercício 1


% Exercício 2
esta_contido([], _).
esta_contido([C|Cs], Ds) :-
    member(C, Ds),
    esta_contido(Cs, Ds).

mesmo_conjunto(Cs, Ds) :-
    length(Cs, L),
    length(Ds, L),
    esta_contido(Cs, Ds),
    esta_contido(Ds, Cs).

% Exercício 3
uniao_conjunto([], Cs, Cs).
uniao_conjunto([C | Cs], Ds, Es) :-
    member(C, Ds),
    uniao_conjunto(Cs, Ds, Es).
uniao_conjunto([C | Cs], Ds, [C | Es]) :-
    \+ member(C, Ds),
    uniao_conjunto(Cs, Ds, Es).

% Exercício 4
inter_conjunto([], _, []).
inter_conjunto([C | Cs], Ds, Es) :-
    \+ member(C, Ds),
    inter_conjunto(Cs, Ds, Es).
inter_conjunto([C | Cs], Ds, [C | Es]) :-
    member(C, Ds),
    inter_conjunto(Cs, Ds, Es).

% Exercício 5
diferenca_conjunto([], _, []).
diferenca_conjunto(Cs, [], Cs).
diferenca_conjunto([C | Cs], Ds, Es) :-
    member(C, Ds),
    diferenca_conjunto(Cs, Ds, Es).
diferenca_conjunto([C | Cs], Ds, [C | Es]) :-
    \+ member(C, Ds),
    diferenca_conjunto(Cs, Ds, Es).


%%%%%%%% Fim dos predicados adicionados
%%%%%%%% Os testes comecam aqui.
%%%%%%%% Para executar os testes, use a consulta:   ?- run_tests.

%%%%%%%% Mais informacoes sobre testes podem ser encontradas em:
%%%%%%%%    https://www.swi-prolog.org/pldoc/package/plunit.html

:- begin_tests(conjuntos).
test(lista_para_conjunto, all(Xs=[[1,a,3,4]]) ) :-
    lista_para_conjunto([1,a,3,3,a,1,4], Xs).
test(lista_para_conjunto2,fail) :-
    lista_para_conjunto([1,a,3,3,a,1,4], [a,1,3,4]).

test(mesmo_conjunto, set(Xs=[[1,a,3],[1,3,a],[a,1,3],[a,3,1],[3,a,1],[3,1,a]])) :-
    mesmo_conjunto([1,a,3], Xs).
test(uniao_conjunto2,fail) :-
    mesmo_conjunto([1,a,3,4], [1,3,4]).

test(uniao_conjunto, set(Ys==[[1,a,3],[1,3,a],[a,1,3],[a,3,1],[3,a,1],[3,1,a]])) :-
    uniao_conjunto([1,a], [a,3], Xs),
    mesmo_conjunto(Xs,Ys).
test(uniao_conjunto2,fail) :-
    uniao_conjunto([1,a,3,4], [1,2,3,4], [1,1,a,2,3,3,4,4]).

test(inter_conjunto, all(Xs==[[1,3,4]])) :-
    inter_conjunto([1,a,3,4], [1,2,3,4], Xs).
test(inter_conjunto2,fail) :-
    inter_conjunto([1,a,3,4], [1,2,3,4], [1,1,3,3,4,4]).

test(diferenca_conjunto, all(Xs==[[2]])) :-
    diferenca_conjunto([1,2,3], [3,a,1], Xs).
test(diferenca_conjunto2,fail) :-
    diferenca_conjunto([1,3,4], [1,2,3,4], [_|_]).

:- end_tests(conjuntos).
