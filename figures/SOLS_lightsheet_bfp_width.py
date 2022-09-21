import numpy as np
from SOLS_optimum_tilt import optimum_tilt

def lightsheet_bfp_width(f_mm, n, theta_x, theta_t, verbose=True):
    x_mm = 2 * f * n * np.sin(theta_t) * theta_x
    if verbose:
        print('Light-sheet BFP width ' +
              '(f_mm=%0.2f, theta_t=%0.2f, theta_x=%0.2f):'%(
                  f_mm, np.rad2deg(theta_t), np.rad2deg(theta_x)))
        print('x_mm=%0.2f'%x_mm)
        print('')
    return x_mm

if __name__ == "__main__":
    # Nikon 100x1.35 Silicone:
    na, n, f = 1.35, 1.41, 2
    theta_1, theta_e, theta_x, theta_t = optimum_tilt(na, n)
    lightsheet_bfp_width(f, n, theta_x, theta_t)

    # Nikon 40x1.15 Water:
    na, n, f = 1.15, 1.33, 5
    theta_1, theta_e, theta_x, theta_t = optimum_tilt(na, n)
    lightsheet_bfp_width(f, n, theta_x, theta_t)

    # Nikon 25x1.00 Water:
    na, n, f = 1.00, 1.33, 8
    theta_1, theta_e, theta_x, theta_t = optimum_tilt(na, n)
    lightsheet_bfp_width(f, n, theta_x, theta_t)
