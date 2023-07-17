import time
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio files
start_time = time.time()
y1, sr1 = librosa.load('dec31evening/dec31evening.wav')
y2, sr2 = librosa.load('jan1midnight/jan1midnight.wav')

##############################################################################
# Spectrogram
##############################################################################

# Create the spectrograms
spec1 = librosa.feature.melspectrogram(y=y1, sr=sr1)
spec_db1 = librosa.power_to_db(spec1, ref=np.max)
spec2 = librosa.feature.melspectrogram(y=y2, sr=sr2)
spec_db2 = librosa.power_to_db(spec2, ref=np.max)

# Plot spectrograms side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
librosa.display.specshow(spec_db1, x_axis='time', y_axis='mel', ax=axs[0])
axs[0].set_title('Dec 31 Evening')
#plt.colorbar(format='%+2.0f dB', ax=axs[0])
librosa.display.specshow(spec_db2, x_axis='time', y_axis='mel', ax=axs[1])
axs[1].set_title('Jan 1 Midnight')
plt.colorbar(format='%+2.0f dB', ax=axs[1])
plt.tight_layout()
plt.show()

##############################################################################
# Time Series plot
##############################################################################

# Generate time arrays for waveform (time series) plot
t1 = np.arange(len(y1)) / sr1
t2 = np.arange(len(y2)) / sr2

# Plot waveforms side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(t1, y1)
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Amplitude")
axs[0].set_title('Dec 31 Evening')
axs[1].plot(t2, y2)
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Amplitude")
axs[1].set_title('Jan 1 Midnight')
plt.tight_layout()
plt.show()

end_time = time.time()
print(f"Time elapsed: {end_time - start_time} seconds")
