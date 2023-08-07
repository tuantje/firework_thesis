import time
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
start_time = time.time()
y, sr = librosa.load('jan1midnight/jan1midnight.wav')
##############################################################################
                            #Spectogram
##############################################################################

# Create the spectrogram
spec = librosa.feature.melspectrogram(y=y, sr=sr)
spec_db = librosa.power_to_db(spec, ref=np.max)

# Display the spectrogram
librosa.display.specshow(spec_db, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.tight_layout()
plt.show()

end_time = time.time()
print(f"Time elapsed: {end_time - start_time} seconds")
##############################################################################
                            #Time Series plot
##############################################################################


# Generate time array for waveform (time series) plot
t = np.arange(len(y)) / sr

# Plot waveform
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title('Waveform (time series) plot')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
##############################################################################
                            #Distinguish Fireworks
##############################################################################












