'''
Created on Mar 10, 2023

@author: Mcrye
'''
import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import hilbert, find_peaks

# read ECG data from the WAV file
sampleRate, data = scipy.io.wavfile.read('ecg.wav')
    
times = np.arange(len(data))/sampleRate
'''
# apply a 3-pole lowpass filter at 0.1x Nyquist frequency
b, a = scipy.signal.butter(3, 0.1)
filtered = scipy.signal.filtfilt(b, a, data)
'''
#w = 6.0E4/(sampleRate/2)
b, a = scipy.signal.butter(3, 0.1)
filtered = scipy.signal.filtfilt(b, a, data)
    
analytic_signal = hilbert(filtered)
peaks, _ = find_peaks(filtered, height = 100)

#amplitude_envelope_01 = np.abs(analytic_signal)
#amplitude_envelope_02 = np.sqrt(filtered**2 + analytic_signal**2)
#for i in range(len(amplitude_envelope)):
#    amplitude_envelope[i] = amplitude_envelope[i]*np.exp(1*i/sampleRate)
    
#log_compressed = 20*np.log10(amplitude_envelope/np.max(amplitude_envelope))

# plot the original data next to the filtered data

plt.figure(figsize=(12, 4))

plt.subplot(121)
plt.plot(times, data)
plt.title("EKG signal with noise")
plt.margins(0, .05)

plt.subplot(122)

#plt.plot(times, amplitude_envelope_01)
#plt.plot(times, amplitude_envelope_02)
plt.plot(times, filtered)
plt.plot(times[peaks], filtered[peaks], "x", markersize = 10)
plt.title("EKG signal without nose")
plt.margins(0, .2)

plt.tight_layout()
plt.show()