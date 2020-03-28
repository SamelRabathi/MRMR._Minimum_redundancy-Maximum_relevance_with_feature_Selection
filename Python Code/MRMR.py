#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:37:31 2020

@author: samelrabathi
"""
import pandas as pd
import numpy as np
from termcolor import colored

class testen:
    
        
    def funktionen_testen(self):
        
        Features = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        Endpunkte = [2,4,8]
        Feature_anzahl = len(Features[1])
        
        testfall = MRMR.calculation(Features,
                                    Endpunkte,
                                    Feature_anzahl,
                                    )
        
        print("Pearson: {:}".format(testfall))
        
            # Vergleich zu pearson und Kendall betrachten
        Features = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        Endpunkte = [2,4,8]
        Feature_anzahl = len(Features[1])
        Methode = "pearson"
        
        testfall = MRMR.calculation(Features,
                                    Endpunkte,
                                    Feature_anzahl,
                                    Methode)
        
        print("spearman: {:}".format(testfall))
        
            # Vergleich zu pearson und Spearman betrachten
        Features = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        Endpunkte = [2,4,8]
        Feature_anzahl = len(Features[1])
        Methode = "kendall"
        
        testfall = MRMR.calculation(Features,
                                    Endpunkte,
                                    Feature_anzahl,
                                    Methode)
        
        print("Kendall: {:}".format(testfall))
        
        return "Ausgaben beachten"


class MRMR:
    
    def __init__(self,
                 feature_set,
                 classifikation,
                 method = "pearson"
                 ):
        self.SetX = feature_set  # Menge: aus m Feature (Spalten)
                                 # mit n Vorkommnissen (Zeilen)
        self.SetY = classifikation  # Menge: eine Reihe (Spalte) Endpunkten
                                    # aus n mal Auftreten (Zeilen)
        self.method = method  # Berechnungsart
    
    
    def calculation(self):
        
        Korrelationstesten = max_rel_cond( self.SetX,
                                           self.SetY,
                                           len(self.SetX),
                                           self.method
                                          )
        
        return 0



class mutual_information:
    
    def __init__(self, feature_set, Y, method):
        self.setX = feature_set  # erste zu korrelierenden Menge
        self.setY = Y  # zweite zu korrelierenden Menge
        
        self.method = method
        """Es wird die Methode gebraucht, um später dementsprechent die
        Korrelation zu bestimmen"""
        
    
    
    def correl(self):
        correlation = 0
        
        if (self.method == "pearson"):
            
            import scipy.stats as scipy
            correlation = scipy.pearsonr(self.setX, self.setY)
            
        elif (self.method == "spearman"):
            
            import scipy.stats as scipy
            correlation = scipy.spearmanr(self.setX, self.setY)
            
        elif (self.method == "kendall"):
            
            import scipy.stats as scipy
            correlation = scipy.kendalltau(self.setX, self.setY)
            
        elif(self.method == "concordance index"):
            
            # Code kommt noch
            print("\nDie Berechnung über den Concordance Index ist noch " +
                  "nicht fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        elif(self.method == "carmer"):
            
            # Code kommt noch
            print("\nDie Berechnung über den Carmer's V ist noch nicht " +
                  "fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        return correlation



class max_rel_cond():
    
    def __init__(self,
                 Feature_set,
                 new_classification,
                 Feature_number,
                 method
                 ):
        self.classification = new_classification
        self.subset_test = Feature_set
        self.method = method
        self.f_n = Feature_number
        
    def max_rel_calc(self):  # Maximum Relevance Calculation
        
        
        "1"
        
        relevance_of_feature_subset = pd.DataFrame(
            columns = ['Koeffizienten'])
        """Dieses DataFrame wird deshalb erstellt, damit dieses immer mehr
           mit Werten, die für die Präsenttation der Relevance der jeweiligen
           Feature vorgesehen ist, gefüllt wird"""
           
        marix_of_subset_test = np.array( self.subset_test )
        """Annahme der Daten"""
        
        marix_of_subset_test  = marix_of_subset_test.reshape(
            ( int( len( self.subset_test ) / self.f_n ), self.f_n)
            )
        """Die Daten Werden wie eine Matrix sortiert, und zwar nach dem Muster,
           dass wir z.B. n=2 Patienten mit jeweils 4 Features haben"""
           
        "1"  # Abschnitt 1 ist für die Initialisierung und befüllen von denen
        
        
        "2"
        
        print("""\nDer Inhalt beim Befüllen von relevance_of_feature_subset: \n
              {:}""" .format(marix_of_subset_test))
        print("\nDie Länge des gefüllten relevance_of_feature_subset: {:}"
              .format(len(marix_of_subset_test)))
        print (colored("\n\nBeginn der while Schleife\n\n", "green"))
        
        "2"  # Abschnitt 2 soll zu Kontrolle Abschnitt 1 ausgeben
        
        
        l = 0
        while (l < len(marix_of_subset_test)):
            print( colored("Lauf {:}".format(l+1), "cyan") )
                # Soll zu Orientierung dienen
            
            input_for_test = mutual_information(self.classification,
                                                marix_of_subset_test[l],
                                                self.method
                                                )
                # Bestimmen der Korrelationen
            
            relevance_of_feature_subset = relevance_of_feature_subset.append(
                {'Koeffizienten' : input_for_test.correl()[0]},
                ignore_index=True)
                # Fügen der Korrelation in der Menge an solchen Werten vom Set
            
            "3"
            print("{:}\n\n".format(relevance_of_feature_subset))
            "3"
            l = l + 1
            
        print( colored("Ende der while Schleife\n\n", "red") )
        
        """Hierbei sind Klassifikationen mit denen die Features jeweils in
        Korrelation gebracht werden, um herrauszufinden wie hoch dessen
        Relevanz im Bezug auf unser Ereignis ist"""
        
        return relevance_of_feature_subset



class min_red_cond():  # Minimum Redundance Condition
    
    def __init__(self, set):
        self.subssettet = set
        
    
    
    def mini_red_calc( self):  # Minimum Redundance Calculation
        
        return 0