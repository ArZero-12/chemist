import os
import re
from colorama import init
from termcolor import colored
import molecules

# PREASSURE UNITS
torr_per_atm = 760.0021
mmHG_per_atm = 760.0021
PSI_per_atm = 14.6959
Pa_per_atm = 101325
Bar_per_atm = 1.01325

atm = 'atm'
torr = 'torr'
mmHg = 'mmhg'
PSI = 'psi'
Pa = 'pa'
KPa = 'kpa'
Bar = 'bar'

# ENERGY UNITS
joule = 'joule'
kilo_joule = 'joule'
calorie = 'cal'
kilo_calorie = 'kcal'

# TEMPERATURE UNITS
kelvin = 'k'
celsius = 'c'
fahrenheit = 'f'

orbital_name = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f', '6s', '6p', '6d', '7s', '7p', '8s']
orbital_num = [2, 2, 6, 2, 6, 10, 2, 6, 10, 16, 2, 6, 10, 16, 2, 6, 10, 2, 6, 2]

periodic_table = {
    'H': ['Hydrogen', 1, 1.008, 'Non Metal'],
    'He': ['Helium', 2, 4.003, 'Noble Gas'],
    'Li': ['Lithium', 3, 6.941, 'Alkali Metal'],
    'Be': ['Beryllium', 4, 9.012, 'Alkaline Earth Metal'],
    'B': ['Boron', 5, 10.811, 'Non Metal'],
    'C': ['Carbon', 6, 12.011, 'Non Metal'],
    'N': ['Nitrogen', 7, 14.007, 'Non Metal'],
    'O': ['Oxygen', 8, 15.999, 'Non Metal'],
    'F': ['Flourine', 9, 18.998, 'Halogen'],
    'Ne': ['Neon', 10, 20.180, 'Noble Gas'],
    'Na': ['Sodium', 11, 22.990, 'Alkali Metal'],
    'Mg': ['Magnesium', 12, 24.305, 'Alkaline Earth Metal'],
    'Al': ['Aluminum', 13, 26.982, 'Other Metal'],
    'Si': ['Silicon', 14, 32.066, 'Non Metal'],
    'P': ['Phosphorus', 15, 30.974, 'Non Metal'],
    'S': ['Sulfur', 16, 32.066, 'Non Metal'],
    'Cl': ['Chlorine', 17, 35.453, 'Halogen'],
    'Ar': ['Argon', 18, 39.948, 'Noble Gas'],
    'K': ['Potassium', 19, 30.098, 'Halogen'],
    'Ca': ['Calcium', 20, 40.078, 'Alkali Metal'],
    'Sc': ['Scandium', 21, 44.956, 'Transition Metal'],
    'Ti': ['Titanium', 22, 47.88, 'Transition Metal'],
    'V': ['Vanadium', 23, 50.942, 'Transition Metal'],
    'Cr': ['Chromium', 24, 51.996, 'Transition Metal'],
    'Mn': ['Manganese', 25, 54.938, 'Transition Metal'],
    'Fe': ['Iron', 26, 55.933, 'Transition Metal'],
    'Co': ['Cobalt', 27, 58.633, 'Transition Metal'],
    'Ni': ['Nickel', 28, 58.693, 'Transition Metal'],
    'Cu': ['Copper', 29, 63.546, 'Transition Metal'],
    'Zn': ['Zinc', 30, 65.39, 'Transition Metal'],
    'Ga': ['Gallium', 31, 69.732, 'Other Metal'],
    'Ge': ['Germanium', 32, 72.61, 'Other Metal'],
    'As': ['Arsenic', 33, 74.922, 'Non Metal'],
    'Se': ['Selenium', 34, 78.09, 'Non Metal'],
    'Br': ['Bromine', 35, 79.904, 'Halogen'],
    'Kr': ['Krypton', 36, 83.798, 'Noble Gas'],
    'Rb': ['Rubidium', 37, 84.468, 'Alkali Metal'],
    'Sr': ['Strontium', 38, 87.62, 'Alkaline Earth Metal'],
    'Y': ['Yttrium', 39, 88.906, 'Transition Metal'],
    'Zr': ['Zirconium', 40, 91.224, 'Transition Metal'],
    'Nb': ['Niobium', 41, 92.906, 'Transition Metal'],
    'Mo': ['Molybdenum', 42, 95.94, 'Transition Metal'],
    'Tc': ['Technetium', 43, 98.907, 'Transition Metal'],
    'Ru': ['Ruthenium', 44, 101.07, 'Transition Metal'],
    'Rh': ['Rhodium', 45, 102.906, 'Transition Metal'],
    'Pa': ['Palladium', 46, 106.42, 'Transition Metal'],
    'Ag': ['Silver', 47, 107.868, 'Transition Metal'],
    'Cd': ['Cadmium', 48, 112.411, 'Transition Metal'],
    'In': ['Indium', 49, 114,818, 'Other Metal'],
    'Sn': ['Tin', 50, 118.71, 'Other Metal'],
    'Sb': ['Antimony', 51, 121.760, 'Other Metal'],
    'Te': ['Tellurium', 52, 127.6, 'Non Metal'],
    'I': ['Iodine', 53, 126.904, 'Halogen'],
    'Xe': ['Xenon', 54, 131.29, 'Noble Gas'],
    'Cs': ['Cesium', 55, 132.905, 'Alkali Metal'],
    'Ba': ['Barium', 56, 137.327, 'Alkaline Earth Metal'],
    'La': ['Lanthanum', 57, 139.906, 'Lanthanide'],
    'Ce': ['Cerium', 58, 140.115, 'Lanthanide'],
    'Pr': ['Praseodymium', 59, 140.908, 'Lanthanide'],
    'Nd': ['Neodymium', 60, 144.24, 'Lanthanide'],
    'Pm': ['Promethium', 61, 144.913, 'Lanthanide'],
    'Sm': ['Samarium', 62, 150.36, 'Lanthanide'],
    'Eu': ['Europium', 63, 151.966, 'Lanthanide'],
    'Gd': ['Gadolinium', 64, 157.25, 'Lanthanide'],
    'Tb': ['Terbium', 65, 158.925, 'Lanthanide'],
    'Dy': ['Dysprosium', 66, 162.5, 'Lanthanide'],
    'Ho': ['Holmium', 67, 164.93, 'Lanthanide'],
    'Er': ['Erbium', 68, 167.26, 'Lanthanide'],
    'Tm': ['Thullium', 69, 168.934, 'Lanthanide'],
    'Yb': ['Yitterbium', 70, 173.04, 'Lanthanide'],
    'Lu': ['Lutetium', 71, 174.967, 'Lanthanide'],
    'Hf': ['Hafnium', 72, 178.49, 'Transition Metal'],
    'Ta':['Tantium', 73, 180.948, 'Transition Metal'],
    'W': ['Tungsten', 74, 180.85, 'Transition Metal'],
    'Re': ['Rhenium', 75, 168.207, 'Transition Metal'],
    'Os': ['Osmium', 76, 190.23, 'Transition Metal'],
    'Ir': ['Iridium', 77, 192.22, 'Transition Metal'],
    'Pt': ['Platinum', 78, 195.08, 'Transition Metal'],
    'Au': ['Gold', 79, 196.967, 'Transition Metal'],
    'Hg': ['Mercury', 80, 200.59, 'Transition Metal'],
    'Tl': ['Thallium', 81, 204.383, 'Basic Metal'],
    'Pb': ['Lead', 82, 207.2, 'Basic Metal'],
    'Bi': ['Bismuth', 83, 208.98, 'Basic Metal'],
    'Po': ['Polonium', 84, 208.982 ,'Non Metal'],
    'At': ['Astatine', 85, 209.987, 'Halogen'],
    'Rn': ['Radon', 86, 222.018, 'Noble Gas'],
    'Fr': ['Francium', 87, 223.02, 'Alkali Metal'],
    'Ra': ['Radium', 88, 226.025, 'Alkaline Metal'],
    'Ac': ['Actinium', 89, 226.028, 'Actinide'],
    'Th': ['Thorium', 90, 232.038, 'Actinide'],
    'Pa': ['Protactinium', 91, 231.036, 'Actinide'],
    'U': ['Uranium', 92, 231.036, 'Actinide'],
    'Np': ['Neptunium', 93, 237.048, 'Actinide'],
    'Pu': ['Plutonium', 94, 244.064, 'Actinide'],
    'Am': ['Americium', 95, 243.061, 'Actinide'],
    'Cm': ['Curium', 96, 247.061, 'Actinide'],
    'Bk': ['Berkelium', 97, 247.07, 'Actinide'],
    'Cf': ['Californium', 98, 251.080, 'Actinide'],
    'Es': ['Einteinium', 99, 254, 'Actinide'],
    'Fm': ['Fermium', 100, 257.095, 'Actinide'],
    'Md': ['Mendelevium', 101, 258.1, 'Actinide'],
    'No': ['Nobelium', 102, 259.101, 'Actinide'],
    'Lr': ['Lawerncium', 103, 262, 'Actinide'],
    'Rf': ['Rutherfordium', 104, 261, 'Transition Metal'],
    'Db': ['Dubium', 105, 262, 'Transition Metal'],
    'Sg': ['Seaborgium', 106, 266, 'Transition Metal'],
    'Bh': ['Bohrium', 107, 264, 'Transition Metal'],
    'Hs': ['Hassium', 108, 269, 'Transition Metal'],
    'Mt': ['Meitnerium', 109, 268, 'Transition Metal'],
    'Ds': ['Darmstadium', 110, 269, 'Transition Metal'],
    'Rg': ['Roentgenium', 111, 272, 'Transition Metal'],
    'Cn': ['Copernicium', 112, 277, 'Transition Metal'],
    'Nh': ['Nihionium', 113, 284, 'Basic Metal'],
    'Fl': ['Flerovium', 114, 289, 'Basic Metal'],
    'Mc': ['Moscovium', 115, 288, 'Basic Metal'],
    'Lv': ['Livermorium', 116, 293, 'Basic Metal'],
    'Ts': ['Tennessine', 117, 294, 'Halogen'],
    'Og': ['Oganesson', 118, 294, 'Noble Gas'],
}

periodic_table_visual = [
    ['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'He'],
    ['Li', 'Be', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    ['Na', 'Mg', '', '', '', '', '', '', '', '', '', '', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
    ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
    ['Rb', 'Sr', 'Y', 'Ze', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
    ['Cs', 'Ba', '||', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At ', 'Rn '],
    ['Fr', 'Ra', '\\/', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts','Og'],
    ['', '--->>','La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'],
    ['', '--->>','Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
]

def show_element(input = ''): 
    os.system('cls' if os.name == 'nt' else 'clear') 
    color = 'green'
    if len(input) == 0:
        input = '.'
        no_input = False
    else:
        input = input
        no_input = True
    x = input
    if x not in periodic_table and x != '.':
        color = 'red'
    for element in periodic_table_visual:
        for i in element:
            if i == x:
                print(colored(f'{i:<4}', 'white', 'on_red'), end='')
            else:
                print(colored(f'{i:<4}', color), end = '')
        print()
    if input in periodic_table:
        print('name:                                    ' + periodic_table[input][0])
        print('atomic number:                           ' + str(periodic_table[input][1]))
        print('molecular weight:                        ' + str(periodic_table[input][2]))
        print('type:                                    ' + periodic_table[input][3])
        return
    if no_input:
        print(colored('Not found!', color))

def get_type(element):
    if element in periodic_table:
        return periodic_table[element][3]
    return 'Not found!'

def get_keys_from_value(d, val):
    a = []
    for i in d:
        if d[i][0] == val:
            a.append(i)
    if len(a) == 1:
        return a[0]
    return a

def get_name(element):
    if element in periodic_table:
        return periodic_table[element][0]
    keys = get_keys_from_value(periodic_table, element)
    if not keys:
        pass
    else:
        return keys
    # If the program doesn't find the element in the periodic table, it looks for 
    # Molecule names.
    if element in molecules.molecules:
        return molecules.molecules[element][0]
    keys = get_keys_from_value(molecules.molecules, element)
    if not keys:
        return 'Element not found!'
    return keys 

def get_atomic_number(element):
    if element in periodic_table:
        return periodic_table[element][1]
    return 'Element not found!'

def get_molecular_mass(amount, show_unit = False):
    elements = re.findall('[A-Z][^A-Z]*', amount)
    result = 0
    unit = ' g/mol '
    nunit = ''
    for element in elements:
        n_element = '' 
        find = re.split(r'(\d+)', element)[0: 2]
        element = find[0]
        for u in find:
            n_element += u
        num = int(find[1]) if len(find) == 2 else 1
        if element in molecules.molecules:
                result += molecules.molecules[element][1] * num
                nunit += f'({molecules.molecules[element][0]}){num}'
                continue
        if element in periodic_table:
                result += periodic_table[element][2] * num
                nunit += n_element
                continue
        print( element + ' Not in table')

    if show_unit == True:
        return str(result) + ' ' + nunit + unit
    elif show_unit == False:
        return result

def unit_conversion(amount, unit, molecule, specific = True,  show_unit = True):
        molar_ratio = 0
        amount = float(amount)
        r = 3
        if specific == True:
            r = 15
        mol = ['n', 'mol', 'moles', 'mols']
        g = ['g', 'gram', 'grams']
        print(unit, molecule)
        molar_ratio = get_molecular_mass(molecule)
        print(molar_ratio)
        if unit in mol:
            result = round(amount * molar_ratio, r)
            a = 'g '
        elif unit in g:
            result = round(amount / molar_ratio, r)
            a = 'mol '
        else:
            return 'Unit can only be in grams or moles!'
        if show_unit == True:
            return str(result) + ' ' + a + unit
        return result

def to_atm(input):
    amount = input[0]
    unit = input[1].lower()
    result = 'null'
    if unit == torr:
        result = amount / torr_per_atm
    elif unit == mmHg:
        result = amount / mmHG
    elif unit == PSI:
        result = amount / PSI_per_atm
    elif unit == Pa:
        result = amount / Pa_per_atm
    elif unit == KPa:
        result = amount / Pa_per_atm / 1000
    elif unit == Bar:
        result = amount / Bar_per_atm
    elif unit == atm:
        result = amount
    unit = ' atm'
    return result

def preassure_unit_conversion(amount, unit, unit_to, specific = True,show_unit = False):
        r = 2
        if specific == True:
            r = 15
        amount = float(amount)
        unit = unit.lower()
        unit_to = unit_to.lower()
        atm_amount = float(to_atm([amount, unit]))
        result = 'null'
        if unit_to == torr:
            result = atm_amount * torr_per_atm
            unit_to = ' torr'
        elif unit_to == mmHg:
            result = atm_amount * mmHg_per_atm
            unit_to = ' mmHg'
        elif unit_to == Pa:
            result = atm_amount / Pa_per_atm
            unit_to = ' Pa'
        elif unit_to == KPa:
            result = atm_amount * Pa_per_atm / 1000
            unit_to = ' kPa'
        elif unit_to == PSI:
            result = atm_amount * PSI_per_atm
            unit_to = ' PSI'
        elif unit_to == Bar:
            result = atm_amount * Bar_per_atm
            unit_to = 'Bar'
        elif unit_to == atm:
            result = atm_amount
        else:
            return 'Invalid unit!'  
        if show_unit == True:
            result = round(result, r)
            out = str(result) + ' ' + unit_to
            return out
        return result

def energy_conversion(amount, unit, unit_to, sp=True, show_unit=False):
    amount = float(amount)
    unit = unit.lower()
    unit_to = unit_to.lower()
    r = 2
    if sp:
        r = 15
    if unit == calorie:
        if unit_to == kilo_calorie:
            result = amount / 1000
            unit3='KCal'
        elif unit_to == joule:
            result = amount * 4.184
            unit3='Joule'
        elif unit_to == kilo_joule:
            result = amount * 0.004184
            unit3='KJoule'
        else:
            return str(amount) + ' Cal'
    elif unit == kilo_calorie:
        if unit_to == calorie:
            result = amount * 1000
            unit3='Cal'
        elif unit_to == joule:
            result = amount * 4184
            unit3='Joule'
        elif unit_to == kilo_joule:
            result = amount * 4.184
            unit3='KJoule'
        else:
            return str(amount) + ' Cal'
    elif unit == joule: 
        if unit_to == kilo_joule:
            result = amount / 1000
            unit3='KJoule'
        elif unit_to == kilo_calorie:
            result = amount / 4184
            unit3='KCal'
        elif unit_to == calorie:
            result = amount / 4.184
            unit3='Cal'
        else:
            return str(amount) + ' Joule'
    elif unit == kilo_joule:
        if unit_to == joule:
            result = amount * 1000
            unit3='Joule'
        elif unit_to == kilo_calorie:
            result = amount / 4184
            unit3='KCal'
        elif unit_to == calorie:
            result = amount / 0.04184
            unit3='Cal'
        else:
            return str(amount) + ' KJoule'
    if show_unit:
        return str(round(result, r)) + ' ' + unit3
    return result


def to_kelvin(amount, unit):
    unit = unit.upper()
    result = amount
    if unit == 'C':
        result = amount + 273.15
    elif unit == 'F':
        result = (amount - 32) *  5/9 + (273.15)
    return result

def temp_change(amount, unit_from, unit_to, sp = True, show_unit=False):
    amount = float(amount)
    r = 2
    unit_from = unit_from.upper()
    unit_to = unit_to.upper()
    valid_units = ['C', 'K', 'F']
    namount = to_kelvin(amount,  unit_from)
    result = namount
    if unit_to == 'C': 
        result = namount - 273.15
    elif unit_to == 'F':
        result = ((namount - 273.15) * (9/5)) + 32
    else:
        unit_to = 'K'
    if show_unit:
        return str(round(result, r)) + unit_to
    return result

def ect():
    for i, e in enumerate(orbital_num):
        print(orbital_name[i] + str(e), end='  ')
    print()

def econfig(element):
    if element not in periodic_table:
        print('Element not found!')
        return
    element = get_atomic_number(element)
    for i, e in enumerate(orbital_num):
        element -= e
        remain = e
        if element <= 0:
            remain = e + element
            print(orbital_name[i] + str(remain), end='  ')
            break
        print(orbital_name[i] + str(remain), end='  ')

    print()
