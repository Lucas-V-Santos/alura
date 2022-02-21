import re

thousand = 'M{0,3}' #Corresponderá a 0xM ( ), 1xM (M), 2xM (MM) ou 3xM (MMM)
hundred  = '(C[MD]|D?C{0,3})' # C[MD] = CM ou CD,    D?C{0,3} = D, DC, DCC, DCCC, C, CC, CCC
ten      = '(X[CL]|L?X{0,3})' # X[CL] = XC ou XL,    L?X{0,3} = L, LX, LXX, LXXX, X, XX, XXX
digit    = '(I[VX]|V?I{0,3})' # I[VX] = IV ou IX,    V?I{0,3} = V, VI, VII, VIII, I, II, III

regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)
print(str(bool(re.match(regex_pattern, 'TTTT'))))