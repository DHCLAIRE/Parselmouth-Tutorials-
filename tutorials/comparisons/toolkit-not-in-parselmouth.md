# Vocal Toolkit Commands Without Native Parselmouth Equivalents

Every command below has a generated Python function in `src/vocal_toolkit_extensions.py`. Commands marked `Direct equivalent` have a compact native Parselmouth route; the others are implemented as Parselmouth wrappers around the original Praat script.

| Command | Script | Status | Python function |
| --- | --- | --- | --- |
| Add noise... | `addnoise.praat` | Extension wrapper | `vocal_toolkit_extensions.add_noise` |
| Analyse to EQ preset... | `analysetoeqpreset.praat` | Extension wrapper | `vocal_toolkit_extensions.analyse_to_eq_preset` |
| Butterworth filter... | `butterworth.praat` | Extension wrapper | `vocal_toolkit_extensions.butterworth_filter` |
| Breathiness... | `breathiness.praat` | Extension wrapper | `vocal_toolkit_extensions.breathiness` |
| Calculate formants of a vocal tract... | `calculateformantsvt.praat` | Extension wrapper | `vocal_toolkit_extensions.calculate_formants_of_a_vocal_tract` |
| Calculate vocal tract length... | `calculatevtl.praat` | Direct equivalent | `vocal_toolkit_extensions.calculate_vocal_tract_length` |
| Change duration... | `changeduration.praat` | Direct equivalent | `vocal_toolkit_extensions.change_duration` |
| Change formants... | `changeformants.praat` | Extension wrapper | `vocal_toolkit_extensions.change_formants` |
| Change note... | `changenote.praat` | Extension wrapper | `vocal_toolkit_extensions.change_note` |
| Change pitch median and variation... | `changepitchmedian.praat` | Extension wrapper | `vocal_toolkit_extensions.change_pitch_median_and_variation` |
| Change semitones... | `changesemitones.praat` | Extension wrapper | `vocal_toolkit_extensions.change_semitones` |
| Change speed... | `changespeed.praat` | Direct equivalent | `vocal_toolkit_extensions.change_speed` |
| Change vocal tract size... | `changevt.praat` | Extension wrapper | `vocal_toolkit_extensions.change_vocal_tract_size` |
| Change vocal tract size, pitch and duration... | `changevtpitchduration.praat` | Extension wrapper | `vocal_toolkit_extensions.change_vocal_tract_size_pitch_and_duration` |
| Compressor... | `compressor.praat` | Extension wrapper | `vocal_toolkit_extensions.compressor` |
| Create vowel... | `createvowel.praat` | Extension wrapper | `vocal_toolkit_extensions.create_vowel` |
| Create waveform... | `createwaveform.praat` | Extension wrapper | `vocal_toolkit_extensions.create_waveform` |
| Cut pauses... | `cutpauses.praat` | Extension wrapper | `vocal_toolkit_extensions.cut_pauses` |
| Declick... | `declick.praat` | Extension wrapper | `vocal_toolkit_extensions.declick` |
| Declip (in-place) | `declip.praat` | Extension wrapper | `vocal_toolkit_extensions.declip` |
| Distortion (clipping)... | `distortion.praat` | Extension wrapper | `vocal_toolkit_extensions.distortion_clipping` |
| Echo... | `echo.praat` | Extension wrapper | `vocal_toolkit_extensions.echo` |
| EQ 10 bands... | `eq10bands.praat` | Extension wrapper | `vocal_toolkit_extensions.eq_10_bands` |
| EQ preset... | `eqpreset.praat` | Extension wrapper | `vocal_toolkit_extensions.eq_preset` |
| Exciter... | `exciter.praat` | Extension wrapper | `vocal_toolkit_extensions.exciter` |
| Extract pitch | `extractpitch.praat` | Direct equivalent | `vocal_toolkit_extensions.extract_pitch` |
| Extract voiced and unvoiced... | `voicedunvoiced.praat` | Extension wrapper | `vocal_toolkit_extensions.extract_voiced_and_unvoiced` |
| Extract vowels... | `extractvowels.praat` | Extension wrapper | `vocal_toolkit_extensions.extract_vowels` |
| Fade... | `fade.praat` | Extension wrapper | `vocal_toolkit_extensions.fade` |
| Fix DC offset (in-place) | `fixdc.praat` | Direct equivalent | `vocal_toolkit_extensions.fix_dc_offset` |
| Flanger... | `flanger.praat` | Extension wrapper | `vocal_toolkit_extensions.flanger` |
| Gate... | `gate.praat` | Extension wrapper | `vocal_toolkit_extensions.gate` |
| Hiss filter (low-pass)... | `hiss.praat` | Extension wrapper | `vocal_toolkit_extensions.hiss_filter_low_pass` |
| Invert pitch contour | `invertpitch.praat` | Extension wrapper | `vocal_toolkit_extensions.invert_pitch_contour` |
| Limiter... | `limiter.praat` | Extension wrapper | `vocal_toolkit_extensions.limiter` |
| Mark regions by pitch | `markpitch.praat` | Extension wrapper | `vocal_toolkit_extensions.mark_regions_by_pitch` |
| Mark regions by syllables... | `marksyllables.praat` | Extension wrapper | `vocal_toolkit_extensions.mark_regions_by_syllables` |
| Mark vowels in a TextGrid | `markvowels.praat` | Extension wrapper | `vocal_toolkit_extensions.mark_vowels_in_a_textgrid` |
| Mix all... | `mixall.praat` | Extension wrapper | `vocal_toolkit_extensions.mix_all` |
| Monotonize | `monotonize.praat` | Extension wrapper | `vocal_toolkit_extensions.monotonize` |
| Multiply or shift formants... | `multiplyshiftformants.praat` | Extension wrapper | `vocal_toolkit_extensions.multiply_or_shift_formants` |
| Normalize (scale peak 0.99) | `normalize.praat` | Direct equivalent | `vocal_toolkit_extensions.normalize` |
| Phase rotation... | `phaserotation.praat` | Extension wrapper | `vocal_toolkit_extensions.phase_rotation` |
| Pitch smoothing... | `pitchsmoothing.praat` | Extension wrapper | `vocal_toolkit_extensions.pitch_smoothing` |
| Raspiness... | `raspiness.praat` | Extension wrapper | `vocal_toolkit_extensions.raspiness` |
| Reverb... | `reverb.praat` | Extension wrapper | `vocal_toolkit_extensions.reverb` |
| Rumble filter (high-pass)... | `rumble.praat` | Extension wrapper | `vocal_toolkit_extensions.rumble_filter_high_pass` |
| Shift frequencies... | `shiftfrequencies.praat` | Extension wrapper | `vocal_toolkit_extensions.shift_frequencies` |
| Syllable Nuclei v3 (Detect Syllables and Filled Pauses)... | `SyllableNucleiv3.praat` | Extension wrapper | `vocal_toolkit_extensions.syllable_nuclei_v3_detect_syllables_and_filled_pauses` |
| Text to Speech... | `tts.praat` | Extension wrapper | `vocal_toolkit_extensions.text_to_speech` |
| Vibrato and tremolo... | `vibratotremolo.praat` | Extension wrapper | `vocal_toolkit_extensions.vibrato_and_tremolo` |
| Vocoder... | `vocoder.praat` | Extension wrapper | `vocal_toolkit_extensions.vocoder` |
| Whisper | `whisper.praat` | Extension wrapper | `vocal_toolkit_extensions.whisper` |
| Combined processes... | `combinedprocesses.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_combined_processes` |
| Duration... | `copyduration.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_duration` |
| Dynamic time warping (DTW)... | `copydtw.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_dynamic_time_warping_dtw` |
| EQ curve | `copyeq.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_eq_curve` |
| Formants... | `copyformants.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_formants` |
| Intensity (average dB)... | `copyintensityaveragedb.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_intensity_average_db` |
| Intensity contour | `copyintensitycontour.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_intensity_contour` |
| Mix... | `copymix.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_mix` |
| Pitch contour | `copypitchcontour.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_pitch_contour` |
| Pitch median and variation... | `copypitchmedian.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_pitch_median_and_variation` |
| Vocal tract size... | `copyvt.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_vocal_tract_size` |
| Vocal tract size, pitch and duration... | `copyvtpitchduration.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_vocal_tract_size_pitch_and_duration` |
| Vocoder (carrier/modulator) | `copyvocoder.praat` | Extension wrapper | `vocal_toolkit_extensions.copy_vocoder_carrier_modulator` |
