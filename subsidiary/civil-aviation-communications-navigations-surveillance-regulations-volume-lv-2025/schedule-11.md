SCHEDULE 11
Regulation 47
REQUIREMENTS FOR A MODE S TRANSPONDER
USED IN CONJUNCTION WITH ACAS
1.
Transponder capabilities. In addition to the
minimum transponder capabilities defined in the secondary
surveillance Radar System Characteristics, the Mode S
transponder used in conjunction with ACAS shall have the
following capabilities:
(a) abilitytohandlethefollowing formats:
(b) ability to receive long Mode S interrogations (UF =
16) and generate long Mode S replies (DF = 16) at a
continuous rate of 16.6 ms (60 per second);
(c) means for delivering the ACAS data content of all
accepted interrogations addressed to the ACAS
equipment;
(d) antenna diversity;
(e) mutu+alsuppressioncapability; and
(f) inactive state transponder output power restriction.
When the Mode S transponder transmitter is in the inactive state,
the peak pulse power at 1 090 MHz ±3 MHz at the terminals of
the Mode S transponder antenna shall not exceed –70 dBm.

CIVIL AVIATION
S.R.O. 31
2.
DATA TRANSFER BETWEEN ACAS AND ITS
MODE S TRANSPONDER
(1) Data transfer from ACAS to its Mode S transponder:
(a) TheModeStranspondershallreceivefromitsACAS
RA information for transmission in an RA report and
in a coordination reply;
(b) the Mode S transponder shall receive from its ACAS
current sensitivity level for transmission in a sensitiv-
ity level report
(c) the Mode S transponder shall receive from its ACAS
capability information for transmission in a data link
capabilityreportand fortransmissionintheRIfieldof
air-air downlink formats DF= 0 and DF = 16; and
(d) the Mode S transponder shall receive from its ACAS
an indication that RAs are enabled or inhibited for
transmissionin the RI field of downlink formats 0 and
16.
(2) Data transfer fromMode S transponder to its ACAS:
(a) The Mode S transponder shall transfer to its ACAS
receivedsensitivitylevel control commands transmit-
ted by Mode S stations;
(b) the Mode S transponder shall transfer to its ACAS
received ACAS broadcast messages transmitted by
other ACASs;
(c) the Mode S transponder shall transfer to its ACAS
received resolution messages transmitted by other
ACASs for air-air coordination purposes; and

CIVIL AVIATION
S.R.O. 31
(d) the Mode S transponder shall transfer to its ACAS
own aircraft’s Mode A identity data for transmission
in an RA broadcast.
3.
COMMUNICATION OF ACAS INFORMATION TO
OTHER ACAS
(1) Surveillance reply. The ACAS Mode S transponder
shallusetheshort (DF = 0) or long (DF = 16) surveillance formats
for replies toACAS surveillanceinterrogations.Thesurveillance
replyshallincludetheVSfield asspecifiedinSub-paragraph8(1)
of Schedule 4, the RI field as specified Sub-paragraph 8(1) of
schedule 4 and in Sub-paragraph 2.(1)(b) of Schedule 5, and the
SL field as specified in Schedule Sub -Paragraph 10(4)(b)(vi).
(2) Coordination reply. The ACAS Mode S transponder
shall transmit a coordination reply upon receipt of a coordination
interrogation from an equipped threat subject to the conditions of
Sub-paragraph 3(2)(a). The coordination reply shall use the long
air-air surveillance reply format, DF= 16, with the VS field as
specified in sub paragraph 8(1) of schedule 4, the RI field as
specified in sub paragraph 8(1) of schedule 4 and sub paragraph
2(1)(b), the SLfield as specified in paragraph 5 of Schedule 10 and
the MV field as specified in paragraph 4 of Schedule 10. Coordi-
nation replies shall be transmitted even if the minimumreplyrate
limits of the transponder are exceeded.
(a) The ACAS Mode S transponder shall reply with a
coordination replytoa coordinationinterrogationre-
ceived from another ACAS if and only if the trans-
ponder is able to deliver theACAS data content of the
interrogation to its associated ACAS.
4.
COMMUNICATION OF ACAS INFORMATION TO
GROUND STATIONS
(1) RA reports to Mode S ground stations. During the

CIVIL AVIATION
S.R.O. 31
period of an RA and for 18±1 s following the end of the RA, the
ACAS Mode S transponder shall indicate that it has an RA report
by setting the appropriate DR field code in replies to a Mode S
sensor as specified in sub paragraph 2(1)(a) of schedule 5. The
RA report shall include the MB field as specified in sub paragraph
1(1) of Schedule 10. The RA report shall describe the most recent
RA that existed during the preceding 18±1 s period.
Note 1.— The last sentence of sub paragraph (1) means that for
18±1 s following the end of an RA, all MB subfields in the RA
report withtheexceptionofbit59(RAterminatedindicator) will
retain the information reported at the time the RA was last active.
Note 2.— Upon receipt of a reply with DR = 2, 3, 6 or 7, a
Mode S ground station may request downlink of the RA
report by setting RR= 19 and either DI = 7, or DI = 7 and RRS
= 0 in a surveillance or Comm-A interrogation to the ACAS
aircraft. When this interrogation is received, the transponder
replies with a Comm-B reply whose MB field contains the RA
report.
(2) Data link capability report. The presence of an
ACAS shall be indicated by its Mode S transponder to a ground
station in the Mode S data link capability report.
(3) AdequateprotectionagainstresidualADS-Bposition
datashall beprovidedintrackstatecomputationwhentransitioning
frompassive toactivesurveillance,inordertoavoidunnecessary
advisoriesduring such transitions.
