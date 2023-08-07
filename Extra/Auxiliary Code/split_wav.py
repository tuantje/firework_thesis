from pydub import AudioSegment

# Load the WAV file
audio = AudioSegment.from_file("jan1midnight/jan1midnight.wav", format="wav")

# Set the duration of each segment in milliseconds
segment_duration = 1 * 60 * 1000  # 1 minute

# Split the audio into segments of the desired duration
segments = []
for start_time in range(0, len(audio), segment_duration):
    end_time = start_time + segment_duration
    if end_time > len(audio):
        end_time = len(audio)
    segment = audio[start_time:end_time]
    segments.append(segment)

# Export each segment as a separate WAV file
for i, segment in enumerate(segments):
    segment.export(f"segment_{i}.wav", format="wav")

