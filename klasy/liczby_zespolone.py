import math

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def addition_complex(self, complex_number):
        return ComplexNumber(self.real.__add__(complex_number.real), self.imag.__add__(complex_number.imag))

    def subtraction_complex(self, complex_number):
        return ComplexNumber(self.real.__sub__(complex_number.real), self.imag.__sub__(complex_number.imag))

    def multiplication_complex(self, complex_number):
       return ComplexNumber(self.real.__mul__(complex_number.real).__sub__(self.imag.__mul__(complex_number.imag)), self.real.__mul__(complex_number.imag).__add__(self.imag.__mul__(complex_number.real)))

    def conjugation_complex(self):
        return ComplexNumber(self.real, (-1).__mul__(self.imag))

    def absolute_complex(self):
        return math.sqrt((self.real.__mul__(self.real)).__add__(self.imag.__mul__(self.imag)))
