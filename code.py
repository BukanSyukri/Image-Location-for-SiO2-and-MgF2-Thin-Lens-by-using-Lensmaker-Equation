import matplotlib.pyplot as plt
import numpy as np

ASiO2 = np.array([0.6961663,0.4079426,0.8974794])
BSiO2 = np.array([0.0684043,0.1162414,9.896161])
AMgF2 = np.array([0.48755108,0.39875031,2.3120353])
BMgF2 = np.array([0.04338408,0.09461442,23.793604])
L = np.linspace(0.4,1,100)

#Refractive index of SiO2
n1SiO2 = (ASiO2[0]*L**2)/(L**2-BSiO2[0]**2)
n2SiO2 = (ASiO2[1]*L**2)/(L**2-BSiO2[1]**2)
n3SiO2 = (ASiO2[2]*L**2)/(L**2-BSiO2[2]**2)
nSiO2 = n1SiO2+n2SiO2+n3SiO2
square_n_SiO2 = 1 + nSiO2
n_SiO2 = np.sqrt(square_n_SiO2)

#Refractive index of MgF2
n1MgF2 = (AMgF2[0]*L**2)/(L**2-BMgF2[0]**2)
n2MgF2 = (AMgF2[1]*L**2)/(L**2-BMgF2[1]**2)
n3MgF2 = (AMgF2[2]*L**2)/(L**2-BMgF2[2]**2)
nMgF2 = n1MgF2+n2MgF2+n3MgF2
square_n_MgF2 = 1 + nMgF2
n_MgF2 = np.sqrt(square_n_MgF2)


R1 = np.array([20,10,20])
R2 = np.array([-20,-30,-999999])
k0 = (1/R1[0]) - (1/R2[0])
k1 = (1/R1[1]) - (1/R2[1])
k2 = (1/R1[2]) - (1/R2[2])
s=40
t = 1/s
n = np.array([n_SiO2,n_MgF2]) 
mSiO2 = n[0] - 1
mMgF2 = n[1] - 1

focusSiO2k0 = mSiO2*k0
focusSiO2k1 = mSiO2*k1
focusSiO2k2 = mSiO2*k2

focusMgF2k0 = mMgF2*k0
focusMgF2k1 = mMgF2*k1
focusMgF2k2 = mMgF2*k2

spSiO2k0 = 1/(focusSiO2k0 - t)
spSiO2k1 = 1/(focusSiO2k1 - t)
spSiO2k2 = 1/(focusSiO2k2 - t)

spMgF2k0 = 1/(focusMgF2k0 - t)
spMgF2k1 = 1/(focusMgF2k1 - t)
spMgF2k2 = 1/(focusMgF2k2 - t)

plt.figure(1)
plt.title("SiO2")
plt.plot(L,spSiO2k0,'-b', label='R1=20 R2=20')
plt.plot(L,spSiO2k1,'-k', label='R1=10 R2=30')
plt.plot(L,spSiO2k2,'-r', label='R1=20 R2=infinity')
plt.legend()
plt.xlabel('wavelength (\u03BCm)')
plt.ylabel('Distance (cm)')

plt.figure(2)
plt.title("MgF2")
plt.plot(L,spMgF2k0,'-g', label='R1=20 R2=20')
plt.plot(L,spMgF2k1,'-c', label='R1=10 R2=30')
plt.plot(L,spMgF2k2,'-m', label='R1=20 R2=infinity')
plt.legend()
plt.xlabel('wavelength (\u03BCm)')
plt.ylabel('Distance (cm)')
