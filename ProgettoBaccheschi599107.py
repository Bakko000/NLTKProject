## -*-coding: utf-8-*- ##


# Importo le librerie

import nltk
import sys
from nltk import pos_tag






#Funzione di Analisi (tokenizzazione, pos) #
def Analisys(frasi):
    tokensTOT = [] # Vettore dei tokens
    tokensPOSTOT = [] # Vettore dei POS

    for frase in frasi:       # Scorre tutte le frasi
        tokens = nltk.word_tokenize(frase) # Tokenizza ogni frase
        tokensTOT += tokens  # Accumula ogni tokens uno dopo l'altro in tokensTOT
        tokensPOS= pos_tag(tokens) # POS di ogni token
        tokensPOSTOT = tokensPOSTOT + tokensPOS # Accumula ogni token pos nei pos totali 
        lunghezzaTOT = len(tokensTOT)  # Lunghezza del Corpus |C|
        lunghezzaPOSTOT = len(tokensPOSTOT) # Totale dei pos del testo

    return tokensTOT, lunghezzaTOT, tokensPOSTOT, lunghezzaPOSTOT








#Funzione per la lunghezza media delle frasi#
def Stats_Frasi(frasi, NumeroFrasi):
    LunghezzaTotale = 0  # Accumulatore di lunghezze 


    for frase in frasi:  # Scorre ogni frase e..
        LunghezzaFrase = len(frase)  # ..ne calcola la lunghezza per ognuna (INCLUSA PUNTEGGIATURA)
        LunghezzaTotale += LunghezzaFrase  # Accumula tutte le lunghezze

    LunghezzaMedia = LunghezzaTotale/NumeroFrasi  # Calcola media

    return LunghezzaMedia







#Funzione per la lunghezza media delle parole in caratteri#
def Stats_Parole(Tokens, Corpus):
    LunghezzaParoleTOT = 0  # Accumulatore

    for tok in Tokens:  # Scorre tutti i tokens e..
        LunghezzaTok = len(tok)  # ..ne calcola la lunghezza per ognuno (INCLUSA PUNTEGGIATURA)
        LunghezzaParoleTOT += LunghezzaTok # Accumula tutte le lunghezze

    LunghezzaMediaParole = LunghezzaParoleTOT/Corpus # Calcola Media

    return LunghezzaMediaParole








#Funzione per la grandezza del vocabolario e TTR nei primi 5000 tokens#
def Stats_Vocabolario(Tokens):
    vocabolario = list(set(Tokens)) # Vocabolario
    tokens5000 = Tokens[0:5000] # Primi 5000 tokens
    vocabolario5000 = list(set(tokens5000)) # Vocabolario dei primi 5000 tokens
    TTR5000 = len(vocabolario5000)/len(tokens5000)  # TTR per i primi 5000 tokens, |V| / |C|

    return vocabolario, vocabolario5000, TTR5000








# Funzione per tracciare l'aumento delle classi di frequenza V1, V5, V10 all'aumentare del corpus#
def Stats_Freq(Tokens):
    for i in range(0, len(Tokens), 500):  # Scorre tutti i tokens con i incrementata di 500 in 500
        listaTokens500 = Tokens[0:i+500]  # Nuovo array contenente tutti i token trovati negli intervalli
        vocabolario500 = list(set(listaTokens500)) # Vocabolario di 500 in 500

        hapax500 = []
        for tok in vocabolario500:  # Scorre il vocabolario di 500 in 500
            conta=listaTokens500.count(tok) # Se appare una sola volta un token in un intervallo...
            if conta == 1:
               hapax500.append(tok) # Inseriscilo nel vettore di tutti gli hapax V1 al momento dell'intervallo

        V5di500 = []
        V10di500 = []

        for tok in listaTokens500:  # Scorre la lista dei token negli intervalli in 500 in 500
            conteggio = Tokens.count(tok)   # Conta l'occorenza del token in tutta la lista dei token   
            if conteggio == 5: # Freq 5
                V5di500.append(tok)
            if conteggio == 10: # Freq 10
               V10di500.append(tok)


        print()
        print()
        print("Intervallo: ", i, "-", len(listaTokens500))
        print("Dimensione Corpus: ", len(listaTokens500))
        print("Classe totale degli hapax: ", len(hapax500))
        print("Classe freq V5: ", len(V5di500))
        print("Classe freq V10: ", len(V10di500))

    return hapax500, V5di500, V10di500




listaPunt = [",", ";", ":", "!", "?", "."]    # Vettore contenente le punteggiatura








# Funzione che calcola la media dei sostantivi e verbi per frase 
def Stats_Pos(TestoPOS, totfrasi): 
    TOTPosSost = 0   # Contatori a 0
    TOTPosVerb = 0
    for pos in TestoPOS:   # Per ogni pos...
        if(pos[1] == "NN" or pos[1]=="NNS" or pos[1]=="NNP" or pos[1]=="NNPS"):   # se sono sostantivi..
            TOTPosSost += 1  # ... incrementa il contatore dei sostantivi
        if(pos[1]=="VB" or pos[1]=="VBD" or pos[1]=="VBG" or pos[1]=="VBN" or pos[1]=="VBP" or pos[1]=="VBZ"): # se sono verbi..
            TOTPosVerb += 1   #...incrementa il contatore dei verbi

    MediaS = TOTPosSost / totfrasi  # Media rispetto il totale delle frasi
    MediaV = TOTPosVerb / totfrasi

    return MediaS, MediaV










# Funzione che calcola la densità lessicale #

def Dens_Lessicale(TestoPOS, tokens):
    TOTPunteggiatura = 0   # Contatore dei segni di punteggiatura
    TOTSost = []   # Vettore dei sostantivi
    TOTVerb = []   # Vettore dei verbi
    TOTAdv = []    # Vettore dei avverbi
    TOTAdj = []    # Vettore dei aggettivi

    for tok in tokens:     # Scorre tutti i tokens
        if(tok in listaPunt):    # Se il token è un segno di punteggiatura
            TOTPunteggiatura += 1    # Incrementa il contatore


    for pos in TestoPOS:    # Scorre tutti i pos

        if(pos[1] not in listaPunt):   # Se il pos[1] cioè il tag non è una punteggiatura...

            if(pos[1] == "NN" or pos[1]=="NNS" or pos[1]=="NNP" or pos[1]=="NNPS"):  # Se sono sostantivi..
              TOTSost.append(pos[1])   # Appendili al vettore dei sostantivi
            elif(pos[1]=="VB" or pos[1]=="VBD" or pos[1]=="VBG" or pos[1]=="VBN" or pos[1]=="VBP" or pos[1]=="VBZ"): # Se sono verbi..
              TOTVerb.append(pos[1])
            elif(pos[1]=="RB" or pos[1]=="RBR" or pos[1] =="RBS"):  # Se sono avverbi..
              TOTAdv.append(pos[1])
            elif(pos[1]=="JJ" or pos[1]=="JJR" or pos[1]=="JJS"):  # Se sono aggettivi
              TOTAdj.append(pos[1])

    TOTLessico = len(TOTSost) + len(TOTVerb) + len(TOTAdv) + len(TOTAdj)  # Calcolo le lunghezze di ogni vettore
    TOTParole = len(tokens)

    Dens = TOTLessico / (TOTParole - TOTPunteggiatura)   # Calcolo la densità lessicale

    return Dens













#Funzione generale#

def main(file1, file2):
    fileInput1 = open(file1, mode="r", encoding="utf-8")  ## Apro i file
    fileInput2 = open(file2, mode="r", encoding="utf-8")

    raw1 = fileInput1.read() # Leggo i file e associo
    raw2 = fileInput2.read()

    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') # Carico il documento di tokenizzazione nella lingua scelta
    frasi1 = sent_tokenizer.tokenize(raw1)  # Divido in frasi
    frasi2 = sent_tokenizer.tokenize(raw2)

    lunFrasi1 = len(frasi1)  # len delle frasi, ottengo il numero delle frasi
    lunFrasi2 = len(frasi2)




    print("------------ STATISTICHE TESTI (PUNTEGGIATURA INCLUSA) ---------")
    print()




############################################### FILE1 


   
    TokensTOT, lunghezza, tokensPOS, lunghezzaPOS = Analisys(frasi1) # Tokenizzo e ottengo i pos dal testo
    Media = Stats_Frasi(frasi1, lunFrasi1)  # Lunghezza media delle frasi
    MediaCaratteri = Stats_Parole(TokensTOT, lunghezza) # Lunghezza media delle parole
    Vocabolario, Vocabolarioin5000, TTRin5000 = Stats_Vocabolario(TokensTOT) # Lunghezza vocabolario e ttr in primi 5000 token
    Msost, Mverb = Stats_Pos(tokensPOS, lunFrasi1) # Media sostantivi e verbi per frase
    DensitaLessicale = Dens_Lessicale(tokensPOS, TokensTOT) # Densità lessicale data da sost+verb+adv+agg /  corpus-punteggiatura
    print()
    print()
    print()
    print()
    print("****************************************** File: ", file1, "***************************************************")
    print()
    print("\tTokens Totali: ", lunghezza, "\tFrasi Totali: ", lunFrasi1,  "\tLunghezza Media Frasi:", Media, "\tLunghezza Media Parole: ", MediaCaratteri)
    print()
    print("\tVocabolario primi 5000 tokens: ", len(Vocabolarioin5000), "\tType Token Ratio primi 5000 tokens: ", TTRin5000, "\tDensità Lessicale(senza punt): ", DensitaLessicale)
    print()
    print( "\tMedia Sostantivi per frase: ", Msost, "\t\tMedia Verbi per frase: ", Mverb)
    print()
    print()
    print()
    print()
    print()
    print()
    print("--- Statistiche del testo negli intervalli di 500 in 500")
    V1, V5, V10 = Stats_Freq(TokensTOT)   # Aumentare delle classi di frequenza all'aumentare del corpus







############################################### FILE2




    TokensTOT2, lunghezza2, tokensPOS_2, lunghezzaPOS_2 = Analisys(frasi2) # Tokenizzo e ottengo i pos dal testo
    Media_2 = Stats_Frasi(frasi2, lunFrasi2)  # Lunghezza media delle frasi
    MediaCaratteri_2 = Stats_Parole(TokensTOT2, lunghezza2) # Lunghezza media delle parole
    Vocabolario_2, Vocabolarioin5000_2, TTRin5000_2 = Stats_Vocabolario(TokensTOT2) # Lunghezza vocabolario e ttr in primi 5000 token
    Msost_2, Mverb_2 = Stats_Pos(tokensPOS_2, lunFrasi2) # Media sostantivi e verbi per frase
    DensitaLessicale_2 = Dens_Lessicale(tokensPOS_2, TokensTOT2) # Densità lessicale data da sost+verb+adv+agg /  corpus-punteggiatura
    print()
    print()
    print()
    print()
    print()
    print("****************************************** File: ", file2, "***************************************************")
    print()
    print("\tTokens Totali: ", lunghezza2, "\tFrasi Totali: ", lunFrasi2,  "\tLunghezza Media Frasi:", Media_2, "\tLunghezza Media Parole: ", MediaCaratteri_2)
    print()
    print("\tVocabolario primi 5000 tokens: ", len(Vocabolarioin5000_2), "\tType Token Ratio primi 5000 tokens: ", TTRin5000_2, "\tDensità Lessicale(senza punt): ", DensitaLessicale_2)
    print()
    print( "\tMedia Sostantivi per frase: ", Msost_2, "\t\tMedia Verbi per frase: ", Mverb_2)
    print()
    print()
    print()
    print()
    print()
    print()
    print("--- Statistiche del testo negli intervalli di 500 in 500")
    V1_2, V5_2, V10_2 = Stats_Freq(TokensTOT2)  # Aumentare delle classi di frequenza all'aumentare del corpus




    
    print()
    print()
    print()






    # ------------ Eseguo confronti --------- #
    
    print()
    print("------------ CONFRONTI DEI TESTI  ------------")
    print()




    # SUI TOKENS #


    # Lunghezza dei Corpora
    if lunghezza > lunghezza2:
        print("\nIl file", file1, " è più lungo rispetto al file ", file2, "\n")
    elif lunghezza2 > lunghezza:
        print("\nIl file ", file2," è più lungo rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno lo stesso numero di tokens\n")


    # Lunghezza media delle parole in caratteri
    if MediaCaratteri > MediaCaratteri_2:
        print("\nIl file", file1, " ha parole mediamente più lunghe rispetto al file ", file2, "\n")
    elif MediaCaratteri_2 > MediaCaratteri:
        print("\nIl file ", file2," ha parole mediamente più lunghe rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno parole mediamente lunghe in egual misura\n")




    # Sul Vocabolario: vocabolario primi 5000 tokens, type token ratio primi 5000 tokens
    if len(Vocabolarioin5000) > len(Vocabolarioin5000_2):
        print("\nIl file", file1, " ha il vocabolario nei primi 5000 tokens più lungo rispetto al file ", file2, "\n")
    elif len(Vocabolarioin5000_2) > len(Vocabolarioin5000):
        print("\nIl file ", file2," ha il vocabolario nei primi 5000 tokens più lungo rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno lo stesso numero di vocaboli nei primi 5000 tokens\n")



    # Totale delle classi di frequenza V1, V5, V10

    #V1 hapax
    if len(V1) > len(V1_2):
        print("\nIl file", file1, " ha più hapax del file ", file2, "\n")
    elif len(V1_2) > len(V1):
        print("\nIl file ", file2," ha più hapax del file ", file1, "\n")
    else:
        print("\nI due file hanno lo stesso numero di hapax\n")

    #V5
    if len(V5) > len(V5_2):
        print("\nIl file", file1, " ha più parole di frequenza 5 rispetto al file ", file2, "\n")
    elif len(V5_2) > len(V5):
        print("\nIl file ", file2," ha più parole di frequenza 5 rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno lo stesso numero parole di frequenza 5\n")
     
    #V10
    if len(V10) > len(V10_2):
       print("\nIl file", file1, " ha più parole di frequenza 10 rispetto al file ", file2, "\n")
    elif len(V10_2) > len(V10):
        print("\nIl file ", file2," ha più parole di frequenza 10 rispetto al file ", file1, "\n")
    else:
       print("\nI due file hanno lo stesso numero parole di frequenza 10\n") 



    # Sui tokens pos: media sostantivi e verbi per frase

    # Sostantivi
    if Msost > Msost_2:
        print("\nIl file", file1, " ha una media di sostantivi per frase maggiore rispetto al file ", file2, "\n")
    elif Msost_2 > Msost:
        print("\nIl file", file2, " ha una media di sostantivi per frase maggiore rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno la stessa media di sostantivi per frase\n")


    # Verbi
    if Mverb > Mverb_2:
        print("\nIl file", file1, " ha una media di verbi per frase maggiore rispetto al file ", file2, "\n")
    elif Mverb_2 > Mverb:
        print("\nIl file", file2, " ha una media di verbi per frase maggiore rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno la stessa media di verbi per frase\n")




    # Densità lessicale calcolata dai pos verbi, aggettivi, avverbi, sostantivi

    if DensitaLessicale > DensitaLessicale_2:
        print("\nIl file", file1, " ha una densità lessicale maggiore rispetto al file ", file2, "\n")
    elif DensitaLessicale_2 > DensitaLessicale:
        print("\nIl file", file2, " ha una densità lessicale maggiore rispetto al file ", file1, "\n")
    else:
        print("\nI due file hanno la stessa densità lessicale\n")





    



    # SULLE FRASI #

    # Numero frasi
    if lunFrasi1>lunFrasi2:
        print("\nIl file ", file1, "ha più frasi rispetto il file ", file2, "\n")
    elif lunFrasi2>lunFrasi1:
        print("\nIl file ", file2," ha più frasi rispetto il file ", file1, "\n")
    else:
        print("\nI due file hanno la stessa lunghezza in frasi.\n")


    #Lunghezza media delle frasi
    if Media>Media_2:
        print("\nIl file ", file1, "ha frasi mediamente più lunghe rispetto il file ", file2, "\n")
    elif Media_2>Media:
        print("\nIl file ", file2," ha frasi mediamente più lunghe rispetto il file ", file1, "\n")
    else:
        print("\nI due file hanno la stessa lunghezza media delle frasi.\n")







main(sys.argv[1], sys.argv[2]) # Mi servono due argomenti, due file
