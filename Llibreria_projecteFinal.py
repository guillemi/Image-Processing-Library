# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:02:43 2020

Algorísmia i Programació Audiovisual

   · Llibreria de funcionalitats per imatges:
       
   - Invertir els colors i funció inversa.
   - Convertir a escala de grisos.
   - Convertir una imatge a negativa.
   - Funció per ajustar la brillantor.
   - Classe
   - Saturació de la imatge
   - Rotació de imatges -270,-120, -90, 90, 180 o 270 graus donats com a parametre.
   - Mirall Hortizontal de la imatge.
   - Mirall Vertical de la imatge.
   - Increment d'una de les components RGB donat un percentatge.
   - Enquadre d'una imatge
   
   

Quim Segura, Guillem Martinez i Marc Sebastià

Creada el dijous 4 de Juny del 2020
"""
import matplotlib.pyplot as plt
import numpy as np
# El plt.imread() de matplotlib.pyplot només admet imatges en format png.



def invertir(imatge):
     
    imatge_ = 1 - imatge
    
    return imatge_

def desinvertir(imatge):
    
    imatge_ = -( imatge - 1 )
    
    return imatge_
    
def escala_grisos(imatge):
    h,w,canals = imatge.shape # alçada,amplada, 3 canals rgb
    imatge_=imatge
    for i in range(h):
        for j in range(w):
            imatge_[i,j] = 0.3 * imatge[i,j][0] + 0.59 * imatge[i,j][1] +  0.11 * imatge[i,j][2]
     
    return imatge_
    

def negativitzar(imatge):
    
    imatge_g = escala_grisos(imatge) # escala de grisos
    negativa = invertir(imatge_g)    # convertir blancs en negres i a la inversa
    
    return negativa

def brillantor(imatge,parametre):
    """
    Definim la brillantor com un parametre entre 0 i 1.
    0 --> Imatge molt fosca, quasi negra
    1 --> Imatge molt clara, es veu perfectament.
     
    """

    imatge_ = imatge*parametre
    return imatge_

def saturacio(imatge,nivell,p):
    """
    p = 1 augmentar saturació
    p = 0 disminuir saturació
    
    nivell = (0-100)
    """
    imatge_=imatge
    if p:
        return imatge_ + nivell/100
    else:
        return imatge_ - nivell/100
    
def rotacio(imatge,graus):
    imatge_=imatge
    if (graus == 90 or graus == -270):
        imatge_ = np.rot90(imatge,1,(1,0))
    elif (graus == 180 or graus == -180):
        imatge_ = np.rot90(imatge,2,(1,0))
    elif (graus == 270 or graus == -90):
        imatge_ = np.rot90(imatge,3,(1,0))
    else:
        print(f"Error: No es pot fer una rotació de {graus} graus")
        imatge_ = imatge
    
    return imatge_

def mirror_horitzontal(imatge):
    return np.fliplr(imatge)

def mirror_vertical(imatge):
    return np.flipud(imatge)
     

def incrementar_RGB(imatge,lletra,percentatge):
    imatge_=imatge
    for i in range (len(imatge)):
        for j in range(len(imatge[0])):
                if(lletra == 'R'):
                    imatge_[i][j][0] = imatge[i][j][0] + percentatge*255
                if(lletra == 'G'):
                    imatge_[i][j][1] = imatge[i][j][1] + percentatge*255
                if(lletra == 'B'):
                    imatge_[i][j][2] = imatge[i][j][2] + percentatge*255
    return imatge_

def exposicio(imatge,percentatge):
    """
    Percentatge recomenat de -0.5 a 0.5
    """
    imatge_=imatge
    for i in range (len(imatge)):
        for j in range(len(imatge[0])):
                    imatge_[i][j][0] = imatge[i][j][0] + percentatge*1
                    imatge_[i][j][1] = imatge[i][j][1] + percentatge*1
                    imatge_[i][j][2] = imatge[i][j][2] + percentatge*1

    return imatge_

def enquadrar(imatge,amplada):
    amp_tot=amplada*2
    m_y, m_x = len(imatge), len(imatge[0])
    
    imatge_enquadrada = np.zeros((amp_tot+m_y, amp_tot+m_x, len(imatge[0][0])))
    imatge_enquadrada[amplada:-amplada,amplada:-amplada] = imatge
    
    return imatge_enquadrada


    







class Imatge_QGM:
    """
    Classe d'importació d'imatges png
    
    nom = Imatge_QGM('nom de la foto')  --> incialització
    nom.metode() --> per cridar algun efecte
    
    Amb fotos de dimensions grans algunes operacions poden trigar fins a 10 segons.
    
    Quim Segura, Guillem Martinez i Marc Sebastià
    Creada el Juny del 2020
    
    """
    
    def __init__(self,foto): # Creació de l'ojecte Imatge_QGM
        self.nom = foto
        self.imatge = plt.imread(foto) # variable foto 
        self.altura = self.imatge.shape[0]
        self.amplada = self.imatge.shape[1]
        self.dimensions = self.imatge.shape[2]
        
        
    def invertir(self):      
        self.imatge_inv = 1 - self.imatge
        return self.imatge_inv
    
    def desinvertir(self):
        self.imatge = -( self.imatge - 1 )
        return self.imatge
    
    def escala_grisos(self):
        h,w,canals = self.imatge.shape # alçada,amplada, 3 canals rgb
        self.imatge = self.imatge 
        for i in range(h):
            for j in range(w):
                self.imatge[i,j] = 0.3 * self.imatge[i,j][0] + 0.59 * self.imatge[i,j][1] +  0.11 * self.imatge[i,j][2]
     
        return self.imatge
    
    def negativitzar(self):
        im_gris = escala_grisos(self.imatge) # escala de grisos
        self.imatge = invertir(im_gris)    # convertir blancs en negres i a la inversa
    
        return self.imatge
    
    def brillantor(self,parametre):
        """
        Definim la brillantor com un parametre entre 0 i 1.
        0 --> Imatge molt fosca, quasi negra
        1 --> Imatge molt clara, es veu perfectament.
     
        """

        self.imatge = self.imatge*parametre
        return self.imatge_
    
    def saturacio(self,nivell,p):
        """
        p = 1 augmentar saturació
        p = 0 disminuir saturació
    
        nivell = (0-100)
        """
        if p:
             self.imatge += nivell/100
        else:
             self.imatge -= nivell/100
        return self.imatge
        
    def rotacio(self,graus):
        if (graus == 90 or graus == -270):
            self.imatge = np.rot90(self.imatge,1,(1,0))
        if (graus == 180 or graus == -180):
            self.imatge = np.rot90(self.imatge,2,(1,0))
        if (graus == 270 or graus == -90):
            self.imatge = np.rot90(self.imatge,3,(1,0))
        else:
            print(f"Error: No es pot fer una rotació de {graus} graus")
            self.imatge = self.imatge
    
        return self.imatge
        
    def mirror_horitzontal(self):
        self.imatge = np.fliplr(self.imatge)
        return self.imatge
    
    def mirror_vertical(self):
        self.imatge = np.flipud(self.imatge)
        return self.imatge
    
    def incrementar_RGB(self,lletra,percentatge):
        """
        lletra: escollir entre [R, G, B]--> representa el color a incrementar
        Percentatge entre 0 i 1.
        """
        imatge = self.imatge
        for i in range (len(imatge)):
            for j in range(len(imatge[0])):
                    if(lletra == 'R'):
                        imatge[i][j][0] = imatge[i][j][0] + percentatge*255
                    if(lletra == 'G'):
                        imatge[i][j][1] = imatge[i][j][1] + percentatge*255
                    if(lletra == 'B'):
                        imatge[i][j][2] = imatge[i][j][2] + percentatge*255
        self.imatge = imatge
        return self.imatge
    
    def exposicio(self,percentatge):
        """
        Percentatge recomanat de -0.5 a 0.5
        """
        imatge = self.imatge
        for i in range (len(imatge)):
            for j in range(len(imatge[0])):
                        imatge[i][j][0] = imatge[i][j][0] + percentatge*1
                        imatge[i][j][1] = imatge[i][j][1] + percentatge*1
                        imatge[i][j][2] = imatge[i][j][2] + percentatge*1
    
        self.imatge = imatge
        return self.imatge
    
    def __repr__(self):
        return f"Classe de processat de la imatge {self.nom} amb varis efectes disponibles"
    
    def __str__(self):
        return f"Classe de processat d'imatges"
        
   
    

        







        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

