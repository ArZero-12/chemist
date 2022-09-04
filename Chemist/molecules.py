
molecules = {
    # Molecules and common names:
    'Oxygen-gas':        ['O2', 31.998],
    'Nitrogen-gas':      ['N2', 28.014],
    'Oxide':             ['O-2', 15.999],
    'Peroxide':          ['O2-2', 31.998],
    'Superoxide':        ['O2-', 31.998],
    'Water':             ['H2O', 18.015],
    'Salt':              ['NaCl', 58.443],
    'Sodium-chloride':   ['NaCl', 58.443],
    'Hydrogen-carbonate':['HCO3-', 61.016],
    'Bicarbonate':       ['HCO3-', 61.016],
    'Hydrochloric-acid': ['HCl', 36.461],
    'Hydroxide':         ['OH-', 17.007],

    # Nobel gassess are monoatmoic:

    'Heluim-gas':        ['He', 4.003],
    'Neon-gas':          ['Ne', 20.180],
    'Argon-gas':         ['Ar', 39.948],
    'Krypton-gas':       ['Kr', 83.798],
    'Xenon-gas':         ['Xe', 131.29],
    'Radon-gas':         ['Rn', 220],

    # Polyatomic Ions:
    'Hydronuim':         ['H3O+', 19.023],
    'Ammonia':           ['NH3', 17.031],
    'Ammonuim':          ['NH4+', 18.039],
    'Carbon-monoxide':   ['CO', 28.01],
    'Carbon-dioxide':    ['CO2', 44],
    'Carbonate':         ['CO3-2', 60.008],
    'Azide':             ['N3-', 42.021],
    'Nitrate':           ['NO3-', 63.004],
    'Nitrite':           ['NO2-', 46.005],
    'Nitride':           ['N-3', 42.021],
    'Sulfate':           ['SO4-', 96.062],
    'Hydrogen-Sulfate':  ['HSO4-', 97.07],
    'Bisulfate':         ['HSO4-2', 97.07],
    'Sulfite':           ['SO3-2', 80.063],
    'Sulfide':           ['S-2', 64.132],
    'Disulfide':         ['S2-2', 64.132],
    'Thiosulfate':       ['S2O3-2', 112.129],
    'Pyrophosphate':     ['P2O7-4', 173.941],
    'Phosphate':         ['PO4-3', 94.97],
    'Phosphite':         ['PO3-3', 78.971],
    'Phosphide':         ['P-3', 30.974],
    'Chloride':          ['Cl-', 35.453],
    'Hypochlorite':      ['ClO-', 51.452],
    'Chlorite':          ['ClO2-', 67.451],
    'Chlorate':          ['ClO3-', 83.45],
    'Perchlorate':       ['ClO4-', 99.449],
    'Borate':            ['BO3-3', 58.808],
    'Bromide':           ['Br-', 79.904],
    'Hypobromide':       ['BrO-', 95.903],
    'Bromite':           ['BrO2-', 111.902],
    'Bromate':           ['BrO3-', 127.907],
    'Perbromate':        ['BrO4-', 143.9],
    'Iodide':            ['I-', 126.904],
    'Hypoiodite':        ['IO-', 142.903],
    'Iodite':            ['IO2-', 158.902],
    'Iodate':            ['IO3-', 174.901],
    'Periodate':         ['IO4-', 190.9],
    'Chromate':          ['CrO4-2', 115.992],
    'Dichromate':        ['Cr2O7-2', 215.985],

    'Permanganate':      ['MnO4-', 118.934],
    'Cynide':            ['CN-', 26.018],
    'Thiocyanate':       ['SCN-', 58.084],

    # Organic compounds:    

    #ALKANES:
    'Methane':           ['CH4', 16.043],
    'Ethane':            ['C2H6', 30.07],
    'Propane':           ['C3H8', 44.097],
    'Butane':            ['C4H10', 58.124],
    'Pentane':           ['C5H12', 72.151],
    'Hexane':            ['C6H14', 86.178],
    'Heptane':           ['C7H16', 100.205],
    'Octane':            ['C8H18', 114.232],
    'Nonane':            ['C9H20', 128.259],
    'Decane':            ['C10H22', 142.286],

    #ALKENES:
    'Ethene':		 ['C2H4', 28.054],
    'Propene':		 ['C3H6', 42.081],
    'Butene':		 ['C4H8', 56.108],
    'Pentene':		 ['C5H10', 70.135],
    'Hexene':		 ['C6H12', 84.162],
    'Heptene':		 ['C7H14', 98.189],
    'Octene':		 ['C8H16', 112.216],
    'Nonene':		 ['C9H18', 126.243],
    'Decene':		 ['C10H20', 140.27],

    #ALKYNES:
    'Ethyne':		 ['C2H2', 26.038],
    'Propyne':		 ['C3H4', 40.065],
    'Butyne':		 ['C4H6', 54.092],
    'Pentyne':		 ['C5H8', 68.119],
    'Hexyne':		 ['C6H10', 82.146],
    'Heptyne':		 ['C7H12', 96.173],
    'Octyne':		 ['C8H14', 110.2],
    'Nonyne':		 ['C9H16', 124.227],
    'Decyne':		 ['C10H18', 138.254],

    #Other organic compounds:

    'Acetate':           ['C2H3O2-', 59.044],
    'Oxalate':           ['C2O4-2', 88.018],
}

def whatis(name):
    name = name[0]
    return (molecules[name][0]) if name in molecules else print('Not found!')


def molecule():
    print('Here are the molecules that are saved in. you can use them in getmass or convert, Case sensitive')
    for item in molecules:
        print(f'{item:<20}{molecules[item][0]:<12}{molecules[item][1]:<12}')
