# implementazione

## concetto base
una operazione ad un array viene applicata per ogni elemento esempio
array = 1, 2, 3, 4 e gli viene applicato + diventerà 1+2+3+4 = 10
**per fare le altre cose si manipola lo stack**

## manipolazione
1. operazione a tutto l'array base

2. operazione numero a tutto l'array es (1, 2, 3) + 1 -> (1+1, 2+1, 3+1) viene fatto creando tanti array quanti n con il paio di numeri es (1, 1) (2, 1) (3, 1) , per tutti questi si applica **il concetto base** -> 1+1, 2+1, 3+1, si avrà uno stack così stack = (2, 3, 4) e si condensa in uno array stack = ((2, 3, 4))

3. operazione array array es (1, 2, 3) (3, 2, 1) + -> si fanno coppie di array come prima ma con il rispettivo ne altro array -> (1, 3) (2, 2) (3, 1) -> il proceso sopra -> stack = ((4, 4, 4))


## comandi specifici repl

* **!quit** per terminare il programma
* **!debug** per fare vedere lo stack

## comandi manipolazione stack

* **;** creazione array vuoto in stak
* **,** aggiunge elemento all ultimo array dello stack
* **:** cancella ultimo array dello stack
* **.** cancella ultimo elemento array dello stack

* **:,;;** prende il penultimo array nello stack e l'ultimo *come numero* e per ogni i in array aggiunge alla base dello stack l'array (i, numero)

* **:;:;** prende 'ultimo ed in penultimo array e crea per ogni i, ii una coppia di array (i, ii)...

* **..:** condensa lo stack in un array, prende tutti gli i nello stack e crea un array

## variabili

* **=@** prende l' ultimo array dello stack e lo mette in un dizzionario sotto il nome del token prima es. : 1 . 2 . 3 . var =@ -> dizzionario = { 'var' = (1, 2, 3)

* **@=** mette nello stack l'array nel dizzionario sotto il nome del token prima

## *circa* funzioni (più macro)

* **=f{...}** per declararla, prende il token prima come nome e mette l'array di comandi in un dictionary sotto quel nome es. f1 =f{ 1 . f}

* **f=** per usarla, prende l'array di comandi sotto quel nome dal dictionary e gli aggiunge alla lista dei comandi da esguire es. f1 f=