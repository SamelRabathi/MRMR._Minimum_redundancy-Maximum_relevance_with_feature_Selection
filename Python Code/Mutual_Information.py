#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:31:40 2020

@author: samelrabathi
"""

class mutual_information:
    
    import scipy.stats
    
    def __init__(self, X, Y, method = "Pearson"):
        self.setX = X  # erste Menge
        self.setY = Y  # zweite Menge
        
        self.method = method
        """Es wird die Methode gebraucht, um später dementsprechent die
        Korrelation zu bestimmen"""


    def correl(self):
        correlation = 0
        
        if (self.method == "Pearson" or self.method == "pearson"):
            
            import scipy.stats as scipy
            correlation = scipy.pearsonr(self.setX, self.setY)
            
        elif (self.method == "Spearman" or self.method == "spearman"):
            
            import scipy.stats as scipy
            correlation = scipy.spearmanr(self.setX, self.setY)
            
        elif (self.method == "Kendall’s Tau" or
              self.method == "Kendall’s tau" or
              self.method == "kendall’s Tau" or
              self.method == "kendall’s tau"
              ):
            
            import scipy.stats as scipy
            correlation = scipy.kendalltau(self.setX, self.setY)
            
        elif(self.method == "Concordance Index" or
             self.method == "Concordance index" or
             self.method == "concordance Index" or
             self.method == "concordance index"
             ):
            
            # Code kommt noch
            print("\nDie Berechnung über den Concordance Index ist noch " +
                  "nicht fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        elif(self.method == "Carmer's V" or
             self.method == "Carmer's v" or
             self.method == "carmer's V" or
             self.method == "carmer's v"
             ):
            
            # Code kommt noch
            print("\nDie Berechnung über den Carmer's V ist noch nicht " +
                  "fertig, gilt noch zu bearbeiten\n")
            correlation = "Fehler"
            
        return correlation