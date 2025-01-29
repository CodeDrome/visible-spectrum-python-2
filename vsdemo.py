import vsdata
import vsoutput


def main():

    data = vsdata.generate_data(interval=8)

    vsoutput.to_console(data)

    # vsoutput.plot_wavelengths_frequencies(data)

    # vsoutput.plot_wavelengths_energies(data)


if __name__ == "__main__":

    main()