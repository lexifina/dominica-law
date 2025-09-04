SCHEDULE 5
Regulations 48 (7), 59
MODE A/C ACAS I INTERFERENCE LIMITS AND
SURVEILLANCE AND COMMUNICATION FOR-
MATS USED BY ACAS
1.
Table 5-1: Mode A/C ACAS I interference limits. The interro-
gator power shall not exceed the following limits:

CIVIL AVIATION
S.R.O. 31
where:
na = number of operating ACAS II and ACAS III equipped
aircraft near own (based on ACAS broadcasts received with a
transponder receiver threshold of –74 dBm);
{ } =average value of the expression within the brackets over last
8 interrogation cycles;
Pa(k) = peak power radiated from the antenna in all directions of
the pulse having the largest amplitude in the group of pulses
comprising a single interrogation during the kth Mode A/C

CIVIL AVIATION
S.R.O. 31
interrogation in a 1s interrogation cycle, W;
k = index number for Mode A/C interrogations, k = 1, 2,..., kt;
kt = number of Mode A/C interrogations transmitted in a 1 s
interrogationcycle;
fr = Mode A/C reply rate of own transponder.
2.Surveillance and Communication Formats used by
ACAS
(Regulation 59)
(1)
The air-air surveillance and communication formats
which are used by ACAS shall be as in Figure 5-1.
Figure 5-1: Surveillance and Communication formats
used by ACAS
(a) DR(downlinkrequest).Thesignificanceofthecoding
of the downlink request field shall be as follows:
Coding
0-1 See sub paragraph 6.(5) (b) of Schedule 4
ACAS message available
Comm-B message available and ACAS message
available
4-5 See sub paragraph 6.(5) (b) of Schedule 4
Comm-B broadcast message 1 available and ACAS
message available
Comm-B broadcast message 2 available and ACAS

CIVIL AVIATION
S.R.O. 31
message available
8-31 See sub paragraph 6.(5) (b) of Schedule 4
(b) RI (air-air reply information). The significanceof the
coding in the RI field shall be as follows:
Coding
No operating ACAS
Not assigned
ACASwithresolutioncapability inhibited
ACASwithvertical-onlyresolution capability
ACASwithverticalandhorizontalresolutioncapability
5-7 Not assigned
8-15 See Sub-paragraph 8.(2)(b) of Schedule 4
Bit 14 of the reply format containing this field shall replicate the
AQ bit of the interrogation.The RI field shall report “no operating
ACAS” (RI = 0) if the ACAS unit has failed or is in standby. The
RI field shall report “ACAS with resolution capability inhibited”
(RI = 2) if sensitivity level is 2 or TA only mode has been selected.
Note.— Codes 0-7 in the RI field indicate that the reply is a tracking
reply and also give the ACAS capability of the interrogated aircraft.
Codes 8-15 indicate that the reply is an acquisition reply and also give
the maximum true airspeed capability of the interrogated aircraft.
(c) RR (reply request). The significance of the coding in
the reply request field shall be as follows:
Coding
0-18 See Sub-paragraph 6(1)(b) of Schedule 4
Transmit a resolution advisory report
20-31 See Sub-paragraph 6(1)(b) of Schedule 4

CIVIL AVIATION
S.R.O. 31
