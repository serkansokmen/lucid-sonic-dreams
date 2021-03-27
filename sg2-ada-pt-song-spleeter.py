from lucidsonicdreams import LucidSonicDream

# spleeter separate -p spleeter:4stems -o output your_audio.mp3
# bass, drums, other, vocals
L = LucidSonicDream(song = 'song.mp3',
                     pulse_audio = 'drums.wav', # Ignore other pulse settings and use this audio track to pulse
                     motion_audio = 'bass.wav',
                     contrast_audio = 'other.wav',
                     flash_audio = 'vocals.wav',
                     style = 'stylegan2/training-runs/00004-face-paintings-styleaug_512-later/network-snapshot-000768.pkl') # pick your pickle!
                     
L.hallucinate(file_name = 'song.mp4',
             fps = 30, # fps is not true. fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 20,
             truncation = 1, # Between 0 and 1
             
             pulse_react = 1.2,
             pulse_percussive = False, # If True while pulse_harmonic is False & no pulase_audio, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False & no pulase_audio, pulse reacts to the audio's harmonic elements.

             motion_react = 1.2,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.6, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.5,
             
             flash_percussive = True,
             flash_strength = 0.5,
                          
             save_frames = False
             ) 
