# Permutazioni

## Def

- **Permutazioni**

> - $X$ insieme
> - $S_X := \{f \mid f:X \rightarrow X$ biiettiva $\}$ è l'**insieme delle permutazioni di $X$**
> - $X = \{1, \ldots, n\} \implies S_n$ è detto **gruppo simmetrico di $n$**

## Oss

- **Hp**
  - $S_X := \{f \mid f : X \rightarrow Y$ biiettiva $\}$
- **Th**
  - $(S_X, \circ)$ è un gruppo, non abeliano se $|X| \ge 3$
- **Dim**
  - la composizione di funzioni è associativa
  - $\textrm{id}$ è biiettiva $\implies \textrm{id} \in S_X$ per definizione, e costituisce l'elemento neutro
  - $\forall f:X \rightarrow Y \in S_X \quad \exists f^{-1}: Y \rightarrow X$, poiché $f \in S_X \implies f$ biiettiva, e ogni funzione biiettiva è invertibile
  - $|X| = 2 \implies X$ è della forma $X = \{a, b\}$, quindi $S_X =\left\{\begin{array}{l}a \rightarrow a \\ b \rightarrow b\end{array}\right. \ ,\ \left.\begin{array}{l}a \rightarrow b \\ b \rightarrow a\end{array}\right\}$, dove uno dei due elementi è $\rm id$
    - $\rm id \circ id = id$
    - $\rm \sigma \circ id = id \circ \sigma = \sigma$
    - $\rm \sigma \circ \sigma = id$ per costruzione
  - quindi $|X| = 2 \implies S_X$ è abeliano, mentre $|X| = 1 \implies S_X$ è abeliano perché contiene un solo elemento

## Def

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

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
  - $1 \le i \lt n \in \mathbb{N}$
  - $I(\sigma, i):=\left\{n \in \mathbb{Z} \mid \sigma^{n}(i)=i\right\}$
- **Th**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è un ideale
- **Dim**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è un sottogruppo
    - $\sigma ^0 = \textrm{id} \implies \forall i \quad \sigma ^0(i) = \textrm{id}(i) = i \implies 0 \in I(\sigma, i)$
    - $m, n \in I(\sigma, i) \implies \sigma^m (i) = \sigma^n(i) = i$, ma $\sigma^{m+n}(i)=\sigma^{m}\left(\sigma^{n}(i)\right) = \sigma^m(i)=i \implies m + n \in I(\sigma, i)$
    - $n \in I(\sigma, i) \implies \sigma ^n (i) = i$, ma per simmetria della permutazione $\sigma^ {-n} (i) = i \implies -n \in I(\sigma, i)$
  - $\forall \tau \in S_n \mid \tau (i) = i \implies \forall k \in \mathbb{Z} \quad  \tau ^k (i) = i$, ma allora $\forall n \in I(\sigma, i) \quad \sigma^n(i) = i$ si può riscrivere come $(\sigma^n)^k(i) = i \quad \forall k \in \mathbb{Z} \implies \sigma^{nk}(i) = i \implies nk \in I(\sigma, i)$

## Oss

- **Hp**
    - ⚠️ **RISCRIVI TUTTO**
    - $I(\sigma, i)$ è **ideale principale** in $\mathbb{Z}$ generato da $I(d)$, dove $d$ è la lunghezza del ciclo di $i$, quindi $I(\sigma, i) = I(d)$
  - $I(\sigma, i) = I(d) \implies d \in I(\sigma, i)$
- **Dim**
  - ⚠️ **MANCA DIMOSTRAZIONE**

## Cor

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n \mid \sigma = \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
  - $d_j:=$ lunghezza di $\gamma_j \quad \forall j \in [1, k]$
  - $m := \textrm{mcm}(d_1, \ldots, d_k)$
  -  $I(\sigma):=\left\{n \in \mathbb{Z} \mid \sigma^{n}=\textrm{id}\right\}$
- **Th**
  - $o(\sigma) = m$
- **Dim**
  - $n \in I(\sigma) \iff \sigma^{n}=\textrm{id} \iff \forall 1 \leq i \leq n \quad \sigma^{n}(i)=i \iff \forall 1 \leq i \leq n \quad n \in I(\sigma, i) \iff n \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - di conseguenza $n \in I(\sigma) \iff n \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$ e dunque $I(\sigma) =I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - inoltre, per dimostrazione precedente $I(\sigma) = I(\sigma, 1) \cap \ldots \cap I(\sigma, n) = I(d_1) \cap \ldots \cap I(d_k)$
  - per dimostrazione precedente $I(d_1) \cap \ldots \cap I(d_k) = I(m) = I(\sigma)$
  - dato $d := o(\sigma)$, per dimostrazione precedente $I(m) = I(\sigma) = I(d) \implies m = d$

****

# Trasposizioni

## Def

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

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
- **Th**
  - $\exists 1 \leq i_1, \ldots, i_k \lt n \mid \sigma = \tau_{i_1, i_1 + 1} \ldots \tau_{i_k, i_k + 1}$, quindi ogni permutazione può essere riscritta come composizione di trasposizioni adiacenti
- **Dim**
  - $\tau_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ 1 & \cdots & j & \cdots & i & \cdots & n\end{array}\right)$ è una trasposizione qualsiasi
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) & \cdots & \sigma(j) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(j) & \cdots & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - in particolare, se le trasposizioni devono essere adiacenti, allora ogni trasposizione invertirà due colonne adiacenti alla volta
  - _esempio_
    - $\sigma=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 3 & 1\end{array}\right) \implies \sigma \tau_{34}\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 1 & 3\end{array}\right) \implies$ $\sigma \tau_{3 4} \tau_{23}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3\end{array}\right) \implies$$\sigma \tau_{3 4} \tau_{23} \tau_{12}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 4 & 3\end{array}\right) \implies$$\sigma \tau_{34} \tau_{23} \tau_{12} \tau_{34}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4\end{array}\right) = \textrm{id}$, ma allora $\textrm{id} = \sigma \tau_{34} \tau_{23} \tau_{12} \tau_{34} \iff \sigma =\tau_{34} \tau_{12} \tau_{23} \tau_{34}$
     
****

# Segno

## Def

- **Segno di una permutazione**

> - $n \in \mathbb{N}$
> - $\sigma \in S_n$
> - $\textrm{Inv}(\sigma) := \{ (i, j) \mid 1 \leq i \lt j \lt n : \sigma(i) \gt \sigma(j)\}$ è l'**insieme delle inversioni di $\sigma$**
> - $\textrm{sgn}(\sigma) := (-1)^{|\textrm{Inv}(\sigma)|} =$$\left\{\begin{array}{ll}+1 & |\operatorname{Inv}(\sigma)| \equiv 0 \ (\bmod  \ 2) \\ -1 & |\operatorname{Inv}(\sigma)| \equiv 1 \ (\bmod \ 2)\end{array}\right. \implies \sigma$ **pari** $\iff \textrm{sgn}(\sigma) = +1$
>   - $\textrm{sgn}(\textrm{id}) = (-1)^0 = 1$, in quando la funzione identità non ha inversioni

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $A_n := \{\sigma \in S_n \mid \sigma$ pari$\}$
- **Th**
    - $A_n \subset S_n$ è un sottogruppo normale, detto _gruppo alterno di ordine $n$_
- **Dim**
    - ⚠️ **MANCA DIMOSTRAZIONE**

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_{n} \mid \sigma=\tau_{1} \ldots \tau_{k}$ dove $\forall j \in [1, k] \quad \tau_{j} = \tau_{j, j + 1}$, dunque tutte le trasposizioni sono adiacenti
- **Th**
    - $\textrm{sgn}(\sigma)= (-1)^k$
- **Dim**
   - $\tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ 1 & \cdots & i + 1 &  & i & \cdots & n\end{array}\right)$ è una trasposizione adiacente
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) &  & \sigma(i + 1) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i + 1) &  & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - di conseguenza $\textrm{Inv}(\sigma \tau_{i, i + 1})=$$\left\{\begin{array}{ll}\operatorname{Inv}(\sigma) \cup\{(i, i+1)\} & (i, i+1) \notin \operatorname{Inv}(\sigma) \\ \operatorname{Inv}(\sigma)-\{(i, i+1)\} & (i, i+1) \in \operatorname{Inv}(\sigma)\end{array}\right.$
      - $\forall i \mid i \lt i + 1 \quad (i, i + 1) \in \textrm{Inv}(\sigma) \iff \sigma(i) \gt \sigma(i + 1)$
    - in $\sigma \tau_{i, i + 1}$ le colonne $i$ e $i + 1$ si invertono, e di conseguenza $\sigma \tau_{i, i + 1}(i) \lt \sigma \tau_{i, i + 1}(i +1) \implies (i, i + 1) \notin \textrm{Inv}(\sigma \tau_{i, i + 1})$ per definizione
  - dunque $|\textrm{Inv}(\sigma \tau_{i, i + 1}) | = | \textrm{Inv}(\sigma) | \pm 1 \implies (-1)^{\mid \textrm{Inv}(\sigma \tau_{i, i + 1})\mid} = (-1)^{\mid \textrm{Inv}(\sigma) \mid \pm 1} \implies \textrm{sgn}(\sigma \tau_{i, i + 1}) = - \textrm{sgn}(\sigma)$ poiché $\pm 1$ all'esponente di $(-1)$ ne invertirà il segno
    - dunque aggiungendo o togliendo una trasposizione adiacente ad una permutazione, si inverte il segno della composizione
  - $\sigma =\tau_{1} \ldots \tau_{k} \implies \textrm{id} = \sigma \tau_k \ldots \tau_1$ poiché ogni trasposizione è l'inversa di sé stessa, e dunque $\textrm{sgn}(\textrm{id}) = 1 = \textrm{sgn}(\sigma \tau_k \ldots \tau_1)$ poiché se sono uguali, saranno uguali anche i loro segni
  - $\textrm{sgn}(\sigma \tau_k \ldots \tau_1) = -\textrm{sgn}(\sigma \tau_k \ldots \tau_2) = \textrm{sgn}(\sigma \tau_k \ldots \tau_3) = \ldots = (-1)^k \cdot \textrm{sgn}(\sigma)$ poiché sono state rimosse esattamente $k$ trasposizioni adiacenti
  - allora $(-1)^k \cdot \textrm{sgn}(\sigma) = \textrm{sgn}(\textrm{id}) = 1$
  - $\textrm{sgn}(\sigma) = \pm 1$, e poiché $(-1)^k \cdot \textrm{sgn}(\sigma)  = 1$, allora necessariamente $\textrm{sgn}(\sigma) = (-1)^k$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^{\prime} \in S_{n} | \left\{\begin{array}{l}\sigma = \tau_1 \ldots \tau_k \\ \sigma ' = \tau_1^{\prime} \ldots \tau_h^{\prime}\end{array}\right.$, dove ogni trasposizione è adiacente
- **Th**
    - $\operatorname{sgn}\left(\sigma \sigma^{\prime}\right)=\operatorname{sgn}(\sigma)\cdot \textrm{sgn}(\sigma ')$
- **Dim**
  - $\sigma \sigma^\prime = \tau_1 \ldots \tau_k \cdot \tau_1^\prime \ldots \tau_h^\prime$, dunque il numero di trasposizioni adiacenti di $\sigma \sigma^\prime$ è $k + h$
  - per dimostrazione precedente $\textrm{sgn}(\sigma \sigma^\prime) = (-1)^ {k + h} = (-1)^k \cdot (-1)^h = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^\prime)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_n$
- **Th**
    - $\textrm{sgn}(\sigma^{-1})=\textrm{sgn}(\sigma)$
- **Dim**
  - $\left.\begin{array}{l}\operatorname{sgn}(\textrm{id})=1 \\ \sigma \sigma^{-1}=\textrm{id} \implies \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\textrm{sgn}(\textrm{id}) \\ \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\operatorname{sgn}(\sigma) \cdot \operatorname{sgn}\left(\sigma^{-1}\right)\end{array}\right\} \implies \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^{-1})= 1$
      - $\forall \sigma \in S_n \quad \textrm{sgn}(\sigma) = \pm 1$, di conseguenza se esistono due permutazioni $\alpha, \beta \in S_n \mid \textrm{sgn}(\alpha) \cdot \textrm{sgn}(\beta) = 1$, allora necessariamente i due segni devono essere o entrambi $1$ o entrambi $-1$, e dunque i segni coincidono
  - dunque $\textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^{-1})= 1 \implies \textrm{sgn}(\sigma)= \textrm{sgn}(\sigma^{-1})$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
  - $\sigma, \sigma^\prime \in S_n$
  - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
- **Th**
    - $\textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$
- **Dim**
  - $\sigma \sim \sigma' \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\alpha)\cdot \textrm{sgn}(\sigma)\cdot \textrm{sgn}(\alpha^{-1})$
  - per dimostrazione precedente $\forall \alpha \in S_n \quad \textrm{sgn}(\alpha)= \textrm{sgn}(\alpha^{-1})$, dunque entrambe $1$ o entrambe $-1
  - quindi $\textrm{sgn}(\alpha) \cdot \textrm{sgn}(\alpha^{-1}) = 1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^\prime \in S_n \mid \sigma := \gamma_1 \ldots \gamma_k, \sigma^\prime := \gamma_1^\prime \ldots \gamma_h^\prime$
    - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$, che costituisce dunque la relazione di coniugio
- **Th**
    - $\sigma \sim \sigma ^\prime \iff$$\left\{\begin{array}{c}k=h \\ d=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}=d_{k}^{\prime}\end{array}\right.$, dove $d_j$ è la lunghezza del ciclo $\gamma_j$ e $d_j^\prime$ è la lunghezza del ciclo $\gamma_j^\prime$
- **Dim**
  - _prima implicazione_
    - ⚠️ **NIENTE HA SENSO DI QUELLO CHE C'È SCRITTO IN QUESTA IMPLICAZIONE**
    - per definizione $\sigma \sim \sigma^\prime \implies \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
    - $\forall i_1, \ldots, i_d \mid (i_1 \ldots i_d)$ è un ciclo di $\sigma$, per la relazione di coniugio si ottiene che $\sigma^\prime(\alpha(i_j))=(\alpha \sigma \alpha^{-1})(\alpha(i_j)) \implies (\alpha\sigma)(i_j)=$$\left\{\begin{array}{ll}\alpha\left(i_{j}+1\right) & j<d \\ \alpha\left(i_{1}\right) & j=d\end{array}\right.$ perché $\sigma(i) = i_{j + 1} \quad \forall j \lt d$ perché $i_j \in (i_1 \ldots i_d)$ ciclo di $\sigma$
    - quindi la relazione di coniugio determina un ciclo in $\sigma^\prime$ della forma $(\alpha(i_1) \ldots \alpha(i_d))$
    - ⚠️ **PERCHÉ È BIUNIVOCA?**
    - $(i_1 \ldots i_d)$ un certo ciclo in $\sigma \implies (\alpha(i_1) \ldots \alpha(i_d))$ è un ciclo in $\sigma^\prime$
      - corrispondenza biunivoca tra cicli di $\sigma$ e $\sigma^\prime \implies h = k$ (devono avere lo stesso numero di cicli), e inoltre implica $\left\{\begin{array}{c}k=h \\ d=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}=d_{k}^{\prime}\end{array}\right.$, ovvero i cicli hanno la stessa lunghezza
  - _seconda implicazione_
    - $\sigma = (i_1 \ldots i_{d_1}) \ldots (j_1 \ldots j_{d_k})$ è la decomposizione in cicli di $\sigma$
    - $\sigma^\prime =(a_1 \ldots a_{d_1}) \ldots (b_1 \ldots b_{d_k})$ è la decomposizione in cicli di $\sigma'$
    - poiché in ipotesi $\sigma$ e $\sigma'$ hanno stesso numero di cicli, e cicli di stessa lunghezza, allora $\exists \alpha \in S_n \mid$$\left\{\begin{array}{c}\alpha\left(i_{p}\right)=a_{p} \\ \vdots \\ \alpha\left(j_{q}\right)=b_{q}\end{array}\right.$

      - _esempio_
        - $\begin{aligned} \sigma\ =\ &(13)(254)(876) \\ & \ \downarrow  \downarrow \ \  \downarrow   \downarrow \downarrow \  \ \ \downarrow \downarrow  \downarrow \\ \sigma^{\prime}=\ &(25)(184)(376) \end{aligned}$ $\implies$$\alpha=\left(\begin{array}{llllllll}1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 2 & 1 & 5 & 4 & 8 & 6 & 7 & 3\end{array}\right)$
    - scelto $\alpha \in S_n$ in questo modo, allora ad esempio $\forall i_p \in (i_1 \ldots i_{d_1})$ primo ciclo di $\sigma \implies i_p = \alpha^{-1}(a_p)$ per definizione di $\alpha \implies \alpha \sigma \alpha^{-1} (a_p) = \alpha \sigma (i_p) =$$\left\{\begin{array}{ll}\alpha\left(i_{p+1}\right) & p<d_1 \\ \alpha\left(i_{1}\right) & p=d_{1}\end{array}\right. \iff \left\{\begin{array}{ll}a_{p+1} & p<d_{1} \\ a_{1} & p=d_{1}\end{array}\right. = \sigma^\prime(a_p)$ per definizione di $\sigma^\prime$
        - poiché in questa osservazione non è stato fatto uso dell'ipotesi per cui $i_p$ fosse stato scelto all'interno del primo ciclo, il ragionamento vale analogamente per ogni altro elemento in ogni altro ciclo
    - allora, $\alpha$ è proprio scelto tale che $\sigma^\prime = \alpha \sigma \alpha ^{-1}$, che per definizione implica che $\sigma \sim \sigma'$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in S_n \mid \sigma := \gamma_1 \ldots \gamma_k$
- **Th**
    - $\textrm{sgn}(\sigma)=(-1)^{n - k}$
- **Dim**
  - $\sigma = (i_1 \ldots i_{d_1}) \ldots (j_1 \ldots j_{d_k})$
  - $\forall \sigma \in S_n \quad \exists \sigma' \in S_n \mid \sigma^\prime := (1 \ldots d_1)(d_1 + 1 \ldots d_1 + d_2) \ldots (n -d_k + 1 \ldots n)$
      - dunque $\sigma^\prime$ è composta da cicli lunghi esattamente come i cicli di $\sigma$, ma ha i numeri da $1$ a $n$ in sequenza nei cicli
      - $\sigma^{\prime}=\left(\begin{array}{cccccccc}1 & 2 & \cdots & d_{1} & d_{1}+1 & \cdots & d_{1}+d_{2} & \cdots \\ 2 & 3 & \cdots & 1 & d_{1}+2 & \cdots & d_{1}+1 & \cdots \end{array}\right)$
  - per portare $1$ nella prima colonna, devo applicare $d_1 - 1$ trasposizioni adiacenti
    - _esempio_
      - in $(2 \ 3 \ 4\ 5\ 6\ 1)$ devo applicare $5$ trasposizioni adiacenti per ottenere $(1\ 2\ 3\ 4\ 5)$
  - per portare $d_1 + 1$ nella colonna corretta, devo applicare $d_2 - 1$ trasposizioni adiacenti, e vale il ragionamento analogo per ogni altro ciclo
  - allora, per ottenere $\textrm{id}$ a partire da $\sigma^\prime$, devo applicare $(d_1 -1) + (d_2 - 1) + \ldots + (d_k - 1)$ trasposizioni adiacenti, ovvero $d_1 + \ldots + d_k - 1 \cdot k = n - k$
    - $d_1 + \ldots + d_k$ è il numero di colonne di $\sigma^\prime \in S_n$, dunque è pari a $n$
    - $k$ è il numero di cicli, quindi nell'equazione $-1$ appare esattamente $k$ volte
  - di conseguenza, $\textrm{id} = \sigma^\prime \tau_1 \ldots \tau_{n -k} \iff \sigma^\prime = \tau_{n - k} \ldots \tau_1 \iff \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\tau_{n-k} \ldots \tau_1)$, e dunque rimuovendo ogni trasposizione adiacente si ottiene che $\textrm{sgn}(\sigma^\prime) = (-1)^{n -k}$ per osservazione in dimostrazione precedente
  - poiché $\sigma$ e $\sigma^\prime$ hanno lo stesso numero di cicli, e i cicli hanno la stessa lunghezza, allora per dimostrazione precedente $\sigma \sim \sigma^\prime \implies \textrm{sgn}(\sigma^\prime)=\textrm{sgn}(\sigma)$ per dimostrazione precedente, e dunque $\textrm{sgn}(\sigma') = \textrm{sgn}(\sigma)=(-1)^{n - k}$
