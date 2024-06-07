import numpy as np
import matplotlib.pyplot as plt

with open(r"a3-data/dataset2.txt","r") as f:
    x=[]
    y=[]
    
    lines=f.readlines()
    
    #Reading x,y pairs from file
    for line in lines:
        data=line.split()
        x.append(float(data[0]))
        y.append(float(data[1]))
    x,y=np.array(x),np.array(y)

    fft_result = np.fft.fft(y)
    frequencies = np.fft.fftfreq(len(x), x[1] - x[0])
    periodicity_estimates = 1 / frequencies[1:]  # Exclude 0 frequency (DC component)

    # Plot FFT to visualize periodicity estimates
    plt.plot(periodicity_estimates, np.abs(fft_result[1:]))
    plt.xlabel('Period')
    plt.ylabel('Magnitude')
    plt.title('FFT Result')
    plt.show()

    # Construct the design matrix M
    M = np.column_stack((np.sin(2 * np.pi *x/ T), np.sin(2 * np.pi *x/ (3 * T))))

    # Use least squares to estimate the amplitudes
    a, _, _, _ = np.linalg.lstsq(M, y, rcond=None)

    # Estimate the y using the amplitudes
    estimated_y = M.dot(a)

    # Use curve_fit for comparison
    def model(x, a1, a2):
        return a1 * np.sin(2 * np.pi *x/ T) + a2 * np.sin(2 * np.pi *x/ (3 * T))

    popt, _ = curve_fit(model, x, y)

    # Print the estimated amplitudes
    print('Amplitude estimates using least squares:', a)
    print('Amplitude estimates using curve_fit:', popt)

    # Plot the original y and the estimated y
    plt.plot(x, y, label='Original y')
    plt.plot(x, estimated_y, label='Estimated y (Least Squares)')
    plt.plot(x, model(x, *popt), label='Estimated y (curve_fit)')
    plt.xlabel('Time')
    plt.ylabel('y')
    plt.legend()
    plt.show()