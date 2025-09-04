SCHEDULE 7
THREAT DETECTION RELATED TO ACAS II AND
ACAS III
1.
Declaration of threat. ACAS shall evaluate appropriate
characteristics of each intruder to determine whether or not it
is a threat.
(1)
Intruder characteristics. As a minimum, the character-
istics of an intruder that are used to identify a threat shall
include:

CIVIL AVIATION
S.R.O. 31
(a) tracked altitude;
(b) tracked rate of change of altitude;
(c) tracked slant range;
(d) tracked rate of change of slant range; and
(e) sensitivity level of intruder’s ACAS, Si.
For an intruder not equipped with ACAS II or ACAS III, Si shall
be set to 1.
(2)
Own aircraft characteristics. As a minimum, the charac-
teristics of own aircraft that are used to identify a threat shall
include:
(a) altitude;
(b) rate of change of altitude; and
(c) sensitivity level of own ACAS
2.
Sensitivity levels. ACAS shall be capable of operating at
any of a number of sensitivity levels. These shall include:
(1)
S = 1, a “standby” mode in which the interrogation
of other aircraft and all advisories are inhibited.
(2)
S = 2, a “TA only” mode in which RAs are
inhibited; and
(3)
for TCAS Version 7.1 compliant systems: S = 3-
7, further levels that enable the issue of RAs that provide
the warning times indicated in Table 7-1 as well as TAs.

CIVIL AVIATION
S.R.O. 31
(4)
for ACAS X compliant systems: S = 3, a “TA/
RA” mode in which RAs and TAs can be issued
3.
Selection of own sensitivity level (So). The selection of
own ACAS sensitivity level shall be determined by sensitivity
level control (SLC) commands which shall be accepted from a
number of sources as follows:
(a) SLC command generated automatically by ACAS
based on altitude band or other external factors;
(b) SLC command from pilot input; and
(c) SLC command from Mode S ground stations.
(1)
Permitted SLC command codes. As a minimum, the
acceptable SLC command codes shall include:
(2)Altitude-band SLC command. Where ACAS selects an
SLC command based on altitude, hysteresis shall be applied to
the nominal altitude thresholds at which SLC command value
changes are required as follows: for a climbing ACAS aircraft
the SLC command shall be increased at the appropriate altitude
threshold plus the hysteresis value; for a descending ACAS
aircraft the SLC command shall be decreased at the appropri-
ate altitude threshold minus the hysteresis value.
(3)
Pilot SLC command. For the SLC command set by the
pilot the value 0 shall indicate the selection of the “automatic”
mode for which the sensitivity level selection shall be based on

CIVIL AVIATION
S.R.O. 31
the other commands.
Table 7-1
(4)
Mode S ground station SLC command for TCAS
Version 7.1 compliant systems. For SLC commands transmit-
ted via Mode S ground stations, the value 0 shall indicate that
the station concerned is not issuing an SLC command and that
sensitivity level selection shall be based on the other com-
mands, including non-0 commands from other Mode S ground
stations. ACAS shall not process an uplinked SLC value of 1.
(a) ATS selection of SLC command code. ATS authori-
tiesshallensurethatproceduresareinplacetoinform
pilotsofanyATSselected SLC command code other
than 0.
(5)
Selection rule. Own ACAS sensitivity level shall be set
to the smallest non-0 SLC command received from any of the
sources listed in paragraph 3.
(6)
For ACAS X compliant systems: ACAS shall receive
any SLC commands from Mode S ground stations but shall not
use their sensitivity level values.
4.
Selection of parameter values for RA generation. When
the sensitivity level of own ACAS is 3 or greater, the param-
eter values used for RA generation that depend on sensitivity
level shall be based on the greater of the sensitivity level of
own ACAS, So, and the sensitivity level of the intruder’s
ACAS, Si.

CIVIL AVIATION
S.R.O. 31
5.
Selection of parameter values for TA generation. The
parameter values used for TA generation that depend on
sensitivity level shall be selected on the same basis as those for
RAs except when an SLC command with a value of 2 (“TA
only” mode) has been received from either the pilot or a Mode
S ground station. In this case, the parameter values for TA
generation shall retain the values they would have had in the
absence of the SLC command from the pilot or Mode S ground
station.
