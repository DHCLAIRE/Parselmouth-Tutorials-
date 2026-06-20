"""Python functions for Vocal Toolkit commands implemented with Parselmouth."""

from src.vocal_toolkit_parselmouth import run_toolkit_script


def _bool_arg(value):
    return int(bool(value))


def add_noise(sound, volume=40, type_index=1, preview=True):
    """Run `addnoise.praat` (Add noise...) through Parselmouth."""
    return run_toolkit_script(
        "addnoise.praat",
        sound,
        volume,
        type_index,
        _bool_arg(preview),
    )


def analyse_to_eq_preset(sound, new_eq_preset_name='untitled'):
    """Run `analysetoeqpreset.praat` (Analyse to EQ preset...) through Parselmouth."""
    return run_toolkit_script(
        "analysetoeqpreset.praat",
        sound,
        new_eq_preset_name,
    )


def butterworth_filter(sound, filter_index=1, frequency=1000, filter_order=2, preview=True):
    """Run `butterworth.praat` (Butterworth filter...) through Parselmouth."""
    return run_toolkit_script(
        "butterworth.praat",
        sound,
        filter_index,
        frequency,
        filter_order,
        _bool_arg(preview),
    )


def breathiness(sound, breathiness=25, preview=True):
    """Run `breathiness.praat` (Breathiness...) through Parselmouth."""
    return run_toolkit_script(
        "breathiness.praat",
        sound,
        breathiness,
        _bool_arg(preview),
    )


def calculate_formants_of_a_vocal_tract(sound, vocal_tract_length=17.5, number_of_formants=5):
    """Run `calculateformantsvt.praat` (Calculate formants of a vocal tract...) through Parselmouth."""
    return run_toolkit_script(
        "calculateformantsvt.praat",
        sound,
        vocal_tract_length,
        number_of_formants,
    )


def calculate_vocal_tract_length(sound, formant_frequency=3500, formant_number=4, calculate_from_the_selected_sounds=True, maximum_formant=5500):
    """Run `calculatevtl.praat` (Calculate vocal tract length...) through Parselmouth."""
    return run_toolkit_script(
        "calculatevtl.praat",
        sound,
        formant_frequency,
        formant_number,
        _bool_arg(calculate_from_the_selected_sounds),
        maximum_formant,
    )


def change_duration(sound, new_duration=3.0, method_index=1, preview=True):
    """Run `changeduration.praat` (Change duration...) through Parselmouth."""
    return run_toolkit_script(
        "changeduration.praat",
        sound,
        new_duration,
        method_index,
        _bool_arg(preview),
    )


def change_formants(sound, new_f1_mean=500.0, new_f2_mean=1500.0, new_f3_mean=2500.0, new_f4_mean=0, new_f5_mean=0, maximum_formant=5500, process_only_voiced_parts=True, retrieve_intensity_contour=True, preview=True):
    """Run `changeformants.praat` (Change formants...) through Parselmouth."""
    return run_toolkit_script(
        "changeformants.praat",
        sound,
        new_f1_mean,
        new_f2_mean,
        new_f3_mean,
        new_f4_mean,
        new_f5_mean,
        maximum_formant,
        _bool_arg(process_only_voiced_parts),
        _bool_arg(retrieve_intensity_contour),
        _bool_arg(preview),
    )


def change_note(sound, new_note_index=1, octave_index=2, monotone=False, preview=True):
    """Run `changenote.praat` (Change note...) through Parselmouth."""
    return run_toolkit_script(
        "changenote.praat",
        sound,
        new_note_index,
        octave_index,
        _bool_arg(monotone),
        _bool_arg(preview),
    )


def change_pitch_median_and_variation(sound, new_pitch_median=0.0, pitch_variation=100, preview=True):
    """Run `changepitchmedian.praat` (Change pitch median and variation...) through Parselmouth."""
    return run_toolkit_script(
        "changepitchmedian.praat",
        sound,
        new_pitch_median,
        pitch_variation,
        _bool_arg(preview),
    )


def change_semitones(sound, semitones=12, preview=True):
    """Run `changesemitones.praat` (Change semitones...) through Parselmouth."""
    return run_toolkit_script(
        "changesemitones.praat",
        sound,
        semitones,
        _bool_arg(preview),
    )


def change_speed(sound, change_by_index=1, factor=0.5, new_duration=2, semitones=-1, original_frame_rate=25, new_frame_rate=23.976, preview=True):
    """Run `changespeed.praat` (Change speed...) through Parselmouth."""
    return run_toolkit_script(
        "changespeed.praat",
        sound,
        change_by_index,
        factor,
        new_duration,
        semitones,
        original_frame_rate,
        new_frame_rate,
        _bool_arg(preview),
    )


def change_vocal_tract_size(sound, formant_shift_ratio=1.2, preview=True):
    """Run `changevt.praat` (Change vocal tract size...) through Parselmouth."""
    return run_toolkit_script(
        "changevt.praat",
        sound,
        formant_shift_ratio,
        _bool_arg(preview),
    )


def change_vocal_tract_size_pitch_and_duration(sound, formant_shift_ratio=1.0, new_pitch_median=0.0, pitch_variation=100, new_duration=0.0, preview=True):
    """Run `changevtpitchduration.praat` (Change vocal tract size, pitch and duration...) through Parselmouth."""
    return run_toolkit_script(
        "changevtpitchduration.praat",
        sound,
        formant_shift_ratio,
        new_pitch_median,
        pitch_variation,
        new_duration,
        _bool_arg(preview),
    )


def compressor(sound, compression=25, preview=True):
    """Run `compressor.praat` (Compressor...) through Parselmouth."""
    return run_toolkit_script(
        "compressor.praat",
        sound,
        compression,
        _bool_arg(preview),
    )


def create_vowel(sound, duration=0.8, left_f0_range=150, right_f0_range=100, f1=500, f2=1500, f3=2500, f4=3500, preset_vowel=True, speaker_index=1, vowel_index=1, synthesis_method_index=1, preview=True):
    """Run `createvowel.praat` (Create vowel...) through Parselmouth."""
    return run_toolkit_script(
        "createvowel.praat",
        sound,
        duration,
        left_f0_range,
        right_f0_range,
        f1,
        f2,
        f3,
        f4,
        _bool_arg(preset_vowel),
        speaker_index,
        vowel_index,
        synthesis_method_index,
        _bool_arg(preview),
    )


def create_waveform(sound, duration=1.0, sampling_frequency=44100, frequency=130.81, amplitude=0.2, fade_in_and_out=0.01, stereo=False, type_index=1, preview=True):
    """Run `createwaveform.praat` (Create waveform...) through Parselmouth."""
    return run_toolkit_script(
        "createwaveform.praat",
        sound,
        duration,
        sampling_frequency,
        frequency,
        amplitude,
        fade_in_and_out,
        _bool_arg(stereo),
        type_index,
        _bool_arg(preview),
    )


def cut_pauses(sound, only_at_start_and_end=False, preview=True):
    """Run `cutpauses.praat` (Cut pauses...) through Parselmouth."""
    return run_toolkit_script(
        "cutpauses.praat",
        sound,
        _bool_arg(only_at_start_and_end),
        _bool_arg(preview),
    )


def declick(sound, threshold=90, sensitivity=80, mark_detected_clicks_in_a_textgrid=False, repair_method_index=1, attenuation=90, preview=True):
    """Run `declick.praat` (Declick...) through Parselmouth."""
    return run_toolkit_script(
        "declick.praat",
        sound,
        threshold,
        sensitivity,
        _bool_arg(mark_detected_clicks_in_a_textgrid),
        repair_method_index,
        attenuation,
        _bool_arg(preview),
    )


def declip(sound):
    """Run `declip.praat` (Declip (in-place)) through Parselmouth."""
    return run_toolkit_script("declip.praat", sound)


def distortion_clipping(sound, type_of_distortion_index=1, input_gain=0.0, positive_amplitude_limit=0.5, negative_amplitude_limit=-0.5, output_gain_index=1, preview=True):
    """Run `distortion.praat` (Distortion (clipping)...) through Parselmouth."""
    return run_toolkit_script(
        "distortion.praat",
        sound,
        type_of_distortion_index,
        input_gain,
        positive_amplitude_limit,
        negative_amplitude_limit,
        output_gain_index,
        _bool_arg(preview),
    )


def echo(sound, delay=0.5, amplitude=0.5, preview=True):
    """Run `echo.praat` (Echo...) through Parselmouth."""
    return run_toolkit_script(
        "echo.praat",
        sound,
        delay,
        amplitude,
        _bool_arg(preview),
    )


def eq_10_bands(sound, band_1_31_5_hz=-24, band_2_63_hz=-24, band_3_125_hz=-24, band_4_250_hz=-24, band_5_500_hz=24, band_6_1000_hz=24, band_7_2000_hz=24, band_8_4000_hz=-24, band_9_8000_hz=-24, band_10_16000_hz=-24, preview=True):
    """Run `eq10bands.praat` (EQ 10 bands...) through Parselmouth."""
    return run_toolkit_script(
        "eq10bands.praat",
        sound,
        band_1_31_5_hz,
        band_2_63_hz,
        band_3_125_hz,
        band_4_250_hz,
        band_5_500_hz,
        band_6_1000_hz,
        band_7_2000_hz,
        band_8_4000_hz,
        band_9_8000_hz,
        band_10_16000_hz,
        _bool_arg(preview),
    )


def eq_preset(sound, preset_index=1, preview=True):
    """Run `eqpreset.praat` (EQ preset...) through Parselmouth."""
    return run_toolkit_script(
        "eqpreset.praat",
        sound,
        preset_index,
        _bool_arg(preview),
    )


def exciter(sound, high_pass_frequency=2000, phase_rotation_index=3, type_of_distortion_index=6, input_gain=0.0, positive_amplitude_limit=1.0, negative_amplitude_limit=-0.3, mix=50, scale_result_to_original_intensity=False, preview=True):
    """Run `exciter.praat` (Exciter...) through Parselmouth."""
    return run_toolkit_script(
        "exciter.praat",
        sound,
        high_pass_frequency,
        phase_rotation_index,
        type_of_distortion_index,
        input_gain,
        positive_amplitude_limit,
        negative_amplitude_limit,
        mix,
        _bool_arg(scale_result_to_original_intensity),
        _bool_arg(preview),
    )


def extract_pitch(sound):
    """Run `extractpitch.praat` (Extract pitch) through Parselmouth."""
    return run_toolkit_script("extractpitch.praat", sound)


def extract_voiced_and_unvoiced(sound, create_textgrid=False):
    """Run `voicedunvoiced.praat` (Extract voiced and unvoiced...) through Parselmouth."""
    return run_toolkit_script(
        "voicedunvoiced.praat",
        sound,
        _bool_arg(create_textgrid),
    )


def extract_vowels(sound, create_textgrid=False, preview=True):
    """Run `extractvowels.praat` (Extract vowels...) through Parselmouth."""
    return run_toolkit_script(
        "extractvowels.praat",
        sound,
        _bool_arg(create_textgrid),
        _bool_arg(preview),
    )


def fade(sound, fade_in=0.05, fade_out=0, preview=True):
    """Run `fade.praat` (Fade...) through Parselmouth."""
    return run_toolkit_script(
        "fade.praat",
        sound,
        fade_in,
        fade_out,
        _bool_arg(preview),
    )


def fix_dc_offset(sound):
    """Run `fixdc.praat` (Fix DC offset (in-place)) through Parselmouth."""
    return run_toolkit_script("fixdc.praat", sound)


def flanger(sound, delay=2.50, rate=0.20, depth=70, waveform_index=1, feedback=50, high_pass_filter_for_delay_signal=True, delay_cutoff_frequency=100, stereo_phase_offset=True, mix=100, preview=True):
    """Run `flanger.praat` (Flanger...) through Parselmouth."""
    return run_toolkit_script(
        "flanger.praat",
        sound,
        delay,
        rate,
        depth,
        waveform_index,
        feedback,
        _bool_arg(high_pass_filter_for_delay_signal),
        delay_cutoff_frequency,
        _bool_arg(stereo_phase_offset),
        mix,
        _bool_arg(preview),
    )


def gate(sound, silence_threshold=-35, minimum_silent_interval_duration=0.1, minimum_sounding_interval_duration=0.05, mark_silences_in_a_textgrid=False, create_extra_sound_with_inverted_gate=False, preview=True):
    """Run `gate.praat` (Gate...) through Parselmouth."""
    return run_toolkit_script(
        "gate.praat",
        sound,
        silence_threshold,
        minimum_silent_interval_duration,
        minimum_sounding_interval_duration,
        _bool_arg(mark_silences_in_a_textgrid),
        _bool_arg(create_extra_sound_with_inverted_gate),
        _bool_arg(preview),
    )


def hiss_filter_low_pass(sound, frequency=7500, preview=True):
    """Run `hiss.praat` (Hiss filter (low-pass)...) through Parselmouth."""
    return run_toolkit_script(
        "hiss.praat",
        sound,
        frequency,
        _bool_arg(preview),
    )


def invert_pitch_contour(sound):
    """Run `invertpitch.praat` (Invert pitch contour) through Parselmouth."""
    return run_toolkit_script("invertpitch.praat", sound)


def limiter(sound, threshold=80, preview=True):
    """Run `limiter.praat` (Limiter...) through Parselmouth."""
    return run_toolkit_script(
        "limiter.praat",
        sound,
        threshold,
        _bool_arg(preview),
    )


def mark_regions_by_pitch(sound):
    """Run `markpitch.praat` (Mark regions by pitch) through Parselmouth."""
    return run_toolkit_script("markpitch.praat", sound)


def mark_regions_by_syllables(sound, silence_threshold=-25, minimum_pause_duration=0.3, minimum_dip_between_peaks=2, show_speech_rate_info=True, trim_initial_and_final_silences=True):
    """Run `marksyllables.praat` (Mark regions by syllables...) through Parselmouth."""
    return run_toolkit_script(
        "marksyllables.praat",
        sound,
        silence_threshold,
        minimum_pause_duration,
        minimum_dip_between_peaks,
        _bool_arg(show_speech_rate_info),
        _bool_arg(trim_initial_and_final_silences),
    )


def mark_vowels_in_a_textgrid(sound):
    """Run `markvowels.praat` (Mark vowels in a TextGrid) through Parselmouth."""
    return run_toolkit_script("markvowels.praat", sound)


def mix_all(sound, avoid_clipping=False, preview=True):
    """Run `mixall.praat` (Mix all...) through Parselmouth."""
    return run_toolkit_script(
        "mixall.praat",
        sound,
        _bool_arg(avoid_clipping),
        _bool_arg(preview),
    )


def monotonize(sound):
    """Run `monotonize.praat` (Monotonize) through Parselmouth."""
    return run_toolkit_script("monotonize.praat", sound)


def multiply_or_shift_formants(sound, method_index=1, multiply_or_shift_f1_by=1.1, multiply_or_shift_f2_by=1.1, multiply_or_shift_f3_by=1.1, multiply_or_shift_f4_by=1, multiply_or_shift_f5_by=1, maximum_formant=5500, process_only_voiced_parts=True, retrieve_intensity_contour=True, preview=True):
    """Run `multiplyshiftformants.praat` (Multiply or shift formants...) through Parselmouth."""
    return run_toolkit_script(
        "multiplyshiftformants.praat",
        sound,
        method_index,
        multiply_or_shift_f1_by,
        multiply_or_shift_f2_by,
        multiply_or_shift_f3_by,
        multiply_or_shift_f4_by,
        multiply_or_shift_f5_by,
        maximum_formant,
        _bool_arg(process_only_voiced_parts),
        _bool_arg(retrieve_intensity_contour),
        _bool_arg(preview),
    )


def normalize(sound):
    """Run `normalize.praat` (Normalize (scale peak 0.99)) through Parselmouth."""
    return run_toolkit_script("normalize.praat", sound)


def phase_rotation(sound, rotation_index=1):
    """Run `phaserotation.praat` (Phase rotation...) through Parselmouth."""
    return run_toolkit_script(
        "phaserotation.praat",
        sound,
        rotation_index,
    )


def pitch_smoothing(sound, pitch_smoothing=50, preview=True):
    """Run `pitchsmoothing.praat` (Pitch smoothing...) through Parselmouth."""
    return run_toolkit_script(
        "pitchsmoothing.praat",
        sound,
        pitch_smoothing,
        _bool_arg(preview),
    )


def raspiness(sound, raspiness=20, preview=True):
    """Run `raspiness.praat` (Raspiness...) through Parselmouth."""
    return run_toolkit_script(
        "raspiness.praat",
        sound,
        raspiness,
        _bool_arg(preview),
    )


def reverb(sound, preset_index=1, mix=50, preview=True):
    """Run `reverb.praat` (Reverb...) through Parselmouth."""
    return run_toolkit_script(
        "reverb.praat",
        sound,
        preset_index,
        mix,
        _bool_arg(preview),
    )


def rumble_filter_high_pass(sound, frequency=120, preview=True):
    """Run `rumble.praat` (Rumble filter (high-pass)...) through Parselmouth."""
    return run_toolkit_script(
        "rumble.praat",
        sound,
        frequency,
        _bool_arg(preview),
    )


def shift_frequencies(sound, shift_by=1000, new_sampling_frequency=44100, preview=True):
    """Run `shiftfrequencies.praat` (Shift frequencies...) through Parselmouth."""
    return run_toolkit_script(
        "shiftfrequencies.praat",
        sound,
        shift_by,
        new_sampling_frequency,
        _bool_arg(preview),
    )


def syllable_nuclei_v3_detect_syllables_and_filled_pauses(sound):
    """Run `SyllableNucleiv3.praat` (Syllable Nuclei v3 (Detect Syllables and Filled Pauses)...) through Parselmouth."""
    return run_toolkit_script("SyllableNucleiv3.praat", sound)


def text_to_speech(sound, language_index=31, voice_index=25, sampling_frequency=44100, gap_between_words=0.01, pitch_multiplier=1.0, pitch_range_multiplier=1.0, words_per_minute=175, create_textgrid_with_annotations=False, text='1 2 3 4 5', preview=True):
    """Run `tts.praat` (Text to Speech...) through Parselmouth."""
    return run_toolkit_script(
        "tts.praat",
        sound,
        language_index,
        voice_index,
        sampling_frequency,
        gap_between_words,
        pitch_multiplier,
        pitch_range_multiplier,
        words_per_minute,
        _bool_arg(create_textgrid_with_annotations),
        text,
        _bool_arg(preview),
    )


def vibrato_and_tremolo(sound, semitones=1, decibels=1, pulses_per_second=5.5, preview=True):
    """Run `vibratotremolo.praat` (Vibrato and tremolo...) through Parselmouth."""
    return run_toolkit_script(
        "vibratotremolo.praat",
        sound,
        semitones,
        decibels,
        pulses_per_second,
        _bool_arg(preview),
    )


def vocoder(sound, frequency=130.81, carrier_waveform_index=1, preview=True):
    """Run `vocoder.praat` (Vocoder...) through Parselmouth."""
    return run_toolkit_script(
        "vocoder.praat",
        sound,
        frequency,
        carrier_waveform_index,
        _bool_arg(preview),
    )


def whisper(sound):
    """Run `whisper.praat` (Whisper) through Parselmouth."""
    return run_toolkit_script("whisper.praat", sound)


def copy_combined_processes(source_sound, target_sound, vocal_tract_size=False, pitch_index=1, time_index=1, eq_curve=False, formant_shift_ratio=1.0, new_pitch_median=0.0, pitch_variation=100, duration_factor=1.0, trim_initial_and_final_silences_first=False, dtw_slope_constraint_index=3, calculate_from_formant=4, maximum_formant_first_sound=5500, maximum_formant_second_sound=5500, show_info=True, preview=True):
    """Run `combinedprocesses.praat` (Combined processes...) through Parselmouth."""
    return run_toolkit_script(
        "combinedprocesses.praat",
        [source_sound, target_sound],
        _bool_arg(vocal_tract_size),
        pitch_index,
        time_index,
        _bool_arg(eq_curve),
        formant_shift_ratio,
        new_pitch_median,
        pitch_variation,
        duration_factor,
        _bool_arg(trim_initial_and_final_silences_first),
        dtw_slope_constraint_index,
        calculate_from_formant,
        maximum_formant_first_sound,
        maximum_formant_second_sound,
        _bool_arg(show_info),
        _bool_arg(preview),
    )


def copy_duration(source_sound, target_sound, method_index=1, preview=True):
    """Run `copyduration.praat` (Duration...) through Parselmouth."""
    return run_toolkit_script(
        "copyduration.praat",
        [source_sound, target_sound],
        method_index,
        _bool_arg(preview),
    )


def copy_dynamic_time_warping_dtw(source_sound, target_sound, slope_constraint_index=3, preview=True):
    """Run `copydtw.praat` (Dynamic time warping (DTW)...) through Parselmouth."""
    return run_toolkit_script(
        "copydtw.praat",
        [source_sound, target_sound],
        slope_constraint_index,
        _bool_arg(preview),
    )


def copy_eq_curve(source_sound, target_sound):
    """Run `copyeq.praat` (EQ curve) through Parselmouth."""
    return run_toolkit_script("copyeq.praat", [source_sound, target_sound])


def copy_formants(source_sound, target_sound, maximum_formant_first_sound=5500, maximum_formant_second_sound=5500, process_only_voiced_parts=True, retrieve_intensity_contour=True, preview=True):
    """Run `copyformants.praat` (Formants...) through Parselmouth."""
    return run_toolkit_script(
        "copyformants.praat",
        [source_sound, target_sound],
        maximum_formant_first_sound,
        maximum_formant_second_sound,
        _bool_arg(process_only_voiced_parts),
        _bool_arg(retrieve_intensity_contour),
        _bool_arg(preview),
    )


def copy_intensity_average_db(source_sound, target_sound, avoid_clipping=True, preview=True):
    """Run `copyintensityaveragedb.praat` (Intensity (average dB)...) through Parselmouth."""
    return run_toolkit_script(
        "copyintensityaveragedb.praat",
        [source_sound, target_sound],
        _bool_arg(avoid_clipping),
        _bool_arg(preview),
    )


def copy_intensity_contour(source_sound, target_sound):
    """Run `copyintensitycontour.praat` (Intensity contour) through Parselmouth."""
    return run_toolkit_script("copyintensitycontour.praat", [source_sound, target_sound])


def copy_mix(source_sound, target_sound, mix=50, avoid_clipping=False, preview=True):
    """Run `copymix.praat` (Mix...) through Parselmouth."""
    return run_toolkit_script(
        "copymix.praat",
        [source_sound, target_sound],
        mix,
        _bool_arg(avoid_clipping),
        _bool_arg(preview),
    )


def copy_pitch_contour(source_sound, target_sound):
    """Run `copypitchcontour.praat` (Pitch contour) through Parselmouth."""
    return run_toolkit_script("copypitchcontour.praat", [source_sound, target_sound])


def copy_pitch_median_and_variation(source_sound, target_sound, copy_pitch_median=True, copy_pitch_variation=True, show_info=True, preview=True):
    """Run `copypitchmedian.praat` (Pitch median and variation...) through Parselmouth."""
    return run_toolkit_script(
        "copypitchmedian.praat",
        [source_sound, target_sound],
        _bool_arg(copy_pitch_median),
        _bool_arg(copy_pitch_variation),
        _bool_arg(show_info),
        _bool_arg(preview),
    )


def copy_vocal_tract_size(source_sound, target_sound, calculate_from_formant=4, maximum_formant_first_sound=5500, maximum_formant_second_sound=5500, show_info=True, preview=True):
    """Run `copyvt.praat` (Vocal tract size...) through Parselmouth."""
    return run_toolkit_script(
        "copyvt.praat",
        [source_sound, target_sound],
        calculate_from_formant,
        maximum_formant_first_sound,
        maximum_formant_second_sound,
        _bool_arg(show_info),
        _bool_arg(preview),
    )


def copy_vocal_tract_size_pitch_and_duration(source_sound, target_sound, copy_vocal_tract_size=True, copy_pitch_median=True, copy_pitch_variation=True, copy_duration=True, calculate_from_formant=4, maximum_formant_first_sound=5500, maximum_formant_second_sound=5500, show_info=True, preview=True):
    """Run `copyvtpitchduration.praat` (Vocal tract size, pitch and duration...) through Parselmouth."""
    return run_toolkit_script(
        "copyvtpitchduration.praat",
        [source_sound, target_sound],
        _bool_arg(copy_vocal_tract_size),
        _bool_arg(copy_pitch_median),
        _bool_arg(copy_pitch_variation),
        _bool_arg(copy_duration),
        calculate_from_formant,
        maximum_formant_first_sound,
        maximum_formant_second_sound,
        _bool_arg(show_info),
        _bool_arg(preview),
    )


def copy_vocoder_carrier_modulator(source_sound, target_sound):
    """Run `copyvocoder.praat` (Vocoder (carrier/modulator)) through Parselmouth."""
    return run_toolkit_script("copyvocoder.praat", [source_sound, target_sound])

