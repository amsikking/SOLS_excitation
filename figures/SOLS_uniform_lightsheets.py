import numpy as np

def lightsheet_thickness(sample_um, n, lambda_um, verbose=True):
    w_fwhm_um = (3 * np.log(2) * lambda_um * sample_um / (np.pi * n))**0.5
    if verbose:
        print('Light-sheet thickness' +
              '(sample_um=%0.2f, n=%0.2f, lambda_um=%0.2f):'%(
                  sample_um, n, lambda_um))
        print('w_fwhm_um=%0.2f\n'%w_fwhm_um)
    return w_fwhm_um

if __name__ == "__main__":
    # Input:
    n, lambda_um = 1.33, 0.532
    w_fwhm_um = lightsheet_thickness(10, n, lambda_um)

    # Plot:
    sample = np.linspace(5, 100, 1000)
    w_fwhm_um = lightsheet_thickness(sample, n, lambda_um, verbose=False)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('SOLS uniform light-sheets\n (n=%0.2f, lambda_um=%0.3f)'%(
        n, lambda_um))
    ax.set_ylabel('FWHM (um)')
    ax.set_xlabel('sample (um)')
    ax.plot(sample, w_fwhm_um, label='thickness (w)', color='g')
    ax.set_ylim(ymin=0)
    plt.legend(loc="center right", framealpha=1)
    fig.savefig('SOLS_uniform_lightsheets.png', dpi=150)
    plt.show()
