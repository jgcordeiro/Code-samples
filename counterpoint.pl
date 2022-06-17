:- use_module(library(clpfd)).
:- use_module(library(lists)).

translate(Note, Index) :- translate(Note, 3, Index).
translate([Number, Letter, Solfege, Interval], Octave, Index) :-
	member([Number, Letter, Solfege, Interval], [
	[0,  c,  do,  p1],
	[1,  cs, di,  a1],
	[1,  db, ra,  min2],
	[2,  d,  re,  maj2],
	[3,  ds, ri,  a2],
	[3,  eb, me,  min3],
	[4,  e,  mi,  maj3],
	[5,  f,  fa,  p4],
	[6,  fs, fi,  a4],
	[6,  gb, se,  d5],
	[7,  g,  sol, p5],
	[8,  gs, si,  a5],
	[8,  ab, le,  min6],
	[9,  a,  la,  maj6],
	[10, as, li,  a6],
	[10, bb, te,  min7],
	[11, b,  ti,  maj7]
	]),
	Index is Number + (12 * Octave).

counterpoint(CF, CP) :-
	counterpoint(CF, CP, 0).
counterpoint(CF, CP, Mode) :-
	length(CF, L),
	length(CP, L),

	% CF should be well formed
	cantus_firmus(CF, Climax_CF, _, Mode),

	% CP follows similar rules to the CF
	cantus(CP, Climax, _, Mode),

	get_intervals(CF, CP, Intervals),
	get_progressions(CF, CFProg),
	get_progressions(CP, CPProg),

	append([FirstInterval|MiddleIntervals], [LastInterval], Intervals),

	% No intervals greater than a 12th
	Intervals ins -19..19,

	% Begin on do, or on the above sol
	FirstInterval in {12, 7, 0, -12},

	% End on do
	LastInterval in {-12, 0, 12},

	% Intervals must be P1, m3, M3, P5, m6, M6, P8, m10, M10, or P12
	consonant(Intervals),

	% No voice crossing
	no_voice_crossing(Intervals),

	% Do not move into a perfect consonance by similar motion
	no_similar_to_perfect(CF, CP, Intervals),

	% No parallel perfects (P5 = P12)
	no_parallel_perfects(Intervals),

	% At most one repeat
	no_multiple_repeats(CP),

	% No voice overlap
	no_voice_overlap(CF, CP),

	% End with contrary motion
	append(_, [LastCFProg], CFProg),
	append(_, [LastCPProg], CPProg),
	LastCFProg * LastCPProg #< 0,

	% Do not use more than three of the same consonance in a row
	no_quadruple_consonance(Intervals),

	% No simultaneous leaps
	no_simultaneous_leaps(CF, CP),

	% No unisons in the middle
	no_unisons(MiddleIntervals),

	% Different climaxes for CF and CP
	different_climaxes(CF, CP, Climax_CF, Climax),

	% Avoid static

	write("").

counterpoint_shave(CF, CP, _) :-
	cantus_firmus_shave(CF),
	cantus_shave(CP),

	% No repeats
	no_repeats_shave(CP),

	% Variety of intervals

	% Variety of types of motion

	% Prefer contrary motion
	contrary_motion_shave(CF, CP),

	% Avoid two perfect chords in a row
	no_adjacent_perfects_shave(CP),

	% Avoid combining similar motion with leaps
	no_similar_leaps_shave(CF, CP),

	% No gaps
	%no_gaps_shave(CP, Minimum..Climax),
	%TODO

	write("").

get_intervals([], [], []).
get_intervals([X|CF], [Y|CP], [Z|Intervals]) :-
	Y - X #= Z,
	get_intervals(CF, CP, Intervals).

cantus_firmus(CF, Climax, Minimum, Mode) :-
	cantus(CF, Climax, Minimum, Mode),

	% Begin and end on do
	append([Do|_], [Do], CF),

	% Range of no more than a tenth
	Climax - Minimum #=< 16,

	write("").

cantus_firmus_shave(CF) :-
	cantus_shave(CF),

	get_progressions(CF, I),

	% Mostly stepwise motion
	step_shave(I),

	% Range less than an octave
	octave_range_shave(CF),

	write("").

cantus([_], _, _, _).
cantus(C, Climax, Minimum, Mode) :-
	C ins 0..87,
	append(_, [Do], C),

	% Stick to the major or harmonic minor scale
	diatonic_scale(C, Do, Mode),

	% Approach final tonic by step
	% All note-to-note progressions are melodic consonances
	get_progressions(C, I),
	consonant_melody(I),

	% Single climax
	unique_climax(C, Climax),
	unique_climax_min(C, Minimum),

	% Large leaps (4th or larger) are followed by a contrary step
	bounded_large_leaps(I),

	% No more than two leaps in a row
	no_triple_leaps(I),

	% No consecutive leaps in the same direction, except when outlining a major triad
	% Also, leaps should be compensated in the opposite direction
	compensate_leaps(I),

	% In minor, the leading tone only appears in the penultimate bar; the raised submediant is only used when progressing to that leading tone
	
	write("").

leading_tone_to_tonic_shave([_], _).
leading_tone_to_tonic_shave([A,B|C], Do) :-
	(	((A - Do) mod 12 < 11)	->	true
	;	((A - Do) mod 12 #= 11),
	(	((B - Do) mod 12 =:= 0)	->	true
	;	((B - Do) mod 12 #> 0)
	)
	),
	leading_tone_to_tonic_shave([B|C], Do).

cantus_shave(C) :-
	append(_, [Do], C),
	get_progressions(C, I),

	% The leading tone progresses to the tonic
	leading_tone_to_tonic_shave(C, Do),

	% Prefer double-bounded leaps
	prebounded_leaps_shave(I),

	% Smooth shape from beginning to climax to ending

	% No repetition of motives

	write("").

diatonic_scale([], _, _).
diatonic_scale([X|C], Do, Mode) :-
	Note #= (X - Do) mod 12,
		Note in {0, 2, 5, 7, 11}
	#\/ Note #=  4 - Mode  % M3 or m3
	#\/ Note #=  9 - Mode  % M6 or m6
	#\/ Note #= 11 - Mode, % m7
	diatonic_scale(C, Do, Mode).

bounded_large_leaps([_]).
bounded_large_leaps([X,Y|I]) :-
		X in -4..4
	#\/	(X #>  4 #/\ Y in {-1, -2})
	#\/ (X #< -4 #/\ Y in { 1,  2}),
	bounded_large_leaps([Y|I]).

prebounded_leaps_shave([_]).
prebounded_leaps_shave([A,B|I]) :-
	(	(B >= -2, B =< 2)		->  true
	;	(B < -2, A > 0, A =< 2)	->  true
	;   (B > 2, A < 0, A >= -2)	->  true
	;	(B #< -2 #/\ (A #=< 0 #\/ A #>  2))
	#\/ (B #>  2 #/\ (A #>= 0 #\/ A #< -2))
	),
	prebounded_leaps_shave([B|I]).

no_adjacent_perfects_shave([_]).
no_adjacent_perfects_shave([A,B|C]) :-
	(	\+ perfect_interval(A)  ->  true
	;	\+ perfect_interval(B)  ->  true
	;	perfect_interval_reif(A,1) #/\ perfect_interval_reif(B,1)
	),
	no_adjacent_perfects_shave([B|C]).

contrary_motion_shave([_],[_]).
contrary_motion_shave([F1,F2|CF], [P1,P2|CP]) :-
	(	motion_type(F1, F2, P1, P2, contrary)  ->  true
	;	motion_type(F1, F2, P1, P2, oblique)   ->  true
	;	(F1 - F2) * (P1 - P2) #> 0
	),
	contrary_motion_shave([F2|CF],[P2|CP]).

no_similar_leaps_shave([_], [_]).
no_similar_leaps_shave([F1,F2|CF], [P1,P2|CP]) :-
	motion_type(F1, F2, P1, P2, Type),
	(	Type = contrary  ->  true
	;	Type = oblique   ->  true
	;	(F1 - F2) * (P1 - P2) #> 0
	% TODO
	),
	no_similar_leaps_shave([F2|CF],[P2|CP]).

motion_type(F1, F2, P1, P2, Type) :-
	F1 - F2 = F,
	P1 - P2 = P,
	F * P = B,
	(	B < 0  ->  Type = contrary
	;	B = 0  ->  Type = oblique
	;   B > 0  ->  (
		F = P  ->  Type = parallel
	;	F \= P ->  Type = similar
	)).

no_triple_leaps([_]).
no_triple_leaps([_,_]).
no_triple_leaps([X,Y,Z|I]) :-
		(X in {-2, -1, 1, 2})
	#\/ (Y in {-2, -1, 1, 2})
	#\/ (Z in {-2, -1, 1, 2}),
	no_triple_leaps([Y,Z|I]).

no_quadruple_consonance([_]).
no_quadruple_consonance([_,_]).
no_quadruple_consonance([_,_,_]).
no_quadruple_consonance([W,X,Y,Z|I]) :-
	(W #\= X) #\/ (X #\= Y) #\/ (Y #\= Z),
	no_quadruple_consonance([X,Y,Z|I]).

is_step(I) :- I in {-2, -1, 1, 2}.

get_progressions([_], []).
get_progressions([X,Y|C], [Progress|I]) :-
	Progress #= Y - X,
	get_progressions([Y|C], I).

compensate_leaps([_]).
compensate_leaps([X,Y|I]) :-
		(X in -4..4)
	#\/ (Y in {-2, -1, 1, 2} #/\ (X * Y #< 0)),
	compensate_leaps([Y|I]).

consonant([]).
consonant([I|Intervals]) :-
	I in {-19, -16, -15, -12, -9, -8, -7, -4, -3,
		0, 19,  16,  15,  12,  9,  8,  7,  4,  3},
	consonant(Intervals).

consonant_melody([I]) :- is_step(I).
consonant_melody([I|Intervals]) :-
	I in {-12, -9, -8, -7, -5, -4, -3, -2, -1,
		   12,  9,  8,  7,  5,  4,  3,  2,  1},
	consonant_melody(Intervals).

no_voice_crossing([_]).
no_voice_crossing([I,J|Intervals]) :-
	I * J #>= 0,
	no_voice_crossing([I|Intervals]).

different_climaxes([], [], _, _).
different_climaxes([X|CF], [Y|CP], Climax_CF, Climax_CP) :-
	(X #\= Climax_CF) #\/ (Y #\= Climax_CP),
	different_climaxes(CF, CP, Climax_CF, Climax_CP).

perfect_interval(I) :-
	member(I, {-19, -12, -7, -5, 0, 5, 7, 12, 19}).

perfect_interval_reif(I,B) :-
	(I in {-19, -12, -7, -5, 0, 5, 7, 12, 19}) #<==> B.

no_similar_to_perfect([_], [_], [_]).
no_similar_to_perfect([F1,F2|CF], [P1,P2|CP], [_,I2|Intervals]) :-
	perfect_interval_reif(I2, B1),
	((F2 - F1) * (P2 - P1) #> 0) #<==> B2,
	#\ (B1 #/\ B2),
	no_similar_to_perfect([F2|CF], [P2|CP], [I2|Intervals]).

no_parallel_perfects([_]).
no_parallel_perfects([I,J|Intervals]) :-
	perfect_interval_reif(I, B1),
	((I mod 12) #= (J mod 12)) #<==> B2,
	#\ (B1 #/\ B2),
	no_parallel_perfects([J|Intervals]).

no_voice_overlap([_], [_]).
no_voice_overlap([F1,F2|CF], [P1,P2|CP]) :-
	((F1 - P1) * (F2 - P1)) #>= 0,
	((P1 - F1) * (P2 - F1)) #>= 0,
	no_voice_overlap([F2|CF], [P2|CP]).

no_simultaneous_leaps([_], [_]).
no_simultaneous_leaps([F1,F2|CF], [P1,P2|CP]) :-
	(abs(F1 - F2) #< 4) #\/	(abs(P1 - P2) #< 4),
	no_simultaneous_leaps([F2|CF], [P2|CP]).

no_unisons([]).
no_unisons([I|Intervals]) :-
	I #> 0,
	no_unisons(Intervals).

no_multiple_repeats(CP) :-
	no_multiple_repeats(CP, 1).
no_multiple_repeats([_], 1).
no_multiple_repeats([X,Y|CP], B) :-
		(X  #= Y #/\ B0 #= 0 #/\ B #= 1)
	#\/ (X #\= Y #/\ B0 #= 1),
	no_multiple_repeats([Y|CP], B0).

no_repeats_shave([_]).
no_repeats_shave([A,B|CP]) :-
	(	A \= B  ->  true
	;	A #= B
	),
	no_repeats_shave([B|CP]).

unique_climax(L, C) :-
	unique_climax(L, C, 1).
unique_climax([], _, 1).
unique_climax([X|L], C, B) :-
		(C #= X #/\ B0 #= 0 #/\ C0 #= C)
	#\/ (C #> X #/\ B0 #= B #/\ C0 #= C)
	#\/ (C #< X #/\ B0 #= 1 #/\ C0 #= X),
	unique_climax(L, C0, B0).

no_gaps_shave(_, []).
no_gaps_shave(C, [V|Vs]) :-
	(	member(V, C)  ->  true
	;	#\ V in C
	),
	no_gaps_shave(C, Vs).

unique_climax_min(L, C) :-
	unique_climax_min(L, C, 1).
unique_climax_min([C], C, 1).
unique_climax_min([X|L], C, B) :-
		(C #= X #/\ B0 #= 0 #/\ C0 #= C)
	#\/ (C #< X #/\ B0 #= B #/\ C0 #= C)
	#\/ (C #> X #/\ B0 #= 1 #/\ C0 #= X),
	unique_climax(L, C0, B0).

step_shave([_]).
step_shave([A,B|I]) :-
	(	member(A, [-2, -1, 1, 2])  ->  true
	;	#\ A in -2..2,
	(	member(A, [-4, -3, 3, 4]), B = sign(A)*7 - A  ->  true
	;	(#\ A in -4..4)
	#\/ (A #< 0 #/\ B #\= -7 - A)
	#\/ (A #> 0 #/\ B #\=  7 - A)
	)
	),
	step_shave([B|I]).

octave_range_shave(CF) :-
	member(X, CF),
	octave_range_shave_help(X, CF).
octave_range_shave_help(_, []).
octave_range_shave_help(X, [Y|CF]) :-
	(   X + 12 > Y  ->  true
	;   X + 12 #=< Y
	),
	octave_range_shave_help(X, CF).

write_counterpoint(CF, CP) :-
	write_counterpoint(CF, CP, _).
write_counterpoint(CF, CP, Mode) :-
	counterpoint(CF, CP, Mode),
	%counterpoint_shave(CF, CP, Mode),
	%TODO
	append(CF, CP, Output),
	labeling([ff, bisect], Output).