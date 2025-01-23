from typing import Dict

import matplotlib
import matplotlib.pyplot as plt


def to_console(data: Dict) -> None:

    """
    Prints the data structure returned by
    vsdata.generate_data in a table format.
    """

    heading = f"| {chr(955)}(nm) | f(THz) |    E(J)    |  R  |  G  |  B  |"

    print("-" * len(heading))
    print(heading)
    print("-" * len(heading))

    for i in range(0, len(data['nm'])):

        print(f"| {data['nm'][i]:>5.0f} |", end="")
        print(f" {data['THz'][i]:>6.0f} |", end="")
        print(f" {data['Jsnsig'][i]:>4.2f}x10⁻¹⁹ |", end="")

        print(f" {data['rgb'][0][i]:>3.0f} |", end="")
        print(f" {data['rgb'][1][i]:>3.0f} |", end="")
        print(f" {data['rgb'][2][i]:>3.0f} |")

    print("-" * len(heading))


def plot_wavelengths_frequencies(data: Dict) -> None:

    """
    Plots vsdata.generate_data dictionary with 
    wavelengths on x-axis and frequencies on y-axis.
    """

    plt.bar(x = data["nm"], height = 1000, width=1.0, color=data["rgbtuples"])

    plt.plot(data["nm"],
             data["THz"],
             linestyle="-",
             linewidth=1.0,
             color='#000000')

    plt.title('Wavelengths and Frequencies of Visible Light')

    plt.xlabel("Wavelengths in Nanometres")
    plt.ylabel("Frequencies in Terahertz")
    plt.margins(x=0, y=0)
    plt.grid(True, color='#000000')

    plt.show()


def plot_wavelengths_energies(data: Dict) -> None:

    """
    Plots vsdata.generate_data dictionary with 
    wavelengths on x-axis and energies on y-axis.
    """

    plt.bar(x = data["nm"], height = 10, width=1.0, color=data["rgbtuples"])

    plt.plot(data["nm"],
             data["Jsnsig"],
             linestyle="-",
             linewidth=2.0,
             color='#000000')

    plt.title('Wavelengths and Energies of Visible Light')

    # causes nanometres to run in descending 
    # order so that energies are in ascending order
    plt.gca().invert_xaxis() 

    plt.xlabel("Wavelengths in Nanometres")
    plt.ylabel("Energies in Joules x 10⁻¹⁹")
    plt.margins(x=0, y=0)
    plt.grid(True, color='#000000')

    plt.show()