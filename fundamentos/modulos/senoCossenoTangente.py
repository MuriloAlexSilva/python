from math import sin,cos,tan,radians

angulo      =   float(input('Digite o ângulo que você deseja: '))
seno        =   sin(radians(angulo)) #Temos que converter o angulo digitado para radiano   
cosseno     =   cos(radians(angulo)) #Temos que converter o angulo digitado para radiano
tangente    =   tan(radians(angulo)) #Temos que converter o angulo digitado para radiano

print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,seno,angulo,cosseno,angulo,tangente))

