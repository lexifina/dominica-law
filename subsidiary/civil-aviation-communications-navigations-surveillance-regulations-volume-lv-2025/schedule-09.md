SCHEDULE 9
Regulation 37
ACAS II AND ACAS III PROTOCOLS
1.
SURVEILLANCE PROTOCOLS
(1)
Surveillance of Mode A/C Transponders
(a)
ACAS shall use the Mode C-only all-call
interrogation for surveillance of aircraft equipped with Mode
A/C transponders.
(b)
Using a sequence of interrogations with
increasing power, surveillance interrogations shall be preceded
by an S1-pulse to reduce interference and improve Mode A/C
target detection.
(2)
Surveillance of Mode S Transponders
(a)
Detection. ACAS shall monitor 1 090 MHz
for Mode S acquisition squitters (DF = 11). ACAS shall detect
the presence and determine the address of Mode S-equipped
aircraft using their Mode S acquisition squitters (DF = 11) or
extended squitters (DF = 17).
Note 1.— It is acceptable to acquire individual aircraft using
eitheracquisitionorextendedsquitters(DF=11orDF=17), and

CIVIL AVIATION
S.R.O. 31
to monitor for both squitters. However, ACAS must monitor for
acquisition squitters because, at any time, not all aircraft will
transmit the extended squitter.
Note 2.— If, in the future, it becomes permitted for aircraft not
to transmit the acquisition squitter, relying instead on continual
transmission of the extended squitter, it would become essential
for all ACAS units to monitor for both the acquisition and the
extended squitters.
(b) Surveillance interrogations. On first receipt of a 24-
bit aircraftaddress froman aircraftthat is determined
to be withith ereliable surveillance range of ACAS
based on reception reliability and that is within an
altitude band 3 050 m (10 000 ft) above and below
own aircraft, ACAS shall transmit a
short air-air
interrogation (UF = 0) for range acquisition. Surveil-
lance interrogationsshall be transmitted at least once
every five cycles when this altitude condition is
satisfied. Surveillance interrogations shall be trans-
mitted each cycle if the range
of the detected air-
craftislessthan5.6km(3NM)orthecalculatedtime
to closest approach is less than 60 s, assuming that
both the detected and own aircraft proceed from their
current positions with unaccelerated motion and that
the range at closest approach equals 5.6 km (3 NM).
Surveillance interrogations shall be suspended for a
period of five cycles if:
·
a reply was successfully received.
·
own aircraft and intruder aircraft are operating
below a pressure-altitude of 5 490 m (18 000 ft);
and
·
the range of the detected aircraft is greater than
5.6 km (3 NM) and the calculated time to closest
approach exceeds 60 seconds, assuming that both
the detected and own aircraft proceed from their

CIVIL AVIATION
S.R.O. 31
current positions with unaccelerated motion and
that the range at closest approach equals 5.6 km
(3 NM).
(i) Rangeacquisition interrogations.ACASshalluse
the short air-air surveillance format (UF = 0) for
rangeacquisition. ACAS shall setAQ = 1 and RL
= 0 in an acquisition interrogation.
Note 1.— Setting AQ = 1 results in a reply with bit 14 of the RI
field equal to 1 and serves as an aid in distinguishing the reply to
own interrogation from replies elicited from other ACAS units
Note 2.— In the acquisition interrogation RL is set to 0 to
command a short acquisition reply (DF = 0).
(ii) Tracking interrogations. ACAS shall use the
short air-airsurveillance format(UF = 0) with RL
= 0 and AQ = 0 for tracking interrogations.
(c) Surveillance replies. These protocols are described in
3.(1) of Schedule 11
(d) ACAS broadcast. An ACAS broadcast shall be
madenominally every 8 to 10 s at full power from the
top antenna. Installations using directional antennas
shall operate such that complete circular coverage is
nominally every 8 to 10 s.
Note.— A broadcast causes other Mode S transponders to
accept the interrogation without replying and to present the
interrogation content containing the MU field at the transponder
output data interface. The UDS1 = 3, UDS2 = 2 combination
identifies the data as an ACAS broadcast containing the 24-bit
address of the interrogating ACAS aircraft. This provides each
ACAS with a means of determining the number of other ACAS
within its detection range for limiting interference. Theformatof

CIVIL AVIATION
S.R.O. 31
the MU field is described in Paragraph 3. of Schedule 10.
2.
AIR-AIR COORDINATION PROTOCOLS
(1) Coordination interrogations. ACAS shall trans
mit UF = 16 interrogations with AQ = 0 and RL =
1 when another aircraft reporting RI = 3 or 4 is
declared a threat. The MU field shall contain the
resolution message in the subfields specified in
sub paragraph 3.(2) of Schedule 10.
Note 1.— A UF = 16 interrogation with AQ = 0 and RL = 1 is
intended to cause a DF = 16 reply from the other aircraft.
Note 2.— An aircraft reporting RI = 3 or RI = 4 is an aircraft
equipped with an operating ACAS which has vertical only or
vertical and horizontal resolution capability, respectively.
(2)
Coordination reply. These protocols are
in sub paragraph 3.(2) of Schedule 11.
3.
PROTOCOLS FOR ACAS COMMUNICATION
WITH GROUND STATIONS
(1)
RA reports to Mode S ground stations.
These protocols are described in sub
paragraph 4(1) of Schedule 11.
(2)
RA broadcasts. RA broadcasts shall be
transmitted at full power from the bottom
antenna at jittered, intervals. The RA
broadcast shall include the MU field as
specified in sub paragraph 1(4) of sched
uled 10. The RA broadcast shall describe
the current. Installations using directional
antennas shall operate such that complete
circular coverage is provided.

CIVIL AVIATION
S.R.O. 31
(3)
Data link capability report. These protocols
are described in sub paragraph 4.(1) of Schedule 11
(4)
ACAS sensitivity level control. ACAS shall
act upon an SLC command if and only if
TMS has the value 0 and DI is either 1 or 7
in the same interrogation.
