from math import cos, sin, tan, radians

num = int(input('Digite o ângulo que você deseja: '))

sen = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))

print('O ângulo de {} tem o SENO de {:.2f}'.format(num, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(num, tan))