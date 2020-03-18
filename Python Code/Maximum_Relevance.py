#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:40:29 2020

@author: samelrabathi
"""
from Mutual_Information import mutual_information
import pandas as pd
import numpy as np

class max_rel_cond():
    
    def __init__(self,
                 new_classification,
                 set,
                 method = "Pearson"
                 ):
        self.classification = new_classification
        self.subset_test = set
        self.method = method


    def max_rel_calc(
            self
            ): # Maximum Relevance Calculation
        relevance_of_feature_subset = pd.DataFrame()  
        print("Der Inhalt beim Erstellen von relevance_of_feature_subset:"
              .format(relevance_of_feature_subset))
        """Dieses DataFrame wird deshalb erstellt, damit dieses immer mehr mit
        Werten, die für die Präsenttation der Relevance der jeweiligen Feature
        vorgesehen ist, gefüllt wird"""
        
        marix_of_subset_test = np.array( self.subset_test )
        marix_of_subset_test  = marix_of_subset_test.reshape( (2, 4))
        print("\nDer Inhalt beim Befüllen von relevance_of_feature_subset:")
        print(marix_of_subset_test)
        print("\nDie Länge des gefüllten relevance_of_feature_subset: {:}"
              .format(len(marix_of_subset_test)))
        
        l = 0
        while (l < len(marix_of_subset_test)):
            print("\nLauf {:}".format(l+1))
            input_for_test = mutual_information(
                self.classification,
                marix_of_subset_test[l],
                self.method
                )
            
            print("Die Länge von marix_of_subset_test: {:}"
              .format(len(marix_of_subset_test[l])))
            print("Die Länge von Klassifikation: {:}"
              .format(len(self.classification)))
            
            relevance_of_feature_subset.append( [input_for_test.correl() ] )
            print(relevance_of_feature_subset)
            l = l + 1
        
        print(relevance_of_feature_subset)
        print(l)
        """Hierbei sind Klassifikationen mit denen die Features jeweils in
        Korrelation gebracht werden, um herrauszufinden wie hoch dessen
        Relevanz im Bezug auf unser Ereignis ist"""
        
        relevance_of_feature_subset.sort_index(self,
                                               axis = 0,
                                               ascending = False,
                                               ignore_index = False
                                               )
        
        return relevance_of_feature_subset