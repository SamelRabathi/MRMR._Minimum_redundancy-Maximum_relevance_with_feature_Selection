#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:15:32 2020

@author: samelrabathi
"""

class MRMR:
    
    import MRMR_korigiert as MRMR
    def __init__(self,
                 feature_set,
                 classifikation,
                 method = "pearson"
                 ):
                 self.SetX = feature_set
                 self.SetY = classifikation
                 self.method = method
#=============================================================================
    "feature_set" # Bei dieser Menge wirddavon ausgegangen, dass es mit
                  # Features gefüllt sein wird
                  # Menge: aus m Feature(Spalten) mit n Vorkommnissen(Zeilen)

    "classifikation" # Hierbei handeln es sich um Endpunkte mit denen nur die
                     # Relevanz bestimmt wird
                     # Menge:
                     # Eine Reihe(Spalte) Endpunkten mit n Annahmen(Zeilen)

    "method" # Die Art der Korrelationenbestimmung
#=============================================================================


    def test(self):
        
        result = MRMR.calculation()
        return result


    def calculation(self):
        import numpy as np
        import pandas as pd
        from termcolor import colored
    
        Relevance = MRMR.max_rel_calc(self.SetX,
                                      self.SetY,
                                      self.method
                                      )
        
        Redundancy = MRMR.min_red_calc(self.SetX,
                                       self.method
                                       )
        
        usefull_features = pd.DataFrame( columns = ['id',
                                                    'score',
                                                    'featurename'] )
        
        mrmr_featid = [] # container for feature id's
        mrmr_scores = [] # container for scores according to `mrmr_features`
        mrmr_featnames = [] # container for names 
        feat_names = ["Aspirin","X2","Bluthochdruck","DrugX","Schuhgroesse"]
        feat_id = [1,2,3,4,5] 
        
        print("Relevance: \n{:}\n\n".format(Relevance))
        print("Redundancy: \n{:}\n\n".format(Redundancy))
        idmax = np.argmax(Relevance)
        print("idmax: \n{:}".format(idmax))
        
        score_tmp = Relevance.pop(idmax) # Übernahme des Scores
        id_tmp = feat_id.pop(idmax) # Übernahme der id
        names_tmp = feat_names.pop(idmax) # Übernahme des Names
        
        mrmr_scores.append(score_tmp) # Einschreiben des Scores
        mrmr_featid.append(id_tmp) # Einschreiben der id
        mrmr_featnames.append(names_tmp) # Einschreiben des Names
        
        usefull_features[0] = ['id','score','featurename']
        
        print( colored("\n\nBeginn der while Schleife\n\n", "green") )
        while (score_tmp > 0):
            list_of_redundanz = []
            idmax = np.argmax(Relevance)
            sl = 0 # Läufer für dasAbarebiten der Spalten einer Zeile
            while (sl < len(id_tmp)):
                list_of_redundanz.append(Redundancy[idmax][ mrmr_featid[sl] ])
                sl = sl + 1
                 # Vielleicht etwas unsschön gemacht, um eine Liste an Werten
                 # zu erstellen, welches über die Redundanz aussagt, eine
                 # andere Art der gezielten Suche müsste ich mir noch finden
                   
            redund_tmp = np.argmax(list_of_redundanz)
            
            idmax_tmp = Relevance.pop(idmax) - redund_tmp
            mrmr_scores.append(idmax_tmp)
            
            score_tmp = feat_id.pop(idmax)
            mrmr_featid.append(score_tmp)
            
            names_tmp = feat_names.pop(idmax)
            mrmr_featnames.append(names_tmp)
            
        
        return usefull_features
#=============================================================================
    "usefull_features" # Gibt Score, Feature-Name und die Position aus der
                       # ursprünglichen Menge von denen bei dem der Score
                       # positiv geblieben ist
#=============================================================================


    def max_rel_calc(feature_set,
                     classification,
                     method
                     ):  # Maximum Relevance Calculation
#=============================================================================
        "feature_set" # Zu analysierende Menge an Feature wurde in Gesprächen
                      # öffters auch als Menge X beschireben
        
        "classification" # Hierbei handelt es sich um Endpunkte, was für die
                         # Korrelationen verrechnet wird, um folglich
                         # einerseits eine Vergleichbarkeit zu haben und
                         # anderseits die Wichtigkeit der Features auszusagen
        
        "method" # Auf welche Methode die Berrechnung durchgeführt werden soll
#=============================================================================
        import pandas as pd
        from termcolor import colored
        print("Start der Relevanzbestimmung")
        "1. Abschnitt:"
        relevance_of_feature = pd.DataFrame( columns = ['Koeffizienten'] )
        "1. Abschnitt"
        # Der 1. Abschnitt ist für das Errichten von notwendigen Datensätzen
        
        "2. Abschnitt:"
        print("\nDer Inhalt vom feature_set:\n{:}".format(feature_set) )
        print("\nDie Anzahl an feature: {:}".format( len(feature_set) ) )
        print( colored("\n\nBeginn der while Schleife\n\n", "green") )
            # Soll den START der Schleife markieren
        "2. Abschnitt"
            # Abschnitt 2 soll zur Kontrolle Abschnitt 1 ausgeben
            # wird nicht mehr nötig sein (Zeile 81 bis 90 fallen dann weg)
        
        sl = 0 # Schleifen-läufer
        while (sl < len(feature_set)):
            # Die while-Schleife ist für die Berrechnung jeder Koorelation aus
            # der Menge von Feature zu den Endpunkten
            input_correl = MRMR.correl(feature_set[sl],
                                       classification,
                                       method
                                       ) # Bestimmung einer Korrelationen
            
            relevance_of_feature = relevance_of_feature.append(dict(zip(
                                        relevance_of_feature.columns,
                                        input_correl ) ),
                                        ignore_index=True)
                # Aufgrund der Tatsache, dass 
            """ Diese while-Schleife soll die Berechnung und das Einfügen der
                neuen Korrelationen ausführen"""
            
            sl = sl + 1
        
        print("Ende der Relevanzbestimmung")
        print("\n{:}\n".format(relevance_of_feature))
        return relevance_of_feature
#=============================================================================
    "relevance_of_feature_subset" # Die Rückgabe ist ein DataFrame, welches
                                  # mit der berechneten Korrelation für die
                                  # Relevanz mit der Reihenfolge der
                                  # übergebenen Features gefüllt wurde
#=============================================================================


    def min_red_calc(feature_set,
                     method
                      ): # Minimum Redundance Calculation
#=============================================================================
        "feature_set" # Die Meenge der Features wird auf Redundanz geprüft,
                      # weshalb auch zweite Menge benötigt wird
        
        "method" # Auf welche Methode die Berrechnung durchgeführt werden soll
#=============================================================================
        import numpy as np
        
        create_matrix = np.empty( [len(feature_set), len(feature_set)] )
        print(create_matrix)
        sl = 0 # Betrachtung der einzelnen Spalten
        while (sl < len(feature_set)):
            zl = 0 # Betrachtung der einzelnen Zeilen
            while (zl < len(feature_set)):
                input_correl = MRMR.correl(feature_set[zl],
                                           feature_set[sl],
                                           method
                                           )
                create_matrix[zl][sl] = input_correl[0]
                zl = zl +1
            sl = sl + 1
        
        print("\n\n{:} \n\n Ende der Redundanz".format(create_matrix))
        return create_matrix
#=============================================================================
    "create_matrix" # Das create_matrix wird soll die Redundanz angeben,
                    # aufgrund dessen, dass wir mit einer Korrelation arbeiten,
                    # hat entweder der ober oder untere Abschnitt von der
                    # Diagonale aus keinen Nutzen, weil es im anderen genau so
                    # enthalten  ein  muss
#=============================================================================


    def correl(setX, setY, method):
#=============================================================================
        "setX" # Die Bezeichnung dieser Mengen gilt nur zur Orientierung
               # in der in dieser def stattfindenden Berechnungen

        "setY" # Hat die selbe Funktion wie setX für die zweite, mit zu
               # vergleichende Menge

        "method" # Der erhalt der Methode ist essentiell, da sonst keine
                 # Berechnung ausgeführt werden würde
        
        """Correlationsbestimmung der zwei erhaltenen Mengen, hierbei muss
           die Länge der Menge berücksichtigt werden, da Ungleichheiten der
           Länge zweier Mengen nicht über Korrelationenbestimmung berechnet
           werden kann"""
#=============================================================================
        import numpy as np
        
        correlation = 0
        if (method == "pearson"):
            
            import scipy.stats as scipy
            correlation = scipy.pearsonr(setX, setY)
        
        elif (method == "spearman"):
            
            import scipy.stats as scipy
            correlation = scipy.spearmanr(setX, setY)
        
        elif (method == "kendall"):
            
            import scipy.stats as scipy
            correlation = scipy.kendalltau(setX, setY)
            
        elif(method == "concordance index"):
            
            # Code kommt noch
            print("\nDie Berechnung über den Concordance Index ist noch " +
                  "nicht fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        elif(method == "carmer"):
            
            # Code kommt noch
            print("\nDie Berechnung über den Carmer's V ist noch nicht " +
                  "fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        return np.abs(correlation)
#=============================================================================
    "correlation" # Die Rückgabe ist der Bertag vom berechneten Korrelationen
                  # zwischen zwei eingeben Mengen
#=============================================================================
