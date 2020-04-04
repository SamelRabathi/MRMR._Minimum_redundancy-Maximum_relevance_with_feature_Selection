#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:19:39 2020

@author: samelrabathi
"""


class concordance:

    import concordance
    def __init__(self,
                 feature_set,
                 classifikation
                 ):
        self.SetX = feature_set
        self.SetY = classifikation

    def start(self):
        result = concordance.ausführen(self.SetX, self.SetY)
        return result

    def ausführen(X, Y):
        from sksurv.metrics import concordance_index_censored as cindex
        import numpy as np

        if((len(Y.columns)) == 2):
            status = (Y.iloc[:,0])
            status = 1 >= status
            print(status)
            time = Y.iloc[:,1]
            print(time)
            cindices = [] # container für c-indices

            l = 0
            while (l < len(X.columns)):
                print()
                print(l)
                cindex_tmp = cindex(status, time, X.iloc[:,l])
                print(np.maximum(cindex_tmp[0], 1-cindex_tmp[0]))
                cindex_tmp = max(cindex_tmp[0], np.maximum(cindex_tmp[0], 1-cindex_tmp[0]))
                cindices.append(cindex_tmp )
                l = l + 1

            return cindices
