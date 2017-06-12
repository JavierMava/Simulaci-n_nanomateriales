

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



'Parametros de trabajo'
'v  -  Volumen del reactor'
'CR -  Calor de reaccion levadura/G (J/gG)'
'dmosto - densidad del mosto (g/L)'
'cmosto - calor especifico del mosto (J/g*K)'
'Ctc - coeficiente de transferencia de calor, en este caso para un tanque aislado (J/m^2*K*h)'
'Ta -  temperatura ambiente'
'Ti - temperatura inicial'
'biomasa - inoculacion (g/L)'
'Ai - azucar inicial (g/L)'



v = 10000 

CR = 587  
dmosto = 1060  
cmosto = 4 
Ctc = .48*3600 
Aci = 10.602875 
Ta = 25+273.15 
Ti =12+273.15 


biomasa =4 
Ai=115 

IC =[.48*biomasa,.02*biomasa,.5*biomasa,Ai,0,0,0,Ti] 
t = np.linspace(0,150,5000)


def cfb(x,t):
    X_ina,X_fun,X_mu,S,E,Acet,Diac,T = x

    
    #Cinetica
    mu_x0 = 1.095E47*np.exp(-63720/(1.99536*T))
    k_m = 3.373E56*np.exp(-76450/(1.99536*T))
    mu_eas = 1.129E39*np.exp(-53056/(1.99536*T))
    mu_D0 = 4.889E14*np.exp(-20020/(1.99536*T))
    mu_s0 = 6.232E-19*np.exp(23254/(1.99536*T))
    mu_a0 = 26.3865*np.exp(-2528.6/(1.99536*T))
    mu_ina = 2.2041E13*np.exp(-18959/(1.99536*T))
    k_s = 1.1081E-52*np.exp(68249.2/(1.99536*T))
    k_dc = 0.000127672
    k_dm = 0.00113864
    
    #Proceso de fermentacion

    
    dX_ina = -mu_ina*X_ina
    dX_fun = (mu_x0*S)/(0.5*Ai+E)*X_fun - k_m*X_fun + mu_ina*X_ina
    dX_mu = k_m*X_fun - (0.5*Ai*mu_D0)/(0.5*Ai+E) * X_mu
    dS = -(mu_s0*S)/(k_s+S)*X_fun
    dE = (mu_a0*S)/(k_s+S)*(1-E/(0.5*Ai))*X_fun
    dAcet = mu_eas*(mu_s0*S)/(k_s+S)*X_fun
    dDiac = k_dc*S*X_fun - k_dm*Diac*E


    #Balance de energia
    dT = -CR*dS/dmosto/cmosto + Ctc*Aci/dmosto/cmosto/v*(Ta-T)
    
    return [dX_ina,dX_fun,dX_mu,dS,dE,dAcet,dDiac,dT]

def sim(t,IC):
    sol = odeint(cfb,IC,t) #
    X_ina,X_fun,X_mu,S,E,Acet,Diac,T  = sol.transpose()
    return [X_ina,X_fun,X_mu,S,E,Acet,Diac,T]

        
X_ina,X_fun,X_mu,S,E,Acet,Diac,T = sim(t,IC)

# graficas 
def graficas(X_ina,X_fun,X_mu,S,E,Acet,Diac,T):
    plt.figure(figsize=(12,7))
    plt.subplot(2,1,1)
    plt.plot(t,T-273.15)
    plt.plot(t,X_ina,t,X_fun,t,X_mu,t,X_ina + X_fun + X_mu)
    plt.xlabel('Tiempo [h]')
    plt.ylabel('Concentracion [g/L]')
    plt.title('Biomasa')
    plt.legend(['Temperatura (Celcius)','Celulas inactivas','Celulas activas','Celulas muertas', 'Celulas totales'])
    

    plt.subplot(2,1,2)
    plt.plot(t,S)
    plt.plot(t,E)
    plt.plot(t,Diac)
    plt.plot(t,Acet)
    plt.xlabel('Tiempo [h]')
    plt.ylabel('Concentracion [g/L]')
    plt.title('Concentracion de etanol y metabolitos secundarios')
    plt.legend(['Azucar','Etanol','Diacetil','Ac. de etilo'])


    plt.tight_layout()
    



graficas(X_ina,X_fun,X_mu,S,E,Acet,Diac,T)
#plt.show()


SSL = [S[len(S)-1],E[len(E)-1],Acet[len(Acet)-1],Diac[len(Diac)-1]]
print("Concentracion de los componentes principales: ")
print("Glucosa- " + str(SSL[0]) + " g/L.")
print("Etanol- " + str(SSL[1]) + " g/L.")
print("Acetato de etilo- " + str(SSL[2]) + " ppm.")
print("Diacetilo- " + str(SSL[3]) + " ppm.")

#etanol produccio 95%
count=0
for x in E:
    if x >= .95*SSL[1]:
        etanolt = t[count]
        break
    count+=1
print(" ")
print("Las horas ocupadas para producir un 95% de etanol son  " + str(etanolt))


plt.show()
