
A, B, C = map(float, input().split())
if not B + C >= A:
    print('NAO FORMA TRIANGULO')
else:
    if (A**2) == (B**2 + C**2):
        print('TRIANGULO RETANGULO')
    if (A**2) < (B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
    if (A**2) > (B**2 + C**2):
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    if A == B or C == A or B == C:
        print('TRIANGULO ISOSCELES')