# Everything

## DISCLAIMER

Questo è un file che contiene una lista di tutti i teoremi, osservazioni, definizioni, esempi, lemmi, corollari, formule e proposizioni **senza alcuna dimostrazione**, di conseguenza molte informazioni risulteranno essere senza alcun contesto se già non si conosce la materia. Detto questo, buona lettura.

****
# Gruppi e Anelli



## Definizione 1


- **Semigruppo**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **semigruppo** $\iff \forall x, y, z \in S \quad m(x, m(y, z))=m(m(x, y),z) \quad$

- **Monoide**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **monoide** $\iff (S, m)$ semigruppo e $\forall x \in S \quad \exists e \in S  \mid m(x, e) = m(e, x) = x$

- **Gruppo**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **gruppo** $\iff (S, m)$ monoide e $\forall x \in S \quad \exists x^{-1} \in S \mid m(x, x^{-1}) =m(x^{-1}, x) =e$

- **Gruppo abeliano**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **gruppo abeliano** $\iff (S,m)$ gruppo e $\forall x, y \in S \quad m(x, y) = m(y, x)$



## Teorema 1


- **Hp**
  - $G$ monoide
  - $\exists e \in G$ elemento neutro
- **Th**
  - $e$ è unico in $G$

## Teorema 2


- **Hp**
  - $(G, m)$ gruppo
  - $x \in G$
  - $\exists x^{-1} \in G$ inverso di $x$ rispetto ad $m$
- **Th**
  - $x^{-1}$ è unico in $G$ per $x$ rispetto a $m$

## Teorema 3


- **Hp**
  - $X, Y$ insiemi,
  - $Y^X = \{f \mid f:X \rightarrow Y\}$
- **Th**
  - $(X^X, \circ)$ è monoide

## Teorema 4


- **Hp**
  - $X, Y$ insiemi finiti
- **Th**
  - $\left| Y^X \right| = \left| Y \right| ^ {|X|}$



## Definizione 2


- **Anello**

> - $A$ insieme
> - $+: A \times A \rightarrow A$
> - $*: A \times A \rightarrow A$
> - $(A, +, *)$ **anello** $\iff (A, +)$ gruppo abeliano, $(A, *)$ monoide e  $\forall a, b, c \in A \quad a*(b + c) = a * b + a * c$
> - $a * b=b * a \quad \forall a, b \in A \implies   (A, *, +)$ è un **anello commutativo**

- **Campo**

> - $(A, +, *)$ anello
> - $(A, +, *)$ è un **campo** $\iff \forall x \in A \quad \exists x^{-1}$ rispetto a $*$

- **Semianello commutativo**

> - $A$ insieme
> - $+: A \times A \rightarrow A$
> - $*: A \times A \rightarrow A$
> - $(A, +, *)$ **semianello commutativo** $\iff (A, +)$ monide commutativo, $(A, *)$ monoide commutativo e $\forall a, b, c \in A \quad a*(b + c) = a*b + a*c$

- **Sottoanello**

> - $(A, +, \cdot)$ anello
> - $(B, + , \cdot) \subset (A, +, \cdot)$ **sottoanello** $\iff (B, +) \subset (A, +)$ sottogruppo e $B \cdot B \subset B$



## Definizione 3


- **Invertibili**

> - $(A, +, \cdot)$ anello commutativo
> - $a \in A$ **invertibile** $\iff \exists a^{-1} \in A \mid a \cdot a^{-1}=e$, dove $e$ è l'elemento neutro dell'anello rispetto a $\cdot$
> - $A^* := \{a \in A \mid a$ invertibile$\}$ è l'**insieme degli invertibili di $A$**




## Teorema 5


- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $(A^*, \cdot)$ è un gruppo

## Teorema 6


- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
    - $(A^*, \cdot) \subset (A, \cdot)$ è un sottogruppo

## Definizione 4


- **Divisori dello $0$**

> - $(A, + , \cdot)$ anello commutativo
> - $a \in A$ **divisore dello $0$** $\iff \exists b \in A - \{0\} \mid a \cdot b = 0$

- **Dominio di integrità**

> - $(A, +, \cdot)$ anello commutativo
> - $A$ **dominio di integrità** $\iff \nexists x \neq 0 : x \mid 0$
> - alternativamente, $A$ è dominio di integrità $\iff$ in $A$ vale la legge di annullamento del prodotto




## Teorema 7


- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $x \mid 0 \iff x \notin A^*$

## Teorema 8


- **Hp**
  - $A$ campo
- **Th**
  - $A$ dominio di integrità

## Definizione 5


- **Elementi irriducibili**

> - $A$ anello commutativo
> - $a \in A - \{0\} \mid a \in A^*$
> - $a$ **irriducibile** $\iff \exists b, c \in A \mid a = b c \implies b \in A^* \lor c \in A^*$

- **Elementi primi**

> - $A$ anello commutativo
> - $a \in A - \{0\} \mid a \in A^*$
> - $a$ **primo** $\iff \exists b, c \in A : a \mid bc \implies a \mid b \lor a \mid c$



## Teorema 9


- **Hp**
    - $A$ dominio di integrità
- **Th**
    - $a$ primo $\implies a$ irriducibile

****

# Sottogruppi


## Definizione 6


- **Sottogruppo**

> - $(G, *)$ gruppo 
> - $(H, *) \subset (G, *)$ **sottogruppo** $\iff \exists e \in H \mid e$ è l'elemento neutro, $H * H \subset H$ e $\exists x^{-1} \in H \quad \forall x \in H$



## Definizione 7


- **Sottogruppo normale**

> - $(G, *)$ gruppo
> - $(H, *) \subset (G, *)$ sottogruppo
> - $x \in G$
> - $xH := \{xh \mid h \in H\}$
> - $Hx := \{hx \mid h \in H\}$
> - $H$ **sottogruppo normale** $\iff \forall x \in G \quad xH = Hx$



## Teorema 10


- **Hp**
  - $G$ gruppo
  1) $H$ è sottogruppo normale
  2) $\forall g \in G, h \in H \quad g \cdot h \cdot g^{-1} \in H$
  3) $\forall g \in G, h \in H \quad \exists k \in H \mid g \cdot h = k \cdot g$
- **Th**
  - le proposizioni sono equivalenti

****

# Ordine


## Definizione 8


- **Ordine di un elemento in un gruppo**

> - $G$ gruppo
> - $g \in G$
> - $H(g):=\left\{g^{n} \mid n \in \mathbb{Z}\right\}$ è detto **sottogruppo ciclico**
>   - prende il nome di _sottogruppo ciclico_ poiché, a seconda del gruppo, le potenze di $g$ possono essere infinite o finite, ma quest'ultimo caso si verifica esclusivamente quando le potenze ciclano su loro stesse
> - $o(g):= |H(g)|$ è detto **ordine di $g \in G$**
>   - tale valore può dunque essere infinito o finito, e in quest'ultimo caso l'ordine costituisce il valore più piccolo, non nullo, per cui $g^{o(g)} = e$, poiché per valori maggiori le potenze ricicleranno infinitamente



## Teorema 11


- **Hp**
    - $(G, +)$ gruppo
    - $g \in G$
- **Th**
    - $(H(g), +) \subset (G, +)$ sottogruppo

## Teorema 12


- **Hp** 
  - $(G, \cdot)$ gruppo
  - $g \in G$
- **Th**
  - $(H(g), \cdot) \subset (G, \cdot)$  è sottogruppo

## Teorema 13


- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $I(g):=\{n \in \mathbb{Z} \mid g^n = e\}$
- **Th**
  - $I(g)$ è un ideale

## Teorema 14


- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $\exists! d \geq 0 \mid I(g)=I(d)$
- **Th**
  - $d = 0 \implies o(g) := |H(g)| = |\mathbb{Z}|$, dunque infinito
  - $d>0 \implies d = o(g)$

## Teorema 15


- **Hp**
  - $(G, \cdot)$ gruppo finito
  - $g \in G \mid d := o(g)$ finito
- **Th**
  - $g^{|G|}=e$

## Teorema 16


- **Hp**
    - $G$ gruppo finito
    - $g \in G$
- **Th**
    - $o(g) = o(g^{-1})$

## Teorema 17


- **Hp**
    - $G$ gruppo finito
    - $k \in \mathbb{Z}$
- **Th**
    - $\forall g \in G \quad o(g^k) \mid o(g)$

## Teorema 18


- **Hp**
    - $G$ gruppo finito
    - $g, h \in G \mid gh = hg$
    - $d := \textrm{MCD}(o(g), o(h))$
    - $m := \textrm{mcm}(o(g), o(h))$
- **Th**
    - $\dfrac{m}{d} \mid o(gh) \land o(gh) \mid m$

## Teorema 19


- **Hp**
    - $G$ gruppo finito
    - $g, h \in G \mid gh = hg$
    - $d := \textrm{MCD}(o(g), o(h)) = 1$
    - $m := \textrm{mcm}(o(g), o(h))$
- **Th**
    - $o(gh) = o(hg) = m$


****
# Ideali



## Definizione 9


- **Ideali**

> - $(A, +, \cdot)$ anello
> - $I \subset A$ **ideale** $\iff (I, +) \subset (A, +)$ è un sottogruppo e $A \cdot I \subset I$ e $I \cdot A \subset I$



## Teorema 20


- **Hp**
  - $(A, +, \cdot)$ anello
  - $a \in \mathbb{Z}$
  - $I(a) := \{ax \mid x \in A\}$
- **Th**
  - $I(a)$ è un ideale, e prende il nome di _ideale di $A$ generato da $a \in A$_

## Teorema 21


- **Hp**
    - $A$ dominio di integrità
    - $a, b \in A$
- **Th**
    - $I(a)=I(b) \iff \exists c \in A^* \mid a = bc$

## Teorema 22


- **Hp**
  - $a, b \in \mathbb{Z} - \{0\}$
- **Th**
  - $I(a)=I(b) \iff a=\pm b$

## Teorema 23


- **Hp**
  - $(A, +, \cdot)$ anello
  - $a_1, \ldots, a_n \in\mathbb{Z}$
  - $I(a_1, \ldots, a_n) := \{ a_1b_1 + \ldots +a_nb_n \mid b_1, \ldots, b_n \in A\}$
- **Th**
  - $I(a_1, \ldots, a_n)$ è un ideale, e prende il nome di _ideale di $A$ generato dagli $a_1, \ldots, a_n \in A$_

## Definizione 10


- **Congruenza modulo di un ideale**

> - $(A, +, \cdot)$ anello
> - $I \subset A$ ideale
> - per definizione, $I$ ideale $\implies(I, +) \subset (A, +)$ sottogruppo, dunque ha senso definire $A/I$, e infatti $I$ induce una relazione di equivalenza su $A$ detta **congruenza modulo $I$**, dove $\forall a, b \in A \quad a \equiv b \ (\bmod \ I) \iff b - a \in I$
> - $b -a \in I \iff  (-a) + b \in I$, di conseguenza questa congruenza coincide con la classe laterale sinistra di $(A, +)$



## Teorema 24


- **Hp**
  - $(A, +, \cdot)$ anello
  - $I \subset A$ ideale
  - $+: A/I \times A/I \rightarrow A/I$
  - $\cdot : A/I \times A/I \rightarrow A/I$
- **Th**
  - $(A/I, +, \cdot)$ è un anello

## Teorema 25


- **Hp**
  - $I \subset \mathbb{Z}$ ideale
- **Th**
  -  $\exists ! \ d \in \mathbb{N} \mid I = I(d)$, o equivalentemente, in $\mathbb{Z}$ ogni ideale è principale

## Teorema 26


- **Hp**
    - $a_1, \ldots, a_n \in \mathbb{Z}$
    - $\exists ! d \in \mathbb{N} \mid I(a_1, \ldots, a_n) = I(d)$
- **Th**
    - $d = \textrm{MCD}(a_1, \ldots, a_n)$

## Definizione 11


- **Massimo Comun Divisore**

> - $a_{1}, \ldots , a_{n} \in \mathbb{Z}$
> - $\exists !d \in \mathbb{N}  \mid I\left(a_{1}, \ldots , a_{n}\right)=I(d)$, ed è detto **massimo comun divisore degli $a_1, \ldots, a_n$**
>    - per dimostrazione precedente $I(a_1, \ldots, a_n)$ è un ideale, e per dimostrazione precedente ogni ideale in $\mathbb{Z}$ è principale, dunque per un certo $d$ coincide con $I(d)$, e in particolare $d$ è proprio il massimo comun divisore degli $a_1, \ldots, a_n$ per dimostrazione precedente



## Teorema 27


- **Hp**
  - $a_1, \ldots, a_n \in \mathbb{Z}$
  - $d := \textrm{MCD}(a_1, \ldots, a_n)$
- **Th**
  - $\exists x_1, \ldots, x_n \in \mathbb{Z} \mid a_1 x_1 + \ldots + a_nx_n=d$, che prende il nome di _identità di Bézout_

## Teorema 28


- ⚠️ **MANCA DIMOSTRAZIONE SISTEMA DI IDENTITÀ DI BÉZOUT**

****

# Operazioni sugli ideali



## Definizione 12


- **$+$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I + J = \{i + j \mid \forall i \in I, j \in J\}$



## Teorema 29


- **Hp**
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- **Th**
  - $I + J$ è un ideale

## Definizione 13


- **$\cap$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cap J = \{x \in I \land x \in J\}$



## Teorema 30


- **Hp**
    - $(A, +, \cdot)$ anello commutativo
    - $I, J \subset A$ ideali
- **Th**
    - $I \cap J$ è un ideale

## Definizione 14


- **Minimo Comune Multiplo**

> - $a_{1}, \ldots, a_{n} \in \mathbb{Z}$
> - $\displaystyle \exists ! m  \in \mathbb{N} \mid I(m) = I(a_1) \cap \ldots \cap I(a_n) = \bigcap_{i=1}^{n}{I(a_i)}$, ed è detto **minimo comune multiplo degli $a_1, \ldots, a_n$**



## Definizione 15


- **$\cdot$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cdot J = \{i_1 j_1 + \ldots + i_k j_k \mid k \ge  1, \forall i_1 , \ldots , i_k \in I, j_1 , \ldots , j_k \in J \}$



## Teorema 31


- **Hp**
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- **Th**
  - $I \cdot J$ è un ideale

## Teorema 32


- **Hp**
  - $a, b \in \mathbb{Z}$
  - $d:= \textrm{MCD}(a, b)$
- **Th**
  - $I(a) + I(b) = I(d)$

## Teorema 33


- **Hp**
  - $a, b \in \mathbb{Z}$
- **Th**
  - $I(a) \cdot I(b)=I(a \cdot b)$


****
# Relazioni



## Definizione 16


- **Relazioni**

> - $S$ insieme
> - ogni elemento $R \subseteq S \times S$ è una **relazione** su $S$

- **Relazione riflessiva**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **riflessiva** $\iff \forall x \in R \quad (x, x) \in R$

- **Relazione simmetrica**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **simmetrica** $\iff \forall x, y \in R \quad (x, y) \in R \implies (y, x) \in R$

- **Relazione transitiva**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **transitiva** $\iff \forall x, y, z \in R \quad (x, y) \in R \land (y, z) \in R \implies (x, z) \in R$

- **Relazione antisimmetrica**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **transitiva** $\iff \forall x, y \in R \quad (x, y) \in R \land (y, x) \in R \implies x = y$

- **Relazione totale**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **totale** $\iff \forall x, y \in R \quad (x, y) \in R \lor (y, x) \in R$

- **Relazione di equivalenza**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ è una **relazione di equivalenza** $\iff R$ riflessiva, simmetrica e transitiva

- **Ordine parziale**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **ordine parziale** $\iff R$ riflessiva, transitiva e antisimmetrica

- **Ordine totale**

> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **ordine totale** $\iff R$ ordine parziale in cui vale la totalità



## Teorema 34


- **Hp**
  - $m, n \in \mathbb{N}$
  - $m \mid n \iff \exists p \in \mathbb{N} \mid mp = n$
- **Th**
  - $\mid$ è ordine parziale

## Teorema 35


- **Hp**
  - $a, b \in \mathbb{Z}$
  - $a \equiv b \ (\bmod \ n) \iff m \mid b-a$ è detta congruenza modulo $n$
- **Th**
  - $\equiv$ è una relazione di equivalenza

## Teorema 36


- **Hp**
  - $x, y \in \mathbb{Z} \mid x \equiv y \ (\bmod \ n)$
  - $d \in \mathbb{Z} : d\mid n$
- **Th**
  - $x \equiv y \ (\bmod  \ d)$

## Teorema 37


- **Hp**
    - $n \in \mathbb{N}$
    - $[a], [b] \in \mathbb{Z}_n$
    - $d:= \textrm{MCD}(a, n)$
- **Th**
    - $d \nmid b \implies \nexists [x] \in \mathbb{Z}_n \mid ax \equiv b \ (\bmod \ n)$
    - $d \mid b \implies \forall [x] \in \mathbb{Z}_n \mid ax \equiv b \ (\bmod \ n) \quad x$ è anche tale che $\dfrac{a}{d}x \equiv \dfrac{b}{d} \ \left(\bmod \ \dfrac{n}{d}\right)$



## Teorema 38


- **Hp**
  - $G$ gruppo
  - $g, h \in G$
  - $g \sim h \iff \exists a \in G \mid h = a\cdot g \cdot a^{-1}$ è detta _relazione di coniugio_
- **Th**
  - $\sim$ è una relazione di equivalenza

****

# Partizioni


## Definizione 17


- **Partizione**

> - $X$ insieme
> - $I$ insieme di indici
> - $\forall i \in I \quad X_i \subset X$
> - $\displaystyle X = \coprod_{i \in I}X_i$



## Teorema 39


- **Hp**
  - $G$ gruppo
- **Th**
  - $\forall x, y \in G \quad x \nsim y \iff [x] \cap [y] = \varnothing \lor x \sim y \iff [x] = [y]$

## Teorema 40


- **Hp**
  - $G$ gruppo
  - $\sim$ è una relazione di equivalenza in $G$
- **Th**
  - $\sim$ induce una partizione di $G$, dunque $\displaystyle G = \coprod_{[x] \in X/\sim}[x]$
     
****

# Classi laterali


## Teorema 41


- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x, y \in G$
- **Th**
  - $x \sim_S y \iff x^{-1}y \in H$ è una relazione di equivalenza

## Definizione 18
 

- **Classi laterali**

> - $(G, \cdot)$ gruppo
> - $(H, \cdot) \subset (G, \cdot)$ sottogruppo
> - $\forall x,y \in G \quad x \sim_S y \iff x^{-1}y \in H$ è una relazione di equivalenza
> - $\forall x, y \in G \quad x \sim_D y \iff xy^{-1} \in H$ è una relazione di equivalenza
> - $x \in G$
> - $[x] = \{y \in G \mid y \sim_S x\}$ è detta **classe laterale sinistra**
> - $[x] = \{y \in G \mid y \sim_D x\}$ è detta **classe laterale destra**
> - $G/H := \{[x] \mid x \in G\}$ è l'**insieme delle classi laterali sinistre o destre**



## Teorema 42


- **Hp**
  - $(\mathbb{Z}, +)$ anello
  - $n \in \mathbb{N}_{\ge 2}$
  - $I(n) := \{n k \mid k \in \mathbb{Z}\}$
  - $a, b \in \mathbb{Z}$
- **Th**
  - $a \sim_S b \iff a \equiv b \ (\bmod \ n)$

## Teorema 43


- **Hp**
    - $G$ gruppo
    - $H \subset G$ sottogruppo
- **Th**
    - $H = [1] \in G/H$

## Teorema 44


- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x \in G$
  - $[x] = \{y \in G \mid y \sim_S x\}$
- **Th**
  - $xH:= \{ xh \mid h \in H\} = [x]$

## Teorema 45


- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x \in G$
- **Th**
  - $| xH |= |H|$

## Teorema 46


- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $+: G/H \times G/H \rightarrow G/H$
- **Th**
  - $(G/H, +)$ è gruppo abeliano


****
# Insieme quoziente



## Definizione 19


- **Insieme quoziente**

> - $G$ gruppo
> - $\sim$ relazione di equivalenza in $G$
> - $\forall x \in G \quad [x]:=\{y \in G \mid x \sim y\}$
> - $G/\sim := \{[x] \mid x \in G\}$ è l'**insieme quoziente**, ovvero l'insieme delle classi di equivalenza determinate da $\sim$



## Definizione 20


- **Insieme quoziente $\mathbb{Z}_n$**

> - $(\mathbb{Z}, +, \cdot)$ anello, in particolare $(\mathbb{Z}, +)$ gruppo
> - $n \in \mathbb{Z}$
> - $\mathbb{Z}/\equiv$ è l'insieme delle classi di equivalenza definite dalla relazione di equivalenza $\equiv$
> - $m \equiv r \ (\bmod \ n)\iff r \equiv m \ (\bmod \ n) \implies n \mid m - r \implies \exists q: nq = m - r \implies m = nq + r \quad 0 \le r \lt n$
> - $0 \le r \lt n \implies$ è possibile definire $\mathbb{Z}_n := \{[0], [1], \ldots, [n - 1]\}$, che coincide con $\mathbb{Z}/\equiv$



## Teorema 47


- **Hp**
  - $n \in \mathbb{Z}$
  - $I(n) := \{nk \mid k \in \mathbb{Z}\}$
- **Th**
  - $(\mathbb{Z}_n, +)$ è un gruppo

## Teorema 48


- **Hp**
  - $p \in \mathbb{P}$
  - $a, b \in \mathbb{Z}$
  - $p \mid ab$
- **Th**
  - $p \mid a \lor p \mid b$

## Teorema 49


- **Hp**
  - $n \in \mathbb{Z}$
- **Th**
  - $\mathbb{Z}_n$ dominio di integrità $\iff n \in \mathbb{P}$

## Teorema 50


- **Hp**
  - $n \in \mathbb{Z}$
- **Th**
  - $\forall [a] \in \mathbb{Z}_n \quad \textrm{MCD}(a, n) = 1 \iff [a] \in \mathbb{Z}^*_n$

## Teorema 51


- **Hp**
  - $p \in \mathbb{P}$
- **Th**
  - $\mathbb{Z}_p$ campo

## Teorema 52


- **Hp**
    - $p \in \mathbb{P}$
- **Th**
    - $(\mathbb{Z}_p^*, \cdot)$ è ciclico

****

# Funzione totiente di Eulero


## Definizione 21


- **Funzione totiente di Eulero**

> - $n \in \mathbb{N}$
> - $\varphi(n) := |\mathbb{Z}_n^* |$



## Teorema 53


- **Hp**
  - $n, m \in \mathbb{N} \mid \textrm{MCD}(a, n) = 1$
- **Th**
  - $[a]  \in \mathbb{Z}_{m n}^{*} \iff[a] \in \mathbb{Z}_{m}^{*} \land [a] \in \mathbb{Z}^*_{n}$

## Teorema 54


- **Hp**
  - $m, n \in \mathbb{N} \mid \textrm{MCD}(m, n) = 1$
- **Th**
  - $\varphi(m \cdot n) = \varphi(m) \cdot \varphi(n)$

## Teorema 55


- **Hp**
    - $p \in \mathbb{P}$
    - $k \in \mathbb{N} \mid k \ge 1$
- **Th**
    - $\varphi(p^k) = p^{k -1}(p-1)$

## Teorema 56


- **Hp**
    - $k \in \mathbb{N} \mid k \ge 1$
    - $p_1, \ldots, p_k \in \mathbb{P}$
    - $i_1, \ldots, i_k \ge 1$
    - $n \in \mathbb{N} \mid n = p_1^{i_1} \cdot \ldots \cdot p_k^{i_k}$ 
- **Th**
    - $\displaystyle\varphi(n)=n \cdot \prod_{p \mid n}\left(1-\frac{1}{p}\right)$


****
# Permutazioni



## Definizione 22


- **Permutazioni**

> - $X$ insieme
> - $S_X := \{f \mid f:X \rightarrow X$ biiettiva $\}$ è l'**insieme delle permutazioni di $X$**
> - $X = \{1, \ldots, n\} \implies S_n$ è detto **gruppo simmetrico di $n$**



## Teorema 57


- **Hp**
  - $S_X := \{f \mid f : X \rightarrow Y$ biiettiva $\}$
- **Th**
  - $(S_X, \circ)$ è un gruppo, non abeliano se $|X| \ge 3$

## Definizione 23


- **Ciclo di una permutazione**

> - $n \in \mathbb{N}$
> - $\sigma \in S_n$
> - $\exists 1 \leq i_1, \ldots, i_d \leq n \in \mathbb{N} \mid \left\{\begin{array}{c}
\sigma\left(i_{1}\right)=i_{2} \\
\sigma\left(i_{2}\right)=i_{3} \\
\vdots \\
\sigma\left(i_{d-1}\right)=i_{d} \\
\sigma\left(i_{d}\right)=i_{1}
\end{array}\right. \implies i_1, \ldots, i_n$ costituiscono un **ciclo di $\sigma$**



## Teorema 58


- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
  - $1 \le i \lt n \in \mathbb{N}$
  - $I(\sigma, i):=\left\{n \in \mathbb{Z} \mid \sigma^{n}(i)=i\right\}$
- **Th**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è un ideale

## Teorema 59


- **Hp**
    - ⚠️ **RISCRIVI TUTTO**
    - $I(\sigma, i)$ è **ideale principale** in $\mathbb{Z}$ generato da $I(d)$, dove $d$ è la lunghezza del ciclo di $i$, quindi $I(\sigma, i) = I(d)$
  - $I(\sigma, i) = I(d) \implies d \in I(\sigma, i)$

## Teorema 60


- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n \mid \sigma = \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
  - $d_j:=$ lunghezza di $\gamma_j \quad \forall j \in [1, k]$
  - $m := \textrm{mcm}(d_1, \ldots, d_k)$
  -  $I(\sigma):=\left\{n \in \mathbb{Z} \mid \sigma^{n}=\textrm{id}\right\}$
- **Th**
  - $o(\sigma) = m$

****

# Trasposizioni


## Definizione 24


- **Trasposizione**

> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \leq i \lt j \leq n \quad$
> - $k \in [1, n]$
> - $\tau_{i, j} \in S_n \mid \tau_{i, j} =$$\left\{\begin{array}{ll}j & k=i \\ i & k=j \\ k & k \neq i, j\end{array}\right.$ è detta **trasposizione**, ovvero una permutazione che inverte esclusivamente due elementi tra loro
>   - $\tau_{i, j}^2 = \textrm{id} \iff \tau_{i, j} = \tau_{i, j} ^{-1}$

- **Trasposizione adiacente**

> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \le i \lt j \le  n \land  j = i + 1$
> - $\tau_{i, j}=\tau_{i, i+1}$ è detta **trasposizione adiacente**, poiché inverte esclusivamente due elementi, adiacenti, tra loro



## Teorema 61


- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
- **Th**
  - $\exists 1 \leq i_1, \ldots, i_k \lt n \mid \sigma = \tau_{i_1, i_1 + 1} \ldots \tau_{i_k, i_k + 1}$, quindi ogni permutazione può essere riscritta come composizione di trasposizioni adiacenti
     
****

# Segno


## Definizione 25


- **Segno di una permutazione**

> - $n \in \mathbb{N}$
> - $\sigma \in S_n$
> - $\textrm{Inv}(\sigma) := \{ (i, j) \mid 1 \leq i \lt j \lt n : \sigma(i) \gt \sigma(j)\}$ è l'**insieme delle inversioni di $\sigma$**
> - $\textrm{sgn}(\sigma) := (-1)^{|\textrm{Inv}(\sigma)|} =$$\left\{\begin{array}{ll}+1 & |\operatorname{Inv}(\sigma)| \equiv 0 \ (\bmod  \ 2) \\ -1 & |\operatorname{Inv}(\sigma)| \equiv 1 \ (\bmod \ 2)\end{array}\right. \implies \sigma$ **pari** $\iff \textrm{sgn}(\sigma) = +1$
>   - $\textrm{sgn}(\textrm{id}) = (-1)^0 = 1$, in quando la funzione identità non ha inversioni



## Teorema 62


- **Hp**
    - $n \in \mathbb{N}$
    - $A_n := \{\sigma \in S_n \mid \sigma$ pari$\}$
- **Th**
    - $A_n \subset S_n$ è un sottogruppo normale, detto _gruppo alterno di ordine $n$_

## Teorema 63


- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_{n} \mid \sigma=\tau_{1} \ldots \tau_{k}$ dove $\forall j \in [1, k] \quad \tau_{j} = \tau_{j, j + 1}$, dunque tutte le trasposizioni sono adiacenti
- **Th**
    - $\textrm{sgn}(\sigma)= (-1)^k$

## Teorema 64


- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^{\prime} \in S_{n} | \left\{\begin{array}{l}\sigma = \tau_1 \ldots \tau_k \\ \sigma ' = \tau_1^{\prime} \ldots \tau_h^{\prime}\end{array}\right.$, dove ogni trasposizione è adiacente
- **Th**
    - $\operatorname{sgn}\left(\sigma \sigma^{\prime}\right)=\operatorname{sgn}(\sigma)\cdot \textrm{sgn}(\sigma ')$

## Teorema 65


- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_n$
- **Th**
    - $\textrm{sgn}(\sigma^{-1})=\textrm{sgn}(\sigma)$

## Teorema 66


- **Hp**
    - $n \in \mathbb{N}$
  - $\sigma, \sigma^\prime \in S_n$
  - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
- **Th**
    - $\textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$

## Teorema 67


- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^\prime \in S_n \mid \sigma := \gamma_1 \ldots \gamma_k, \sigma^\prime := \gamma_1^\prime \ldots \gamma_h^\prime$
    - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$, che costituisce dunque la relazione di coniugio
- **Th**
    - $\sigma \sim \sigma ^\prime \iff$$\left\{\begin{array}{c}k=h \\ d=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}=d_{k}^{\prime}\end{array}\right.$, dove $d_j$ è la lunghezza del ciclo $\gamma_j$ e $d_j^\prime$ è la lunghezza del ciclo $\gamma_j^\prime$

## Teorema 68


- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_n \mid \sigma := \gamma_1 \ldots \gamma_k$
- **Th**
    - $\textrm{sgn}(\sigma)=(-1)^{n - k}$


****
# Morfismi



## Definizione 26
 

- **Morfismo di gruppi**

> - $(G, \cdot), (H, \cdot)$ gruppi
> - $f: G \rightarrow H$
> - $f$ **morfismo di gruppi** $\iff \forall x, y \in G \quad f(x\cdot y)=f(x)\cdot f(y)$

- **Morfismo di anelli**

> - $(A, +, \cdot), (B, +, \cdot)$ anelli
> - $f: A \rightarrow B$
> - $f$ **morfismo di anelli** $\iff \forall x, y \in A \quad f(x+ y) = f(x) + f(y) \land f(x \cdot y) = f(x) \cdot f(y)$
>     -   la stessa definizione si applica per morfismo di campi



## Teorema 69


- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1_G$ neutro per $G$
  - $1_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(1_G) = 1_H$

## Teorema 70


- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1_G$ neutro per $G$
  - $1_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(g^{-1}) = f(g)^{-1}$

****

# Isomorfismi


## Definizione 27


- **Isomorfismo**

> - $f$ isomorfismo $\iff f$ morfismo e $f$ biiettiva



## Teorema 71


- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $f: G \rightarrow H$ isomorfismo
- **Th**
  - $f ^{-1}: H \rightarrow G$ isomorfismo

## Teorema 72


- **Hp**
    - $\cong$ è la relazione di isomorfismo
- **Th**
    - $\cong$ è una relazione di equivalenza

## Teorema 73


- **Hp**
  - $z \in \mathbb{C} \mid z^n = 1$ sono le radici $n$-esime di $1$
  - $\zeta := e^{i \frac{2 \pi}{n}}$
  - $H := \{\zeta ^0, \zeta^1, \zeta^k, \ldots, \zeta^{n-1}\}$ è l'insieme delle radici $n$-esime di $1$
- **Th**
  - $(H, \cdot) \subset (\mathbb{C}-\{0\}, \cdot)$ è un sottogruppo

## Teorema 74


- **Hp**
  - $f: \mathbb{Z}_n \rightarrow H : [k] \rightarrow \zeta^k$
- **Th**
  - $f$ isomorfismo di gruppi $(\mathbb{Z}_n , +)$ e $(H, \cdot)$

## Teorema 75


- **Hp**
  - $(G, \cdot)$ gruppo
  - $g \in G$
  - $f: \mathbb{Z} \rightarrow G: n \rightarrow g^n$
- **Th**
  - $f$ morfismo di gruppi $(\mathbb{Z}, +)$ e $(G, \cdot)$

## Teorema 76


- **Hp**
  - $f: \mathbb{Z} \rightarrow \mathbb{Z}_n : k \rightarrow [k]$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z},+, \cdot\right)$ e $\left(\mathbb{Z}_{n},+, \cdot\right)$

## Teorema 77


- **Hp**
  - $n, m \in \mathbb{Z} : n \mid m$
  - $f : \mathbb{Z}_m \rightarrow \mathbb{Z}_n: x \ (\bmod \ m) \rightarrow x \ (\bmod\ n)$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z}_{m},+, \cdot\right)$ e $\left(\mathbb{Z}_{n},+, \cdot\right)$

## Teorema 78


- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $f: G \rightarrow G : h \rightarrow g \cdot h \cdot g^{-1}$
- **Th**
  - $f$ morfismo di gruppi $(G, \cdot)$ e $(G, \cdot)$

****

# Kernel e immagine


## Definizione 28


- **Kernel e immagine di gruppi**

> - $G, H$ gruppi
> - $f: G \rightarrow H$ morfismo
> - $\textrm{ker}(f):=\{g \in G \mid f(g) = 1_H\}$ è detto **kernel/nucleo di $f$**
> - $\textrm{im}(f):=\{h \in H \mid \exists g \in G : f(g) = h\}$ è detta **immagine di $f$**

- **Kernel e immagine di anelli**

> - $A, B$ gruppi
> - $f: A \rightarrow B$ morfismo
> - $\textrm{ker}(f):=\{a \in A \mid f(a)= 0_B\}$ è detto **kernel/nucleo di $f$**
> - $\textrm{im}(f):=\{b \in B \mid \exists a \in A : f(a) = b\}$ è detto **immagine di $f$**



## Teorema 79


- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{ker}(f) \subset G$ è sottogruppo

## Teorema 80


- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{im}(f) \subset H$ è sottogruppo

## Teorema 81


- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f$ iniettiva $\iff \textrm{ker}(f) = \{1_G\}$

## Teorema 82


- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $\textrm{ker}(f)$ ideale

## Teorema 83


- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $\textrm{im}(f) \subset B$ sottoanello

## Teorema 84


- **Hp**
  - $f: \mathbb{Z} \rightarrow \mathbb{C} - \{0\} : k \rightarrow \zeta^k$
  - $f$ morfismo di gruppi $(\mathbb{Z}, +)$ e $(\mathbb{C} - \{0\}, \cdot)$
  - $I(n)$ ideale generato da $n$
- **Th**
  - $\textrm{ker}(f) = I(n)$

## Teorema 85


- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{ker}(f) \subset G$ sottogruppo normale


****
# Gruppi diedrali



## Definizione 29


- **Gruppo diedrale**

> - $n \in \mathbb{N}_{\ge 2}$
> - $D_n$ è l'**insieme delle simmetrie dell'$n$-gono regolare**
>   - l'insieme delle rotazioni che lasciano l'$n$-gono invariato, e delle riflessioni rispetto agli assi di simmetria
> - $\rho :=$ rotazione di $\frac{360°}{n}$ gradi di un $n$-gono regolare
> - $\sigma_i :=$ riflessione rispetto all'$i$-esimo asse di simmetria dell'$n$-gono regolare



## Teorema 86


- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $D_n$ insieme delle simmetrie dell'$n$-gono regolare
- **Th**
  - $|D_n| = 2n$

## Teorema 87


- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $D_n$ insieme delle simmetrie dell'$n$-gono regolare
  - $\cdot$ è l'operazione di composizione delle simmetrie
- **Th**
  - $(D_n, \cdot)$ è un gruppo

## Teorema 88


- **Hp**
  - $D_2$ gruppo diedrale
- **Th**
  - $(D_2, \cdot)$ è l'unico gruppo diedrale abeliano

## Teorema 89


- **Hp**
  - $D_n$ gruppo diedrale
- **Th**
  - $D_n \hookrightarrow S_n$
  - $\exists X \subset S_n$ sottogruppo di $S_n$ $\mid D_n \cong X$
    - $D_3 \cong S_3$

## Definizione 30


- **Gruppo di Klein**

> - $K_4 := \{1, a, b, c\}$
> - $a^2=b^2=c^2=1$
> - $ab=c=ba$
> - $ac=b=ca$
> - $cb=a=bc$



## Teorema 90


- **Hp**
  - $K_4$ è il gruppo di Klein
- **Th**
  - $K_4 \cong D_2$


****
# Polinomi



## Definizione 31


- **Polinomi**

> - $\mathbb{K}$ campo
> - $a(x) := \displaystyle{\sum_{k = 0}^na_kx^k} = a_0x^0 + \ldots + a_nx^n$ è un **polinomio**
> - $\mathbb{K}[x] := \{a_0x^0 + \ldots + a_n x^n \mid a_0, \ldots, a_n \in \mathbb{K}\}$ è l'**insieme dei polinomi a coefficienti in $\mathbb{K}$**
> - $p(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$ è detto **polinomio monico** $\iff a_n = 1$



## Teorema 91


- **Hp**
    - ($\mathbb{K}, +, \cdot)$ anello
- **Th**
    - $(\mathbb{K}[x], +, \cdot)$ è un anello

## Definizione 32


- **Grado del polinomio**

> - $\mathbb{K}$ campo
> - $a(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $\deg(a(x)):=\left\{\begin{array}{ll} n & a(x) \neq 0 \\ - \infty & a(x) = 0\end{array}\right.$



## Teorema 92


- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x]$
- **Th**
    - $\deg(a(x) \cdot b(x)) = \deg(a(x)) + \deg(b(x))$

## Teorema 93


- **Hp**
    - $\mathbb{K}$ campo
    - $a(x) \in \mathbb{K}[x] \mid \deg(a(x)) \ge 1$
- **Th**
    - $\nexists a^{-1}(x) \in \mathbb{K}[x]$

## Teorema 94


- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]^* = \mathbb{K}^* \subset \mathbb{K}[x]$

## Teorema 95


- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]$ è un dominio di integrità

## Definizione 33


- **Radici di un polinomio**

> - $\mathbb{K}$ campo
> - $p(x) \in \mathbb{K}[x]$
> - $\{c \in \mathbb{K}\ \mid p(c) = 0\}$ è l'**insieme delle radici di $p(x)$**



## Teorema 96


- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
- **Th**
    - $p(c) = 0 \iff x - c \mid p(x)$

## Teorema 97


- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $n := \deg(p(x))$
- **Th**
    - $|\{c \in \mathbb{K} \mid p(c) = 0\}| \le n$

## Teorema 98


- **Hp**
    - $\mathbb{K}$ campo
    - $I \subset \mathbb{K}[x]$ ideale
- **Th**
    - $I$ è un ideale principale

## Teorema 99


- **Hp**
    - $\mathbb{K}$ campo
    - $I(a_1(x)), \ldots, I(a_n(x)) \subset \mathbb{K}[x]$ ideali
    - $\exists d(x) \in \mathbb{K}[x]\mid I(a_1(x), \ldots, a_n(x)) = I(d(x))$
- **Th**
    - $d(x)=\textrm{MCD}(a_1(x), \ldots, a_n(x))$

## Teorema 100


- **Hp**
    - $\mathbb{K}$ campo
    - $I(a_1(x)), \ldots, I(a_n(x)) \subset \mathbb{K}[x]$ ideali
    - $\exists m(x) \in \mathbb{K}[x] \mid I(a_1(x)) \cap \ldots \cap I(a_1(x)) = I(m(x))$
- **Th**
    - $m(x)=\textrm{mcm}(a_1(x), \ldots, a_n(x))$

## Teorema 101


- **Hp**
    - $\mathbb{K}$ campo
    - $a_1(x), \ldots ,a_n(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
    - $d(x):= \textrm{MCD}(a_1(x), \ldots, a_n(x))$
- **Th**
    - $a_1(c) = \ldots = a_n(c) = 0 \iff d(c) = 0$

## Teorema 102


- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
- **Th**
    - $p(x) \in \mathbb{K}[x]$ irriducibile $\iff p(x)$ primo

## Teorema 103


- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x] - \{0\}$
- **Th**
    - $\exists ! q_1(x), \ldots ,q_k(x) \in \mathbb{K}[x]$ irriducibili e monici$, c \in \mathbb{K} - \{0\} \mid p(x) = c \cdot q_1(x) \cdot \ldots \cdot q_k(x)$
    - in particolare, i polinomi sono unici a meno di un riordinamento

## Teorema 104


- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1$

## Teorema 105


- **Hp**
    - $p(x) \in \mathbb{R}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1$ oppure $\deg(p(x)) = 2 \land \Delta \lt 0$

## Teorema 106


- **Hp**
    - $a_0, \ldots, a_n \in \mathbb{Z} \mid a_0, a_n \neq 0$
    - $p(x) \in \mathbb{Z}[x] \mid p(x) = a_0 + \ldots + a_nx^n$
    - $a, b \in \mathbb{Z} \mid \textrm{MCD}(a, b) = 1$
    - $p(\frac{a}{b}) = 0$
- **Th**
    - $a \mid a_0 \land b \mid a_n$

## Teorema 107


- ⚠️  **MANCA UN TEOREMA ENORME**



****
# Spazi Vettoriali



## Definizione 34
 

- **Spazio vettoriale**

> - $\mathbb{K}$ campo
> - $x \in \mathbb{K}$ è detto **scalare**
> - $V$ è **spazio vettoriale su $\mathbb{K}$** $\iff (V, +)$ gruppo abeliano, è ben definita un'operazione di $\cdot: K \times V \rightarrow V$ che ammetta elemento neutro, inoltre $\forall s, t \in \mathbb{K}, v \in V \quad s\cdot (t \cdot v) = (s \cdot t) \cdot v, (s + t) \cdot v = s\cdot v + t \cdot v$ e infine $\forall s \in \mathbb{K}, v, w \in V \quad s \cdot (v + w) = s \cdot v + s \cdot w$
> - $x \in V$ è detto **vettore**

- **Spazio di Hilbert**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $V$ spazio di Hilbert $\iff$ in $V$ è ben definito il prodotto scalare



## Teorema 108


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}^n$ spazio vettoriale su $\mathbb{K}$

## Definizione 35


- **Sottospazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $W$ è **sottospazio vettoriale di $V$** $\iff (W, +) \subset (V, +)$ sottogruppo, e $\forall w \in W, \lambda \in \mathbb{K} \quad \lambda \cdot w \in W$



## Definizione 36


- **Span di vettori**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $\textrm{span}(v_1, \ldots, v_n) := \{\lambda_1 v_1 + \ldots + \lambda_n v_n \mid \lambda_1, \ldots , \lambda_n \in \mathbb{K}\}$, ovvero l'insieme delle combinazioni lineari degli $v_1, \ldots, v_n$




## Teorema 109


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $\textrm{span}(v_1, \ldots, v_n)$ è un sottospazio vettoriale di $V$

## Definizione 37


- **Vettori generatori**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono **generatori di $V$** $\iff \textrm{span}(v_1, \ldots, v_n) = V$
>     - equivalentemente, ogni altro vettore in $V$ è una combinazione lineare degli $v_1, \ldots, v_n$

- **Indipendenza lineare**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono **linearmente indipendenti** se e solo se $\lambda_1 v_1 + \ldots + \lambda_n v_n = 0_V \iff \lambda_1 = \ldots = \lambda_n = 0_{\mathbb{K}}$
>    - equivalentemente, nessuno degli $v_1, \ldots, v_n$ è combinazione lineare degli altri

- **Base di uno spazio vettoriale**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono una **base di $V$** $\iff$ $v_1, \ldots, v_n$ sono generatori di $V$ e linearmente indipendenti
> - $n$ è detta **cardinalità della base di $V$**



## Teorema 110


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $e_1 := (1, 0, \ldots, 0), \ldots, e_n :=(0, \ldots, 0, 1) \in \mathbb{K}^n$
- **Th**
    - $e_1, \ldots, e_n$ sono una base di $\mathbb{K}^n$, ed è detta _base canonica_

## Teorema 111


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $v_1, \ldots, v_n$ linearmente indipendenti $\iff v_1, \ldots, v_{n - 1}$ linearmente indipendenti $\land v_n \notin \textrm{span}(v_1, \ldots, v_{n - 1})$

## Teorema 112


- **Hp**
    - $m, k \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $w_1, \ldots, w_m \in V$
    - $v_1, \ldots, v_k \in \textrm{span}(w_1, \ldots, w_m) \mid v_1, \ldots, v_k$ linearmente indipendenti
- **Th**
    - $k \le m$

## Teorema 113


- **Hp**
    - $n, m \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $w_1, \ldots, w_m \in V \mid w_1, \ldots, w_m$ base di $V$
    - $v_1, \ldots, v_n \in V \mid v_1, \ldots, v_n$ base di $V$
- **Th**
    - $n = m$, il che implica che la cardinalità delle basi di uno spazio vettoriale è unica

## Definizione 38


- **Base ortogonale di uno spazio di Hilbert**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio di Hilbert su $\mathbb{K}$
> - $v_1, \ldots, v_n$ base di $V$
> - $v_1, \ldots, v_n$ **base ortogonale di $V$** $\iff \forall i, j \in [1, n], i \neq j \quad v_i \cdot v_j = 0$

- **Base ortonormale di uno spazio di Hilbert**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio di Hilbert su $\mathbb{K}$
> - $v_1, \ldots, v_n$ base ortogonale di $V$
> - $v_1, \ldots, v_n$ **base ortonormale** di $V \iff \forall i, j \in [1, n] \quad v_i \cdot v_j = \left\{\begin{array}{cc} 1 & i = j \\ 0 & i \neq j \end{array}\right.$
>   - in particolare, è possibile ottenere $v_1, \ldots, v_n$ a partire da $e_1, \ldots, e_n$ tramite rotazioni e riflessioni



## Teorema 114


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $v \in \mathbb{K}^n$
    - $v_1, \ldots, v_k$ base ortonormale di $\mathbb{K}^n$
- **Th**
    - $v = (v \cdot v_1)v_1 + \ldots + (v \cdot v_n)v_n$



## Teorema 115


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $A \in O(n)$
- **Th**
    - $A_1, \ldots, A_n$ e $A^1, \ldots, A^n$ basi ortonormali di $\mathbb{K}^n$



## Definizione 39


- **Dimensione di uno spazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $\dim(V)$ è detta **dimensione di $V$**, ed è la cardinalità delle basi di $V$



## Teorema 116


- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $v_1, \ldots, v_n$ base di $V \iff \forall v \in V \quad \exists ! \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1 v_1 + \ldots + \lambda_n v_n$

## Teorema 117


- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(W)$
    - $k \in \mathbb{N} \mid k \lt n$
    - $w_1, \ldots, w_k \in W$ linearmente indipendenti
- **Th**
    - $\exists w_{k + 1}, \ldots, w_n \in W \mid w_1, \ldots, w_n$ è una base di $W$

## Teorema 118


- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n := \dim(W)$
    - $m \in \mathbb{N} \mid m \ge n$
    - $w_1, \ldots, w_m \in W \mid w_1, \ldots, w_m$ generatori di $W$
- **Th**
    - $\exists 1 \le i_1, \ldots, i_n \le m \mid w_{i_1}, \ldots, w_{i_n}$ è una base di $W$

## Teorema 119


- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(W)$
    - $w_1, \ldots, w_n \in W$
- **Th**
    - $w_1, \ldots, w_n$ linearmente indipendenti $\iff w_1, \ldots, w_n$ generatori di $W$

## Teorema 120


- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $U, V \subset W$ sottospazi vettoriali
- **Th**
    - $\dim(U + V) = \dim(U) + \dim(V) - \dim(U \cap V)$

## Teorema 121


- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $W \subset V$ sottospazio vettoriale
- **Th**
    - $V/W$ sottospazio vettoriale

## Teorema 122


- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $W \subset V$ sottospazio vettoriale
- **Th**
    - $\dim(V/W) = \dim(V) - \dim(W)$

## Teorema 123


- **Hp**
    - $\mathbb{K}$ campo
    - $k \in \mathbb{N}$
    - $V_1, \ldots, V_k$ spazi vettoriali su $\mathbb{K}$
- **Th**
    - $\dim(V_1 \times \ldots \times V_k) = \dim(V_1) \cdot \ldots \cdot \dim(V_k)$

****

# Applicazioni lineari



## Definizione 40


- **Applicazioni lineari**

> - $\mathbb{K}$ campo
> - $V$ e $W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ **morfismo di spazi vettoriali** $\iff \forall x, y \in V \quad f(x + y) = f(x) + f(y)$ e $\forall v \in V, \lambda \in \mathbb{K} \quad f(\lambda v) = \lambda f(v)$
>     - un morfismo su spazi vettoriali è detto anche **applicazione lineare** o **trasformazione lineare**



## Teorema 124


- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(V)$
- **Th**
    - $V \cong \mathbb{K}^n$

## Teorema 125


- ⚠️ **QUI C'È UN BUCO DI COSE CHE NON HO CAPITO**



## Teorema 126


- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
- **Th**
    - $V \cong W \iff \dim(V) = \dim(W)$

## Definizione 41


- **Kernel e immagine**

> - $\mathbb{K}$ campo
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $f : V \rightarrow W$ trasformazione lineare
> - $\ker(f) = \{v \in V \mid f(v) = 0_W\}$
> - $\textrm{im}(f) = \{w \in W \mid \exists v \in V : w = f(v)\}$



## Teorema 127


- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\ker(f) \subset V$ sottospazio



## Teorema 128


- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\textrm{im}(f) \subset W$ sottospazio



## Definizione 42


- **Rango di un'applicazione lineare**

> - $\mathbb{K}$ campo
> - $V$ e $W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ applicazione lineare
> - $\textrm{rk}(f) := \dim(\textrm{im}(f))$ è detto **rango di $f$**

****

# Sottospazi affini



## Teorema 129


- ⚠️ **TODO**

****



## Teorema 130


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
    - $X := \{x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A\cdot x = b\}$
    - $X \neq \varnothing$
- **Th**
    - $X$ sottospazio affine di $\mathbb{K}^n$, con dimensione pari a $n - \textrm{rk}(A)$


****
# Matrici



## Definizione 43


- **Matrici**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\textrm{Mat}_{m \times n}(\mathbb{K})$ è l'**insieme delle matrici aventi $m$ righe e $n$ colonne a coefficienti in $\mathbb{K}$**

- **Vettori riga e vettori colonna**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\forall A \in \textrm{Mat}_{1 \times n}(\mathbb{K}) \quad A = \left(x_1, \ldots, x_n\right)$ è detto **vettore riga**
> - $\forall A \in \textrm{Mat}_{m \times 1}(\mathbb{K}) \quad A = \left(\begin{array}{ccc} x_1 \\ \vdots \\ x_m \end{array}\right)$ è detto **vettore colonna**
> - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad \exists A^1, \ldots, A^n \in \mathbb{K}^m$ vettori colonna e $A_1, \ldots, A_m \in \mathbb{K}^n$ vettori riga $\mid A = \left(A^1, \ldots, A^n \right) = \left(\begin{array}{ccc} A_1 \\ \vdots \\ A_m\end{array}\right)$



## Definizione 44


- **Somma tra matrici**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\forall i \in [1, m], j \in [1, n] \quad a_{i, j}, b_{i, j} \in \mathbb{K}$
> - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} \ddots & & \\ & a_{i, j} & \\ & & \ddots \end{array}\right) \land B = \left(\begin{array}{ccc}\ddots & & \\ & b_{i, j} & \\ & & \ddots\end{array}\right)$
> - $A + B = \left(\begin{array}{ccc}\ddots & & \\ & a_{i, j} + b_{i, j} & \\ & & \ddots\end{array}\right)$ è la **somma tra $A$ e $B$**



## Teorema 131


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
- **Th**
    - $\textrm{Mat}_{m \times n}(\mathbb{K})$ è uno spazio vettoriale



## Definizione 45


- **Prodotto tra matrici**

> - $\mathbb{K}$ campo
> - $l, m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{l \times m}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} a_{1, 1} & \cdots & a_{1, m} \\ \vdots & \ddots & \vdots \\ a_{l, 1} & \cdots & a_{l, m} \end{array}\right)$
> - $B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid B = \left(\begin{array}{ccc} b_{1, 1} & \cdots & b_{1, n} \\ \vdots & \ddots & \vdots \\ b_{m, 1} & \cdots & b_{m, n} \end{array}\right)$
> - $C \in \textrm{Mat}_{l \times n}(\mathbb{K}) \mid C = AB$ è il **prodotto tra $A$ e $B$**, ed è definito come $\left(\begin{array}{ccc}a_{1, 1}b_{1, 1} + \ldots + a_{1, m}b_{m, 1} & \cdots & a_{1, 1}b_{1, n} + \ldots + a_{1, m}b_{m,n} \\ \vdots & \ddots & \vdots \\a_{l,1}b_{1, 1} + \ldots + a_{l,m}b_{m, 1} & \cdots & a_{l,1}b_{1,n} + \ldots + a_{l, m}b_{m,n}\end{array}\right)$



## Teorema 132


- **Hp**
    - $\mathbb{K}$ campo
    - $\lambda \in \mathbb{K}$
    - $l, m, n, k \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{l \times m}(\mathbb{K})$
    - $B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - **⚠️  TODO**
    - $\forall C \in \textrm{Mat}_{n \times k}(\mathbb{K}) \quad (AB)C = A(BC)$
    - $\forall C \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad A(B+C) = AB+AC$
    - $\forall C \in \textrm{Mat}_{n \times k}(\mathbb{K}) \quad (A+B)C = AC+BC$
    - $\lambda(AB) = (\lambda A)B = A (\lambda B)$



## Teorema 133


- **Hp**
    - $\mathbb{K}$ campo
    - $\lambda \in \mathbb{K}$
    - $n \in \mathbb{N} - \{0\}$
- **Th**
    - $(\textrm{Mat}_{n \times n}(\mathbb{K}), +, \cdot)$ è un anello

****

# Interpretazione geometrica dei vettori


## Definizione 46


- **Prodotto scalare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
> - $u \cdot v := \displaystyle \sum_{i = 1}^n{x_i \cdot y_i}$ è il **prodotto scalare tra $u$ e $v$**



## Teorema 134


- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $u, v \in \mathbb{K}^n$
- **Th**
    - $u \cdot v = v \cdot u$
    - $\forall w \in \mathbb{K}^n \quad u \cdot (v + w) = u \cdot v + u \cdot w$
    - $u \cdot (\lambda v) = \lambda(u \cdot v)$
    



## Definizione 47


- **Norma di un vettore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $u \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
> - $||u|| := \sqrt{x_1^2 + \ldots + x_n^2}$ è detta **norma di $u$**
>   - graficamente, corrisponde alla lunghezza del vettore $u$ nel piano cartesiano



## Teorema 135


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $u \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
- **Th**
    - $||u|| = \sqrt{u \cdot u}$

****

# Matrici particolari



## Definizione 48


- **Vettore trasposto**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $v \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid \exists x_1, \ldots, x_n \in \mathbb{K} : v = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
> - $v^T = \left(x_1, \ldots, x_n\right)$ è il **vettore trasposto di $v$**
>   - vicendevolmente, se $v$ è un vettore riga, il suo trasposto sarà il corrispondente vettore colonna

- **Matrice trasposta**

> - $m, n \in \mathbb{N} - \{0\}$
> - $\mathbb{K}$ campo
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(A^1, \ldots, A^n\right)$
> - $A^T = \left(\begin{array}{c} {A^1}^T \\ \vdots \\ {A^n}^T \end{array}\right)$ è la **matrice trasposta di $A$**
>   - vale il ragionamento analogo considerando le righe di $A$ al posto delle colonne

- **Matrice simmetrica**

> - $n \in \mathbb{N} - \{0\}$
> - $\mathbb{K}$ campo
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **simmetrica** $\iff A^T = A$



## Teorema 136


- **Hp**
    - $m, n \in \mathbb{N} - \{0\}$
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $(A\cdot B)^T = B^T\cdot A^T$



## Definizione 49


- **Matrice identità**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $I_n = \left(\begin{array}{c}e_1 \\ \vdots \\ e_n \end{array}\right) = \left(e_1^T, \ldots, e_n^T\right) = \left(\begin{array}{ccccc}1 & 0 & \cdots & \cdots & 0 \\ \vdots & \ddots & & & \vdots\\ 0 & \cdots & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots\\ 0 &\cdots & \cdots & 0 & 1\end{array}\right)$ è detta **matrice identità**

- **Matrice invertibile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ **invertibile** $\iff \exists A^{-1} \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A\cdot A^{-1} = A^{-1} \cdot A = I_n$

- **Gruppo Generale Lineare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $\textrm{GL}(n, \mathbb{K}) := \{A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ invertibile$\}$ è detto **gruppo generale lineare invertibile**



## Teorema 137


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
- **Th**
    - $(\textrm{GL}(n, \mathbb{K}), \cdot)$ è un gruppo



## Teorema 138


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $f: \textrm{GL}(n, \mathbb{K}) \rightarrow \mathbb{K}^*$
- **Th**
    - $f$ morfismo di gruppi



## Definizione 50


- **Matrice ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{GL}(n, \mathbb{K})$
> - $A$ è detta **ortogonale** $\iff A \cdot A^T = A^T \cdot A = I_n$
>   - in particolare $A^{-1} = A^T$

- **Gruppo ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{GL}(n, \mathbb{K})$
> - $O(n) := \{ A \in \textrm{GL}(n, \mathbb{K}) \mid A$ ortogonale$\}$ è detto **gruppo ortogonale**



## Definizione 51


- **Gruppo Speciale Lineare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $\textrm{SL}(n, \mathbb{K}) := \{A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) = 1\}$ è detto **gruppo generale lineare invertibile**



## Definizione 52


- **Matrici simili**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ **simile a $B$** $\iff \exists C \in \textrm{GL}(n, \mathbb{K}) \mid A = C^{-1}BC$



## Definizione 53


- **Traccia**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\textrm{tr}(A) := a_{1,1}+ \ldots + a_{n,n}$ è detta **traccia di $A$**



## Teorema 139


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\textrm{tr}(A) = \textrm{tr}(B)$



## Definizione 54
 

- **Matrice triangolare superiore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare superiore** $\iff \forall i, j \in [1, n], i \gt j \quad a_{i,j} = 0$

- **Matrice triangolare inferiore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare superiore** $\iff \forall i, j \in [1, n], i \lt j \quad a_{i,j} = 0$

- **Matrice triangolare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare $\iff$** $A$ triangolare superiore o triangolare inferiore

- **Matrice triangolarizzabile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolarizzabile** $\iff \exists B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid B$ triangolare $\land \ B$ simile ad $A$

- **Matrice diagonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **diagonale** $\iff \forall i, j \in [1, n], i \neq j \quad a_{i, j} = 0$
>   - in particolare, $A$ è diagonale $\iff A$ triangolare superiore ed inferiore

- **Matrice diagonalizzabile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **diagonalizzabile** $\iff \exists B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid B$ diagonale $\land \ B$ simile ad $A$



## Teorema 140


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ diagonalizzabile
- **Th**
    - $A$ triangolarizzabile



## Definizione 55


- **Sottomatrice di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $A_i^j$ è una **sottomatrice di $A$** $\iff A_i^j$ si ottiene rimuovendo $A_i$ e $A^j$ da $A$

- **Minore di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $M$ è un **minore di $A$** $\iff M$ è una sottomatrice quadrata di $A$

- **Orlato di un minore**

> - $\mathbb{K}$ campo
> - $m, n, r \in \mathbb{N} - \{0\} \mid r \lt m \land r \lt n$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $M \in \textrm{Mat}_{r \times r}(\mathbb{K})$ è un minore di $A$
> - $M' \in \textrm{Mat}_{(r + 1) \times (r + 1)}(\mathbb{K})$ è un **orlato di $M$** $\iff M'$ è un minore di $A$ e $M$ si ottiene rimuovendo una riga e una colonna da $M'$



## Teorema 141


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n, r \in \mathbb{N} - \{0\} \mid r \lt m \land r \lt n$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $M \in \textrm{Mat}_{r \times r}(\mathbb{K})$ è un minore di $A$
- **Th**
    - $M$ ha $(m-r)\cdot(n-r)$ orlati in $A$
    


## Definizione 56


- **Matrice completa**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
> - $A_b:=\left(\begin{array}{cccc}a_{1, 1} & \cdots & a_{1, n} & b_1 \\ \vdots & \ddots & \vdots & \vdots \\ a_{m, 1} & \cdots & a_{m,n} & b_m\end{array}\right)$



## Definizione 57


- **Matrice di un'applicazione lineare**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $\mathcal{B}=\{v_1, \ldots, v_n\}$ base di $V$
> - $\mathcal{C}=\{w_1, \ldots, w_m\}$ base di $W$
> - $f: V \rightarrow W$ isomorfismo
> - $\varphi_\mathcal{B}: \mathbb{K}^N \rightarrow V$ isomorfismo
> - $\varphi_\mathcal{C}: \mathbb{K}^M \rightarrow W$ isomorfismo
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid f = \varphi_\mathcal{C}\cdot L_A \cdot \varphi_\mathcal{B}^{-1}$ è detta **matrice di $f$**
>   - è possibile dimostrare che $\forall f$ applicazione lineare$\quad \exists ! A \in \textrm{Mat}_{m \times n}(\mathbb{K})$

****

# Rango



## Definizione 58


- **Sottospazio ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $V \subset \mathbb{K}^n$ sottospazio vettoriale
> - $V^{\perp} := \{w \in \mathbb{K}^n \mid \forall v \in V \quad w \cdot v = 0_{\mathbb{K}^n}\}$ è detto **sottospazio ortogonale di $\mathbb{K}^n$**
>     - la definizione ha significato poiché il prodotto scalare tra due vettori è nullo esattamente quando i due vettori sono perpendicolari tra loro, per osservazione precedente



## Teorema 142


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $V^{\bot}$ è sottospazio vettoriale di $\mathbb{K}^n$



## Teorema 143


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $\dim(V^{\bot}) = \dim(\mathbb{K}^n) - \dim(V)$



## Definizione 59


- **Moltiplicazione sinistra**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $L_A:\mathbb{K}^n \rightarrow \mathbb{K}^m: x \rightarrow A\cdot x$ è detta **moltiplicazione sinistra di $A$**



## Teorema 144


- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $L_A$ è una trasformazione lineare



## Teorema 145


- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\ker(L_A) = \textrm{span}(A_1, \ldots, A_m)^\bot$
    - $\textrm{im}(L_A) = \textrm{span}(A^1, \ldots, A^n)$

## Definizione 60


- **Rango di una matrice**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\textrm{rk}(A):=\textrm{rk}(L_A)$ è il **rango di $A$**



## Teorema 146


- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\textrm{rk}(A) =\dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A_1, \ldots, A_n))$

****

# Operazioni su righe e colonne


## Definizione 61


- **Scambio di righe di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A_1, \ldots, A_m$ righe di $A$, scambiare $A_i$ e $A_j$ lascia invariato $\ker(L_A)$

- **Moltiplicazione di una riga per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, moltiplicare $A_i$ per $\lambda$ lascia invariato $\ker(L_A)$

- **Somma di una riga con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, sommare ad $A_i$ un certo $\lambda \cdot A_j$ lascia invariato $\ker(L_A)$

- **Scambio di colonne di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, scambiare $A^i$ e $A^j$ lascia invariato $\textrm{im}(L_A)$

- **Moltiplicazione di una colonna per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, moltiplicare $A^i$ per $\lambda$ lascia invariato $\textrm{im}(L_A)$

- **Somma di una colonna con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ righe di $A$, sommare ad $A^i$ un certo $\lambda \cdot A^j$ lascia invariato $\textrm{im}(L_A)$



## Teorema 147


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni _tra righe_ definite precedentemente
- **Th**
    - $\equiv$ una relazione di equivalenza



## Teorema 148


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni _tra righe_ definite precedentemente
- **Th**
    - $A \equiv B \implies \ker(L_A) = \ker(L_B) \land \textrm{rk}(A) = \textrm{rk}(B)$



## Teorema 149


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni _tra colonne_ definite precedentemente
- **Th**
    - $\equiv$ una relazione di equivalenza



## Teorema 150


- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni _tra colonne_ definite precedentemente
- **Th**
    - $A \equiv B \implies \textrm{im}(L_A) = \textrm{im}(L_B) \land \textrm{rk}(A) = \textrm{rk}(B)$




****
# Determinante



## Definizione 62


- **Applicazione multilineare**

> - $\mathbb{K}$ campo
> - $k \in \mathbb{N}$
> - $V_1, \ldots, V_k, W$ spazi vettoriali
> - $f: V_1 \times \ldots \times V_k \rightarrow W:(v_1, \ldots, v_k) \rightarrow w$
> - $f$ **multilineare** $\iff \forall i \in [1, k], \ \forall v_1 \in V_1, \ldots, v_i', v_i'' \in V_i, \ldots, v_k \in V_k, \ \forall \lambda, \mu \in \mathbb{K} \quad f(v_1, \ldots, \lambda v_i'+\mu v_i'', \ldots, v_k) = \lambda f(v_1, \ldots, v_i', \ldots, v_k) + \mu f(v_1, \ldots, v_i'', \ldots, v_k)$

- **Determinante**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $\det : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
> - 1. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad \det$ multilineare su $A_1, \ldots A_n$ e $A^1, \ldots, A^n$
> - 2. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad A_1, \ldots A_n$ e $A^1, \ldots, A^n$ basi di $\mathbb{K}^n \iff \det(A) \neq 0$
> - 3. $\det(I_n) = 1$
> - 4. per $\mathbb{K} \mid 1 \neq -1 \quad$ scambiando due righe o due colonne $\det(A)$ cambia segno
> - $\det$ è il **determinante** $\iff \det$ verifica 1, 2 e 3, oppure 1, 3 e 4
>   - poiché è possibile dimostrare che la funzione che verifica tali condizioni esiste ed è unica, allora il $\det$ è totalmente determinato da tali caratteristiche



## Teorema 151


- **Hp**
    - $\mathbb{K}$ campo $\mid 1 \neq -1$
    - $n \in \mathbb{N} - \{0\}$
    - $f : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
    4. **⚠️  SCRIVI**
- **Th**
    - **⚠️  DETERMINANTE ALTERNANTE**



## Definizione 63


- **Matrice singolare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **singolare** $\iff \det(A) = 0$



## Teorema 152


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ invertibile
    2. $\textrm{rk}(A)=n$
    3. $A_1, \ldots, A_n$ base di $\mathbb{K}^n$
    4. $A^1, \ldots, A^n$ base di $\mathbb{K}^n$
    5. $\det(A) \neq 0$
    6. $A \equiv I_n$ tramite la relazione di equivalenza delle operazioni sulle righe
    7. $A \equiv I_n$ tramite la relazione di equivalenza delle operazioni sulle colonne
- **Th**
    - le proposizioni sono equivalenti

## Teorema 153


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \exists i \in [1, n] : A_i = 0_{\mathbb{K}^n} \lor \exists j \in [1, n] : A^j = 0_{\mathbb{K}^n}$, ovvero in $A$ è presente o una riga, o una colonna nulla
- **Th**
    - $\det(A) = 0$



## Teorema 154


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A) = \det(A^T)$



## Teorema 155


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\det(A) = \det(B)$

## Teorema 156


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\displaystyle{\det(A) = \sum_{\sigma \in S_n} \textrm{sgn}(\sigma) \cdot \prod_{i=1}^n{a_{i, \sigma_i}}}$



## Teorema 157


- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K})$
    - $A = \left(\begin{array}{cc}a_{1,1} & a_{1, 2} \\ a_{2, 1} & a_{2, 2}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}-a_{1,2}a_{2,1}$



## Teorema 158


- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{3 \times 3}(\mathbb{K})$
    - $A = \left(\begin{array}{ccc}a_{1,1} & a_{1, 2} & a_{1,3}\\ a_{2, 1} & a_{2, 2} & a_{2,3} \\ a_{3,1} & a_{3,2} & a_{3,3}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}a_{3,3}+a_{1,3}a_{2,1}a_{3,2}+a_{1,2}a_{2,3}a_{3,1} - a_{1,3}a_{2,2}a_{3,1}-a_{1,1}a_{2,3}a_{3,2}-a_{1,2}a_{2,1}a_{3,3}$



## Teorema 159


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ triangolare
- **Th**
    - $\det(A) = a_{1,1} \cdot \ldots \cdot a_{n, n}$



## Teorema 160


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $\lambda \in \mathbb{K}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $A' = \left(\begin{array}{c}A_1 \\ \vdots \\ \lambda A_i \\ \vdots \\ A_n \end{array}\right)$
- **Th**
    - $\det(A')=\lambda \cdot \det(A)$



## Teorema 161


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\forall 1 \le i, j \le n \quad \det(A) = \displaystyle \sum_{k = 1}^{n}{(-1)^{i + k}\cdot a_{i, k} \cdot \det(A_i^k)} = \sum_{h = 1}^n{(-1)^{h + j}\cdot a_{h, j} \cdot \det(A_h^j)}$



## Definizione 64


- **Aggiunta di una matrice**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A^*$ è detta **aggiunta di $A$** $\iff \forall i, j \in [1, n] \quad a^*_{i, j} = (-1)^{i + j}\cdot \det(A_i^j)$



## Teorema 162


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0$
- **Th**
    - $A^{-1}=\dfrac{(A^*)^T}{\det(A)}$



## Teorema 163


- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K}) \mid \det(A) \neq 0$
    - $A = \left(\begin{array}{cc}a & b \\ c & d\end{array}\right)$
- **Th**
    - $A^{-1}=\dfrac{1}{ad - bc} \left(\begin{array}{cc}d & -b \\ -c & a\end{array}\right)$

****

# Polinomio caratteristico



## Definizione 65


> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $p_A(x) := \det(x\cdot I_n - A)$ è detto **polinomio caratteristico di $A$**



## Teorema 164


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $p_A(x) = x^n - \textrm{tr}(A)\cdot x^{n -1} + \ldots + (-1)^n \cdot \det(A)$



## Teorema 165


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $p_A(x) = p_B(x)$



## Definizione 66


- **Autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K} \mid p_A(\lambda) = 0$ è detto **autovalore di $A$**

- **Spettro**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\textrm{sp}(A) := \{\lambda \in \mathbb{K} \mid p_A(\lambda) = 0\}$ è detto **spettro di $A$**



## Teorema 166


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\textrm{sp}(A) = \textrm{sp}(B)$



## Teorema 167


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \mathbb{K}$
- **Th**
    - $\lambda$ autovalore $\iff \exists v \in \mathbb{K}^n - \{0\} \mid A \cdot v = \lambda \cdot v$

## Definizione 67


- **Autovettore relativo ad un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $v \in \mathbb{K}^n - \{0\}$ è detto **autovettore di $A$ relativo a $\lambda$** $\iff (A- \lambda \cdot I_n) \cdot v = 0$



## Teorema 168


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda_1, \ldots, \lambda_k \in \textrm{sp}(A)$
    - $v_1, \ldots, v_k$ autovettori di $A$ relativi rispettivamente a $\lambda_1, \ldots, \lambda_k$
- **Th**
    - $v_1, \ldots, v_k$ linearmente indipendenti



## Definizione 68


- **Autospazio relativo ad un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\textrm{E}_\lambda(A) := \{v \in \mathbb{K}^n \mid (A - \lambda \cdot I_n) \cdot v = 0\}$ è detto **autospazio di $A$ relativo a $\lambda$**
>   - in particolare $0_{\mathbb{K}^n} \in \textrm{E}_\lambda(A)$



## Teorema 169


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\textrm{E}_\lambda(A) \subset \mathbb{K}$ sottospazio vettoriale



## Definizione 69


- **Molteplicità algebrica di un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\mu(\lambda) := \max(\{\varepsilon \in \mathbb{N} : (x - \lambda)^\varepsilon \mid p_A(x)\})$ è detta **molteplicità algebrica di $\lambda$**



## Teorema 170


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
    - $\lambda \in \textrm{sp}(A) = \textrm{sp}(B)$
- **Th**
    - $\mu_A(\lambda) = \mu_B(\lambda)$



## Definizione 70


- **Molteplicità geometrica di un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\nu(\lambda):=\dim(\textrm{E}_\lambda(A))$ è detta **molteplicità geometrica di $\lambda$**



## Teorema 171


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
    - $\lambda \in \textrm{sp}(A) = \textrm{sp}(B)$
- **Th**
    - $\nu_A(\lambda) = \nu_B(\lambda)$



## Teorema 172


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\nu(\lambda) = n - \textrm{rk}(A - \lambda \cdot I_n)$

## Teorema 173


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\nu(\lambda) \le \mu(\lambda)$



## Teorema 174


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ triangolarizzabile
    2. $\displaystyle \sum_{\lambda \in \textrm{sp}(A)}{\mu(\lambda)} = n$
    3. $\displaystyle p_A(x) = \prod_{\lambda \in \textrm{sp}(A)}{(x - \lambda)}^{\mu(\lambda)}$, ovvero $p_A(x)$ è completamente fattorizzabile
- **Th**
    - le proposizioni sono equivalenti



## Teorema 175


- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{C})$
- **Th**
    - $A$ è triangolarizzabile

## Teorema 176


- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{R})$
- **Th**
    - $A$ triangolarizzabile $\iff \forall \lambda \in \textrm{sp}(A) \quad \lambda \in \mathbb{R}$



## Teorema 177


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ diagonalizzabile
    2. $\displaystyle \sum_{\lambda \in \textrm{sp}(A)}{\nu(\lambda)} = n$
    3. $\exists B^1, \ldots, B^n$ autovettori di $A \mid B^1, \ldots, B^n$ base di $\mathbb{K}^n$
- **Th**
    - le proposizioni sono equivalenti



## Teorema 178


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $B^1, \ldots, B^n$ autovettori di $A \mid B = (B^1, \ldots, B^n) \in \textrm{GL}(n, \mathbb{K}) \land B^1, \ldots, B^n$ base di $\mathbb{K}^n$
- **Th**
    - $A$ diagonalizzabile



****
# Numeri complessi



## Definizione 71


- **Insieme dei complessi**

> - $\mathbb{C}:=\left\{a+i b \mid a, b \in \mathbb{R}, \  i : i^{2}=-1\right\}$ è l'**insieme dei complessi**
> - $\forall z \in \mathbb{C} \quad \left\{\begin{array}{l}a:=\operatorname{Re}(z) \\ b:=\operatorname{Im}(z)\end{array}\right.$



## Teorema 179


- **Hp**
    - $a, b, c, d \in \mathbb{R}$
    - $z \in \mathbb{C} \mid z=a+i b$
    - $w \in \mathbb{C} \mid w=c+i d$
- **Th**
    - $z + w = (a+b)+i (c +d)$
    - $z\cdot w=(a c-b d)+i(ad+ bc)$



## Definizione 72


- **Coniugato**

> - $a, b \in \mathbb{R}$
> - $z \in \mathbb{C} \mid z=a+i b$
> - $\bar{z}:=a-i b$ è il **coniugato** di $z$



## Teorema 180


- **Hp**
    - $a,b, c, d, \in \mathbb{R}$
    - $z \in \mathbb{C} \mid z=a+i b$
    - $w \in \mathbb{C} \mid w=c+i d$
- **Th**
    - $\overline{z}+\overline{w}=\overline{z+w}$
    - $\overline{z} \cdot \overline{w}=\overline{z \cdot w}$



## Teorema 181


- **Hp**
    - $0 \le \theta \lt 2 \pi$
- **Th**
    - $e^{i \theta}=\cos \theta+i \sin \theta$



## Definizione 73


- **Raggio**

> - $a, b \in \mathbb{R}$
> - $z \in \mathbb{C} \mid z = a+ib$
> - $|z|:=\sqrt{a^{2}+b^{2}}$ è il **raggio** di $z$
>   - corrisponde alla distanza di $z$ dall'origine nel piano di Gauss



## Definizione 74


- **Forma polare**

> - $a, b \in \mathbb{C}$
> - $z \in \mathbb{C}-\{0\}$
> - $z=|z|\cdot e^{i \theta}$ è detta **forma polare di $z$**



## Definizione 75


- **Soluzione principale**

> - $a, b \in \mathbb{R}$
> - $z \in \mathbb{C} \mid z = a + i b$
> - $\arg(z) \subset \mathbb{R}$ è l'**insieme delle soluzioni** del sistema $\left\{\begin{array}{l}\cos \theta=\frac{a}{|z|} \\ \sin \theta=\frac{b}{|z|}\end{array}\right.$
> - per definizione, $\textrm{arg}(z) \implies \exists ! \theta \mid 0 \leq \theta \le 2 \pi$ tale che $\theta$ sia soluzione del sistema, e questo prende il nome di $\textrm{Arg}(z)$, detta **soluzione principale**



## Teorema 182


- **Hp**
  - $(\mathbb{C}, +, \cdot)$ è un gruppo
- **Th**
  - $(\mathbb{C}, +, \cdot )$ è un campo

## Teorema 183


- **Hp**
    - $z, w \in \mathbb{C}$
- **Th**
    - $|z \cdot w|=|z|\cdot |w| \quad \arg(z\cdot w)=\arg(z) + \arg(w)$
    - $|\overline{w}|=|w| \quad \arg(\overline{w})=-\arg(w)$
    - $|w^{-1}|={|w|}^{-1}\quad \arg(w^{-1})=-\arg(w)$
    - $\left|\dfrac{z}{w}\right|=\dfrac{|z|}{|w|} \quad \arg\left(\dfrac{z}{w}\right)=\arg(z) - \arg(w)$



## Teorema 184


- **Hp**
    - $z \in \mathbb{C}$
- **Th**
    - $z^{n}=|z|^{n} e^{i  \theta n} \quad \arg \left( z^{n} \right)=n \arg (z)$



****
# Coefficienti binomiali



## Definizione 76


- **Coefficiente binomiale**

> - $0! := 1$
> - $n, k \in \mathbb{N}$
> - $\displaystyle \binom{n}{k}:=\left\{\begin{array}{ll}\frac{n !}{n !(n-k) !} & k \leqslant n \\ 0 & k>n\end{array}\right.$



## Teorema 185


- **Hp**
  - $n, k \in \mathbb{N}$
- **Th**
  - $\displaystyle \binom{n}{k} = \binom{n}{n-k}$

## Teorema 186


- **Hp**
  - $n, k \in \mathbb{N}$
- **Th**
  - $\displaystyle \binom{n}{k + 1} = \binom{n - 1}{k + 1} \binom{n - 1}{ k}$

## Teorema 187


- **Hp**
  - $p \in \mathbb{P}$
  - $k \in \mathbb{N} \mid 0 \lt k \lt p$
- **Th**
  - $p \ \bigg\vert \displaystyle \binom{p}{k}$

## Teorema 188


- **Hp**
  - $n \in \mathbb{Z}$
  - $p \in \mathbb{P} : p \mid n$
  - $[a] \in \mathbb{Z}_{p}$
- **Th**
  - $n \cdot [a] = [0]$ in $\mathbb{Z}_p$

## Teorema 189


- **Hp**
  - $n \in \mathbb{Z}$
  - $p \in \mathbb{P} : p \mid n$
  - $[a] \in \mathbb{Z}_{p}$
  - $k \in \mathbb{N} \mid 0 \lt k \lt p$
- **Th**
  - $\displaystyle \binom{p}{k} \cdot [a] = [0]$ in $\mathbb{Z}_p$

## Teorema 190


- **Hp**
  - $p \in \mathbb{P}$
  - $[a], [b] \in \mathbb{Z}_p$
- **Th**
  - $([a]+[b])^{p}=[a]^{p}+[b]^{p}$ in $\mathbb{Z}_p$

## Teorema 191


- **Hp**
  - $p \in \mathbb{P}$
  - $[a_1], \ldots, [a_n] \in \mathbb{Z}_p$
- **Th**
  - $\left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}=\left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}$ in $\mathbb{Z}_p$


****
# Induzione



## Definizione 77


- **Induzione**

> - successione di proposizioni infinita $P_{1}, P_{2}, P_{3}, \ldots$
>  - $\left\{\begin{array}{l}P_{1} \textrm{ vera}\\ P_{1}, P_{2}, P_{3}, \ldots, P_{n} \implies P_{n+1} \quad \forall n \ge 1 \end{array}\right.$
>  - allora $P_n$ vera $\forall n$



## Teorema 192


- **Hp**
  - $\left\{\begin{array}{l}F_0 = 0 \\ F_1 = 1 \\ F_n = F_{n - 1} + F_{n - 2} \quad \forall n \ge 2\end{array}\right.$ è detta _sequenza di Fibonacci_

  - $x^2 -x -1 = 0$ ha come soluzioni $\left\{\begin{array}{l}\phi := \dfrac{1+\sqrt{5}}{2} \\ \psi := \dfrac{1 - \sqrt{5}}{2}\end{array}\right.$
- **Th**
  - $\forall n \in \mathbb{N} \quad F_{n}=\dfrac{\varphi^{n}-\psi^{n}}{\varphi-\psi}=\dfrac{\varphi^{n}-\psi^{n}}{\sqrt{5}}$


****
# Teorema fondamentale dell'algebra

- **Hp**
  - $\mathbb{K}$ campo
  - $p(x) \in \mathbb{K}[x] \mid p(x) = a_{0}x^0 + \ldots +a_{n} x^{n}$
- **Th**
  - $\exists z \in \mathbb{C} \mid p(z) = 0$



****


# Teorema della divisione euclidea con il resto

- **Hp**
  - $m \in \mathbb{Z}$
  - $n \in \mathbb{Z} - \{0\}$
- **Th**
  - $\exists !  \ q, r \in \mathbb{Z} \mid m=n q+r \quad 0 \leq r<n$

## Teorema 193


- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x] \mid b(x) \neq 0$
- **Th**
    - $\exists ! q(x), r(x) \in \mathbb{K}[x] \mid a(x) = b(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(b(x))$, che è detto _teorema della divisione con il resto tra polinomi_



****


# Teorema di Lagrange

- **Hp**
  - $G$ gruppo finito
  - $H \subset G$ sottogruppo finito
- **Th**
  - $|G| = |H| \cdot |G / H|$

****


# Teorema fondamentale dell'aritmetica

- **Hp**
  - $a, b \in \mathbb{N}$
- **Th**
  - $\textrm{mcm}(a, b) \cdot \textrm{MCD}(a, b) = a \cdot b$

****


# Teorema cinese dei resti


## Teorema 194


- **Hp**
  - $a_1, \ldots, a_n \ge 2 \in \mathbb{Z}  \mid \textrm{MCD}(a_i, a_j) = 1 \quad \forall i, j \in [1, n] : i \neq j$
  - $m := \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $m = a_1 \cdot \ldots \cdot a_n$

## Teorema 195


- **Hp**
  - $n \in \mathbb{N}$
  - $a_1, \ldots, a_n \in \mathbb{Z}_{n \ge 2}$
  - $m:= \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $\exists \phi \mid \phi: \mathbb{Z}_m \rightarrow \mathbb{Z}_{a_1} \times \ldots \times \mathbb{Z}_{a_n}: x \ (\bmod \ m) \rightarrow (x \ (\bmod \ a_1), \ldots, x \ (\bmod \ a_n))$
  - $\phi$ è una funzione ben definita, ed è iniettiva

## Teorema 196


- **Hp**
  - $n \in \mathbb{N}$
  - $a_1, \ldots, a_n \in \mathbb{Z}_{\ge 2} \mid \forall i, j \in [1, n] \quad i \neq j \implies \textrm{MCD}(a_i, a_j) = 1$
  - $b_1, \ldots, b_n \in \mathbb{Z} \mid 0 \leq b_{1}<a_{1}, \ldots, 0 \leq b_n \lt a_n$
  - $m := \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $\exists ! x \ (\bmod \ m) \mid$ $\left\{\begin{array}{c}x \equiv b_{1}\ \left(\bmod  \ a_{1}\right) \\ \vdots \\ x \equiv b_{n}\ \left(\bmod  \ a_{n}\right)\end{array}\right.$

## Teorema 197


- **Hp**
    - $k \in \mathbb{N}$
    - $n_1, \ldots, n_k \in \mathbb{N} - \{0\} \mid \forall i, j \in [1, k] \quad i \neq j \implies \textrm{MCD}(n_i, n_j) = 1$
    - $N := \textrm{mcm}(n_1, \ldots, n_k)$
    - $[a] \in \mathbb{Z}_N^*$
    - $o := o([a])$ in $\mathbb{Z}_N^*$
    - $\forall h \in [1, k] \quad o_h := o([a])$ in $\mathbb{Z}_{n_h}^*$
- **Th**
    - $o = \textrm{mcm}(o_1, \ldots, o_k)$

****


# Teorema del binomio di Newton

- **Hp**
  - $A$ anello commutativo
  - $a, b \in A$
  - $n \in \mathbb{N}$
- **Th**
  - $(a+b )^n = \displaystyle{\sum_{k = 0}^{n}{\binom{n}{k} a^k b ^{n - k}}}$

## Teorema 198


- ⚠️ **NON HO CAPITO UN CAZZO**



****


# Piccolo teorema di Fermat

- **Hp**
  - $p \in \mathbb{P}$
  - $a \in \mathbb{Z}$
- **Th**
  - $a^{p} \equiv a \ (\bmod \ p)$

## Teorema 199


- **Hp**
  - $p \in \mathbb{P}$
  - $[a] \in \mathbb{Z}_{p}-\{0\}$
- **Th**
  - $[a]^{-1}=\left[a\right]^{p-2}$

## Teorema 200


- **Hp**
    - $p \in \mathbb{P}$
- **Th**
    - $\displaystyle \prod_{0 \lt a \lt p} (x - a) \equiv x^{p - 1} - 1 \ (\bmod \ p)$

## Teorema 201


- ⚠️ **NON HO CAPITO UN CAZZO**



****


# Teorema di Eulero

- **Hp**
    - $a, n \in \mathbb{N} \mid \textrm{MCD}(a, n) = 1$
- **Th**
    - $a^{\varphi(n)} \equiv 1 \ (\bmod \ n)$

****


# Teorema fondamentale di isomorfismo

- **Hp**
    - $A, B$ anelli
    - $f: A \rightarrow B$ morfismo di anelli
- **Th**
    - $A / \textrm{ker}(f) \cong \textrm{im}(f)$, ovvero $\exists \varphi \mid \varphi : A / \textrm{ker}(f) \rightarrow \textrm{im}(f): [a] \rightarrow f(a)$ isomorfismo di anelli

## Teorema 202


- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo di gruppi
- **Th**
  - $G / \textrm{ker}(f) \cong \textrm{im}(f)$, o alternativamente $\exists \varphi \mid \varphi : G / \textrm{ker}(f) \rightarrow \textrm{im}(f): [g] \rightarrow f(g)$ isomorfismo di gruppi

## Teorema 203


- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f:V \rightarrow W$ trasformazione lineare
- **Th**
    - $V/\ker(f) \cong \textrm{im}(f)$, o alternativamente $\exists \varphi \mid \varphi : V/\ker(f) \rightarrow \textrm{im}(f):[v] \rightarrow f(v)$

****


# Teorema di Cauchy

- **Hp**
  - $G$ gruppo finito
  - $p \in \mathbb{P}$
  - $p \bigg\vert |G|$
- **Th**
  - $\exists g \in G \mid o(g) = p$


## Teorema 204


- **Hp**
  - $G$ gruppo $\bigg\vert |G|=4$
- **Th**
  - $G \cong \mathbb{Z}_4$ oppure $G \cong K_4$

****


# Teorema di Carnot

- **Hp**
    - $n \in \mathbb{N} - \{0\}$ 
    - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
    - $\theta$ l'angolo compreso tra $u$ e $v$
- **Th**
    - $||v - u||^2 = ||u||^2 + ||v||^2 - 2\cos(\theta) \cdot||u||\cdot ||v||$


## Teorema 205


- **Hp**
    - $n \in \mathbb{N} - \{0\}$ 
    - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
    - $\theta$ l'angolo compreso tra $u$ e $v$
- **Th**
    - $\cos(\theta)= \dfrac{u \cdot v}{||u|| \cdot ||v||}$

****


# Teorema del rango

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f:V \rightarrow W$ trasformazione lineare
- **Th**
    - $\textrm{rk}(f) = \dim(V) - \dim(\ker(f))$

****


# Teorema di Rouché-Capelli

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
- **Th**
    - $\exists x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A\cdot x = b \iff \textrm{rk}(A) = \textrm{rk}(A_b)$

****


# Teorema di Cramer

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0$
    - $b \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
- **Th**
    - $\left\{\begin{array}{c}x_1 = \dfrac{1}{\det(A)} \cdot \det\left(\begin{array}{cccc}b_1 & a_{1,2} &\cdots & a_{1,n} \\ \vdots & \vdots & \ddots & \vdots \\ b_n & a_{n, 2} & \cdots & a_{n,n}\end{array}\right) \\ \vdots \\ x_n = \dfrac{1}{\det(A)} \cdot \det\left(\begin{array}{cccc}a_{1,1} & \cdots & a_{1,n-1} & b_1\\ \vdots & \ddots & \vdots & \vdots \\ a_{n, 1} & \cdots & a_{n,n-1} & b_n\end{array}\right) \end{array}\right.$ sono le componenti del vettore $x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A \cdot x = b$



****


# Teorema di Kronecker

- **Hp**
    - $\mathbb{K}$ campo
    - $n, r, r' \in \mathbb{N} - \{0\} \mid r \lt r' \lt n$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $M_1 \in \textrm{Mat}_{r \times r}(\mathbb{K}) \mid M_1$ minore di $A \land \det(A) \neq 0$
- **Th**
    - $\textrm{rk}(A)=r \iff \forall M_1'$ orlato di $M_1 \quad \det(M_1') = 0 \iff \forall M_2 \in \textrm{Mat}_{r' \times r'}(\mathbb{K}) \mid M_2$ minore di $A \quad \det(M_2) = 0$



****


# Teorema di Binet

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A \cdot B) = \det(A) \cdot \det(B)$


## Teorema 206


- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A)^{-1}=\det(A^{-1})$

****


# Teorema spettrale

- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{R}) \mid A$ simmetrica
    1. $\forall \lambda \in \textrm{sp}(A) \quad \lambda \in \mathbb{R}$
    2. $A$ diagonalizzabile
    3. $\exists B^1, \ldots, B^n$ autovettori di $A \mid B^1, \ldots, B^n$ base ortonormale di $\mathbb{R}^n$
    4. $\exists B \in O(n) \mid B^{-1}AB$ diagonale
- **Th**
    - le proposizioni sono equivalenti

