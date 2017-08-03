import mido
import numpy as np

# default parameters
QUANTIZATION = 0.05
NUM_NOTES = 128
TPB = 480

def track2chords(track, tpb=TPB, quantization=QUANTIZATION, num_notes=NUM_NOTES):
    chords = []
    
    tempo = mido.bpm2tempo(120) # default tempo, 120 bpm = 500000 micro s / beat 
    steps = 0 # number of steps
    chord = np.zeros(num_notes, dtype=np.int32)
    for msg in track:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
        
        steps += int(round(mido.tick2second(msg.time, tpb, tempo)/quantization)) # time steps in quantization
        
        if steps > 0:
            chords += [np.array(chord) for _ in range(steps)]
            steps = 0
        
        if msg.type in ['note_on', 'note_off']:
            note = msg.note % num_notes
            if msg.type == 'note_on':
                chord[note] = 1 if msg.velocity > 0 else 0 # on or off
            elif msg.type == 'note_off':
                chord[note] = 0

    return chords


def chords2track(chords, tpb=TPB, quantization=QUANTIZATION, num_notes=NUM_NOTES):
    track = mido.MidiTrack()
    
    tempo = mido.bpm2tempo(120)
    steps = 0
    x_prev = np.zeros(num_notes, dtype=np.int32)
    track.append(mido.MetaMessage('set_tempo', tempo=tempo))
    for x in chords:
        if np.array_equal(x, x_prev):
                steps += 1
        else:
            for i in np.where(x != x_prev)[0]:
                t = int(round(mido.second2tick(steps*quantization, tpb, tempo)))
                msg = mido.Message('note_on', note=i + (128-num_notes)//24 * 12, velocity=64 if x[i] > 0 else 0, time=t)
                track.append(msg)
                steps = 0

            x_prev = x
        
    return track 

def chordify(file, quantization=QUANTIZATION, num_notes=NUM_NOTES):
    mid = mido.MidiFile(file)
    chords = track2chords(mido.merge_tracks(mid.tracks), tpb=mid.ticks_per_beat, quantization=quantization, num_notes=num_notes)
    
    return chords

def chords2midi(chords, quantization=QUANTIZATION, num_notes=NUM_NOTES, name='output.mid'):
    mid = mido.MidiFile()
    mid.tracks.append(chords2track(chords, quantization=quantization, num_notes=num_notes))
    mid.save(name)

def test_quantization(file, quantization=QUANTIZATION, num_notes=NUM_NOTES, name='test.mid'):
    chords2midi(chordify(file, quantization=quantization, num_notes=num_notes), quantization=quantization, num_notes=num_notes, name=name) 
    
