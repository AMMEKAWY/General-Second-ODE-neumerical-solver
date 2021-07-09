#2nd order ODE using RK4
import math
import matplotlib.pyplot as plt
import numpy

xo=0
x=[xo]
xf=4
uo=1        #u=dy/dx at point xo
u=[uo]
yo=1
y=[yo]
n=100
h=round(math.sqrt(((xf-xo)/n)**2),4)
i=0
j=0
k=0
oo=0
E=[]


#----- eqn must be on form P(x)(d2y/dx2)+Q(x)(dy/dx)+l(x)y=0----------

def P(x):
    return 1


def Q(x):
    return 5


def l(x):
    return 4*x

#--------------------------------------------------------------------
#------------------------defining RK4 Coeff.s------------------------
#--------------------------------------------------------------------
def m1(t):
    return u[t]
def k1(t):
    return u[t]


def m2(t):
    return u[t]+(0.5)*h*k1(t)
def k2(t):
    return u[t]+(0.5)*h*k1(t)


def m3(t):
    return u[t]+(0.5)*h*k2(t)
def k3(t):
    return u[t]+(0.5)*h*k2(t)


def m4(t):
    return u[t]+h*k3(t)
def k4(t):
    return u[t]+h*k3(t)



#---------------------------Building The X-Axis-----------------------

while len(x)!= n+1:
    x.append(round(x[i]+h,4))
    i+=1
    
#----------------------------- Iterations -----------------------

while j != n:
    u.append(round((-l(x[j])*y[j]-Q(x[j])*u[j])*h/P(x[j])+u[j],4))
    y.append(round(y[j]+((h/6)*((k1(j)+2*(k2(j)+k3(j))+k4(j)))),4))
    j+=1
#-----------------------Approximate Error calculations---------------------
while k != j:
    E.append(round((y[k+1]-y[k]),4))
    k+=1
#-------------------------------------------------------------------------
print("--","x","--", "--","y","--","--","Approximate Error","--") 
while oo < len(E):
    print(" ",x[oo]," ", y[oo]," "," ", E[oo])
    oo+=1
    if oo == len(E):
        while oo != len(y):
            print(" ",x[oo]," ", y[oo])
            oo+=1

#-----------------------------plotting Results--------------------------

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()








