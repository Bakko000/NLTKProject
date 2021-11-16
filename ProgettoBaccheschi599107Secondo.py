## -*-coding: utf-8-*- ##

import nltk
import sys
import math
from nltk import pos_tag
from nltk import bigrams







listaPunt = ["?","!",",",";","'","\"", ".", ":", "''", "``"]  # Listato dei segni di punteggiatura








# FUnzione di analisi del testo, tokenizza e ottiene i POS #
def Analisys(frasi):
    tokensTOT = []
    tokensPOSTOT = []

    for frase in frasi:       # Scorre tutte le frasi
        tokens = nltk.word_tokenize(frase) # Tokenizza ogni frase
        tokensTOT += tokens  # Accumula ogni tokens uno dopo l'altro in tokensTOT
        tokensPOS= pos_tag(tokens)
        tokensPOSTOT = tokensPOSTOT + tokensPOS
        lunghezzaTOT = len(tokensTOT)  # Lunghezza del Corpus |C|


    return lunghezzaTOT, tokensTOT, tokensPOSTOT








# Funzione di estrazione dei soli POS#
def EstraiPOS(POSTotali):
    listaPos = []    # Lista inizialmente vuota

    for pos in POSTotali:   # Per ogni POS nei bigrammi POS...

        listaPos.append(pos[1])   # Arrichisci di soli POS la listaPos

    return listaPos






# Funzione di esclusione punteggiatura dai bigrammi #
def EstraiBigrammi(Bigrammi):
    bigrammi = []    # Lista inizialmente vuota

    for bigramma in Bigrammi:   # Per ogni bigramma ...
        if(bigramma[0] not in listaPunt and bigramma[1] not in listaPunt):
           bigrammi.append(bigramma)   # Arrichisci di soli bigrammi senza punteggiatura

    return bigrammi







# Funzione di ordinamento per frequenza dei POS#
def POSInOrdineDiFrequenza(lista):
    POSSDistribuiti = nltk.FreqDist(lista)  # Distribuzione di frequenza ai POS
    POSOrdinati = POSSDistribuiti.most_common(10)  # Si conteggino e si ordini solo i primi 10

     
    print()
    print("####################################### La lista ORDINATA per frequenza delle prime 10 Part-of-Speech dell'intero testo (POS, senza punteggiatura):\n")

    for elem in POSOrdinati:  # Per ogni elemento trovato nei pos ordinati per frequenza
        if(elem[0] not in listaPunt):  # Escludiamo la punteggiatura
           pos = elem[0]  # Il pos è il primo elemento del bigramma
           freq = elem[1] # La frequenza ne è il secondo elemento
           print()
           print("\tPOS:", pos, "\tFrequenza:", freq) # Stampa a video

    print()
    print()








# Funzione che analizza i primi 20 sostantivi #
def Analisi20Sostantivi(tokensPOSTOT):
    DistrFreq=nltk.FreqDist(tokensPOSTOT) # Calcola la frequenza di ogni token
    Primi20Sost = DistrFreq.most_common()
    listaSostantivi=[]

    for elem in Primi20Sost:

        if(elem[0][1] == "NN" or elem[0][1]=="NNS" or elem[0][1]=="NNP" or elem[0][1]=="NNPS"):  # Se sono sostantivi..
           token = elem[0][0]
           POS = elem[0][1]
           freq = elem[1]
           listaSostantivi.append(elem) # "Appende" cioè aggiunge l'elemento con il token, il pos e la frequenza nel nuovo vettore


    DistrFreq=nltk.FreqDist(listaSostantivi)   # Esegue la frequenza di ogni solo sostantivo
    listaSostantivi = DistrFreq.most_common(20) # Ordina solamente i primi 20

    for elem in listaSostantivi:
      
        print()
        print("\tToken: ", elem[0][0][0], "\tPOS: ", elem[0][0][1], "\tFrequenza: ", elem[0][1]) # Stampa a video il token, il pos del sostantivo e la frequenza
        print()










# Funzione che analizza i primi 20 verbi #
def Analisi20Verbi(tokensPOSTOT):
    DistrFreq=nltk.FreqDist(tokensPOSTOT)
    Primi20Verbi = DistrFreq.most_common()
    listaVerbi=[]

    for elem in Primi20Verbi:

        if(elem[0][1]=="VB" or elem[0][1]=="VBD" or elem[0][1]=="VBG" or elem[0][1]=="VBN" or elem[0][1]=="VBP" or elem[0][1]=="VBZ"):  # Se sono verbi..
           token = elem[0][0]
           POS = elem[0][1]
           freq = elem[1]
           listaVerbi.append(elem) # Aggiunge l'elemento alla nuova lista

    

    DistrFreq=nltk.FreqDist(listaVerbi) # Esegue la frequenza di ogni solo verbo
    listaVerbi = DistrFreq.most_common(20) # Ordina solamente i primi 20

    for elem in listaVerbi:
      
        print()
        print("\tToken: ", elem[0][0][0], "\tPOS: ", elem[0][0][1], "\tFrequenza: ", elem[0][1]) # Stampa a video il token, il pos del verbo e la frequenza
        print()
    









listato1 = ["NN", "NNS", "NNP", "NNPS", "VBD", "VBG", "VBN", "VBP", "VBZ"] # Verbi e sostantivi
listato2 = ["NN", "NNS", "NNP", "NNPS", "JJ", "JJR", "JJS"] # Aggettivi e sostantivi




# Funzione che analizza i bigrammi pos e li ordina secondo l'esigenze#
def Stats_BigramsPOS(Bigrammi, ordine):

    BigrammiDistribuiti = nltk.FreqDist(Bigrammi)  # Distribuisce la frequenza per ogni bigramma
    BigrammiOrdinati = BigrammiDistribuiti.most_common() # Ordina per frequenza i bigrammi



##################### Sostantivi - Verbi ##########################################


    if ordine=="Sostantivi-V":   # Se l'ordinamento è Sostantivo-Verbo...

       print()
       print("############################# Lista bigrammi in ordine di frequenza formati da Sostantivo seguito da Verbo:")
       print()

       listaSostVerb = []


       for bigramma in BigrammiOrdinati:

           if(bigramma[0][-1][-1] in listato1 and bigramma[0][0][1] in listato1):  # Se il primo elemento e il secondo elemento del bigramma sono pos ammessi

              if(bigramma[0][0][1] == "NN" or bigramma[0][0][1]=="NNS" or bigramma[0][0][1]=="NNP" or bigramma[0][0][1]=="NNPS"): # Se il primo è sostantivo e se...

                 if(bigramma[0][-1][-1]=="VBD" or bigramma[0][-1][-1]=="VBG" or bigramma[0][-1][-1]=="VBN" or bigramma[0][-1][-1]=="VBP" or bigramma[0][-1][-1]=="VBZ"): #...il secondo è un verbo
                    listaSostVerb.append(bigramma) # Aggiungi l'intero bigramma alla lista 



       for bigramma in listaSostVerb[0:20]:  # Per i prmi 20 bigrammi formati da sostantivo-verbo
        
           print()
           print("\tBigramma: ", bigramma[0][0][0], "-", bigramma[0][1][0], "", "\tFrequenza: ", bigramma[1]) # Stampa a video
           print()




###################### Aggettivi - Sostantivi ##################################################



    if ordine=="Aggettivi-S": # Se l'ordinamento è Aggettivo - Sostantivo..
        
       listaAggSost = []
       
       print()
       print("############################# Lista bigrammi in ordine di frequenza formati da Aggettivo seguito da Sostantivo:")
       print()

       for bigramma in BigrammiOrdinati:

           if(bigramma[0][-1][-1] in listato2 and bigramma[0][0][1] in listato2): # Vincolo di ammissione a priori

              if(bigramma[0][-1][1] == "NN" or bigramma[0][-1][-1]=="NNS" or bigramma[0][-1][-1]=="NNP" or bigramma[0][-1][-1]=="NNPS"): # Condizione se sono sostantivi e..

                 if(bigramma[0][0][1]=="JJ" or bigramma[0][0][1]=="JJR" or bigramma[0][0][1]=="JJS"): # ...se sono aggettivi
                    listaAggSost.append(bigramma) # Aggiungi



       for bigramma in listaAggSost[0:20]: # Per i primi 20 bigrammi formati da agg-sostantivo
        
           print()
           print("\tBigramma: ", bigramma[0][0][0], "-", bigramma[0][1][0], "", "\tFrequenza: ", bigramma[1]) # Stampa a video
           print()


    print()


    






# Funzione che compie e dimostra statistiche sui bigrammi, probabilità congiunta, condizionata e LMI#
def Stats_Bigrammi(bigrammi, tokens):
    probCongMax = 0.0
    probCondMax = 0.0
    LMIMax = 0.0
    bigrammiDistribuiti = nltk.FreqDist(bigrammi) # Frequennza di bigrammi
    bigrammiOrdinati = bigrammiDistribuiti.most_common(20) # Ordinmaneto primi 20 bigrammi


    for bigramma in bigrammiOrdinati:

            token1 = bigramma[0][0] # Token 1 del bigramma
            token2 = bigramma[0][1]
            
            freqtok1 = tokens.count(token1) # Frequenza del token uno del bigramma
            freqtok2 = tokens.count(token2)

            freqbigramma = bigramma[1] # Frequenza del bigramma come l'ultima parte della tupla

            probCond = freqbigramma*1.0/freqtok1*1.0  # Probabilità condizionata data dalla frequenza del bigramma fratto la frequenza del primo token
            probTok1 = freqtok1*1.0/len(tokens)*1.0 # Probabilità del primo token, token/corpus (frequenza relativa)
            probTok2 = freqtok2*1.0/len(tokens)*1.0 
            probCong = probCond * probTok1 # Probabilità congiunta come probabilita condizionata per la probabilità del primo token

            p = probCong * 1.0 / (probTok1 * probTok2) # Probabilità finale data dalla probabilità congiunta fratta le probabilità dei token
            mi = math.log(p,2) # Mutua informazione 
            LMI = freqbigramma*mi # Local Mutual Information, frequenza del bigramma * MI


            if probCong > probCongMax:  # Calcolo la probabilità congiunta massima confrontando mano a mano
                probCongMax = probCong
                bigrammaMaxx = bigramma

            if(probCond > probCondMax):   # Calcolo la probabilità condizionata massima confrontando mano a mano
                probCondMax = probCond
                bigrammaMaxCond = bigramma

            if LMI > LMIMax:    # Calcolo la LMI massima confrontando mano a mano
                LMIMax = LMI
                bigrammaMaxLMI = bigramma

            print()
            print("Bigramma: ", token1, token2)                  # Stampo tutte le statistiche a video #
            print("Frequenza Bigrammma: ", freqbigramma)
            print("Probabilità condizionata: ", probCond)
            print("Probabilità congiunta: ", probCong)
            print("LMI = ", LMI)
            print()
    print()
    print() 

    # Stampo prob cong max, lmi max e prob cond max
    print(bigrammaMaxx[0][0], bigrammaMaxx[0][1], "è il bigramma con probabilità congiunta massima ", "(",  probCongMax,")")
    print(bigrammaMaxCond[0][0], bigrammaMaxCond[0][1], "è il bigramma con probabilità condizionata massima ", "(",  probCondMax,")")
    print(bigrammaMaxLMI[0][0], bigrammaMaxLMI[0][1], "è il bigramma con forza associativa massima (LMI) ", "(",  LMIMax ,")")

    print()
    print()









# Funzione che tramite un MarkovModel1 e l'add one smoothing, restituisce la frase con probabilità maggiore #
def Markov1(frasi, Corpus, DistribuzioneFrequenzeToken, DistribuzioneFrequenzeBigrammi, vocaboulary):

    FraseMax = ""  # La frase è vuota

    for frase in frasi:
           
        tokensFrase = nltk.word_tokenize(frase)  # Tokenizza le frasi

        if(len(tokensFrase) >= 8 and len(tokensFrase)<=15): # Quando i token per frase sono fra 8 e 15

            bigrammiFrase = list(bigrams(tokensFrase)) # Restituisce bigrammi per la frase
           
            probsmooth = 1 # La probabilità smoothed parte da 1

            for bigramma in bigrammiFrase:

                 token1 = bigramma[0]  # Primo token del bigramma
                 token2 = bigramma[1]
                 FreqBi = (DistribuzioneFrequenzeBigrammi[bigramma])  # Frequenza del bigramma
                 FreqTok1 = DistribuzioneFrequenzeToken[bigramma[0]] # Frequenza del primo token del bigramma
                 FreqTok2 = DistribuzioneFrequenzeToken[bigramma[1]]

                 probsmooth = probsmooth * ((FreqBi+1) / (FreqTok1 + len(vocaboulary))) 

            probsmooth = probsmooth * ((FreqTok1 + 1) / (Corpus + len(vocaboulary))) # Probabilità totale smoothed come la P * (f(tok)+1) / (|C|+|V|)

            maxprob = 0

            if probsmooth > maxprob: # Calcolo mano a mano confrontando le probabilità smoothed maggioir
                maxprob = probsmooth
                FraseMax = frase

    print("\nLa frase con Markov1 con probabilità maggiore (smoothed) è: ", FraseMax)   # Stampo a video
    print("Probabilità: ", maxprob)
    











# Funzione di estrazione dei Name Entity e ordinamento #
def EstraiNE(POS):
    nomi = []
    luoghi = []
    analisi = nltk.ne_chunk(POS) # Ottiene i ne
    for nodo in analisi:
        NE = ''
        if hasattr(nodo, 'label'): # Se esiste
            if nodo.label() == 'PERSON': # Se si tratta di tipo PERSON
                for partNE in nodo.leaves(): # Per ogni foglia
                    NE = NE + '' + partNE[0] # Estrae e combina le NE
                nomi.append(NE) # Le aggiunge nel vettore dei soli nomi propri di persona


            if nodo.label() == 'GPE': # Se si tratta di tipo GPE
                for partNE in nodo.leaves():
                    NE = NE + '' + partNE[0]
                luoghi.append(NE) # Le aggiunge nel vettore dei soli nomi propri di luogo

    DistrNomi = nltk.FreqDist(nomi) # Frequenza per ogni nome proprio di persona
    DistrLuoghi = nltk.FreqDist(luoghi)
    NomiOrdinati = DistrNomi.most_common(15) # Ordinamento dei primi 15 nomi propri di persona
    LuoghiOrdinati = DistrLuoghi.most_common(15)
    
    print()
    print()
    print()
    print("############################## Primi 15 nomi propri di persona ordinati per frequenza: ")
    print()

    for elem in NomiOrdinati:
        print("Il nome proprio di persona: ", elem[0], " ha una frequenza di: ", elem[1])  # Stampa a video nome p di persona e frequenza
    

    print()
    print()
    print()

    
    print()
    print("############################## Primi 15 nomi propri di luogo ordinati per frequenza: ")
    print()

    for elem in LuoghiOrdinati:
        print("Il nome proprio di luogo: ", elem[0], " ha una frequenza di: ", elem[1]) # Stampa a video nome p di luogo e frequenza





















#Funzione Generale#

def main(file1, file2):
    fileInput1 = open(file1, mode="r", encoding="utf-8")  ## Apro i file
    fileInput2 = open(file2, mode="r", encoding="utf-8")

    raw1 = fileInput1.read() # Leggo i file e associo
    raw2 = fileInput2.read()

    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') # Carico il documento di tokenizzazione nella lingua scelta
    frasi1 = sent_tokenizer.tokenize(raw1)  # Divido in frasi
    frasi2 = sent_tokenizer.tokenize(raw2)












    ####################################################          FILE 1       #########################################################

    
    print("####################################################    FILE",file1,  " #########################################################")






    lunghezza, tokenstot, postot = Analisys(frasi1)    # Tokenizza e ottiene i POS


    print()
    vocabolario = list(set(tokenstot)) # Calcolo vocabolario
    Bigrammi = list(bigrams(tokenstot))  # Calcolo bigrammi
    DistFreqTokens = nltk.FreqDist(tokenstot) # Distribuzione di frequenza tokens
    DistFreqBigram = nltk.FreqDist(Bigrammi) # Distribuzione di frequenza bigrammi
    Bigrams = list(bigrams(postot)) # Calcolo bigrammi per i pos
    OrdinaBigrammiPerFrequenza = Stats_BigramsPOS(Bigrams, "Sostantivi-V")  # Ordina determinati bigrammi per frequenza, questo per sostantivi seguiti da verbi
    print()
    print()
    OrdinaBigrammiPerFrequenza = Stats_BigramsPOS(Bigrams, "Aggettivi-S")  # Ordina determinati bigrammi per frequenza, questo per sostantivi seguiti da aggettivi
    print()
  

    print()
    print("########################################## Lista dei primi 20 sostantivi del testo in ordine di frequenza:")
    print()
    Analisi20TokensSost = Analisi20Sostantivi(postot) # Primi 20 sostantivi pos in ordine di frequenze
    print()



    print()
    print()
    print()
    print("######################################## Lista dei primi 20 verbi del testo in ordine di frequenza:")
    print()
    Analisi20TokensVerbi = Analisi20Verbi(postot)  # Primi 20 verbi pos in ordine di frequenze
    print()



    print()
    POSTOT = EstraiPOS(postot)  # Estrae i pos
    print()




    print()
    StampaPOSOrdinati= POSInOrdineDiFrequenza(POSTOT) # Stampa a video i primi 10 pos ordinati per frequenza
    print()


    
    BigrammiSenzaPunt = EstraiBigrammi(Bigrammi)

    print()
    print("######################################## Lista dei primi 20 bigrammi in ordine di frequenza:")
    print()
    StampaBigrammiOrdinati = Stats_Bigrammi(BigrammiSenzaPunt, tokenstot) 
    print()


    
    

    print()
    print()
    print()
    print("#################################### Fra le frasi da 8 a 15 tokens, dimostro con Markov1 e Add-One Smoothing:")
    print()
    StatisticheFrasi = Markov1(frasi1, lunghezza, DistFreqTokens, DistFreqBigram, vocabolario)  # Calcola la frase con probabilità smoothed in mark1 più alta
    


    print()
    OrdinaNomieLuoghi = EstraiNE(postot) # Ordina i primi 15 nomi propri di persona e di luoghi, per frequenza

    
    print()
    print()





    print()
    print()
    print()
    print()
    print()
    print()



















    ####################################################          FILE 2       #########################################################

    print()
    print()
   ####################################################          FILE 1       #########################################################

    
    print("####################################################    FILE",file2,  " #########################################################")






    lunghezza2, tokenstot2, postot2 = Analisys(frasi2)    # Tokenizza e ottiene i POS


    print()
    vocabolario2 = list(set(tokenstot2)) # Calcolo vocabolario
    Bigrammi2 = list(bigrams(tokenstot2))  # Calcolo bigrammi
    DistFreqTokens2 = nltk.FreqDist(tokenstot2) # Distribuzione di frequenza tokens
    DistFreqBigram2 = nltk.FreqDist(Bigrammi2) # Distribuzione di frequenza bigrammi
    Bigrams2 = list(bigrams(postot2)) # Calcolo bigrammi per i pos
    OrdinaBigrammiPerFrequenza = Stats_BigramsPOS(Bigrams2, "Sostantivi-V")  # Ordina determinati bigrammi per frequenza, questo per sostantivi seguiti da verbi
    print()
    print()
    OrdinaBigrammiPerFrequenza = Stats_BigramsPOS(Bigrams2, "Aggettivi-S")  # Ordina determinati bigrammi per frequenza, questo per sostantivi seguiti da aggettivi
    print()
  

    print()
    print("########################################## Lista dei primi 20 sostantivi del testo in ordine di frequenza:")
    print()
    Analisi20TokensSost = Analisi20Sostantivi(postot2) # Primi 20 sostantivi pos in ordine di frequenze
    print()



    print()
    print()
    print()
    print("######################################## Lista dei primi 20 verbi del testo in ordine di frequenza:")
    print()
    Analisi20TokensVerbi = Analisi20Verbi(postot2)  # Primi 20 verbi pos in ordine di frequenze
    print()


  

    print()
    POSTOT2 = EstraiPOS(postot2)  # Estrae i pos
    print()




    print()
    StampaPOSOrdinati= POSInOrdineDiFrequenza(POSTOT2) # Stampa a video i primi 10 pos ordinati per frequenza
    print()


    
    BigrammiSenzaPunt2 = EstraiBigrammi(Bigrammi2)

    print()
    print("######################################## Lista dei primi 20 bigrammi in ordine di frequenza:")
    print()
    StampaBigrammiOrdinati = Stats_Bigrammi(BigrammiSenzaPunt2, tokenstot2)
    print()


    
    

    print()
    print()
    print()
    print("#################################### Fra le frasi da 8 a 15 tokens, dimostro con Markov1 e Add-One Smoothing:")
    print()
    print()
    StatisticheFrasi = Markov1(frasi2, lunghezza2, DistFreqTokens2, DistFreqBigram2, vocabolario2) # Calcola la frase con probabilità smoothed in mark1 più alta

    print()
    OrdinaNomieLuoghi = EstraiNE(postot2) # Ordina i primi 15 nomi propri di persona e di luoghi, per frequenza

    

    



main(sys.argv[1], sys.argv[2]) # Mi servono due argomenti, due file



