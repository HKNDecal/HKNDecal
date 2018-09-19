from textx.metamodel import metamodel_from_file
import matplotlib.pyplot as plt
import numpy as np

frequency_table = {
    'A#0': 29.14,
    'A#1': 58.27,
    'A#2': 116.54,
    'A#3': 233.08,
    'A#4': 466.16,
    'A#5': 932.33,
    'A#6': 1864.66,
    'A#7': 3729.31,
    'A#8': 7458.62,
    'A0': 27.5,
    'A1': 55.0,
    'A2': 110.0,
    'A3': 220.0,
    'A4': 440.0,
    'A5': 880.0,
    'A6': 1760.0,
    'A7': 3520.0,
    'A8': 7040.0,
    'Ab0': 25.96,
    'Ab1': 51.91,
    'Ab2': 103.83,
    'Ab3': 207.65,
    'Ab4': 415.3,
    'Ab5': 830.61,
    'Ab6': 1661.22,
    'Ab7': 3322.44,
    'Ab8': 6644.88,
    'B0': 30.87,
    'B1': 61.74,
    'B2': 123.47,
    'B3': 246.94,
    'B4': 493.88,
    'B5': 987.77,
    'B6': 1975.53,
    'B7': 3951.07,
    'B8': 7902.13,
    'Bb0': 29.14,
    'Bb1': 58.27,
    'Bb2': 116.54,
    'Bb3': 233.08,
    'Bb4': 466.16,
    'Bb5': 932.33,
    'Bb6': 1864.66,
    'Bb7': 3729.31,
    'Bb8': 7458.62,
    'C#0': 17.32,
    'C#1': 34.65,
    'C#2': 69.3,
    'C#3': 138.59,
    'C#4': 277.18,
    'C#5': 554.37,
    'C#6': 1108.73,
    'C#7': 2217.46,
    'C#8': 4434.92,
    'C0': 16.35,
    'C1': 32.7,
    'C2': 65.41,
    'C3': 130.81,
    'C4': 261.63,
    'C5': 523.25,
    'C6': 1046.5,
    'C7': 2093.0,
    'C8': 4186.01,
    'D#0': 19.45,
    'D#1': 38.89,
    'D#2': 77.78,
    'D#3': 155.56,
    'D#4': 311.13,
    'D#5': 622.25,
    'D#6': 1244.51,
    'D#7': 2489.02,
    'D#8': 4978.03,
    'D0': 18.35,
    'D1': 36.71,
    'D2': 73.42,
    'D3': 146.83,
    'D4': 293.66,
    'D5': 587.33,
    'D6': 1174.66,
    'D7': 2349.32,
    'D8': 4698.63,
    'Db0': 17.32,
    'Db1': 34.65,
    'Db2': 69.3,
    'Db3': 138.59,
    'Db4': 277.18,
    'Db5': 554.37,
    'Db6': 1108.73,
    'Db7': 2217.46,
    'Db8': 4434.92,
    'E0': 20.6,
    'E1': 41.2,
    'E2': 82.41,
    'E3': 164.81,
    'E4': 329.63,
    'E5': 659.25,
    'E6': 1318.51,
    'E7': 2637.02,
    'E8': 5274.04,
    'Eb0': 19.45,
    'Eb1': 38.89,
    'Eb2': 77.78,
    'Eb3': 155.56,
    'Eb4': 311.13,
    'Eb5': 622.25,
    'Eb6': 1244.51,
    'Eb7': 2489.02,
    'Eb8': 4978.03,
    'F#0': 23.12,
    'F#1': 46.25,
    'F#2': 92.5,
    'F#3': 185.0,
    'F#4': 369.99,
    'F#5': 739.99,
    'F#6': 1479.98,
    'F#7': 2959.96,
    'F#8': 5919.91,
    'F0': 21.83,
    'F1': 43.65,
    'F2': 87.31,
    'F3': 174.61,
    'F4': 349.23,
    'F5': 698.46,
    'F6': 1396.91,
    'F7': 2793.83,
    'F8': 5587.65,
    'G#0': 25.96,
    'G#1': 51.91,
    'G#2': 103.83,
    'G#3': 207.65,
    'G#4': 415.3,
    'G#5': 830.61,
    'G#6': 1661.22,
    'G#7': 3322.44,
    'G#8': 6644.88,
    'G0': 24.5,
    'G1': 49.0,
    'G2': 98.0,
    'G3': 196.0,
    'G4': 392.0,
    'G5': 783.99,
    'G6': 1567.98,
    'G7': 3135.96,
    'G8': 6271.93,
    'Gb0': 23.12,
    'Gb1': 46.25,
    'Gb2': 92.5,
    'Gb3': 185.0,
    'Gb4': 369.99,
    'Gb5': 739.99,
    'Gb6': 1479.98,
    'Gb7': 2959.96,
    'Gb8': 5919.91,
    'N': 0
}  # nothing

metamodel = metamodel_from_file("music.tx")


def load_song(filename):
    return metamodel.model_from_file(filename)


def song_to_frequencies(song):
    parts = {}
    for part in song.parts:
        parts[part.name] = [
            (frequency_table[note.note], note.duration) for note in part.notes
        ]
    return parts

def frequencies_to_stream(freq, samplerate, bpm):
    # 1 beat / beats per minute * min per second * samples per second
    data = []
    for f, beats in freq:
        seconds = beats / bpm * 60
        data.append(np.cos(np.linspace(0, 2 * np.pi * f * seconds, int(round(samplerate * seconds)))))
    return np.concatenate(data)


def smooth(data, length):
    return np.convolve(np.ones(length, dtype=data.dtype)/length, data)


def to_chunks(data, chunks_per_second = 1, datarate=44100):
    num_chunks = int(round(chunks_per_second * len(data) / datarate))
    chunks = [data[int(datarate / chunks_per_second * i) : int(datarate / chunks_per_second * (i + 1))] for i in range(num_chunks)]
    frequencies = np.asarray([np.abs(np.fft.rfft(chunk)) for chunk in chunks]).T
    return frequencies


def load_dictionary(filename):
    words = {}
    with open(filename) as f:
        for index, line in enumerate(f):
            words[line.lower().strip()] = index
    return words


def encode(string, dictionary):
    return " ".join([str(dictionary[s.lower().strip()]) for s in string.split()])


def decode(string, dictionary):
    reversed_dictionary = {value: key for key, value in dictionary.items()}
    return " ".join([reversed_dictionary[int(num.strip())] for num in string.split()])

def im_size(im, pretty=True):
    '''Returns the # of bytes of the given color im. Assumes im is encoded in uint8
    '''
    uniquePix = set()
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            uniquePix.add(tuple(im[i,j]))
    bytes = len(uniquePix) * 3
    if pretty:
        return "~{} bytes".format(bytes)
    return bytes

def im_show_gray(im):
    if im.dtype == np.uint8:
        vmin, vmax = 0, 255
    elif im.dtype == np.float64:
        vmin, vmax = 0., 1.
    else:
        vmin, vmax = min(im), max(im)
    
    plt.imshow(im, cmap="gray", interpolation='none', vmin=vmin, vmax=vmax)