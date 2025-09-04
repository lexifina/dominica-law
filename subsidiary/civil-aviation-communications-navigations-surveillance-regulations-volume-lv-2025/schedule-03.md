SCHEDULE 3
(Regulation 20)
TECHNICAL CHARACTERISTICS OF TRANSPONDERS
WITH MODE A AND MODE C CAPABILITIES ONLY
1. The transponder shall reply (not less than 90 per cent
triggering) when all of the following conditions have been met—
(1) the received amplitude of P3 is in excess of a level 1 dB
belowthereceivedamplitudeofP1butnogreaterthan3dBabove
the received amplitude of P1;
(2) eithernopulseisreceivedintheinterval1.3microsec-
onds to 2.7 microseconds after P1, or P1 exceeds by more than 9
dB any pulse received in this interval;
(3) the received amplitude of a proper interrogation is
more than 10 dB above the received amplitude of random pulses
where the latter are not recognised by the transponder as P1, P2
or P3.
Reply.

CIVIL AVIATION
S.R.O. 31
2. (1)to interrogations when the interval between pulses P1
and P3 differs from those specified in regulation 17 by more than
plus or minus 1.0 microsecond;
(2) upon receipt of any single pulse which has no ampli-
tude variations approximating a normal interrogation condition.
3. After recognition of a proper interrogation, the trans-
ponder shall not reply to any other interrogation, at least for the
duration of the reply pulse train. This dead time shall end no later
than 125 microseconds after the transmission of the last reply
pulse of the group.
4. Note. — This characteristic is used to prevent replies to
interrogations received via the side lobes of the interrogator
antenna, and toprevent Mode A/C transponders from replying to
Mode S interrogations.
(1) The transponder shall be suppressed when the re-
ceived amplitude of P2 is equal to, or in excess of, the received
amplitude of P1 and spaced 2.0 plus or minus 0.15 microseconds.
The detection of P3 is not required as a prerequisite for initiation
of suppression action.
(2) The transponder suppression shall be for a period of
35 plus or minus 10 microseconds.
(3) The suppression shall be capable of being reinitiated
for the full duration within 2 microseconds after the end of any
suppressionperiod.
(4) Suppression in presence of S1 pulse
The transponder
shall not reply under
the following
conditions:
Dead time.
Suppression.

CIVIL AVIATION
S.R.O. 31
Note.— The S1 pulse is used in a technique employed by ACAS
known as “whisper-shout” to facilitate ACAS surveillance of
Mode A/C aircraft in higher traffic densities. The whisper-shout
technique is explainedintheAirborneCollisionAvoidanceSystem
(ACAS) Manual (Doc 9863).
WhenanS1pulseisdetected2.0plusorminus0.15microseconds
before the P1 of a Mode A or Mode C interrogation:
(a) with S1 and P1 above MTL, the transponder shall
be suppressed as specified in sub paragraph (1);
(b) with P1 at MTL and S1at MTL, the transponder
shallbesuppressed andshallreplytonomorethan
10 per cent of Mode A/C interrogations;
(c) with P1 at MTL and S1 at MTL -3 dB, the
transponder shall reply to Mode A/C interroga-
tions at least 70 per cent of the time; and
(d) with P1 at MTL and S1 at MTL -6 dB, the
transponder shall reply to Mode A/C interroga-
tions at least 90 per cent of the time.
Note 1.— The suppression action is because of the detection of
S1 and P1 and does not require detection of a P2 or P3 pulse.
Note 2.— S1 has a lower amplitude than P1. Certain ACAS use
this mechanism to improve target detection
Note 3.— These requirements also apply to a Mode A/C only
capable transponder when an S1 precedes an intermode interro-
gation
5. (1)The minimum triggering level of the transponder shall be
such that replies are generated to at least 90 per cent of the
interrogationsignals when:
Receiver sensitivity and
dynamic range.

CIVIL AVIATION
S.R.O. 31
(a) the two pulses P1 and P3 constituting an interro-
gation are of equal amplitude and P2 is not
detected; and
(b) the amplitudeofthesesignals isnominally71dB
below 1 mW, with limits between 69 dB and 77
dB below 1 mW.
(2) Thereplyandsuppressioncharacteristicsshallapply
over areceivedamplitudeofP1betweenminimumtriggeringlevel
and 50 dB above that level.
(3) The variation of the minimum triggering level be-
tween modes shall not exceed 1 dB for nominal pulse spacing and
pulsewidths.
6. Signals of received amplitude between minimum trigger-
ing level and 6 dB above this level, and of duration less than 0.3
microsecond, shall not cause the transponder to initiate reply or
suppression action. With the exception of single pulses with
amplitude variations approximating an interrogation, any single
pulse of duration more than 1.5 microseconds shall not cause the
transponder to initiate reply orsuppressionaction overthesignal
amplitude range of minimum triggering level (MTL) to 50 dB
above that level.
7. Thetranspondershallcontainanecho suppressionfacility
designed to permit normal operation in the presence of echoes of
signals-in-space. The provision of this facility shall be compatible
with the requirements for suppression of side lobes given in sub-
paragraph 4 (1).
(1) Desensitisation. Upon receipt of any pulse more
than 0.7 microsecond in duration, the receiver shall be desensi-
tised by an amount that is within at least 9 dB of the amplitude of
the desensitising pulse but shall at no time exceed the amplitude
ofthedesensitizingpulse,withthe exception of possible overshoot
Pulse duration
discrimination.
Echo suppression and
recovery.

CIVIL AVIATION
S.R.O. 31
during the first microsecond following the desensitising pulse.
Note.— Single pulses of duration less than 0.7 microsecond are
not required to cause the specified desensitisation nor to cause
desensitisation of duration greater than permitted by sub para-
graph 7(1) and sub paragraph 7 (2).
(2) Recovery. Following desensitization, the receiver
shall recover sensitivity (within 3 dB of minimum triggering level)
within 15 microseconds after reception of a desensitizing pulse
having a signal strength up to 50 dB above minimum triggering
level. Recovery shall be at an average rate not exceeding 4.0 dB
per microsecond.
8. In the absence of valid interrogation signals, Mode A/C
transponders shall not generate more than 30 unwanted Mode A
or Mode C replies per second as integrated over an interval
equivalent to at least 300 random triggers, or 30 seconds, which-
ever is less. This random triggering rate shall not be exceeded
when all possible interfering equipment installed in the same
aircraft are operating at maximum interference levels.
Random triggering rate in the presence of low-level in-band
continuous wave (CW) interference. The total random trigger
rate on all Mode A and/or Mode C replies shall not be greater than
10 reply pulse groups or suppressions per second, averaged over
a period of 30 seconds, when operated in the presence of non-
coherent CW interference at a frequency of 1 030 ±0.2 MHz and
a signal level of –60 dBm or less.
9. (1)All transponders shall be capable of continuously gen-
erating at least 500 replies per second for a 15-pulse coded reply.
Transponder installations used solely below 4 500 m (15 000 ft), or
below a lesser altitude established by the appropriate authority or
by regional air navigation agreement, and in aircraft with a
maximum cruising true airspeed not exceeding 175 kt (324 km/h)
shall be capableofgeneratingatleast100015-pulsecodedreplies
per second for a duration of 100 milliseconds. Transponder
Random triggering rate.
Reply Rate.

CIVIL AVIATION
S.R.O. 31
installationsoperated above4500m(15000ft.)orinaircraftwith
amaximumcruisingtrue airspeedinexcessof175kt(324km/h),
shallbecapableofgenerating at least 1 200 15-pulse coded replies
per second for a duration of 100 milliseconds.
Note 1.— A 15-pulse reply includes 2 framing pulses, 12
information pulses, and the SPI pulse.
Note 2.— The reply rate requirement of 500 replies per second
establishes the minimum continuous reply rate capability of the
transponder. As per the altitude and speed criteria above, the 100
or 120 replies in a 100-millisecond interval defines the peak
capability of the transponder. The transponder must be capable of
replying to this short-term burst rate, eventhough the transponder
may not be capable of sustaining this rate. If the transponder is
subjected to interrogation rates beyond its reply rate capability, the
reply rate limit control of sub paragraph 9(2) below acts to
gracefully desensitize the transponder in a manner that favours
closer interrogators. Desensitization eliminates weaker interro-
gation signals.
(2) Reply rate limit control. To protect the system from
the effects of transponder over-interrogation by preventing re-
sponse to weaker signals when a predetermined reply rate has
been reached, a sensitivity reduction type reply limit control shall
be incorporated in the equipment. The range of this control shall
permit adjustment, as a minimum, to any value between 500 and
2 000 replies per second, or to the maximumreplyrate capability
iflessthan2000replies per second, without regard to the number
of pulses in each reply. Sensitivityreductioninexcessof3dBshall
not take effect until 90 per cent of the selected value is exceeded.
Sensitivity reduction shall be at least 30 dB for rates in excess of
150 per cent of the selected value.
10. The time delay between the arrival, at the transponder
receiver, of the leading edge of P3 and the transmission of the
leading edge of the first pulse of the reply shall be 3 plus or minus
Reply delay and jitter.

CIVIL AVIATION
S.R.O. 31
0.5 microseconds. The total jitter of the reply pulse code group,
with respect to P3, shall not exceed 0.1 microsecond for receiver
input levels between 3 dB and 50 dB above minimum triggering
level. Delay variations between modes on which the transponder
is capable of replying shall not exceed 0.2 microsecond.
11. The peak pulse power available at the antenna end of the
transmission lineofthetranspondershallbeatleast21dBandnot
more than 27 dB above 1 W, except that for transponder
installations used solely below 4 500 m (15 000 ft), or below a lesser
altitude established by the appropriate authority or by regional air
navigation agreement, a peak pulse power available at the antenna
end of the transmission line of the transponder of at least 18.5 dB
and not more than 27 dB above 1 W shall be permitted.
Note.— An extended squitter non-transponder device on an
aerodrome surface vehicle may operate with a lower minimum
power output as specified insub paragraph 1(1)(b) of schedule 15.
The peak pulse power specified in sub-paragraph (1) shall be
maintained over a range of replies fromcode 0000 at a rate of 400
replies per second to a maximum pulse content at a rate of 1 200
replies per second or a maximum value below 1 200 replies per
second of which the transponder is capable.
12. (1) Identification. The reply to a Mode A interrogation
shall consistofthetwoframingpulsesspecifiedinregulation19(1)
together with the information pulses (Mode A code) specified in
regulation 19(2) and (3).
Note.— The Mode A code designation is a sequence of four digits
in accordance with regulation 19(11).
(a) The Mode A code shall be manually selected from
the 4 096 codes available.
Transponder power
output and duty cycle.
 Reply codes.

CIVIL AVIATION
S.R.O. 31
(2) Pressure-altitude transmission. The reply to Mode
C interrogation shall consist of the two framing pulses specified in
regulation 19(1). Where digitised pressure-altitude information is
available,theinformationpulsesspecifiedinregulation19(2)and
(3) shall also be transmitted.
(3) Transpondersshallbeprovidedwithmeanstoremove
the information pulses but to retain the framing pulses when the
provision of in sub-paragraph (6) below is not complied with in
reply to Mode C interrogation.
(4) Theinformationpulses shall be automatically selected
by an analog-to-digital converter connected to a pressure-altitude
data source in the aircraft referenced to the standard pressure
setting of 1,013.25 hectopascals.
Note.— The pressure setting of 1 013.25 hectopascals is equal
to 29.92 inches of mercury.
(5) Pressure-altitude shall be reported in 100-ft incre-
ments by selection of pulses as shown in the table 2 of this
Schedule.
(6) The digitizer code selected shall correspond to within
plus or minus 38.1 m (125 ft), on a 95 per cent probability basis,
with the pressure-altitude information (referenced to the standard
pressure setting of 1,013.25 hectopascals), used on board the
aircraft to adhere to the assigned flight profile.
13.When required,thispulseshallbetransmittedwithMode
Areplies,asspecified in regulation 19(4), for a period of between
15 and 30 seconds.
14. (1) The transponder antenna system, when installed on
an aircraft, shall have a radiation pattern which is essentially
omnidirectional in the horizontal plane.
Transmission of the
special position
identification (SPI)
pulse.
Antenna.

CIVIL AVIATION
S.R.O. 31
(2) The vertical radiation pattern shall be nominally equiva-
lent to that of a quarter-wave monopole on a ground plane.
