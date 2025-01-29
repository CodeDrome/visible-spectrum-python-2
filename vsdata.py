from typing import Dict

import numpy as np

import wavelengthrgb as wlrgb


def generate_data(interval: int=1) -> Dict:

    """
    Creates a dictionary containing 
    NumPy arrays of data on the visible
    portion of the electromagnetic spectrum.
    The interval is the wavelength in nanometres.
    """

    wavelength_to_rgb = np.vectorize(wlrgb.wavelength_to_rgb)

    c = 3 * 10**8  # speed of light in m/s
    h = 6.62607015 * 10**-34  # Planck's constant in Js

    # array of wavelengths in nanometres
    nm = np.arange(380,781,interval)

    # interim array of frequencies in hertz
    Hz = c / (nm * 10**-9)
    # calculate terahertz from hertz
    THz = Hz * 10**-12
    
    # interim array of energies in joules
    J = h * Hz
    # calculate joules^-19 to provide the 
    # significand of scientific notation
    Jsnsig = J * 10**19

    # array of rgb values
    rgb = wavelength_to_rgb(nm)

    # rgb values in tuple form
    rgbtuples = tuple(tv/255 for tv in rgb)
    rgbtuples = np.rec.fromarrays(rgbtuples)

    # assemble arrays into dictionary
    data = {'nm': nm,
            'THz': THz,
            'Jsnsig': Jsnsig,
            'rgb': rgb,
            'rgbtuples': rgbtuples}

    return data