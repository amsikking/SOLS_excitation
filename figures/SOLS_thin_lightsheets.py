import numpy as np
from SOLS_optimum_tilt import optimum_tilt

def lightsheet_fwhm(theta_x, n, lambda_um, verbose=True):
    w_fwhm_um = (2 * np.log(2))**0.5 * lambda_um / (np.pi * theta_x * n)
    z_fwhm_um = 2 * lambda_um / (np.pi * theta_x**2 * n)
    if verbose:
        print('Light-sheet size (theta_x=%0.2f, n=%0.2f, lambda_um=%0.2f):'%(
            np.rad2deg(theta_x), n, lambda_um))
        print('w_fwhm_um=%0.2f'%w_fwhm_um)
        print('z_fwhm_um=%0.2f'%z_fwhm_um)
        print('')
    return w_fwhm_um, z_fwhm_um

if __name__ == "__main__":
    # Input:
    lambda_um = 0.532
    w_fwhm_um_135sil, z_fwhm_um_135sil = lightsheet_fwhm(
        optimum_tilt(1.35, 1.41)[2], 1.41, lambda_um)
    w_fwhm_um_100wat, z_fwhm_um_100wat = lightsheet_fwhm(
        optimum_tilt(1.00, 1.33)[2], 1.33, lambda_um)

    # Plot:
    na = np.linspace(0.7, 0.96, 1000)
    theta_1, theta_e, theta_x, theta_t = optimum_tilt(na, 1.00, verbose=False)
    n = 1.33
    w_fwhm_um, z_fwhm_um = lightsheet_fwhm(theta_x, n, lambda_um, verbose=False)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title('SOLS thin light-sheets\n (n=%0.2f, lambda_um=%0.3f)'%(
        n, lambda_um))
    ax.set_ylabel('FWHM (um)')
    ax.set_xlabel('theta_1 (deg)')
    ax.plot(np.rad2deg(theta_1), w_fwhm_um, label='thickness (w)',
            linestyle='-', color='g')
    ax.plot(np.rad2deg(theta_1), z_fwhm_um, label='length (z)',
            linestyle=':', color='k')
    ax.axvline(x=73.23, label='NA 1.35 sil (w=%0.1f, z=%0.1f)'%(
        w_fwhm_um_135sil, z_fwhm_um_135sil), linestyle='--', color='r')
    ax.axvline(x=48.75, label='NA 1.00 wat (w=%0.1f, z=%0.1f)'%(
        w_fwhm_um_100wat, z_fwhm_um_100wat), linestyle='-.', color='b')
    ax.set_ylim(ymin=0)
    plt.legend(loc="upper right", framealpha=1)
    fig.savefig('SOLS_thin_lightsheets.png', dpi=150)
    plt.show()
