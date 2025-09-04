SCHEDULE 6
SURVEILLANCE PERFORMANCE REQUIREMENT
RELATED TO ACAS II AND ACAS III
1.
General surveillance requirements. ACAS shall inter-
rogate SSR Mode A/C and Mode S transponders in other aircraft
and detect the transponder replies. ACAS shall measure the range
and relative bearing of responding aircraft. Using these measure-
ments and information conveyed by transponder replies, ACAS
shall estimate the relative positions of each responding aircraft.
ACAS shall include provisions for achieving such position deter-
mination in the presence of ground reflections, interference and
variations in signal strength.
(1) Track establishment probability. ACAS shall gener-
ate an established track, with at least a 0.90 probability that the
track is established 30 s before closest approach, on aircraft
equipped with transponders when all of the following conditions
are satisfied:
(1)
the elevation angles of these aircraft are
within ±10 degrees relative to the ACAS
aircraft pitch plane;
(2)
the magnitudes of these aircraft’s rates of
change of altitude are less than or equal to
51 m/s (10 000 ft/min);
(3)
the transponders and antennas of these
aircraft meet the requirements of Second
ary Surveillance Radar Systemshaving only
Mode A and Mode C capabilities and
Secondary Surveillance Radar Systems
having Mode S capabilities (regulation 25)
contained in these Regulations.;

CIVIL AVIATION
S.R.O. 31
(4)
the closing speeds and directions of these
aircraft, the local density of SSR trans
ponder-equipped aircraft and the number
of other ACAS interrogators in the vicinity
(as determined by monitoringACAS
broadcasts, 1.1.2.4 of the eight schedule)
satisfy the conditions specified in Table 6-1;
and
(5)
the minimum slant range is equal to or greater
than 300 m (1 000 ft).
Table 6-1 ACAS Design assumptions
Note.— Table 6-1 shows the design assumption upon which the
development of ACAS was based. Operational experience and
simulation show that ACAS provides adequate surveillance for
collision avoidance even when the maximum number of other
ACAS within 56 km (30 NM) is somewhat higher than that
shown in Table 6-1. Future ACAS designs will take account of
current and expected ACAS densities.
(a) ACAS shall continue to provide surveillance with no
abrupt degradationintrackestablishmentprobability

CIVIL AVIATION
S.R.O. 31
as any one of the condition bounds defined in sub-
paragraph (1) is exceeded.
(b) ACAS shall not track Mode S aircraft that report that
they are on the ground.
Note.— A Mode S aircraft may report that it is on the ground by
coding in the capability (CA) field in a DF = 11 or DF = 17
transmission or by coding in the vertical status (VS) field in a DF
= 0 transmission. Alternatively, if the aircraft is under Mode S
ground surveillance, ground status may be determined by monitor-
ing the flight status (FS) field in downlink formats DF = 4, 5, 20 or
21 .
(c) ACAS shall achieve the required tracking perform-
ance when the average SSR Mode A/C asynchro-
nous reply rate from transpondersin the vicinity of the
ACAS aircraft is 240 replies per second andwhenthe
peak interrogation rate received by the individual
transponders under surveillance is 500 per second.
Note.— The peak interrogation rate mentioned above includes
interrogations from all sources.
(2)
False track probability. The probability that an estab-
lished Mode A/C track does not correspond in range and
altitude, if reported, to an actual aircraft shall be less than 10-2.
For an established Mode S track this probability shall be less
than 10-6. These limits shall not be exceeded in any traffic
environment.
(3)
RANGE AND BEARING ACCURACY
(a)
Range shall be measured with a resolution of 14.5 m
(1/128 NM) or better.
(b) The errors in the relative bearings of the estimated

CIVIL AVIATION
S.R.O. 31
positions of intruders shall not exceed 10 degrees
rms.
Note.— This accuracy in the relative bearing of intruders is
practicable and sufficient as an aid to the visual acquisition of
potential threats. In addition, such relative bearing information has
been found useful in threat detection, where it can indicate that an
intruder is a threat. However, this accuracy is not sufficient as a
basis for horizontal RAs, nor is it sufficient for reliable predictions
of horizontal miss distance.
2.
INTERFERENCE CONTROL
(1)
Maximum radiated RF power. The effective radiated
power of an ACAS transmission at 0 degree elevation relative
to the longitudinal axis of the aircraft shall not exceed 27 dBW.
(a) Unwanted radiated power. When ACAS is not trans-
mitting an interrogation,theeffectiveradiatedpower
in any direction shall not exceed –70 dBm.
(2)
Interference limiting. Each ACAS interrogator operating
below a pressure-altitude of 5 490 m (18 000 ft) shall control
its interrogation rate or power or both so as to conform with
specific inequalities.
(a) Determination of the number of other ACAS. ACAS
shall count the number of other ACAS II and III
interrogatorsinthevicinity toensurethattheinterfer-
ence limits are met. This count shall be obtained by
monitoringACASbroadcasts(UF=16), Each ACAS
shall monitor such broadcast interrogations to deter-
mine the number of other ACAS within detection
range.
(b) ACAS interference limiting inequalities. ACAS shall
adjust its interrogation rate and interrogation power

CIVIL AVIATION
S.R.O. 31
such that the following three inequalities remain true,
except as provided in Sub-paragraph 2(3).
The variables in these inequalities shall be defined as follows:
it = number of interrogations (Mode A/C and Mode S) trans-
mitted in a 1 s interrogation cycle. This shall include all Mode S
interrogations used by the ACAS functions, including those in
addition to UF = 0 and UF = 16 interrogations, except as
provided in Sub-paragraph 2(3).
Note.— UF = 19 interrogations are included in it as specified
in sub paragraph 8(9)(d) of schedule 4.
i =
index number for Mode A/C and Mode S interrogations,
i = 1, 2,...,it;
á = the minimum of á 1 calculated as 1/4 [nb/nc] subject to the
special conditions given below and á2 calculated as Log10 [na/nb]
/ Log10 25, where nb and nc are defined as the number of operating
ACAS II and ACAS III equipped aircraft (airborne or on the
ground) within 11.2 km (6 NM) and 5.6 km (3 NM) respectively,
of own ACAS (based on ACAS surveillance). ACAS aircraft
operating on the ground or at or below a radio altitude of 610 m
(2 000 ft) AGL shall include both airborne and on-ground ACAS
II and ACAS III aircraft in the value for nb and nc. Otherwise,

CIVIL AVIATION
S.R.O. 31
ACAS shall include only airborne ACASIIand ACASIIIaircraft
in the value for nb and nc. The values of á, á1 and á2 are further
constrained to a minimum of 0.5 and a maximum of 1.0.
In addition;
p(i) = peak power radiated from the antenna in all directions of
the pulse having the largest amplitude in the group of pulses
comprising a single interrogation during the ith interrogation in a
1 s interrogation cycle, W;
m(i) = duration of the mutual suppression interval for own
transponder associated with the ith interrogation in a 1 s
interrogationcycle,s;
B = beam sharpening factor (ratio of 3 dB beam width to
beamwidth resulting from interrogation side-lobe suppression).
For ACAS interrogators that employ transmitter side-lobe
suppression (SLS), the appropriate beamwidth shall be the
extent in azimuth angle of the Mode A/C replies from one
transponder as limited by SLS, averaged over the transponder
population;
Note.— RA and ACAS broadcasts are interrogations.
(3)
Transmissions during RAs. All air-to-air coordination
interrogations shall be transmitted at full power and these
interrogations shall be excluded from the summations of Mode
S interrogations in the left-hand terms of inequalities (1) and (2)

CIVIL AVIATION
S.R.O. 31
in sub paragraph 2(2)(b) for the duration of the RA.
(4)
Transmissions from ACAS units on the ground. When-
ever the ACAS aircraft indicates that it is on the ground,
ACAS interrogations shall be limited by setting the number of
other ACAS II and III aircraft (na) count in the interference
limiting inequalities to a value that is three times the value
obtained based on ACAS broadcasts received with a trans-
ponder receiver threshold of –74 dBm. Whenever Mode A/C
interrogation power is reduced because of interference limiting,
the Mode A/C interrogation power in the forward beam shall
be reduced first until the forward sequence matches the right
and left sequences. The forward, right and left interrogation
powers shall then sequentially be reduced until they match the
rear interrogation power. Further reduction of Mode A/C
power shall be accomplished by sequentially reducing the
forward, side and rear interrogation powers.
(5)
Transmissions from ACAS units above 5 490 m (18 000
ft) altitude. Each ACAS interrogator operating above a pres-
sure-altitude of 5 490 m (18 000 ft) shall control its interroga-
tion rate or power or both such that inequalities (1) and (3) in
sub paragraph 2(2)(b) remain true when na and á are equal to
1, except as provided in Sub-paragraph 2(3).
