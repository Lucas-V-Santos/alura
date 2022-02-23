import re


def valida_email_by_name():
    iteration_number = int(input("Digite o número:"))
    dados = []

    for i in range(iteration_number):
        pair = input("Enter name and e-mail separated by space in this format: name <e-mail>")
        dados.append(pair)

def valida_numero_telefone():
    iterations_number = int(input("Digite o numero de interações: "))
    phone_numbers_list = []

    for i in range(iterations_number):
        number = input("Digite o {}º número:".format(i))
        phone_numbers_list.append(number)

    for number in phone_numbers_list:
        if (bool(re.match(r'^[7-9]\d{9}$', number))):
            print("YES")
        else:
            print("NO")

def valida_numero_romano():
    thousand = 'M{0,3}' #Corresponderá a 0xM ( ), 1xM (M), 2xM (MM) ou 3xM (MMM)
    hundred  = '(C[MD]|D?C{0,3})' # C[MD] = CM ou CD,    D?C{0,3} = D, DC, DCC, DCCC, C, CC, CCC
    ten      = '(X[CL]|L?X{0,3})' # X[CL] = XC ou XL,    L?X{0,3} = L, LX, LXX, LXXX, X, XX, XXX
    digit    = '(I[VX]|V?I{0,3})' # I[VX] = IV ou IX,    V?I{0,3} = V, VI, VII, VIII, I, II, III

    regex_pattern = r"%s%s%s%s$" % ('M{0,3}', '(C[MD]|D?C{0,3})', '(X[CL]|L?X{0,3})', '(I[VX]|V?I{0,3})')
    print(str(bool(re.match(regex_pattern, ''))))

resultado = valida_numero_telefone()