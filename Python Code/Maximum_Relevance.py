#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:40:29 2020

@author: samelrabathi
"""
from Mutual_Information import mutual_information
from own_timsort import own_timsort
import pandas as pd
import numpy as np
from termcolor import colored


class max_rel_cond():
    
    def __init__(self,
                 new_classification,
                 Feature_set,
                 Feature_number,
                 method = "Pearson",
                 ):
        self.classification = new_classification
        self.subset_test = Feature_set
        self.method = method
        self.f_n = Feature_number


    def max_rel_calc(
            self
            ):  # Maximum Relevance Calculation
        
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
           
        "1"
        # Abschnitt 1 ist für die Initialisierung und befüllen von denen
        
        "2"
        print("""\nDer Inhalt beim Befüllen von relevance_of_feature_subset: \n
              {:}""" .format(marix_of_subset_test))
        print("\nDie Länge des gefüllten relevance_of_feature_subset: {:}"
              .format(len(marix_of_subset_test)))
        print (colored("\n\nBeginn der while Schleife\n\n", "green"))
        "2"
        # Abschnitt 2 soll zu Kontrolle Abschnitt 1 ausgeben
        
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
        
        # Für die Sortierung von relevance_of_feature_subset
        sorted_r_o_f_s = pd.DataFrame(columns = ['Koeffizienten'])
        l = 0
        while( l < len(relevance_of_feature_subset) ):
            print( colored("Lauf {:}".format(l+1), "cyan") )
                # Soll zu Orientierung dienen
            sorting_set = own_timsort(relevance_of_feature_subset)
            print(sorting_set.timsort())
            """
            sorted_r_o_f_s = sorted_r_o_f_s.append( {'Koeffizienten' :
                own_timsort( relevance_of_feature_subset ) } )
            
            relevance_of_feature_subset = relevance_of_feature_subset.append(
                {'Koeffizienten' : input_for_test.correl()},
                ignore_index=True)"""
                # Fügen der Korrelation in der Menge an solchen Werten vom Set
            l = l + 1
        
        print("{:}\n\n".format(sorted_r_o_f_s))
        
        return sorted_r_o_f_s