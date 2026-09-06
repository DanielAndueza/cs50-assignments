# Einstein assignment:

def main():
    mass = int(input('Please, put the mass in kilograms:\n'))
    formula(mass)

def formula(mass):
    constant = 300000000*300000000
    energy = (mass*constant)
    print('the energy is', energy, 'joules')
main()
