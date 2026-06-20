# Parselmouth API Tutorials

Generated from the public Parselmouth API manifest. The manifest was introspected from `praat-parselmouth 0.4.7` with embedded Praat `6.1.38`.

Source reference: [https://parselmouth.readthedocs.io/en/stable/api_reference.html](https://parselmouth.readthedocs.io/en/stable/api_reference.html)

## Functions And Properties

| API member | Kind | Owners | Vocal Toolkit coverage |
| --- | --- | --- | --- |
| [add](functions/add.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Related |
| [add_note](functions/add-note.md) | `method` | `PraatError`, `PraatFatal`, `PraatWarning` | Related |
| [as_array](functions/as-array.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [at_xy](functions/at-xy.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [autocorrelate](functions/autocorrelate.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [bin_width](functions/bin-width.md) | `property` | `Spectrum` | Not in Vocal Toolkit |
| [ceiling](functions/ceiling.md) | `property` | `Pitch` | Not in Vocal Toolkit |
| [centre_time](functions/centre-time.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [cepstral_smoothing](functions/cepstral-smoothing.md) | `method` | `Spectrum` | Related |
| [class_name](functions/class-name.md) | `property` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [combine_to_stereo](functions/combine-to-stereo.md) | `method` | `Sound` | Related |
| [concatenate](functions/concatenate.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [convert_to_mono](functions/convert-to-mono.md) | `method` | `Sound` | Related |
| [convert_to_stereo](functions/convert-to-stereo.md) | `method` | `Sound` | Related |
| [convolve](functions/convolve.md) | `method` | `MFCC`, `Sound` | Covered |
| [copy](functions/copy.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [count_differences](functions/count-differences.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [count_voiced_frames](functions/count-voiced-frames.md) | `method` | `Pitch` | Related |
| [cross_correlate](functions/cross-correlate.md) | `method` | `MFCC`, `Sound` | Not in Vocal Toolkit |
| [de_emphasize](functions/de-emphasize.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [deepen_band_modulation](functions/deepen-band-modulation.md) | `method` | `Sound` | Related |
| [df](functions/df.md) | `property` | `Spectrum` | Not in Vocal Toolkit |
| [divide](functions/divide.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Not in Vocal Toolkit |
| [dt](functions/dt.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [duration](functions/duration.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [dx](functions/dx.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [dy](functions/dy.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [end_time](functions/end-time.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [extract_all_channels](functions/extract-all-channels.md) | `method` | `Sound` | Related |
| [extract_channel](functions/extract-channel.md) | `method` | `Sound` | Related |
| [extract_features](functions/extract-features.md) | `method` | `MFCC` | Related |
| [extract_left_channel](functions/extract-left-channel.md) | `method` | `Sound` | Related |
| [extract_part](functions/extract-part.md) | `method` | `Sound` | Related |
| [extract_part_for_overlap](functions/extract-part-for-overlap.md) | `method` | `Sound` | Related |
| [extract_right_channel](functions/extract-right-channel.md) | `method` | `Sound` | Related |
| [fifth_down](functions/fifth-down.md) | `method` | `Pitch` | Related |
| [fifth_up](functions/fifth-up.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [fmax](functions/fmax.md) | `property` | `CC`, `MFCC`, `Spectrum` | Not in Vocal Toolkit |
| [fmin](functions/fmin.md) | `property` | `CC`, `MFCC`, `Spectrum` | Not in Vocal Toolkit |
| [formula](functions/formula.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Pitch`, `Sound` | Covered |
| [frame_number_to_time](functions/frame-number-to-time.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [from_tgt](functions/from-tgt.md) | `method` | `TextGrid` | Related |
| [full_name](functions/full-name.md) | `property` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [get_average](functions/get-average.md) | `method` | `Intensity` | Related |
| [get_band_density](functions/get-band-density.md) | `method` | `Spectrum` | Related |
| [get_band_density_difference](functions/get-band-density-difference.md) | `method` | `Spectrum` | Related |
| [get_band_energy](functions/get-band-energy.md) | `method` | `Spectrum` | Related |
| [get_band_energy_difference](functions/get-band-energy-difference.md) | `method` | `Spectrum` | Related |
| [get_bandwidth_at_time](functions/get-bandwidth-at-time.md) | `method` | `Formant` | Related |
| [get_bin_number_from_frequency](functions/get-bin-number-from-frequency.md) | `method` | `Spectrum` | Related |
| [get_bin_width](functions/get-bin-width.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_c0_value_in_frame](functions/get-c0-value-in-frame.md) | `method` | `CC`, `MFCC` | Related |
| [get_center_of_gravity](functions/get-center-of-gravity.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_central_moment](functions/get-central-moment.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_centre_of_gravity](functions/get-centre-of-gravity.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_column_distance](functions/get-column-distance.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_end_time](functions/get-end-time.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_energy](functions/get-energy.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_energy_in_air](functions/get-energy-in-air.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_frame](functions/get-frame.md) | `method` | `CC`, `MFCC`, `Pitch` | Related |
| [get_frame_number_from_time](functions/get-frame-number-from-time.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_frequency_from_bin_number](functions/get-frequency-from-bin-number.md) | `method` | `Spectrum` | Related |
| [get_highest_frequency](functions/get-highest-frequency.md) | `method` | `Spectrum` | Related |
| [get_highest_x](functions/get-highest-x.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_highest_y](functions/get-highest-y.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_imaginary_value_in_bin](functions/get-imaginary-value-in-bin.md) | `method` | `Spectrum` | Related |
| [get_index_from_time](functions/get-index-from-time.md) | `method` | `Sound` | Related |
| [get_intensity](functions/get-intensity.md) | `method` | `Sound` | Related |
| [get_kurtosis](functions/get-kurtosis.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_lowest_frequency](functions/get-lowest-frequency.md) | `method` | `Spectrum` | Related |
| [get_lowest_x](functions/get-lowest-x.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_lowest_y](functions/get-lowest-y.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_maximum](functions/get-maximum.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_mean_absolute_slope](functions/get-mean-absolute-slope.md) | `method` | `Pitch` | Related |
| [get_minimum](functions/get-minimum.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_nearest_zero_crossing](functions/get-nearest-zero-crossing.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_number_of_bins](functions/get-number-of-bins.md) | `method` | `Spectrum` | Related |
| [get_number_of_channels](functions/get-number-of-channels.md) | `method` | `Sound` | Related |
| [get_number_of_coefficients](functions/get-number-of-coefficients.md) | `method` | `CC`, `MFCC` | Related |
| [get_number_of_columns](functions/get-number-of-columns.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_number_of_frames](functions/get-number-of-frames.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_number_of_rows](functions/get-number-of-rows.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_number_of_samples](functions/get-number-of-samples.md) | `method` | `Sound` | Related |
| [get_power](functions/get-power.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_power_at](functions/get-power-at.md) | `method` | `Spectrogram` | Not in Vocal Toolkit |
| [get_power_in_air](functions/get-power-in-air.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_real_value_in_bin](functions/get-real-value-in-bin.md) | `method` | `Spectrum` | Related |
| [get_rms](functions/get-rms.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [get_root_mean_square](functions/get-root-mean-square.md) | `method` | `Sound` | Related |
| [get_row_distance](functions/get-row-distance.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_sampling_frequency](functions/get-sampling-frequency.md) | `method` | `Sound` | Related |
| [get_sampling_period](functions/get-sampling-period.md) | `method` | `Sound` | Related |
| [get_skewness](functions/get-skewness.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_slope_without_octave_jumps](functions/get-slope-without-octave-jumps.md) | `method` | `Pitch` | Related |
| [get_standard_deviation](functions/get-standard-deviation.md) | `method` | `Spectrum` | Not in Vocal Toolkit |
| [get_start_time](functions/get-start-time.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_sum](functions/get-sum.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_time_from_frame_number](functions/get-time-from-frame-number.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_time_from_index](functions/get-time-from-index.md) | `method` | `Sound` | Related |
| [get_time_step](functions/get-time-step.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_total_duration](functions/get-total-duration.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [get_value](functions/get-value.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Related |
| [get_value_at_time](functions/get-value-at-time.md) | `method` | `Formant`, `Pitch` | Related |
| [get_value_at_xy](functions/get-value-at-xy.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_value_in_bin](functions/get-value-in-bin.md) | `method` | `Spectrum` | Related |
| [get_value_in_cell](functions/get-value-in-cell.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [get_value_in_frame](functions/get-value-in-frame.md) | `method` | `CC`, `MFCC`, `Pitch` | Related |
| [get_x_of_column](functions/get-x-of-column.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [get_y_of_row](functions/get-y-of-row.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [highest_frequency](functions/highest-frequency.md) | `property` | `Spectrum` | Related |
| [info](functions/info.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [interpolate](functions/interpolate.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [kill_octave_jumps](functions/kill-octave-jumps.md) | `method` | `Pitch` | Related |
| [lengthen](functions/lengthen.md) | `method` | `Sound` | Covered |
| [lowest_frequency](functions/lowest-frequency.md) | `property` | `Spectrum` | Related |
| [lpc_smoothing](functions/lpc-smoothing.md) | `method` | `Spectrum` | Related |
| [max_n_candidates](functions/max-n-candidates.md) | `property` | `Pitch` | Not in Vocal Toolkit |
| [max_n_coefficients](functions/max-n-coefficients.md) | `property` | `CC`, `MFCC` | Not in Vocal Toolkit |
| [multiply](functions/multiply.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Related |
| [multiply_by_window](functions/multiply-by-window.md) | `method` | `Sound` | Related |
| [n_bins](functions/n-bins.md) | `property` | `Spectrum` | Not in Vocal Toolkit |
| [n_channels](functions/n-channels.md) | `property` | `Sound` | Not in Vocal Toolkit |
| [n_columns](functions/n-columns.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [n_frames](functions/n-frames.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [n_rows](functions/n-rows.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [n_samples](functions/n-samples.md) | `property` | `Sound` | Not in Vocal Toolkit |
| [name](functions/name.md) | `property` | `AmplitudeScaling`, `CC`, `Data`, `Formant`, `FormantUnit` | Related |
| [nf](functions/nf.md) | `property` | `Spectrum` | Not in Vocal Toolkit |
| [nt](functions/nt.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [nx](functions/nx.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [ny](functions/ny.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [octave_down](functions/octave-down.md) | `method` | `Pitch` | Related |
| [octave_up](functions/octave-up.md) | `method` | `Pitch` | Related |
| [override_sampling_frequency](functions/override-sampling-frequency.md) | `method` | `Sound` | Covered |
| [path_finder](functions/path-finder.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [praat.call](functions/praat-call.md) | `function` | `parselmouth.praat` | Covered |
| [praat.run](functions/praat-run.md) | `function` | `parselmouth.praat` | Not in Vocal Toolkit |
| [praat.run_file](functions/praat-run-file.md) | `function` | `parselmouth.praat` | Covered |
| [pre_emphasize](functions/pre-emphasize.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [read](functions/read.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Not in Vocal Toolkit |
| [resample](functions/resample.md) | `method` | `Sound` | Covered |
| [reverse](functions/reverse.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [sampling_frequency](functions/sampling-frequency.md) | `property` | `Sound` | Related |
| [sampling_period](functions/sampling-period.md) | `property` | `Sound` | Related |
| [save](functions/save.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Not in Vocal Toolkit |
| [save_as_binary_file](functions/save-as-binary-file.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Not in Vocal Toolkit |
| [save_as_headerless_spreadsheet_file](functions/save-as-headerless-spreadsheet-file.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Not in Vocal Toolkit |
| [save_as_matrix_text_file](functions/save-as-matrix-text-file.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [save_as_short_text_file](functions/save-as-short-text-file.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [save_as_text_file](functions/save-as-text-file.md) | `method` | `CC`, `Data`, `Formant`, `Function`, `Harmonicity` | Related |
| [scale](functions/scale.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Related |
| [scale_intensity](functions/scale-intensity.md) | `method` | `Sound` | Covered |
| [scale_peak](functions/scale-peak.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Covered |
| [scale_times_by](functions/scale-times-by.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [scale_times_to](functions/scale-times-to.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [scale_x_by](functions/scale-x-by.md) | `method` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Related |
| [scale_x_to](functions/scale-x-to.md) | `method` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Related |
| [selected](functions/selected.md) | `property` | `Pitch` | Related |
| [selected_array](functions/selected-array.md) | `property` | `Pitch` | Related |
| [set_imaginary_value_in_bin](functions/set-imaginary-value-in-bin.md) | `method` | `Spectrum` | Related |
| [set_real_value_in_bin](functions/set-real-value-in-bin.md) | `method` | `Spectrum` | Related |
| [set_to_zero](functions/set-to-zero.md) | `method` | `Sound` | Related |
| [set_value](functions/set-value.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [set_value_in_bin](functions/set-value-in-bin.md) | `method` | `Spectrum` | Related |
| [shift_times_by](functions/shift-times-by.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [shift_times_to](functions/shift-times-to.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [shift_x_by](functions/shift-x-by.md) | `method` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Related |
| [shift_x_to](functions/shift-x-to.md) | `method` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Related |
| [smooth](functions/smooth.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [start_time](functions/start-time.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [step](functions/step.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [subtract](functions/subtract.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Not in Vocal Toolkit |
| [subtract_linear_fit](functions/subtract-linear-fit.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [subtract_mean](functions/subtract-mean.md) | `method` | `Harmonicity`, `Intensity`, `Sound`, `Vector` | Covered |
| [synthesize_sound](functions/synthesize-sound.md) | `method` | `Spectrogram` | Related |
| [t1](functions/t1.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [t_bins](functions/t-bins.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [t_grid](functions/t-grid.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [time_range](functions/time-range.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [time_step](functions/time-step.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [time_to_frame_number](functions/time-to-frame-number.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [tmax](functions/tmax.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [tmin](functions/tmin.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [to_array](functions/to-array.md) | `method` | `CC`, `MFCC`, `Pitch` | Not in Vocal Toolkit |
| [to_formant_burg](functions/to-formant-burg.md) | `method` | `Sound` | Covered |
| [to_harmonicity](functions/to-harmonicity.md) | `method` | `Sound` | Covered |
| [to_harmonicity_ac](functions/to-harmonicity-ac.md) | `method` | `Sound` | Covered |
| [to_harmonicity_cc](functions/to-harmonicity-cc.md) | `method` | `Sound` | Covered |
| [to_harmonicity_gne](functions/to-harmonicity-gne.md) | `method` | `Sound` | Covered |
| [to_intensity](functions/to-intensity.md) | `method` | `Sound` | Covered |
| [to_matrix](functions/to-matrix.md) | `method` | `CC`, `MFCC`, `Pitch` | Not in Vocal Toolkit |
| [to_matrix_features](functions/to-matrix-features.md) | `method` | `MFCC` | Not in Vocal Toolkit |
| [to_mfcc](functions/to-mfcc.md) | `method` | `Sound` | Not in Vocal Toolkit |
| [to_pitch](functions/to-pitch.md) | `method` | `Sound` | Covered |
| [to_pitch_ac](functions/to-pitch-ac.md) | `method` | `Sound` | Covered |
| [to_pitch_cc](functions/to-pitch-cc.md) | `method` | `Sound` | Covered |
| [to_pitch_shs](functions/to-pitch-shs.md) | `method` | `Sound` | Covered |
| [to_pitch_spinet](functions/to-pitch-spinet.md) | `method` | `Sound` | Covered |
| [to_sound](functions/to-sound.md) | `method` | `MFCC`, `Spectrogram`, `Spectrum` | Covered |
| [to_sound_hum](functions/to-sound-hum.md) | `method` | `Pitch` | Related |
| [to_sound_pulses](functions/to-sound-pulses.md) | `method` | `Pitch` | Related |
| [to_sound_sine](functions/to-sound-sine.md) | `method` | `Pitch` | Related |
| [to_spectrogram](functions/to-spectrogram.md) | `method` | `Sound`, `Spectrum` | Covered |
| [to_spectrum](functions/to-spectrum.md) | `method` | `Sound` | Covered |
| [to_spectrum_slice](functions/to-spectrum-slice.md) | `method` | `Spectrogram` | Not in Vocal Toolkit |
| [to_tgt](functions/to-tgt.md) | `method` | `TextGrid` | Not in Vocal Toolkit |
| [total_duration](functions/total-duration.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Related |
| [trange](functions/trange.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [ts](functions/ts.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [unvoice](functions/unvoice.md) | `method` | `Pitch` | Not in Vocal Toolkit |
| [value](functions/value.md) | `property` | `AmplitudeScaling`, `FormantUnit`, `Interpolation`, `PitchUnit`, `SignalOutsideTimeDomain` | Related |
| [values](functions/values.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `Sound`, `Spectrogram` | Related |
| [with_traceback](functions/with-traceback.md) | `method` | `PraatError`, `PraatFatal`, `PraatWarning` | Related |
| [x1](functions/x1.md) | `property` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [x_bins](functions/x-bins.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [x_grid](functions/x-grid.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [xmax](functions/xmax.md) | `property` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Not in Vocal Toolkit |
| [xmin](functions/xmin.md) | `property` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Not in Vocal Toolkit |
| [xrange](functions/xrange.md) | `property` | `CC`, `Formant`, `Function`, `Harmonicity`, `Intensity` | Not in Vocal Toolkit |
| [xs](functions/xs.md) | `method` | `CC`, `Formant`, `Harmonicity`, `Intensity`, `MFCC` | Not in Vocal Toolkit |
| [y1](functions/y1.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [y_bins](functions/y-bins.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [y_grid](functions/y-grid.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [ymax](functions/ymax.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [ymin](functions/ymin.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [yrange](functions/yrange.md) | `property` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |
| [ys](functions/ys.md) | `method` | `Harmonicity`, `Intensity`, `Matrix`, `SampledXY`, `Sound` | Not in Vocal Toolkit |

## Classes And Enums

| Class or enum | Values |
| --- | --- |
| `AmplitudeScaling` | `INTEGRAL`, `NORMALIZE`, `PEAK_0_99`, `SUM` |
| `CC` |  |
| `Data` |  |
| `Formant` |  |
| `FormantUnit` | `BARK`, `HERTZ` |
| `Function` |  |
| `Harmonicity` |  |
| `Intensity` |  |
| `Interpolation` | `CUBIC`, `LINEAR`, `NEAREST`, `SINC70`, `SINC700` |
| `Matrix` |  |
| `MFCC` |  |
| `Pitch` |  |
| `PitchUnit` | `ERB`, `HERTZ`, `HERTZ_LOGARITHMIC`, `LOG_HERTZ`, `MEL`, `SEMITONES_1`, `SEMITONES_100`, `SEMITONES_200`, `SEMITONES_440` |
| `PraatError` |  |
| `PraatFatal` |  |
| `PraatWarning` |  |
| `Sampled` |  |
| `SampledXY` |  |
| `SignalOutsideTimeDomain` | `SIMILAR`, `ZERO` |
| `Sound` |  |
| `SoundFileFormat` | `AIFC`, `AIFF`, `FLAC`, `KAY`, `NEXT_SUN`, `NIST`, `RAW_16_BE`, `RAW_16_LE`, `RAW_24_BE`, `RAW_24_LE`, `RAW_32_BE`, `RAW_32_LE`, `RAW_8_SIGNED`, `RAW_8_UNSIGNED`, `SESAM`, `WAV`, `WAV_24`, `WAV_32` |
| `SpectralAnalysisWindowShape` | `BARTLETT`, `GAUSSIAN`, `HAMMING`, `HANNING`, `SQUARE`, `WELCH` |
| `Spectrogram` |  |
| `Spectrum` |  |
| `TextGrid` |  |
| `Thing` |  |
| `TimeFrameSampled` |  |
| `TimeFunction` |  |
| `ValueInterpolation` | `CUBIC`, `LINEAR`, `NEAREST`, `SINC70`, `SINC700` |
| `Vector` |  |
| `WindowShape` | `GAUSSIAN1`, `GAUSSIAN2`, `GAUSSIAN3`, `GAUSSIAN4`, `GAUSSIAN5`, `HAMMING`, `HANNING`, `KAISER1`, `KAISER2`, `PARABOLIC`, `RECTANGULAR`, `TRIANGULAR` |
