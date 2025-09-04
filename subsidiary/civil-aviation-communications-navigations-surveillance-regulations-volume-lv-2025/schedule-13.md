SCHEDULE 13
ACAS USE OF EXTENDED SQUITTER
An ACAS equipped to receive extended squitter airborne position
messages for passive surveillance of nonthreatening intruders
shall utilize this passive position information in the manner speci-
fied in Paragraph 1. of this Schedule.
1.
ACAS Hybrid surveillance using extended squitter
position data
(1)
PASSIVE SURVEILLANCE
(a)
Validation. To validate the position of an intruder
reported by extendedsquitter,ACASshalldetermine
the relative range and relative bearing as computed
from the position and geographical heading of own
aircraft and the intruder’s position as reported in the
extended squitter. This derived range and relative
bearing andthealtitudereportedinthesquittershallbe
compared to the range, relative bearing and altitude
determined by active ACAS interrogation of the
aircraft. Differences between the derived and meas-
ured range and relative bearing and the squitter and
reply altitude shall be computed and used in tests to
determine whethertheextendedsquitterdataisvalid.
Ifthesetestsaresatisfiedthe passivepositionshallbe
considered to be validated and the track shall be
maintained on passive data unless it is a near threat as
described in sub-paragraph 1.(1)(a)(2). If any of
these validation tests fail, active surveillance shall be
used to track the intruder.
Note.— Suitable tests for validating extended squitter data infor-
mation for the purposes of ACAS hybrid surveillance can be found
in RTCA/DO-300.

CIVIL AVIATION
S.R.O. 31
(b) Supplementary active interrogations. In order to en-
sure that an intruder’s track is updated at least as
frequently as reuired in the absence of extended
squitter data, each time a track is updated using
squitter information the time at which an active
interrogation would next be required shall be calcu-
lated. An active interrogation shall be made at that
time if a further squitter has not been received before
the interrogation is due.
(2)
Near threat. An intruder shall be tracked under active
surveillance if it is a near threat, as determined by separate
tests on the range and altitude of the aircraft. These tests shall
be such that an intruder is considered a near threat before it
becomes a potential threat, and thus triggers a traffic advisory
as described in Regulation 31. These tests shall be performed
once per second. All near threats, potential threats and threats
shall be tracked using active surveillance.
Note.— Suitable tests for determining that an intruder is a near
threat can be found in RTCA/DO-300.
(3)
Revalidation and monitoring. If an aircraft is being
tracked using passive surveillance, periodic active interroga-
tions shall be performed to validate and monitor the extended
squitter data as required in sub- paragraph 1.(1)(a). The default
rates of revalidation shall be once per minute for a non-threat
and once per 10 seconds for a near threat. The tests required
in Sub-paragraph 1.(1)(a) shall be performed for each interro-
gation, and active surveillance shall be used to track the in-
truder if these revalidation tests fail.
(4)
Full active surveillance. If the following condition is met
for a track being updated via passive surveillance data:

CIVIL AVIATION
S.R.O. 31
the aircraft shall be declared an active track and shall be updated
on active range measurements once per second for as long as the
above condition is met.
(a) All near threats, potential threats and threats shall be
tracked using active surveillance.
(b) A track under active surveillance shall transition to
passive surveillance if it is neither a near threat,
potential threat nor a threat. The tests used to deter-
mine it is no longer a near threat shall be similar to
those used in sub-paragraph (2) but with larger
thresholdsinordertohavehysteresiswhichprevents
the possibility of frequent transitions between active
and passive surveillance
Note.—Suitabletestsfordeterminingthatanintruderisno longer
a near threat can be found in RTCA/DO-300.
2.
ACAS operation with an improved receiver MTL
Note.—Applicationsofextendedsquitterthatareindependentof
ACASmightbeimplemented(forconvenience)usingthe ACAS

CIVIL AVIATION
S.R.O. 31
receiver. The use of an improved receiver minimum
triggering level (MTL) will make it possible to receive ex-
tended squitters from ranges of up to 60 NM and beyond in
support of such applications.
(1) An ACAS operating with a receiver having a MTL
more sensitive than –74 dBm shall implement the capabilities
specified in the following paragraphs.
(2) Dual minimum triggering levels. The ACAS receiver
shall be capable of setting an indication for each squitter reception
as to whether the reply would have been detected by an ACAS
operating with a conventional MTL (–74 dBm). Squitter recep-
tions received at the conventional MTL shall be passed to the
ACAS surveillance function for further processing. Squitter
receptions that do not meet this condition shall not be passed to the
ACAS surveillance function.
Note 1.— Extended squitters containing position report informa-
tion will be disseminated for display in connection with an
extendedsquitterapplication.
Note 2.— Use of the conventional MTL for the ACAS surveil-
lance function preserves the current operation of ACAS surveil-
lance when operating with a receiver with an improved MTL.
(3) Dual or re-triggerable reply processor. The ACAS
Mode S reply processing function shall:
(a) use separate reply processors for Mode S reply
formats received at or above the conventional MTL and a
separate reply processor for Mode S reply formats received
below the conventional MTL; or,
(b) use a Mode S reply processor that will re-trigger if it
detects a Mode S preamble that is 2 to 3 dB stronger than the
reply that is currently being processed.

CIVIL AVIATION
S.R.O. 31
Note.— Care must be taken to ensure that low-level squitters (i.e. those below
the conventional MTL) do not interfere with the processing of acquisition squitters
for ACAS. This could happen if the low-level squitter is allowed to capture the
reply processor. This can be prevented by using a separate reply processor for
each function, or by requiring the reply processor to be re-triggered by a higher
level squitter.
