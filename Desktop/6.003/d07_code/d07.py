import sys
lpc_module = __import__('lpc_compiled.lpc_py%s' % ''.join(map(str, max(sys.version_info[:3], (3,5,0)))), fromlist=['R', 'LPC'])
globals().update({i: getattr(lpc_module, i) for i in ('R', 'LPC', 'pulse_train')})

from math import e,sin,cos,pi
j = complex(0,1)
from wav_utils import Wave
from matplotlib import pyplot
import random


## CODE TO GENERATE FREQUENCIES CORRESPONDING TO NOTE NAMES
_offset = {'E': -5, 'F': -4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'Bb': 1,
           'B': 2, 'C': 3, 'C#': 4, 'D': 5, 'Eb': 6,}

_higher = {'C', 'C#', 'D', 'Eb'}

_semitone = 2**(1/12)

# here we'll take note names as a tuple (note, octave)
def note_to_freq(note):
    name, octave = note
    if name in _higher:
        octave -= 1
    base = 440
    return _semitone**(_offset[name]) * base * 2**(octave-4) # find the relevant A

def voiced(segment, threshold):
    pass  # your code here


def energy(segment):
    pass  # your code here


def hann(n,N):
    if n<N:
        return sin(pi*n/(N-1))**2
    else:
        return 1

tempo = 200 # beats per minute
tempo /= 60 # beats per second
tempo = 1 / tempo  # seconds per beat
scale = [('C', 2), ('D', 2), ('E', 2), ('F', 2), ('G', 2), ('A', 2), ('B', 2), ('C', 3)]
scale += scale[::-1]

# some input frequencies to try
scale_freqs = [(i*tempo, note_to_freq(x)) for i, x in enumerate(scale)]
flat_freq = [(0, 150)]

def resynthesize(inp_fname, P, frequencies, out_fname, step_size=None,
                 window_size=None, play=False):
    """
    inp_fname: string, the name of the file we're resynthesizing
    P: the P value to use when computing LPC coefficients
    frequencies: a list of (time, frequency) pairs, as in the pulse_train function
    out_fname: string, the name of the output file we should write

    step_size: float, the number of milliseconds of a step (default: 30ms)
    window_size: float, the size of a window as a number N such that N*step_size = window_size (default: 2)
    play: if True, play the output instead of writing it to a file
    """
    if step_size is None:
        step_size = 30  # ms
    if window_size is None:
        window_size = 2

    # load in the input file and store some information about it
    w = Wave.from_file(inp_fname)
    n_samples = len(w.samples)  # the number of samples in the original
    sample_rate = w.sample_rate  # the sample rate of the original

    # compute step_size and window_size in number of samples
    step_size = int(sample_rate * (step_size / 1000))
    window_size = window_size * step_size


    # compute a pulse train for the desired frequencies
    pulses = pulse_train(n_samples, frequencies, sample_rate)

    outputs = []  # this will hold the samples of our output
    save = step_size*[0]

    for i in range(int((n_samples-window_size)/step_size)+1):
        segment = w.samples[i*step_size:i*step_size + window_size]
        windowed_segment = [i*hann(ix, window_size) for ix, i in enumerate(segment)]

        # TODO: compute the LPC coefficients associated with the windowed
        # segment (use the R and LPC functions described in the c07 writeup)
        lpc = None

        # determine whether this segment is voiced or unvoiced, and compute the
        # energy.
        segment_voiced = voiced(windowed_segment, 0.5)  # feel free to mess with this parameter
        segment_energy = energy(windowed_segment)

        if segment_voiced:
            # if this portion is voiced, grab the relevant piece of the pulse
            # train as our input
            source = pulses[i*step_size:i*step_size + window_size]

            # TODO: find an appropriate scale factor below (replace the 1), in
            # terms of segment_energy.
            source = [1*i for i in source]
        else:
            # if this portion is unvoiced, generate Gaussian white noise as our
            # input

            # TODO: find an appropriate standard deviation below (replace the
            # 1), in terms of segment_energy.
            standard_deviation = 1
            source = [random.gauss(0, standard_deviation) for _ in range(window_size)]

        # TODO: apply the computed LPC coefficients to `source`, and store the
        # output samples in `output` (replace the code below)
        output = []
        for i in source:
            output.append(i)

        # combine this window into our output samples
        outputs += [hann(n+step_size,window_size)*save[n]+hann(n,window_size)*output[n]
                    for n in range(step_size)]
        save = output[step_size:]

    # once we've computed all the windows, rescale to avoid clipping
    z = max(outputs, key=abs)
    # now, compile the output wave and either save it or play it
    output_wave = Wave([i/z for i in outputs], sample_rate)
    if play:
        output_wave.play()
    else:
        output_wave.save(out_fname)

# example:
# resynthesize('phrase.wav', 15, flat_freq, 'output_flat.wav')
# resynthesize('phrase.wav', 15, scale_freqs, 'output_scale.wav')
