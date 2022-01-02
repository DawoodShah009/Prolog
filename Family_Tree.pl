%MianBiwi

mianbiwi(chotakhan,chotirani).
mianbiwi(barakhan,barirani).
mianbiwi(salim,kausar).
mianbiwi(asad,sumra).
mianbiwi(nadir,nahid).
mianbiwi(rizwan,sanam).

%Parents.

parent(chotakhan,kausar).
parent(chotakhan,nadir).
parent(chotakhan,asad).
parent(chotirani,kausar).
parent(chotirani,nadir).
parent(chotirani,asad).

parent(barakhan,nahid).
parent(barakhan,sumra).
parent(barirani,nahid).
parent(barirani,sumra).

parent(salim,rizwan).
parent(kauser,rizwan).

parent(asad,salima).
parent(asad,sanam).
parent(sumra,salima).
parent(sumra,sanam).

parent(nadir,burhan).
parent(nadir,rashid).
parent(nadir,akram).
parent(nahid,burhan).
parent(nahid,rashid).
parent(nahid,akram).

parent(rizwan,rabia).
parent(sanam,rabia).

%Gender.
%male:
gins(mard,chotakhan).
gins(mard,barakhan).
gins(mard,salim).
gins(mard,asad).
gins(mard,nadir).
gins(mard,rizwan).
gins(mard,burhan).
gins(mard,rashid).
gins(mard,akram).

%female.
gins(aurat,chotirani).
gins(aurat,barirani).
gins(aurat,kausar).
gins(aurat,sumra).
gins(aurat,nahid).
gins(aurat,sanam).
gins(aurat,salima).
gins(aurat,rabia).

%Relations.
%
baap(Baap,Bacha) :- parent(Baap,Bacha),gins(mard,Baap).
maan(Maan,Bacha):-parent(Maan,Bacha),gins(aurat,Maan).
beti(Beti,Waldeen):-parent(Waldeen,Beti),gins(aurat,Beti).
beta(Beta,Waldeen):-parent(Waldeen,Beta),gins(mard,Beta).
dada(Dada,Pota):-baap(Dada,X),baap(X,Pota).
nana(Nana,Pota):-baap(Nana,X),maan(X,Pota).
dadi(Dadi,Pota):-maan(Dadi,X),baap(X,Pota).
nani(Nani,Pota):-maan(Nani,X),maan(X,Pota).
sussar(Sussar,Me):-gins(mard,Me),mianbiwi(Me,X),baap(Sussar,X)
|gins(aurat,Me),mianbiwi(X,Me),baap(Sussar,X).
sala(Sala,Me):-sussar(X,Me),baap(X,Sala),gins(mard,Sala).
behn(Behn,Man):-baap(Y,Behn),baap(Y,Man),gins(aurat,Behn),not(Behn=Man).
bhai(Bhai,Man):-baap(Y,Bhai),baap(Y,Man),gins(mard,Bhai),not(Bhai=Man).

khala(Khala,Me):-behn(Khala,X),maan(X,Me),gins(aurat,Khala).

chacha(Chacha,Me):-bhai(Chacha,X),baap(X,Me),gins(mard,Chacha).

