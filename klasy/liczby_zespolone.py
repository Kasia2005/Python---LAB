class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return "Complex number: {0}+{1}j".format(self.real, self.imag)
        else:
            return "Complex number: {0}{1}j".format(self.real, self.imag)

    def __add__(self, complex_number):
        r = self.real + complex_number.real
        i = self.imag + complex_number.imag
        return ComplexNumber(r, i)

    def __sub__(self, complex_number):
        r = self.real - complex_number.real
        i = self.imag - complex_number.imag
        return ComplexNumber(r, i)

    def __mul__(self, complex_number):
        r = self.real * complex_number.real - self.imag * complex_number.imag
        i = self.real * complex_number.imag + self.imag * complex_number.real
        return ComplexNumber(r, i)
    
