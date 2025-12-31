58. (1) Technical characteristics
(a) Emergency locator transmitters shall operate on
oneofthefrequencychannelsassignedforusein
the frequency band 406.0 to 406.1 MHz.
(b) The period between transmissions shall be 50
seconds plus or minus 5 per cent.
(c) Over a period of 24 hours of continuous operation
at an operating temperature of –20°C, the trans-
mitter power output shall be within the limits of 5
W plus or minus 2 dB.
(d) The 406 MHz ELT shall be capable of transmit-
ting a digital message.
(2) Transmitteridentification coding
(a) Emergency locator transmitters operating on 406
MHz shall be assigned a unique coding for iden-
tification of the transmitter or aircraft on which it
is carried.
(b) Theemergencylocatortransmittershallbecoded
inaccordancewitheithertheaviationuserproto-
col or one of the serialized user protocols de-
scribed in the Appendix to this chapter, and shall
be registered with the appropriate authority.
Specification for the
406 MHz component of
emergency locator
transmitter (ELT) for
search and rescue.

CIVIL AVIATION
S.R.O. 32
SCHEDULE 1: Figure, Tables and Notes for PART II
(PART II)
Table 1-1.  Mapping of ATN communication priorities

CIVIL AVIATION
S.R.O. 32
Table 1-2.  Mapping of ATN network priority to mobile subnetwork priority

CIVIL AVIATION
S.R.O. 32
Figure 1-1. Conceptual model of the ATN
(1)
Notes for the start of PART II
Note 1.— Detailed technical specifications for ATN/OSI applications are
contained in the Manual on Detailed Technical Specifications for the Aeronauti-
cal Telecommunication Network (ATN) using ISO/OSI Standards and Protocols
(Doc 9880) and in the Manual of Technical Provisions for the Aeronautical
Telecommunication Network (ATN) (Doc 9705).
Note 2.— Detailed technical specifications for ATN/IPS applications are
contained in the Manual for the Aeronautical Telecommunication Network
(ATN) using Internet Protocol Suite (IPS) Standards and Protocols (Doc 9896)
(available electronically on the ICAO-Net).

CIVIL AVIATION
S.R.O. 32
(2)
Note at the beginning of Regulation 5.
The regulations comprising the remainder of PART II define
the minimum required protocols and services that will enable
the global implementation of the aeronautical telecommunica-
tion network (ATN).
(3)
Notes after Sub-regulation 6.(1)
Note 1.— ATN/IPS implementation is preferred for ground-
ground networks. While ATN/OSI continues to be supported
in air-ground networks, particularly when using VDL Mode 2,
it is expected that future air-ground implementations will use
the ATN/IPS.
Note 2.— Interoperability between interconnecting OSI/IPS
networks is expected to be arranged prior to implementation.
Note 3.— Guidance material on interoperability between
ATN/OSI and ATN/IPS is contained in Doc 9896.
(4)
Note after Sub-regulation 6.(6)
The Manual on Required Communication Performance
(RCP)(Doc 9869) contains the
necessaryinformationonRCP.
(5)
Note after Sub-regulation 6.(14)
The time accuracy value results in synchronization errors of up
to two seconds.
(6)
Note at the start of Sub-regulation 7.(1)
System applications provide services that are necessary for
operation of the ATN.
(7)
Note after Sub-regulations 7.(2)(a) and 7.(3)(a)
See the Manual of Air Traffic Services Data Link Applica-
tions (Doc 9694).

CIVIL AVIATION
S.R.O. 32
(8)
Note at the start of Regulation 9.
The ATN naming and addressing scheme supports the princi-
ples of unambiguous identification of intermediate systems
(routers) and end-systems (hosts) and provides global address
standardization.
(9)
Note after Sub-regulation 10.(1)
This is achieved through the current and next data authority
aspects of the controller-pilot data link
communications (CPDLC) application.
(10)
Note after Sub-regulation10.(3)
The use of security is the default; however, its implementation
is based on local policy.
SCHEDULE 2: MODE S CHARACTERISTICS
(Regulation 17)
(1)
General provisions
Note 1.— Reference ISO document. When the term “ISO 8208”
is referred to in this standard, it means the ISO Standard
“Information technology — Data communications — X.25 Packet
Layer Protocol for Data Terminal Equipment, Reference Number
ISO/IEC 8208: 1990(E)”.
Note 2.— The overall architecture of the Mode S subnetwork is
presented in the diagram on the following page.

CIVIL AVIATION
S.R.O. 32
Note 3.— The processing splits into three different paths. The
first consists of the processing of switched virtual circuits (SVCs),
thesecondconsistsoftheprocessingofModeSspecificservices,
and the third consists of the processing of subnetwork manage-
ment information. SVCs utilize the reformatting process and the
ADCE or GDCE function. Mode S specific services utilize the
Mode S specific services entity (SSE) function.
(1) The Mode S subnetwork shall only carry aeronautical
communications classified under categories of flight safety and
flight regularity as specified in Annex 10, Volume II, Chapter 5,
5.1.8.4 and 5.1.8.6.
(2) Signals in space. The signal-in-space characteris-
tics of the Mode S subnetwork shall conform to the provisions
contained in Annex 10, Volume IV, Chapter 3, 3.1.2.
(3) Code and byte independency. The Mode S
subnetwork shall be capable of code and byte independent
transmission of digital data.
(4) Data transfer. Data shall be conveyed over the
Mode S data link in segments using either standard length
message (SLM) protocols or extended length message (ELM)
protocols as defined in 3.1.2.6.11 and 3.1.2.7 of Annex 10,
Volume IV.
Note 1.— An SLM segment is the contents of one 56-bit MA
or MB field. An ELM segment is the contents of one 80-bit
MC or MD field.
Note 2.— An SLM frame is the contents of up to four linked
MA or MB fields. An ELM frame is the contents of 2 to 16
MC or 1 to 16 MD fields.
(5) Bit numbering. In the description of the data ex-
change fields, the bits shall be numbered in the order of their

CIVIL AVIATION
S.R.O. 32
transmission, beginning with bit 1. Bit numbers shall continue
through the second and higher segments of multi-segment frames.
Unless otherwise stated, numerical values encoded by groups
(fields)ofbitsshallbeencodedusingpositive binary notation and
the first bit transmitted shall be the most significant bit (MSB)
(3.1.2.3.1.3 of Annex 10, Volume IV).
(6) Unassigned bits. When the length of the data is not
sufficient to occupy all bit positions within a message field or
subfield, the unassigned bit positions shall be set to 0.
(2)
Frames
(1) UPLINK FRAMES
(a) SLM frame. An uplink SLM frame shall be
composed of up to four selectively addressed
Comm-A segments.

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32
Note.— Each Comm-A segment (MA field) received by the
ADLP is accompanied by the first 32 bits of the interrogation that
delivered the segment (3.1.2.10.5.2.1.1 of Annex 10, Volume
IV). Within these 32 bits is the 16-bit special designator (SD)
field (3.1.2.6.1.4 of Annex 10, Volume IV).
(i) SD field.When the designator identification
(DI) field (bits 14-16) has a code value of 1
or 7, the special designator (SD) field (bits
17-32) of each Comm-A interrogation shall
be used to obtain the interrogator identifier
subfield (IIS, bits 17-20) and the linked
Comm-A subfield (LAS, bits 30-32). The
action to be taken shall depend on the value
of LAS. The contents of LASand IIS shall be
retained and shall be associated with the
Comm-A message segment for use in as-
sembling the frame as indicated below. All
fields other than the LAS field shall be as
defined in 3.1.2 of Annex 10, Volume IV.
Note.— The SD field structure is shown in Figure 6-1 of
Schedule 6 of these regulations.
(ii) LAS coding. The 3-bit LAS subfield shall be
coded as follows:
LAS MEANING
single segment
linked, 1st segment
linked, 2nd but not final segment
linked, 3rd but not final segment
linked, 4th and final segment
linked, 2nd and final segment
linked, 3rd and final segment
unassigned

CIVIL AVIATION
S.R.O. 32
(iii) Single segment SLM frame. If LAS = 0, the
data in the MA field shall be considered a
complete frame and shall be made available
for further processing.
(iv) Multiple segment SLM frame. The ADLP
shall accept and assemble linked 56-bit
Comm-A segments associated with all six-
teen possible interrogator identifier (II) codes.
Correct linking of Comm-A segments shall
be achieved by requiring that all Comm-A
segments have the same value of IIS. If LAS
= 1 through 6, the frame shall consist of two
to four Comm-A segments as specified in the
following paragraphs.
(aa) Initial segment. If LAS = 1, the
MA field shall be assembled as the
initial segment of an SLM frame.
The initial segment shall be stored
until all segments of the frame have
been received or the frame is
cancelled.
(bb) Intermediate segment. If LAS = 2
or 3, the MA field shall be assem-
bled in numerical order as an
intermediate segment of the SLM
frame. It shall be associated with
previous segments containing the
same value of IIS.
(cc) Final segment. If LAS = 4, 5 or 6,
the MA field shall be assembled as
the final segment of the SLM
frame. It shall be associated with
previous segments containing the

CIVIL AVIATION
S.R.O. 32
same value of IIS.
(dd) Frame completion. The frame shall be con-
sidered complete and shall be made available
for further processing as soon as all segments
of the frame have been received.
(ee) Frame cancellation. An incomplete SLM
frame shall be cancelled if one or more of the
following conditions apply:
(A) a new initial segment (LAS = 1) is
received with the same value of
IIS. In this case, the new initial
segment shall be retained as the
initial segment of a new SLM
frame;
(B) the sequence of received LAS
codes (after the elimination of
duplicates) is not contained in the
following list:
1) LAS = 0
2) LAS = 1,5
3) LAS = 1,2,6
4) LAS = 1,6,2
5) LAS = 1,2,3,4
6) LAS = 1,3,2,4
7) LAS = 1,2,4,3
8) LAS = 1,3,4,2
9) LAS = 1,4,2,3
10) LAS = 1,4,3,2
(C) Tc seconds have elapsed since the last
Comm-A segment with the same value
of IIS was received (Table 5-1).

CIVIL AVIATION
S.R.O. 32
(ff) Segment cancellation. A received
segment for an SLM frame shall be
discarded if it is an intermediate or
final segment and no initial segment
has been received with the same
value of IIS.
(gg) Segment duplication. If a received
segment duplicates a currently
received segment number with the
same value of IIS, the new seg-
ment shall replace the currently
received segment.
Note.— The action of the Mode S subnetwork protocols may
result in the duplicate delivery of Comm-A segments.
(b) ELM frame. An uplink ELM frame shall consist
of from 20 to 160 bytes and shall be transferred
from the interrogator to the transponder using the
protocol defined in3.1.2.7 of Annex 10, Volume
IV. The first 4 bits of each uplink ELM segment
(MC field) shall contain the interrogator identifier
(II) code of the Mode S interrogator transmitting
the ELM. The ADLP shall check the II code of
each segment of a completed uplink ELM. If all
of the segments contain the same II code, the II
code in each segment shall be deleted and the
remaining message bits retained as user data for
further processing. If all of the segments do not
contain the same II code, the entire uplink ELM
shall be discarded.
Note.— An uplink ELM frame consists of two to sixteen
associated Comm-C segments, each of which contains the 4-
bit II code. Therefore, the capacity for packet transfer is 19 to

CIVIL AVIATION
S.R.O. 32
152 bytes per uplink ELM frame.
(2) DOWNLINK FRAMES
(a) SLM frame. A downlink SLM frame shall be
composed of up to 4 Comm-B segments. The
MB field of the first Comm-B segment of the
frame shall contain a 2-bit linked Comm-B subfield
(LBS, bits 1 and 2 of the MB field). This subfield
shall be used to control linking of up to four
Comm-B segments.
Note.— The LBS uses the first 2-bit positions in the first segment
of a multi or single segment downlink SLM frame. Hence, 54 bits
are available for Mode S packet data in the first segment of a
downlink SLM frame. The remaining segments of the downlink
SLM frame, if any, have 56 bits available.
(i) LBS coding.Linking shall be indicated by the
coding of the LBS subfield of the MB field of
the initial Comm-B segment of the SLM
frame.
The coding of LBS shall be as follows:
LBS
MEANING
single segment
initial segment of a two-segment SLM frame
initial segment of a three-segment SLM frame
initial segment of a four-segment SLM frame
(ii) Linking protocol
(aa) In the Comm-B protocol, the initial
segment shall be transmitted using
the air-initiated or multisite- di-

CIVIL AVIATION
S.R.O. 32
rected protocols. The LBS field of
the initial segment shall indicate to
the ground the number of additional
segments to be transferred (if any).
Before the transmission of the
initial segment to the transponder,
the remaining segments of the
SLM frame (if any) shall be
transferred to the transponder for
transmission to the interrogator
using the ground-initiated Comm-B
protocol. These segments shall be
accompanied by control codes that
cause the segments to be inserted
in ground-initiated Comm-B regis-
ters 2, 3 or 4, associated respec-
tively with the second, third, or
fourth segment of the frame.
(bb) Close-out of the air-initiated seg-
ment that initiated the protocol shall
not be performed until all segments
have been successfully transferred.
Note.— The linking procedure including the use of the ground-
initiated Comm-B protocol is performed by the ADLP.
(iii) Directing SLM frames. If the SLM frame is
to be multisite-directed, the ADLP shall de-
termine the II code of the Mode S interroga-
tor or cluster of interrogators that shall re-
ceive the SLM frame.
(b) ELM FRAME
Note.— A downlink ELM consists of one to sixteen associated
Comm-D segments.

CIVIL AVIATION
S.R.O. 32
(i) Procedure. Downlink ELM frames shall be
used to deliver messages greater than or
equal to 28 bytes and shall be formed using
the protocol defined in 3.1.2.7 of Annex 10,
Volume IV.
(ii) Directing ELM frames. If the ELM frame is
to be multisite-directed, the ADLP shall de-
termine the II code of the Mode S interroga-
tor or cluster of interrogators that shall re-
ceive the ELM frame.
(3) XDLP frame processing. Frame processing shall be
performed on all Mode S packets (except for the MSP packet) as
specified in Sub-paragraph (2)(3) to (2)(5) of Schedule 2. Frame
processing for Mode S specific services shall be performed as
specified in Paragraph 7 of Schedule 2.
(a) Packet length. All packets (including a group of
packets multiplexed into a single frame) shall be
transferred in a frame consisting of the smallest
number of segments needed to accommodate the
packet. The user data field shall be an integral
multiple of bytes in length. A 4-bit parameter
(LV) shall be provided in the Mode S DATA,
CALL REQUEST, CALL ACCEPT, CLEAR
REQUEST and INTERRUPT packet headers
so that during unpacking no additional bytes are
added to the user data field. The LV field shall
define the number of full bytes used in the last
segment of a frame. During LV calculations, the
4-bit II codein the last segment of an uplink ELM
message shall be (1) ignored for uplink ELM
frames with an odd number of Comm-C seg-
ments and (2) counted for uplink ELM frames
with an even number of Comm-C segments. The
value contained in the LV field shall be ignored if

CIVIL AVIATION
S.R.O. 32
the packet is multiplexed.
Note.— A specific length field is used to define the lengthof each
element of a multiplexed packet. Therefore the LV field value is
not used. LV field error handling is described in Tables 5-16 and
5-19.
(b) Multiplexing.When multiplexing multiple Mode
S packets into single SLM on ELM frame, the
following procedures shall be used. Multiplexing
of the packets within the ADLP shall not be
applied to packets associated with SVCs of
different priorities.
Note.— Multiplexing is not performed on MSP packets.
(i) Multiplexing optimization
When multiple packets are awaiting transfer to the same XDLP,
they should be multiplexed into a single frame in order to optimize
throughput, provided that packets associated with SVCs of
different priorities are not multiplexed together.
(ii) Structure. The structure of the multiplexed
packets shall be as follows:
HEADER:6 or 8
LENGTH:8
1ST PACKET:v LENGTH:8 2ND PACKET:v
Note.—Anumberinthefieldsignifiesthefieldlengthinbits;“v”
signifies that the field is of variable length.
(aa) Multiplexing header. The header
for the multiplexed packets shall be
as follows:
DP:1
MP:1
SP:2
ST:2
FILL2:0 or 2

CIVIL AVIATION
S.R.O. 32
Where,
Data packet type (DP) = 0
MSP packet type (MP) = 1
Supervisory packet (SP) = 3
Supervisory type (ST) = 2
Note.— See Figure 5-23 for a definition for the field structure
used in the multiplexing header.
(bb) This field shall contain the length of
the following packet in bytes. Any
error detected in a multiplexed
DATA packet, such as inconsist-
ency between length as indicated in
the LENGTH field and the length
of the frame hosting that packet,
shall result in the discarding of the
packet unless the error can be
determined to be limited to the
LENGTH field, in which case a
REJECT packet with the expected
PS value can be sent.
(A) For multiplex packets, if the
entire packet cannot be de-
multiplexed, then the first con-
stituent packet should be treated
as a format error, and the re-
mainder should be discarded.
(iii) Termination. The end of a frame containing
a sequence of multiplexed packets shall be
determined by one of the following events:
a) a length field of all zeros; or

CIVIL AVIATION
S.R.O. 32
b) less than eight bits left in the frame.
(c) MODE S CHANNEL SEQUENCE PRESER-
VATION
(i) Application. In the event that multiple Mode
S frames from the same SVC are awaiting
transfer to the same XDLP, the following
procedure shall be used.
(ii) Procedure
Note 1.— SLM and ELM transactions can occur independently.
Note2.—Uplinkanddownlinktransactionscanoccur independ-
ently.
(aa) SLM frames. SLM frames await-
ing transfer shall be transmitted in
the order received.
(bb) ELM frames. ELM frames await-
ing transfer shall be transmitted in
the order received.
(4) GDLP FRAME PROCESSING
(a) GENERAL PROVISIONS
(i) The GDLP shall determine the data link
capability of the ADLP/transponder installa-
tion from the data link capability report (5.2.9)
before performing any data link activity with
that ADLP.
(ii) GDLP frame processing shall provide to the
interrogator all data for the uplink

CIVIL AVIATION
S.R.O. 32
transmissionthatarenot provided directly by
the interrogator.
(b) Delivery status. GDLP frame processing shall
accept an indication from the interrogator func-
tion that a specified uplink frame that was previ-
ously transferred to the interrogator has been
successfully delivered over the ground-to- air
link.
(c) Aircraft address. GDLP frame processing shall
receive from the interrogator along with the data
in each downlink SLM or ELM frame, the 24-bit
address of the aircraft that transmitted the frame.
GDLP frame processing shall be capable of
transferring to the interrogator the 24-bit address
of the aircraft that is to receive an uplink SLM or
ELM frame.
(d) Mode S protocol type identification. GDLP
frame processing shall indicate to the interrogator
the protocol to be used to transfer the frame:
standard length message protocol, extended length
message protocol or broadcast protocol.
(e) Frame determination. A Mode S packet (includ-
ing multiplexed packetsbut excluding MSP pack-
ets) intended for uplink and less than or equal to
28 bytes shall be sent as an SLM frame. A Mode
S packet greater than 28 bytes shall be sent as an
uplink ELM frame for transponders with ELM
capability, using M-bit processing as necessary.
If the transponder does not have ELM capability,
packets greater than 28 bytes shall be sent using
the M-bit or S-bit assembly procedures as neces-
sary and multiple SLM frames.

CIVIL AVIATION
S.R.O. 32
Note.— The Mode S DATA, CALL REQUEST, CALL AC-
CEPT, CLEAR REQUEST and INTERRUPT packets are the
only Mode S packets that use M-bit or S-bit sequencing.
(5) ADLP FRAME PROCESSING
(a) General provisions. With the possible exception
of the last 24 bits (address/parity), ADLP frame
processing shall accept from the transponder the
entire content of both 56-bit and 112-bit received
uplink transmissions, excluding all- callandACAS
interrogations. ADLP frame processing shall
providetothetransponderalldataforthedownlink
transmission that is not provided directly by the
transponder.
(b) Delivery status. ADLP frame processing shall
accept an indication from the transponder that a
specified downlink frame that was previously
transferred to the transponder has been closed
out.
(c) Interrogator identifier. ADLP frame process-
ingshallacceptfromthetransponder,alongwith
the data in each uplink SLM and ELM, the
interrogator identifier (II) code of the interrogator
that transmitted the frame. ADLP frame process-
ing shall transfer to the transponder the IIcode of
the interrogator or cluster of interrogators that
shall receive a multisite-directed frame.
(d) Mode S protocol type identification. ADLP
frame processing shall indicate to the trans-
ponder the protocol to be used to transfer the
frame: ground-initiated, air-initiated, broadcast,
multisite-directed, standard length or extended

CIVIL AVIATION
S.R.O. 32
length.
(e) Frame cancellation. ADLP frame processing
shall be capable of cancelling downlink frames
previously transferred to the transponder for
transmission but for which a close-out has not
been indicated. If more than one frame is stored
within the transponder, the cancellation proce-
dure shall be capable of cancelling the stored
frames selectively.
(f) Frame determination. A Mode S packet (includ-
ing multiplexed packetsbut excluding MSP pack-
ets) intended for downlink and less than or equal
to 222 bits shall be sent as an SLM frame. A
Mode S packet greater than 222 bits shall be sent
as a downlink ELM frame for transponders with
ELM capability using M-bit processing as neces-
sary. When M-bit processing is used, all ELM
frames containing M = 1 shall contain the maxi-
mum number of ELM segments that the trans-
ponder is capable of transmitting in response to
one requesting interrogation (UF = 24). If the
transponder does not have ELM capability, pack-
ets greater than 222 bits shall be sent using the M-
bit or S-bit assembly procedures and multiple
SLM frames.
Note.— The maximum length of a downlink SLM frame is 222
bits. This is equal to 28 bytes (7 bytes for 4 Comm-B segments)
minus the 2-bit linked Comm-B subfield.
(6) PRIORITY MANAGEMENT
(a) ADLP priority management. Frames shall be
transferred from the ADLP to the transponder in
the following order of priority (highest first):

CIVIL AVIATION
S.R.O. 32
a) Mode S specific services;
b) search requests;
c) frames containing only high priority SVC packets; and
d) frames containing only low priority SVC packets.
(b) GDLP PRIORITY MANAGEMENT
Uplink frames should be transferred in the following order of
priority(highest first):
a) Mode S specific services;
b) frames containing at least one Mode S ROUTE packet;
c) frames containing at least one high priority SVC packet; and
d) frames containing only low priority SVC packets.
(3)
Data exchange interfaces
(1) THE DTE ISO 8208 INTERFACE
(a) General provisions. The interface between the
XDLP and theDTE(s) shallconformto ISO 8208
packet layer protocol (PLP). The XDLP shall
support the procedures of the DTE as specified
in ISO 8208. As such, the XDLP shall contain a
DCE (5.2.4).
(b) Physical and link layer requirements for the
DTE/DCE interface. The requirements are:

CIVIL AVIATION
S.R.O. 32
a) the interface shall be code and byte independent and shall not
impose restrictions on the sequence, order, or pattern of the bits
transferred within a packet; and
b)the interface shall support the transfer of variable length
network layer packets.
(c) DTE ADDRESS
(i) Ground DTE address. The ground DTE
address shall have a total length of 3 binary
coded decimal (BCD) digits, as follows:
X0X1X2
X0shallbethemostsignificantdigit.GroundDTEaddressesshall
be decimal numbers in the range of 0 through 255 coded in BCD.
Assignment of the DTE address shall be a local issue. All DTEs
connected to GDLPs having overlapping coverage shall have
unique addresses. GDLPs which have a flying time less than Tr
(Table 5-1) between their coverage areas shall be regarded as
having overlapping coverage.
(ii) Mobile DTE address. The mobile DTE ad-
dress shall have a total length of 10 BCD
digits,as follows:
X0X1X2X3X4X5X6X7X8X9
X0 shall be the most significant digit. The digits X0 to X7 shall
contain the octal representation of the aircraft address coded in
BCD. The digits X8X9 shall identify a sub-address for specific
DTEs on board an aircraft. This sub-address shall be a decimal
number in the range of 0 and 15 coded in BCD. The following sub-
address assignments shall be used:
ATN router

CIVIL AVIATION
S.R.O. 32
to 15
Unassigned
(iii) Illegal DTE addresses. DTE addresses out-
side of the defined ranges or not conforming
to the formats for the ground and mobile DTE
addresses specified in Sub-paragraphs
(3)(1)(c)(i) and (ii) shall be defined to be
illegal DTE addresses. The detection of an
illegal DTE address in a CALL REQUEST
packet shall lead to a rejection of the call as
specified in Sub-paragraph (5)(1)(e).
(d) PACKET LAYER PROTOCOL REQUIRE-
MENTS OF THE DTE/DCE INTERFACE
(i) Capabilities.The interface between the DTE
and the DCE shall conform to ISO 8208 with
the followingcapabilities:
a) expedited data delivery, i.e. the use of INTERRUPT
packets with a user data field of up to 32 bytes;
b)
priorityfacility(withtwolevels, Sub-paragraph
(5)(2)(a)(i)(ff);
c)
fast select (5)(2)(a)(i)(mm), (5)(2)(a)(i)(pp); and
d)
called/calling address extension facility, if required by
local conditions (i.e. the XDLP is connected to the DTE via a
network protocol that is unable to contain the Mode S address
as defined).
Other ISO 8208 facilities and the D-bit and the Q-bit shall not be
invoked for transfer over the Mode S packet layer protocol.
Parameter values. The timer and counter parameters for the
DTE/DCE interface shall conform to the default ISO 8208

CIVIL AVIATION
S.R.O. 32
values.
(2) MODE S SPECIFIC SERVICES INTERFACE
Note.— Mode S specific services consist of the broadcast
Comm-A and Comm-B, GICB and MSP.
(a) ADLP
(i) General provisions. The ADLP shall sup-
port the accessing of Mode S specific serv-
ices through the provision of one or more
separate ADLP interfaces for this purpose.
(ii) Functional capability. Message and con-
trol coding via this interface shall support all
of the capabilities specified in Sub-Paragraph
(7)(1).
(b) GDLP
(i) General provisions. The GDLP shall sup-
port the accessing of Mode S specific serv-
ices through the provision of a separate GDLP
interface for this purpose and/or by providing
access to these services through the DTE/
DCE interface.
(ii) Functional capability. Message and con-
trol coding via this interface shall support all
of the capabilities specified in Sub-Paragraph
(7)(1).
(3) ADLP/TRANSPONDER INTERFACE
(a) TRANSPONDER TO ADLP

CIVIL AVIATION
S.R.O. 32
(i) The ADLP shall accept an indication of
protocol type from the transponder in con-
nection with data transferred from the trans-
ponder to the ADLP. This shall include the
followingtypes of protocols:
a) surveillance interrogation;
b)
Comm-A interrogation;
c)
Comm-A broadcast interrogation; and
d)
uplink ELM.
The ADLP shall also accept the II code of the interrogator used
to transmit the surveillance, Comm-A or uplink ELM.
Note.—Transponderswillnotoutputall-callandACASinforma-
tion on this interface.
(ii) The ADLP shall accept control information
from the transponder indicating the status of
downlinktransfers.
Thisshall include:
a) Comm-B close-out;
b)
Comm-B broadcast timeout; and
c)
downlinkELMclose-out.
(iii) The ADLP shall have access to current
information defining the communication ca-
pability of the Mode S transponder with which

CIVIL AVIATION
S.R.O. 32
it is operating. This information shall be used
to generate the data link capability report.
(b) ADLP TO TRANSPONDER
(i) The ADLP shall provide an indication of
protocoltypetothetransponderinconnection
with data transferred from the ADLP to the
transponder. This shall include the following
types of protocols:
a)
ground-initiatedComm-B;
b)
air-initiatedComm-B;
c)
multisite-directedComm-B;
d)
Comm-B broadcast;
e)
downlinkELM; and
f)
multisite-directeddownlink ELM.
The ADLP shall also provide the II code for transfer of a
multisite-directed Comm-B or downlink ELM and the Comm-B
data selector (BDS) code (3.1.2.6.11.2 of Annex 10, Volume IV)
for a ground-initiated Comm-B.
(ii) The ADLP shall be able to perform frame
cancellation as specified in Sub-paragraph
(2)(5)(e).
(4)
GDLP/MODE S INTERROGATOR INTERFACE
(a) INTERROGATOR TO GDLP
(i) The GDLP shall accept an indication of
protocoltypefromtheinterrogatorinconnec-

CIVIL AVIATION
S.R.O. 32
tion with data transferred from the interroga
tor to the GDLP. This shall include the follow-
ing types of protocols:
a)
ground-initiatedComm-B;
b)
air-initiatedComm-B;
c)
air-initiated Comm-B broadcast; and
d)
downlink ELM.
The GDLP shall also accept the BDS code used to identify the
ground-initiatedComm-B segment.
(ii) The GDLP shall accept control information
from the interrogator indicating the status of
uplink transfers and the status of the ad-
dressed Mode S aircraft.
(b) GDLP to interrogator. The GDLP shall provide
an indication of protocol type to the interrogator
in connection with data transferred from the
GDLP to the interrogator. This shall include the
following types of protocols:
a)
Comm-A interrogation;
b)
Comm-A broadcast interrogation;
c)
uplinkELM; and
d)
ground-initiatedComm-B request.
The GDLP shall also provide the BDS code for the ground-
initiatedComm-B protocol.

CIVIL AVIATION
S.R.O. 32
(4) DCE operation
Note.— The DCE process within the XDLP acts as a peer
process to the DTE. The DCE supports the operations of the DTE
with the capability specified in Sub-paragraph (3)(1)(d). The
following requirements do not specify format definitions and flow
control on the DTE/DCE interface. The specifications and
definitions in ISO 8208 apply for these cases.
(1) State transitions. The DCE shall operate as a state
machine. Upon entering a state, the DCE shall perform the
actions specified in Table 5-2 of Schedule 5. State transitions and
additional action(s) shall be as specified in Table 5-3 through
Table 5-12 of Schedule 5.
Note.— The next state transition (if any) that occurs when the
DCE receives a packet from the DTE is specified by Table 5-3
through Table 5-8 of Schedule 5. These tables are organized
according to the hierarchy illustrated in Figure 6-2 of schedule 6.
The same transitions are defined in Table 5-9 through Table 5-12
of Schedule 5 when the DCE receives a packet from the XDCE
(via the reformatting process).
(2) DISPOSITION OF PACKETS
(a) Upon receipt of a packet from the DTE, the
packet shall be forwarded or not forwarded to the
XDCE (via the reformatting process) according
to theparenthetical instructions contained in Ta-
bles 5-3 to 5-8 of Schedule 5. If no parenthetical
instruction is listed or if the parenthetical instruc-
tion indicates “do not forward”, the packet shall
be discarded.
(b) Upon receipt of a packet from the XDCE (via the
reformatting process), the packet shall be for-
warded or not forwarded to the DTE according

CIVIL AVIATION
S.R.O. 32
to the parenthetical instructions contained in Ta-
bles 5-9 to 5-12 of Schedule 5. If no parenthetical
instruction is listed or if the parenthetical instruc-
tion indicates “do not forward”, the packet shall
be discarded.
(5) Mode S packet layer processing
(1) GENERAL REQUIREMENTS
(a) BUFFER REQUIREMENTS
(i) ADLP buffer requirements
(aa) The followingrequirements apply to
the entire ADLP and shall be
interpreted as necessary for each
of the main processes (DCE,
reformatting, ADCE, frame
processing and SSE).
(bb) The ADLP shall be capable of
maintaining sufficient buffer space
for fifteen SVCs:
a)
maintain sufficient buffer space to hold fifteen Mode S
subnetwork packets of 152 bytes each in the uplink direction
per SVC for a transponder with uplink ELM capability or 28
bytes otherwise;
b)
maintain sufficient buffer space to hold fifteen Mode S
subnetwork packets of 160 bytes each in the downlink direc-
tion per SVC for a transponder with downlink ELM capability
or 28 bytes otherwise;
c)
maintain sufficient buffer space for two Mode S

CIVIL AVIATION
S.R.O. 32
subnetwork INTERRUPT packets of 35 bytes each (user data
field plus control information), one in each direction, for each
SVC;
d)
maintain sufficient resequencing buffer space for storing
thirty-one Mode S subnetwork packets of 152 bytes each in
the uplink direction per SVC for a transponder with uplink
ELM capability or 28 bytes otherwise; and
e)
maintain sufficient buffer space for the temporary
storage of at least one Mode S packet of 160 bytes undergoing
M-bit or S-bit processing in each direction per SVC.
(aa) The ADLP shall be capable of
maintaining a buffer of 1 600 bytes
in each direction to be shared
among all MSPs.
(ii) GDLP buffer requirements
(aa) The GDLP should be capable of
maintaining sufficient buffer space
for an average of 4 SVCs for each
Mode S aircraft in the coverage
area of the interrogators connected
to it, assuming all aircraft have
ELMcapability.
Note.— Additional buffer space may be required if DTEs
associated with end-systems are supported.
(b) CHANNEL NUMBER POOLS
(i) The XDLP shall maintain several SVC chan-
nel number pools; the DTE/DCE (ISO 8208)
interface uses one set. Its organization, struc-
ture and use shall be as defined in the ISO

CIVIL AVIATION
S.R.O. 32
8208 standard. The other channel pools shall
be used on the ADCE/GDCE interface.
(ii) The GDLP shall manage a pool of temporary
channel numbers in the range of 1 to 3, for
each ground DTE/ADLP pair. Mode S CALL
REQUEST packets generated by the GDLP
shall contain the ground DTE address and a
temporary channel number allocated from
the pool of that ground DTE. The GDLP shall
not reuse a temporary channel number allo-
cated to an SVC that is still in the CALL
REQUEST state.
Note 1.— The use of temporary channel numbers allows the
GDLP to have up to three call requests in process at the same time
for a particular ground DTE and ADLP combination. It also
allows the GDLP or ADLP to clear a channel before the
permanent channel number is assigned.
Note 2.— The ADLP may be in contact with multiple ground
DTEs at any one time. All the ground DTEs use temporary
channel numbers ranging from 1 to 3.
(iii) The ADLP shall use the ground DTE address
to distinguish the temporary channel numbers
used by the various ground DTEs. The ADLP
shall assign a permanent channel number (in
the range of 1 to 15) to all SVCs and shall
inform the GDLP of the assigned number by
including it in the Mode S CALL REQUEST
by ADLP or Mode S CALL ACCEPT by
ADLP packets. The temporary channel
number shall be included in the Mode S
CALL ACCEPT by ADLP together with the
permanent channel number in order to define
the association of these channel numbers.

CIVIL AVIATION
S.R.O. 32
The ADLP shall continue to associate the
temporary channel number with the perma-
nent channel number of an SVC until the
SVC is returned to the READY (p1) state, or
else, while in the DATA TRANSFER (p4)
state, a Mode S CALL REQUEST by GDLP
packet is received bearing the same tempo-
rary channel number. A non-zero permanent
channel number in the Mode S CLEAR
REQUEST by ADLP, CLEAR REQUEST
by GDLP, CLEAR
C O N F I R M A -
TION by ADLP or CLEAR CONFIRMA-
TION by GDLP packet shall indicate that the
permanent channel number shall be used and
the temporary channel number shall be ig-
nored. In the event that an XDLP is required
to send one of these packets in the absence of
a permanent channel number, the permanent
channel number shall be set to zero, which
shall indicate to the peer XDLP that the
temporary channel number is to be used.
Note.— The use of a zero permanent channel number allows the
ADLP to clear an SVC when no permanent channel number is
available, and allows the GDLP to do likewise before it has been
informed of the permanent channel number.
(iv) The channel number used by the DTE/DCE
interface and that used by the ADCE/GDCE
interface shall be assigned independently.
The reformatting process shall maintain an
association table between the DTE/DCE and
the ADCE/GDCE channel numbers.
(c) Receive ready and receive not ready condi-
tions. The ISO 8208 interface and the ADCE/
GDCE interface management procedures shall

CIVIL AVIATION
S.R.O. 32
be independent operations since each system
must be able to respond to separate receive ready
and receive not ready indications.
(d) PROCESSING OF M-BIT AND S-BIT SE-
QUENCES
Note.— M-bit processing applies to the sequencing of the DATA
packet. S-bit processing applies to the sequencing of Mode S
CALL REQUEST, CALL ACCEPT, CLEAR REQUEST and
INTERRUPT packets.
(i) M-bit processing
Note.— The packet size used on the DTE/DCE interface can
be different from that used on the ADCE/GDCE interface.
(aa) M-bit  processing shall be used
when DATA packets are
reformatted. M-bit processing shall
utilize the specifications contained
in the ISO 8208 standard. The M-
bit sequence processing shall apply
on a per channel basis. The M-bit
set to 1 shall indicate that a user
data field continues in the subse-
quent DATA packet. Subsequent
packets in an M-bit sequence shall
use the same header format (i.e.
the packet format excluding the
user data field).
(bb) If the packet size for the XDCE
interface is larger than that used on
the DTE/DCE interface, packets
shall be combined to the extent
possible as dictated by the M-bit,

CIVIL AVIATION
S.R.O. 32
when transmitting a Mode S
DATA packet. If the packet size is
smaller on the XDCE interface
than that defined on the DTE/DCE
interface, packets shall be frag-
mented to fit into the smaller Mode
S packet using M-bit assembly.
(cc) A packet shall be combined with
subsequent packets if the packet is
filled and more packets exist in the
M-bit sequence (M-bit = 1). A
packet smaller than the maximum
packet size defined for this SVC
(partial packet) shall only be
allowed when the M-bit indicates
the end of an M-bit sequence. A
received packet smaller than the
maximum packet size with M-bit
equal to 1 shall cause a reset to be
generated as specified in ISO 8208
and the remainder of the sequence
should be discarded.
(dd) In order to decrease delivery delay,
reformatting should be performed
on the partial receipt of an M-bit
sequence, rather than delay
reformatting until the complete M-
bit sequence is received.
(ii) S-bit processing. S-bit processing shall ap-
ply only to Mode S CALL REQUEST, CALL
ACCEPT, CLEAR REQUEST and INTER-
RUPT packets. This processing shall be per-
formed as specified for M-bit processing
except that the packets associated with any

CIVIL AVIATION
S.R.O. 32
S-bit sequence whose reassembly is not com-
pleted in Tq seconds shall be discarded and
receipt of a packet shorter than the maximum
packet size with S = 1 shall cause the entire
S-bit sequence to be treated as a format error
in accordance with Table 5-16 of Schedule 5.
(e) MODE S SUBNETWORK ERROR PROCESS-
ING FOR ISO 8208 PACKETS
(i) D-bit. If the XDLP receives a DATA packet
with the D-bit set to 1, the XDLP shall send
a RESET REQUEST packet to the originat-
ing DTE containing a cause code (CC) = 133
and a diagnostic code (DC) = 166. If the D-
bit is set to 1 in a CALL REQUEST packet,
the D-bit shall be ignored by the XDLP. The
D-bit of the corresponding CALL ACCEPT
packet shall always be set to 0. The use of CC
is optional.
(ii) Q-bit. If the XDLP receives a DATA packet
with the Q-bit set to 1, the XDLP shall send
a RESET REQUEST packet to the originat-
ing DTE containing CC = 133 and DC = 83.
The use of CC is optional.
(iii) Invalid priority. If the XDLP receives a call
requestwithaconnectionpriorityvalueequal
to 2 through 254, the XDLP shall clear the
virtual circuit using DC = 66 and CC = 131.
The use of CC is optional.
(iv) Unsupported facility. If the XDLP receives
a call request with a request for a facility that
it cannot support, the XDLP shall clear the
virtual circuit usingDC= 65 andC= 131. The

CIVIL AVIATION
S.R.O. 32
use of CC is optional.
(v) Illegal calling DTE address. If the XDLP
receives a call request with an illegal calling
DTE address, the XDLP shall clear the vir-
tual circuit usingDC= 68 and CC= 141. The
use of CC is optional.
(vi) Illegal called DTE address. If the XDLP
receives a call request with an illegal called
DTE address, the XDLP shall clear the vir-
tual circuit usingDC= 67 and CC= 141. The
use of CC is optional.
(2) REFORMATTING PROCESS
Note.— The reformatting process is divided into two subprocesses:
uplink formatting and downlink formatting. For the ADLP, the
uplink process reformats Mode S packets into ISO 8208 packets
and the downlink process reformats ISO 8208 packets into Mode
S packets. For the GDLP, the uplink process reformats ISO 8208
packets into Mode S packets and the downlink process reformats
Mode S packets into ISO 8208 packets.
(a) CALL REQUEST BY ADLP
(i) Translation into Mode S packets
(aa) Translated packet format. Reception
by the ADLP reformatting process of
an ISO 8208 CALL REQUEST
packet from the local DCE shall result
in the generation of corresponding
Mode S CALL REQUEST by ADLP
packet(s) (as determined by S-bit
processingas follows:

CIVIL AVIATION
S.R.O. 32
DP:1
MP:1
SP:2
ST:2
FILL2:0 or 2 P:1
FILL:1
SN:6
CH:4
AM:4
AG:8
S:1
FS:2
F:1
LV:4
UD:v
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 1.
(ee) Supervisory type (ST). This field
shall be set to 0.
(ff) Priority (P). This field shall be set
to 0 for a low priority SVC and to 1
for a high priority SVC. The value
for this field shall be obtained from
the data transfer field of the priority
facility of the ISO 8208 packet, and
shall be set to 0 if the ISO 8208
packet does not contain the priority
facility or if a priority of 255 is
specified. The other fields of the
priority facility shall be ignored.
(gg) Sequence number (SN). For a
particular SVC, each packet shall
be numbered.

CIVIL AVIATION
S.R.O. 32
(hh) Channel number (CH). The
channel number shall be chosen
from the pool of SVC channel
numbers available to the ADLP.
The pool shall consist of 15 values
from 1 through 15. The highest
available channel number shall be
chosen from the pool. An available
channel shall be defined as one in
state p1. The correspondence
between the channel number used
by the Mode S subnetwork and the
number used by the DTE/DCE
interface shall be maintained while
the channel is active.
Note.— Also refer to Sub-paragraph (5)(1)(b) on channel pool
management.
(ii) Address, mobile (AM). This
address shall be the mobile DTE
sub-address in the range of 0 to 15.
The address shall be extracted
from the two least significant digits
of the calling DTE address con-
tained in the ISO 8208 packet and
converted to binary representation.
Note.— The 24-bit aircraft address is transferred within the
Mode S link layer.
(jj) Address, ground (AG). This
address shall be the ground DTE
address in the range of 0 to 255.
The address shall be extracted
from the called DTE address
contained in the ISO 8208 packet

CIVIL AVIATION
S.R.O. 32
and converted to binary representa-
tion.
(kk) Fill field. The fill field shall be used
to align subsequent data fields on
byte boundaries. When indicated as
“FILL:n”, the fill field shall be set
to a length of “n” bits. When
indicated as “FILL1: 0 or 6”, the fill
field shall be set to a length of 6
bits for a non-multiplexed packet in
a downlink SLM frame and 0 bit
for all other cases. When indicated
as “FILL2: 0 or 2”, the fill field
shall be set to a length of 0 bit for a
non-multiplexed packet in a
downlink SLM frame or for a
multiplexing header and 2 bits for
all other cases.
(ll) S field (S). A value of 1 shall
indicate that the packet is part of
an S-bit sequence with more
packets in the sequence to follow.
A value of 0 shall indicate that the
sequence ends with this packet.
This field shall be set as specified
in Sub-paragraph (5)(1)(d)(ii).
(mm) FS field (FS). A value of 0 shall
indicate that the packet does not
contain fast select data. A value of
2 or 3 shall indicate that the packet
contains fast select data. A value
of 2 shall indicate normal fast
select operation. A value of 3 shall
indicate fast select with restricted

CIVIL AVIATION
S.R.O. 32
response. An FS value of 1 shall be
undefined.
(nn) First packet flag (F). This field
shall be set to 0 in the first packet
of an S-bit sequence and in a
packet that is not part of an S-bit
sequence. Otherwise it shall be set
to 1.
(oo) User data length (LV). This field
shall indicate the number of full
bytes used in the last SLM or ELM
segment as defined in Sub-para-
graph (2)(3)(a).
(pp) User data field (UD). This field
shall only be present if optional
CALL REQUEST user data
(maximum 16 bytes) or fast select
user data (maximum 128 bytes) is
contained in the ISO 8208 packet.
The user data field shall be trans-
ferred from ISO 8208 packet
unchanged using S-bit processing
as specified in Sub-Paragraph
(5)(1)(d)(ii).
(ii) Translation into ISO 8208 packets
(aa) Translation. Reception by the
GDLP reformatting process of a
Mode S CALL REQUEST by
ADLP packet (or an S-bit se-
quence of packets) from the
GDCE shall result in the generation
of a corresponding ISO 8208

CIVIL AVIATION
S.R.O. 32
CALL REQUEST packet to the
local DCE. The translation from the
Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(1)(2)(a)(i) with the
exceptions as specified in Sub-
paragraph (5)(2)(a)(ii)(bb).
(bb) Called DTE, calling DTE address
and length fields. The calling DTE
address shall be composed of the
aircraft address and the value
contained in the AM field of the
Mode S packet, converted to BCD.
The called DTE address shall be
the ground DTE address contained
in the AG field of the Mode S
packet, converted to BCD. The
length field shall be as defined in
ISO 8208.
(b) CALL REQUEST BY GDLP
(i) Translation into Mode S packets
(aa) General. Reception by the GDLP
reformatting process of an ISO
8208 CALL REQUEST packet
from the local DCE shall result in
the generation of corresponding
Mode S CALL REQUEST by
GDLP packet(s) (as determined by
S-bit processing (5)(1)(d)(ii)) as
follows:

CIVIL AVIATION
S.R.O. 32
DP:1 MP:1 SP:2 ST:2 FILL:2
P:1 FILL:1
SN:6 FILL:2
TC:2 AM:4
AG:8
S:1
FS:2
F:1
LV:4 UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in Sub-paragraph
(5)(2)(a).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 1.
(ee) Supervisory type (ST). This field
shall be set to 0.
(ff) Temporary channel number field
(TC). This field shall be used to
distinguish multiplecallrequests
from a GDLP. The ADLP
reformatting process, upon receipt
of a temporary channel number,
shall assign a channel number from
those presently in the READY
state, p1.
(gg) Address, ground (AG). This
address shall be the ground DTE
address in the range of 0 to 255.
The address shall be extracted
from the calling DTE address

CIVIL AVIATION
S.R.O. 32
contained in the ISO 8208 packet
and converted to binary representa-
tion.
(hh) Address, mobile (AM). This
address shall be the mobile DTE
sub-address in the range of 0 to 15.
The address shall be extracted
from the two least significant digits
of the called DTE address con-
tained in the ISO 8208 packet and
converted to binary representation.
(ii) Translation into ISO 8208 packets
(aa) Translation. Reception by the
ADLP reformatting process of a
Mode S CALL REQUEST by
GDLP packet (or an S-bit se-
quence of packets) from the
ADCE shall result in the generation
of a corresponding ISO 8208
CALL REQUEST packet to the
local DCE. The translation from
the Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(2)(b)(i) with the excep-
tions as specified in Sub-paragraph
(5)(2)(b)(ii)(bb).
(bb) Called DTE, calling DTE address
and length fields. The called DTE
address shall be composed of the
aircraft address and the value
contained in the AM field of the
Mode S packet, converted to BCD.

CIVIL AVIATION
S.R.O. 32
The calling DTE address shall be
the ground DTE address contained
in the AG field of the Mode S
packet, converted to BCD. The
length field shall be as defined in
ISO 8208.
(c) CALL ACCEPT BY ADLP
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the ADLP reformatting
process of an ISO 8208 CALL
ACCEPT packet from the local
DCE shall result in the generation
of corresponding Mode S CALL
ACCEPT by ADLP packet(s) (as
determined by S-bit processing as
follows:
DP:1 MP:1 SP:2
ST:2 FILL2:0 or 2
TC:2 SN:6
CH:4 AM:4 AG:8 S:1
FILL:2
F:1
LV:4
UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in Sub-paragraph
(5)(2)(a).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.

CIVIL AVIATION
S.R.O. 32
(dd) Supervisory packet (SP). This
field shall be set to 1.
(ee) Supervisory type (ST). This field
shall be set to 1.
(ff) Temporary channel number (TC).
The TC value in the originating
Mode S CALL REQUEST by
GDLP packet shall be returned to
the GDLP along with the channel
number (CH) assigned by the
ADLP.
(gg) Channel number (CH). The field
shall be set equal to the channel
number assigned by the ADLP as
determined during the CALL
REQUEST procedures for the
Mode S connection.
(hh) Address, mobile and address,
ground. The AM and AG values
in the originating Mode S CALL
REQUEST by GDLP packet shall
be returned in these fields. When
present, DTE addresses in the ISO
8208 CALL ACCEPT packet shall
be ignored.
(ii) Translation into ISO 8208 packets
(aa) Translation. Reception by the
GDLP reformatting process of a
Mode S CALL ACCEPT by
ADLP packet (or an S-bit se-
quence of packets) from the

CIVIL AVIATION
S.R.O. 32
GDCE shall result in the generation
of a corresponding ISO 8208
CALL ACCEPT packet to the
local DCE. The translation from
the Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(3)(b)(i) with the excep-
tions as specified in Sub-paragraph
(5)(2)(c)(ii)(bb).
(bb) Called DTE, calling DTE address
and length fields. Where present,
the called DTE address shall be
composed of the aircraft address
and the value contained in the AM
field of the Mode S packet, con-
verted to BCD. Where present, the
calling DTE address shall be the
ground DTE address contained in
the AG field of the Mode S packet,
converted to BCD. The length field
shall be as defined in ISO 8208.
Note.— The called and calling DTE addresses are optional in the
corresponding ISO 8208 packet and are not required for correct
operation of the Mode S subnetwork.
(d) CALL ACCEPT BY GDLP
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the GDLP reformatting
process of an ISO 8208 CALL
ACCEPT packet from the local
DCE shall result in the generation

CIVIL AVIATION
S.R.O. 32
of corresponding Mode S CALL
ACCEPT by GDLP packet(s) (as
determined by S-bit processing as
follows:
DP:1
MP:1
SP:2
ST:2
FILL:2
FILL:2 SN:6 CH:4
AM:4 AG:8
S:1
FILL:2
F:1
LV:4
UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in Sub-paragraph
(5)(2)(a).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 1.
(ee) Supervisory type (ST). This field
shall be set to 1.
(ff) Address, mobile and address,
ground. The AM and AG values
in the originating Mode S CALL
REQUEST by ADLP packet shall
be returned in these fields. When
present, DTE addresses in the ISO
8208 CALL ACCEPT packet shall
be ignored.
(ii) Translation into ISO 8208 packets

CIVIL AVIATION
S.R.O. 32
(aa) Translation. Reception by the
ADLP reformatting process of a
Mode S CALL ACCEPT by
GDLP packet (or an S-bit se-
quence of packets) from the
ADCE shall result in the generation
of a corresponding ISO 8208
CALL ACCEPT packet to the
local DCE. The translation from
the Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(2)(d)(i) with the excep-
tions as specified in Sub-paragraph
(5)(2)(d)(ii)(bb).
(bb) Called DTE, calling DTE address
and length fields. Where present,
the calling DTE address shall be
composed of the aircraft address
and the value contained in the AM
field of the Mode S packet, con-
verted to BCD. Where present, the
called DTE address shall be the
ground DTE address contained in
the AG field of the Mode S packet,
converted to BCD. The length field
shall be as defined in ISO 8208.
Note.— The called and calling DTE addresses are optional in the
corresponding ISO 8208 packet and are not required for correct
operation of the Mode S subnetwork.
(e) CLEAR REQUEST BY ADLP
(i) Translation into Mode S packets

CIVIL AVIATION
S.R.O. 32
(aa) Translated packet format. Recep-
tion by the ADLP reformatting
process of an ISO 8208 CLEAR
REQUEST packet from the local
DCE shall result in the generation
of a corresponding Mode S
CLEAR REQUEST by ADLP
packet(s) (as determined by S-bit
processing as follows:
DP:1 MP:1 SP:2 ST:2
FILL2:0 or 2 TC:2
SN:6
CH:4
AM:4 AG:8 CC:8 DC:8 S:1
FILL:2
F:1
LV:4
UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in Sub-paragraphs
(5)(2)(a) and (5)(2)(b).
(bb) Data packet type (DP). This field shall
be set to 0.
(cc) MSP packet type (MP). This field shall
be set to 1.
(dd) Supervisory packet (SP). This field shall
be set to 1.
(ee) Channel number (CH): If a channel
number has been allocated during
the call acceptance phase, then CH
shall be set to that value, otherwise
it shall be set to zero.
(ff)Temporary channel (TC): If a channel
number has been allocated during
the call acceptance phase, then TC

CIVIL AVIATION
S.R.O. 32
shall be set to zero, otherwise it
shall be set to the value used in the
CALL REQUEST by GDLP.
(gg) Supervisory type (ST). This field
shall be set to 2.
(hh) Address, ground or address,
mobile. The AG and AM values in
the originating Mode S CALL
REQUEST by ADLP or CALL
REQUEST by GDLP packets shall
be returned in these fields. When
present, DTE addresses in the ISO
8208 CLEAR REQUEST packet
shall be ignored.
(ii) Clearing cause (CC) and diag-
nostic code (DC) fields. These
fields shall be transferred without
modification from the ISO 8208
packet to the Mode S packet when
the DTE has initiated the clear
procedure. If the XDLP has
initiated the clear procedure, the
clearing cause field and diagnostic
field shall be as defined in the state
tables for the DCE and XDCE .
The coding and definition of these
fields shall be as specified in ISO
8208.
(ii) Translation into ISO 8208 packets
(aa) Translation. Reception by the
GDLP reformatting process of a
Mode S CLEAR REQUEST by

CIVIL AVIATION
S.R.O. 32
ADLP packet (or an S-bit se-
quence of packets) from the local
GDCE shall result in the generation
of a corresponding ISO 8208
CLEAR REQUEST packet to the
local DCE. The translation from the
Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(2)(e)(i) with the excep-
tions specified in Sub-paragraphs
(5)(2)(e)(ii)(bb) and (cc).
(bb) Called DTE, calling DTE and
length fields. These fields shall be
omitted in the ISO 8208 CLEAR
REQUEST packet.
(cc) Clearing cause field. This field
shall be set taking account of Sub-
paragraph (6)(3)(c).
(f) CLEAR REQUEST BY GDLP
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the GDLP reformatting
process of an ISO 8208 CLEAR
REQUEST packet from the local
DCE shall result in the generation
of corresponding Mode S CLEAR
REQUEST by GDLP packet(s) (as
determined by S-bit processing as
follows:

CIVIL AVIATION
S.R.O. 32
DP:1 MP:1 SP:2
ST:2
FILL:2 TC:2 SN:6 CH:4 AM:4
AG:8 CC:8 DC:8 S:1
FILL:2
F:1
LV:4 UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in Sub-paragraphs
(5)(2)(a), (5)(2)(b) and (5)(2)(e).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 1.
(ee) Channel number (CH): If a
channel number has been allocated
during the call acceptance phase,
then CH shall be set to that value,
otherwise it shall be set to zero.
(ff) Temporary channel (TC): If a
channel number has been allocated
during the call acceptance phase,
then TC shall be set to zero,
otherwise it shall be set to the value
used in the CALL REQUEST by
GDLP.
(gg) Supervisory type (ST). This field
shall be set to 2.
(ii) Translation into ISO 8208 packets

CIVIL AVIATION
S.R.O. 32
(aa) Translation. Reception by the
ADLP reformatting process of a
Mode S CLEAR REQUEST by
GDLP packet (or an S-bit se-
quence of packets) from the local
ADCE shall result in the generation
of a corresponding ISO 8208
CLEAR REQUEST packet to the
local DCE. The translation from
the Mode S packet to the ISO 8208
packet shall be the inverse of the
processing defined in Sub-para-
graph (5)(2)(f)(i).
(bb) Called DTE, calling DTE and
length fields. These fields shall be
omitted in the ISO 8208 CLEAR
REQUEST packet.
(g) DATA
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the XDLP reformatting
process of ISO 8208 DATA
packet(s) from the local DCE shall
result in the generation of corre-
sponding Mode S DATA packet(s)
as determined by M-bit processing,
as follows:
DP:1 M:1 SN:6 FILL1:0 or 6
PS:4 PR:4
CH:4 LV:4 UD:v

CIVIL AVIATION
S.R.O. 32
(bb) Data packet type (DP). This field
shall be set to 1.
(cc) M field (M). A value of 1 shall
indicate that the packet is part of
an M-bit sequence with more
packets in the sequence to follow.
A value of 0 shall indicate that the
sequence ends with this packet.
The appropriate value shall be
placed in the M-bit field of the
Mode S packet.
Note.— See (5)(1)(d) and ISO 8208 for a complete explana-
tion.
(dd) Sequence number (SN). The
sequence number field shall be set
as specified in (5)(2)(a)(i)(gg).
(ee) Packet send sequence number
(PS). The packet send sequence
number field shall be set as speci-
fied in Sub-regulation (6)(4)(d).
(ff) Packet receive sequence number
(PR). The packet receive sequence
number field shall be set as speci-
fied in Sub-regulation (6)(4)(d).
(gg) Channel number (CH). The
channel number field shall contain
the Mode S channel number that
corresponds to the incoming ISO
8208 DATA packet channel
number.

CIVIL AVIATION
S.R.O. 32
(hh) User data length (LV). This field
shall indicate the number of full
bytes used in the last SLM or ELM
segment as defined in (2)(3)(a).
(ii) Fill (FILL1). This field shall be set
as specified in Sub-paragraph
(5)(2)(a)(i)(kk).
(jj) User data (UD). The user data
shall be transferred from the ISO
8208 packet to the Mode S packet
utilizing the M-bit packet assembly
processing as required.
(ii) Translation into ISO 8208 packets. Re-
ception by the XDLP reformatting process of
Mode S DATA packet(s) from the local
XDCE shall result in the generation of corre-
sponding ISO 8208 DATA packet(s) to the
local DCE. The translation from Mode S
packet(s) to the ISO 8208 packet(s) shall be
the inverse of the processing defined in
(5)(2)(g)(i).
(h) INTERRUPT
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the XDLP reformatting
process of an ISO 8208 INTER-
RUPT packet from the local DCE
shall result in the generation of
corresponding Mode S INTER-
RUPT packet(s) (as determined by
S-bit processing  as follows:

CIVIL AVIATION
S.R.O. 32
DP:1 MP:1 SP:2 ST:2 FILL2:0 or 2
S:1 F:1 SN:6 CH:4
 LV:4 UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 3.
(ee) Supervisory type (ST). This field
shall be set to 1.
(ff) User data length (LV). This field
shall be set as specified in
(2)(3)(a).
(gg) User data (UD). The user data
shall be transferred from the ISO
8208 packet to the Mode S packet
using the S-bit packet reassembly
processing as required. The maxi-
mum size of the user data field for
an INTERRUPT packet shall be
32 bytes.
(ii) Translation into ISO 8208 packets. Re-
ception by the XDLP reformatting process of
Mode S INTERRUPT packet(s) from the
local XDCE shall result in the generation ofa

CIVIL AVIATION
S.R.O. 32
corresponding ISO 8208 INTERRUPT
packet to the local DCE. The translation from
the Mode S packet(s) to the ISO 8208 packet
shall be the inverse of the processing defined
in (5)(2)(h)(i).
(i) INTERRUPT CONFIRMATION
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the XDLP reformatting
process of an ISO 8208 INTER-
RUPT CONFIRMATION packet
from the local DCE shall result in
the generation of a corresponding
Mode S INTERRUPT CONFIR-
MATION packet as follows:
DP:1 MP:1 SP:2 ST:2
SS:2 FILL2:0 or 2
SN:6
CH:4
FILL:4
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a).
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 3.

CIVIL AVIATION
S.R.O. 32
(ee) Supervisory type (ST). This field
shall be set to 3.
(ff) Supervisory subset (SS). This field
shall be set to 0.
(ii) Translation into ISO 8208 packets. Re-
ceptionbytheXDLPreformattingprocessof
a Mode S INTERRUPT CONFIRMATION
packet from the local XDCE shall result in the
generation of a corresponding ISO 8208 IN-
TERRUPT CONFIRMATION packet to
the local DCE. The translation from the
Mode S packet to the ISO 8208 packet shall
be the inverse of the processing defined in
Sub-paragraph (5)(2)(i)(i).
(j) RESET REQUEST
(i) Translation into Mode S packets
(aa) Translated packet format. Recep-
tion by the XDLP reformatting
process of an ISO 8208 RESET
REQUEST packet from the local
DCE shall result in the generation
of a corresponding Mode S RESET
REQUEST packet as follows:
DP:1
MP:1 SP:2 ST:2
FILL2:0 or 2 FILL:2
SN:6
CH:4
FILL:4
RC:8 DC:8
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a).

CIVIL AVIATION
S.R.O. 32
(bb) Data packet type (DP). This field
shall be set to 0.
(cc) MSP packet type (MP). This field
shall be set to 1.
(dd) Supervisory packet (SP). This
field shall be set to 2.
(ee) Supervisory type (ST). This field
shall be set to 2.
(ff) Reset cause code (RC) and
diagnostic code (DC). The reset
cause and diagnostic codes used in
the Mode S RESET REQUEST
packet shall be as specified in the
ISO 8208 packet when the reset
procedure is initiated by the DTE.
If the reset procedure originates
with the DCE, the DCE state
tables shall specify the diagnostic
fields coding. In this case, bit 8 of
the reset cause field shall be set to
0.
(ii) Translation into ISO 8208 packets. Re-
ception by the XDLP reformatting process of
a Mode S RESET packet from the local
XDCE shall result in the generation of a
corresponding ISO 8208 RESET packet to
the local DCE. The translation from the
Mode S packet to the ISO 8208 packet shall
be the inverse of the processing defined in
Sub-paragraph (5)(2)(j)(i).

CIVIL AVIATION
S.R.O. 32
(k) ISO 8208 RESTART REQUEST to Mode S
CLEAR REQUEST. The receipt of an ISO 8208
RESTART REQUEST from the local DCE shall
result in the reformatting process generating a
Mode S CLEAR REQUEST by ADLP or Mode
S CLEAR REQUEST by GDLP for all SVCs
associated with the requesting DTE. The fields of
the Mode S CLEAR REQUEST packets shall be
set as specified in (5)(2)(e) and (5)(2)(f).
Note.— There are no restart states in the Mode S packet layer
protocol.
(3) PACKETS LOCAL TO THE MODE S SUBNETWORK
Note.— Packets defined in this section do not result in the
generation of an ISO 8208 packet.
(a) MODE S RECEIVE READY
(i) Packet format. The Mode S RECEIVE
READY packet arriving from an XDLP is
not related to the control of the DTE/DCE
interface and shall not cause the generation
of an ISO 8208 packet. The format of the
packet shall be as follows:
DP:1 MP:1 SP:2
ST:2 FILL2:0 or 2
FILL:2
SN:6
CH:4 PR:4
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a). The
packet shall be processed as specified in Sub-paragraph (6)(5).
(ii) Data packet type (DP). This field shall be
set to 0.

CIVIL AVIATION
S.R.O. 32
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 2.
(v) Supervisory type (ST). This field shall be set
to 0.
(vi) Packet receive sequence number (PR).
Thisfieldshallbesetasspecifiedin (6)(4)(d).
(b) MODE S RECEIVE NOT READY
(i) Packet format. The Mode S RECEIVE
NOT READY packet arriving from an XDLP
is not related to the control of the DTE/DCE
interface and shall not cause the generation
of an ISO 8208 packet. The format of the
packet shall be as follows:
DP:1
MP:1 SP:2 ST:2 FILL2:0 or 2 FILL:2
SN:6
CH:4
PR:4
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a). The
packet shall be processed as specified in Sub-paragraph (6)(6).
(ii) Data packet type (DP). This field shall be
set to 0.
(iii) MSP packet type (MP). This field shall be
set to 1.

CIVIL AVIATION
S.R.O. 32
(iv) Supervisory packet (SP). This field shall be
set to 2.
(v) Supervisory type (ST). This field shall be set
to 1.
(vi) Packet receive sequence number (PR).
Thisfieldshallbesetasspecifiedin (6)(4)(d).
(c) MODE S ROUTE
(i) Packet format. The format for the packet
shall be as follows:
DP:1
MP:1
SP:2 ST:2 OF:1 IN:1 RTL:8
RT:v
ODL:0 or 8
OD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a). The
packet shall only be generated by the GDLP. It shall be processed
by the ADLP as specified in (8)(1)(b) and shall have a maximum
size as specified in (6)(4)(b)(i).
(ii) Data packet type (DP). This field shall be
set to 0.
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 3.
(v) Supervisory type (ST). This field shall be set
to 0.

CIVIL AVIATION
S.R.O. 32
(vi) Option flag (OF).This field shall indicate the
presence of the optional data length (ODL)
and optional data (OD) fields. OF shall be set
to 1 if ODL and OD are present. Otherwise
it shall be set to 0.
(vii) Initialization bit (IN).This field shall indicate
the requirement for subnetwork initialization.
It shall be set by the GDLP as specified in
(8)(1)(b)(d).
Note.— Initialization causes the clearing of any open SVCs
associated with the DTE addresses contained in the ROUTE
packet. This is needed to assure that all channels are closed at
acquisition and for initialization following recovery after a GDLP
failure.
(viii) Route table length (RTL). This field shall
indicate the size of the route table, expressed
in bytes.
(ix) Route table (RT)
(aa) Contents. This table shall consist of
a variable number of entries each
containing information specifying
the addition or deletion of entries in
the II code-DTE cross-reference
table.
(bb) Entries. Each entry in the route
table shall consist of the II code, a
list of up to 8 ground DTE ad-
dresses, and a flag indicating
whether the resulting II code-DTE
pairs shall be added or deleted from
the II code-DTE cross-reference

CIVIL AVIATION
S.R.O. 32
table. A route table entry shall be
coded as follows:
II:4
AD:1
ND:3
DAL:v
(cc) Interrogator identifier (II). This
field shall contain the 4-bit II code.
(dd) Add/delete flag (AD). This field
shall indicate whether the II code-
DTE pairs shall be added (AD = 1)
or deleted (AD = 0) from the II
code-DTE cross-reference table.
(ee) Number of DTE addresses (ND).
This field shall be expressed in
binary in the range from 0 to 7 and
shall indicate the number of DTE
addresses present in DAL minus 1
(in order to allow from 1 to 8 DTE
addresses).
(ff) DTE address list (DAL). This list
shall consist of up to 8 DTE ad-
dresses, expressed in 8-bit binary
representation.
(gg) Optional data length (ODL). This
field shall containthe lengthin
bytes of the following OD field.
(hh) Optional data (OD). This variable
length field shall contain optional
data.
(d) MODE S CLEAR CONFIRMATION BY ADLP

CIVIL AVIATION
S.R.O. 32
(i) Packet format. The format for this packet
shall be as follows:
DP:1 MP:1 SP:2 ST:2
FILL2:0 or 2
TC:2
SN:6
CH:4 AM:4 AG:8
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a) and
(5)(2)(e). This packet shall be processed as specified in Sub-
paragraph (6)(3)
(ii) Data packet type (DP). This field shall be
set to 0.
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 1.
(v) Channel number (CH): If a channel number
has been allocated during the call acceptance
phase, then CH shall be set to that value,
otherwise it shall be set to zero.
(vi) Temporary channel (TC): If a channel
number has been allocated during the call
acceptance phase, then TC shall be set to
zero, otherwise it shall be set to the value used
in the CALL REQUEST by GDLP.
(vii) Supervisory type (ST). This field shall be set
to 3.
(e) MODE S CLEAR CONFIRMATION BY GDLP

CIVIL AVIATION
S.R.O. 32
(i) Packet format. The format for this packet
shall be as follows:
DP:1 MP:1
SP:2
ST:2
FILL:2
TC:2
SN:6
CH:4
AM:4 AG:8
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a) and
(5)(2)(f). This packet shall be processed as specified in (6)(3).
(ii) Data packet type (DP). This field shall be
set to 0.
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 1.
(v) Channel number (CH): If a channel number
has been allocated during the call acceptance
phase, then CH shall be set to that value,
otherwise it shall be set to zero.
(vi) Temporary channel (TC): If a channel
number has been allocated during the call
acceptance phase, then TC shall be set to
zero, otherwise it shall be set to the value used
in the CALL REQUEST by GDLP.
(vii) Supervisory type (ST). This field shall be set
to 3.
(f) MODE S RESET CONFIRMATION

CIVIL AVIATION
S.R.O. 32
(i) Packet format. The format for this packet
shall be as follows:
DP:1 MP:1 SP:2
ST:2 FILL2:0 or 2
FILL:2
SN:6
CH:4 FILL:4
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a). This
packet shall be processed as specified in Table 5-14.
(ii) Data packet type (DP). This field shall be
set to 0.
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 2.
(v) Supervisory type (ST). This field shall be set
to 3.
(g) MODE S REJECT
(i) Packet format. The format for this packet
shall be as follows:
DP:1 MP:1 SP:2 ST:2 SS:2 FILL2:0 or 2 SN:6 CH:4 PR:4
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a). This
packet shall be processed as specified in (6)(8).
(ii) Data packet type (DP). This field shall be
set to 0.

CIVIL AVIATION
S.R.O. 32
(iii) MSP packet type (MP). This field shall be
set to 1.
(iv) Supervisory packet (SP). This field shall be
set to 3.
(v) Supervisory type (ST). This field shall be set
to 3.
(vi) Supervisory subset (SS). This field shall be
set to 1.
(vii) Packet receive sequence number (PR).
Thisfieldshallbesetasspecifiedin (6)(4)(d).
(6)
XDCE operation
Note.— The ADCE process within the ADLP acts as a peer
process to the GDCE process in the GDLP.
(1) State transitions. The XDCE shall operate as a state
machine. Upon entering a state, the XDCE shall perform the
actionsspecifiedinTable5-14 of Schedule 5.Statetransitionand
additional action(s) shall be as specified in Table 5-15 through
Table 5-22 of Schedule 5.
Note 1.— The next state transition (if any) that occurs when the
XDCE receives a packet from the peer XDCE is specified by
Table 5-15 through Table 5-19 of Schedule 5. The same transi-
tions are defined in Table 5-20 through Table 5-22 of Schedule 5
when the XDCE receives a packet from the DCE (via the
reformatting process).
Note 2.— The XDCE state hierarchy is the same as for the
DCE as presented in Figure 6-2 of Schedule 6, except that
states r2, r3 and p5 are omitted.

CIVIL AVIATION
S.R.O. 32
(2) DISPOSITION OF PACKETS
(a) Upon receipt of a packet from the peer XDCE,
the packet shall be forwarded or not forwarded to
the DCE (via the reformatting process) accord-
ing to the parenthetical instructions contained in
Tables 5-15 to 5-19 of Schedule 5. If no paren-
thetical instruction is listed or if the parenthetical
instruction indicates “do not forward” the packet
shall be discarded.
(b) Upon receipt of a packet from the DCE (via the
reformatting process), the packet shall be for-
warded or not forwarded to the peer XDCE
according to the parenthetical instructions con-
tained in Tables 5-20 to 5-22 of Schedule 5. If no
parenthetical instruction is listed or if the paren-
thetical instruction indicates “do not forward” the
packet shall be discarded.
(3) SVC CALL SETUP AND CLEAR PROCEDURE
(a) Setup procedures. Upon receipt of a CALL
REQUEST from the DCE or peer XDCE, the
XDLP shall determine if sufficient resources
exist to operate the SVC. This shall include:
sufficient buffer space (refer to (5)(1)(a) for
buffer requirements) and an available p1 state
SVC. Upon acceptance of the CALL REQUEST
from the DCE (via the reformatting process), the
Mode S CALL REQUEST packet shall be for-
warded to frame processing. Upon acceptance
of a Mode S CALL REQUEST from the peer
XDCE (via frame processing), the Mode S CALL
REQUEST shall be sent to the reformatting
process.

CIVIL AVIATION
S.R.O. 32
(b) Aborting a call request. If the DTE and/or the
peer XDCE abort a call before they have
received(a)
a CALL ACCEPT packet, they
shall indicate this condition by issuing a CLEAR
REQUEST packet. Procedures for handling these
cases shall be as specified in Table 5-16 and
Table 5-20 of Schedule 5.
(C) VIRTUAL CALL CLEARING
(i) If the XDCE receives a Mode S CALL
REQUEST from the reformatting process
that it cannot support, it shall initiate a Mode
S CLEAR REQUEST packet that is sent to
the DCE (via the reformatting process) for
transfer to the DTE (the DCE thus enters the
DCE CLEAR REQUEST to DTE state, p7).
(ii) If the XDCE receives a Mode S CALL
REQUEST packet from the peer XDCE (via
frame processing) which it cannot support, it
shall enter the state p7.
(iii) Ameansshall beprovided to advise theDTE
whether an SVC has been cleared due to the
action of the peer DTE or due to a problem
within the subnetwork itself.
(iv) The requirement of (6)(3)(c)(iii) should be
satisfied by setting bit 8 of the cause field
to 1 to indicate that the problem originated
in the Mode S subnetwork and not in the
DTE. The diagnostic and cause codes
should be set as follows:
a)
no channel number available, DC = 71, CC = 133;

CIVIL AVIATION
S.R.O. 32
b)
buffer space not available, DC = 71, CC = 133;
c)
DTE not operational, DC = 162, CC = 141; and
d)
link failure, DC = 225, CC = 137.
(v) If the ADLP receives a Mode S ROUTE
packet with the IN bit set to ONE, the ADLP
shall perform local initialization by clearing
Mode S SVCs associated with the DTE
addresses contained in the ROUTE packet.
If the GDLP receives a search request (Ta-
ble 5-23) from an ADLP, the GDLP shall
perform local initialization by clearing Mode S
SVCs associated with that ADLP. Local
initialization shall be accomplished by:
a)
releasing all allocated resources associated with these
SVCs (including the resequencing buffers);
b)
returning these SVCs to the ADCE ready state (p1);
and
c)
sending Mode S CLEAR REQUEST packets for these
SVCs to the DCE (via the reformatting process) for transfer
to the DTE.
Note.— This action will allow all ISO 8208 SVCs attached to
the Mode S SVCs to be cleared and return to their ready states
(p1).
(d)
Clear confirmation. When the XDCE receives a
Mode S CLEAR CONFIRMATION packet, the remaining
allocated resources to manage the SVC shall be released
(including the resequencing buffers) and the SVC shall be
returned to the p1 state. Mode S CLEAR CONFIRMATION

CIVIL AVIATION
S.R.O. 32
packets shall not be transferred to the reformatting process.
(e) Clear collision. A clear collision occurs at the
XDCE when it receives a Mode S CLEAR
REQUEST packet from the DCE (via the
reformatting process) and then receives a Mode
S CLEAR REQUEST packet from the peer
XDCE (or vice versa). In this event, the XDCE
does not expect to receive a Mode S CLEAR
CONFIRMATION packet for this SVC and
shall consider the clearing complete.
(f) Packet processing. The XDCE shall treat an S-
bit sequence of Mode S CALL REQUEST,
CALL ACCEPT and CLEAR REQUEST pack-
ets as a single entity.
(4) DATA TRANSFER AND INTERRUPT PROCEDURES
(a) GENERAL PROVISIONS
(i) Data transfer and interrupt procedures shall
apply independently to each SVC. The con-
tents of the user data field shall be passed
transparently to the DCE or to the peer
XDCE. Data shall be transferred in the order
dictated by the sequence numbers assigned
to the data packets.
(ii) To transfer DATApackets, the SVC shall be
in a FLOW CONTROL READY state (d1).
(b) MODE S PACKET SIZE
(i) The maximum size of Mode S packets shall
be 152 bytes in the uplink direction and 160

CIVIL AVIATION
S.R.O. 32
bytes in the downlink direction for installa-
tions that have full uplink and downlink ELM
capability. The maximum downlink packet
size forlevelfourtransponderswith lessthan
16segmentdownlink ELMcapabilityshallbe
10 bytes times the maximum number of
downlink ELM segments that the transponder
specifies in its data link capability report. If
there is no ELM capability, the maximum
Mode S packet size shall be 28 bytes.
(ii) The Mode S subnetwork shall allow packets
of less than the maximum size to be trans-
ferred.
(C) FLOW CONTROL WINDOW SIZE
(i) The flow control window size of the Mode S
subnetwork shall be independent of that used
on the DTE/DCE interface. The Mode S
subnetwork window size shall be 15 packets
in the uplink and downlink directions.
(d) SVC FLOW CONTROL
(i) Flow control shall be managed by means of a
sequence number for received packets (PR)
and one for packets that have been sent (PS).
A sequence number (PS) shall be assigned
for each Mode S DATA packet generated by
the XDLP for each SVC. The first Mode S
DATA packet transferred by the XDCE to
frame processing when the SVC has just
entered the flow control ready state shall be
numbered zero. The first Mode S packet
received from the peer XDCE after an SVC
has just entered the flow control ready state

CIVIL AVIATION
S.R.O. 32
shall be numbered zero. Subsequent packets
shall be numbered consecutively.
(ii) A source of Mode S DATA packets (the
ADCE or GDCE) shall not send (without
permission from the receiver) more Mode S
DATA packets than would fill the flow con-
trol window. The receiver shall give explicit
permission to send more packets.
(iii) The permission information shall be in the
form of the next expected packet sequence
number and shall be denoted PR. If a receiver
wishes to update the window and it has data
to transmit to the sender, a Mode S DATA
packet shall be used for information transfer.
If the window must be updated and no data
are to be sent, a Mode S RECEIVE READY
(RR) or Mode S RECEIVE NOT READY
(RNR) packet shall be sent. At this point, the
“sliding window” shall be moved to begin at
the new PR value. The XDCE shall now be
authorized to transfer more packets without
acknowledgement up to the window limit.
(iv) When the sequence number (PS) of the next
Mode S DATA packet to be sent is in the
range PR d” PS d” PR + 14 (modulo 16), the
sequence number shall be defined to be “in
the window” and the XDCE shall be author-
ized to transmit the packet. Otherwise, the
sequence number (PS) of the packet shall be
defined to be “outside the window” and the
XDCE shall not transmit the packet to the
peer XDCE.

CIVIL AVIATION
S.R.O. 32
(v) When the sequence number (PS) of the
packet received is next in sequence and
within the window, the XDCE shall accept
this packet. Receipt of a packet with a PS:
a)
outside the window; or
b)
out of sequence; or
c)
not equal to 0 for the first data packet after entering
FLOW CONTROL READY state (d1); shall be considered
an error ((6)(8)).
(vi) The receipt of a Mode S DATA packet with
a valid PS number (i.e. the next PS in se-
quence) shall cause the lower window PR to
be changed to that PS value plus 1. The
packet receive sequence number (PR) shall
be conveyed to the originating XDLP by a
Mode S DATA, RECEIVE READY, RE-
CEIVE NOT READY, or REJECT packet.
A valid PR value shall be transmitted by the
XDCE to the peer XDCE after the receipt of
8 packets provided that sufficient buffer space
exists to store 15 packets. Incrementing the
PR and PS fields shall be performed using
modulo 16 arithmetic.
Note.— The loss of a packet which contains the PR value may
cause the ADLP/GDLP operations for that SVC to cease.
(vii) A copy of a packet shall be retained until the
user data has been successfully transferred.
Following successful transfer, the PS value
shall be updated.
(viii) The PR value for user data shall be updated

CIVIL AVIATION
S.R.O. 32
as soon as the required buffer space for the
window (as determined by flow control man-
agement) is available within the DCE.
(ix) Flow control management shall be provided
between the DCE and XDCE.
(e) INTERRUPT PROCEDURES FOR SWITCHED
VIRTUAL CIRCUITS
(i) If user data is to be sent via the Mode S
subnetwork without following the flow con-
trol procedures, the interrupt procedures shall
be used. The interrupt procedure shall have
no effect on the normal data packet and flow
control procedures.Aninterruptpacketshall
be delivered to the DTE (or the transponder
or interrogator interface) at or before the
point in the stream of data at which the
interrupt was generated. The processing of a
Mode S INTERRUPT packet shall occur as
soon as it is received by the XDCE.
Note.— The use of clear, reset, and restart procedures can cause
interrupt data to be lost.
(ii) The XDCE shall treat an S-bit sequence of
Mode S INTERRUPT packets as a single
entity.
(iii) Interrupt processing shall have precedence
over any other processing for the SVC occur-
ring at the time of the interrupt.
(iv) The reception of a Mode S INTERRUPT
packet before the previous interrupt of the
SVC has been confirmed (by the receipt of a

CIVIL AVIATION
S.R.O. 32
Mode S INTERRUPT CONFIRMATION
packet)shallbedefinedasanerror.Theerror
results in a reset (see Table 5-18).
(5) RECEIVE READY PROCEDURE
(a) The Mode S RECEIVE READY packet shall be
sent if no Mode S DATA packets (that normally
contain the updated PR value) are available for
transmittal and it is necessary to transfer the
latest PR value. It also shall be sent to terminate
a receiver not ready condition.
(b) Receipt of the Mode S RECEIVE READY
packet by the XDCE shall cause the XDCE to
update its value of PR for the outgoing SVC. It
shall not be taken as a demand for retransmission
of packets that have already been transmitted
and are still in the window.
(c) Upon receipt of the Mode S RECEIVE READY
packet, the XDCE shall go into the ADLP(GDLP)
RECEIVE READY state (g1).
(6) RECEIVE NOT READY PROCEDURE
(a) The Mode S RECEIVE NOT READY packet
shall be used to indicate a temporary inability to
accept additional DATA packets for the given
SVC. The Mode S RNR condition shall be cleared
by the receipt of a Mode S RR packet or a Mode
S REJECT packet.
(b) When the XDCE receives a Mode S RECEIVE
NOT READY packet from the peer XDCE, it
shall update its value of PR for the SVC and stop

CIVIL AVIATION
S.R.O. 32
transmitting Mode S DATA packets on the SVC
to the XDLP. The XDCE shall go into the
ADLP(GDLP) RECEIVE NOT READY state
(g2).
(c) The XDCE shall transmit a Mode S RECEIVE
NOT READY packet to the peer XDCE if it is
unable to receive from the peer XDCE any more
Mode S DATA packets on the indicated SVC.
Under these conditions, the XDCE shall go into
the ADCE(GDCE) RECEIVE NOT
READY state (f2).
(7) RESET PROCEDURE
(a) When the XDCE receives a Mode S RESET
REQUEST packet from either the peer XDCE or
the DCE (via the reformatting process) or due to
an error condition performs its own reset, the
following actions shall be taken:
a)
those Mode S DATA packets that have been transmit-
ted to the peer XDCE shall be removed from the window;
b)
those Mode S DATA packets that are not transmitted to
the peer XDCE but are contained in an M-bit sequence for
which some packets have been transmitted shall be deleted
from the queue of DATA packets awaiting transmission;
c)
those Mode S DATA packets received from the peer
XDCE that are part of an incomplete M-bit sequence shall be
discarded;
d)
the lower window edge shall be set to 0 and the next
packet sent shall have a sequence number (PS) of 0;
e)
any outstanding Mode S INTERRUPT packets to or

CIVIL AVIATION
S.R.O. 32
from the peer XDCE shall be left unconfirmed;
f)
any Mode S INTERRUPT packet awaiting transfer
shall be discarded;
g)
data packets awaiting transfer shall not be discarded
(unless they are part of a partially transferred M-bit se-
quence); and
h)
the transition to d1 shall also include a transition to i1, j1,
f 1 and g1.
(b) The reset procedure shall apply to the DATA
TRANSFER state (p4). The error procedure in
Table 5-16 shall be followed. In any other state
the reset procedure shall be abandoned.
(8) REJECT PROCEDURE
(a) When the XDCE receives a Mode S DATA
packet from the peer XDCE with incorrect for-
mat or whose packet sequence number (PS) is
not within the defined window (Table 5-19 of
Schedule 5) or is out of sequence, it shall discard
the received packet and send a Mode S REJECT
packet to the peer XDCE via frame processing.
The Mode S REJECT packet shall indicate a
value of PR for which retransmission of the
Mode S DATA packets is to begin. The XDCE
shall discard subsequent out-of-sequence Mode
S DATA packets whose receipt occurs while the
Mode S REJECT packet response is still out-
standing.
(b) When the XDCE receives a Mode S REJECT
packet from the peer XDCE, it shall update its
lower window value with the new value of PR

CIVIL AVIATION
S.R.O. 32
and begin to (re)transmit packets with a se-
quence number of PR.
(c) Reject indications shall not be transferred to the
DCE. If the ISO 8208 interface supports the
reject procedures, the reject indications occur-
ring on the ISO 8208 interface shall not be
transferred between the DCE and the XDCE.
(9) PACKET RESEQUENCING AND DUPLICATE SUPPRESSION
Note 1.— If the frames for an SVC include both types (SLM and
ELM), the sequence of packets may be lost due to the different
delivery times. The order may also be lost if multiple interrogators
are used to deliver frames for the same SVC to a given XDLP.
The following procedure will correct for a limited amount of
desequencing.
Note 2.— This process serves as an interface between frame
processing and the XDCE function.
(a) Resequencing.Resequencing shall be performed
independently for the uplink and downlink trans-
fers of each Mode S SVC. The following vari-
ables and parameters shall be used:
SNRA 6-bit variable indicating the sequence number of a received
packet on a specific SVC. It is contained in the SN field of the
packet.
NESNThe next expected sequence number following a series of
consecutive sequence numbers.
HSNR
The highest value of SNR in the resequencing
window.

CIVIL AVIATION
S.R.O. 32
Tq
Resequencing timers (see Tables 5-1 and 5-13) associated
with a specific SVC.
All operations involving the sequence number (SN) shall be
performed modulo 64.
(b) Duplication window. The range of SNR values
betweenNESN– 32 andNESN –1 inclusive shall
be denoted the duplication window.
(c) Resequencing window. The range of SNR val-
ues between NESN + 1 and NESN + 31 inclusive
shall be denoted the resequencing window. Re-
ceived packets with a sequence number value in
this range shall be stored in the resequencing
window in sequence number order.
(d) TRANSMISSION FUNCTIONS
(i) For each SVC, the first packet sent to estab-
lish a connection (the first Mode S CALL
REQUEST or first Mode S CALL ACCEPT
packet) shall cause the value of the SN field
to be initialized to zero. The value of the SN
field shall be incremented after the transmis-
sion (or retransmission) of each packet.
(ii) The maximum number of unacknowledged
sequence numbers shall be 32 consecutive
SNnumbers. Should this condition be reached,
then it shall be treated as an error and the
channel cleared.
Note.— A limit on the number of unacknowledged packets is
required since the SN field is six bits long and therefore has a
maximum of 64 different values before the values repeat.

CIVIL AVIATION
S.R.O. 32
(e) RECEIVE FUNCTIONS
(i) Resequencing. The resequencing algorithm
shall maintain the variablesHSNRandNESN
for each SVC. NESN shall be initialized to 0
for all SVCs and shall be reset to 0 when the
SVC re-enters the channel number pool.
(ii) Processing of packets within the duplica-
tion window. If a packet is received with a
sequence number value within the duplication
window, the packet shall be discarded.
(iii) Processing of packets within the
resequencing window. If a packet is re-
ceived with a sequence number within the
resequencing window, it shall be discarded as
a duplicate if a packet with the same se-
quence number has already been received
and stored in the resequencing window. Oth-
erwise, the packet shall be stored in the
resequencing window. Then, if no Tq timers
are running, HSNRshall be set to the value of
SNR for this packet and a Tq timer shall be
started withits initial value (Tables 5-1 and 5-
13). If at least one Tq timer is running, and
SNR is not in the window between NESNand
HSNR + 1 inclusive, a new Tq timer shall be
started and the value of HSNR shall be
updated. If at least one Tq timer is running,
and SNR for this packet is equal to HSNR +
1, the value of HSNR shall be updated.
(iv) Release of packets to the XDCE. If a packet
is received with a sequence number equal to
NESN, the following procedure shall be ap-
plied:

CIVIL AVIATION
S.R.O. 32
a)
the packet and any packets already stored in the
resequencing window up to the next missing sequence number
shall be passed to the XDCE;
b)
NESN shall be set to 1 + the value of the sequence
number of the last packet passed to the XDCE; and
c)
the Tq timer associated with any of the released packets
shall be stopped.
(f) Tq timer expiration. If a Tq timer expires, the
followingprocedureshallbe applied:
a)
NESN shall be incremented until the next missing
sequence number is detected after that of the packet associ-
ated with the Tq timer that has expired;
b)
any stored packets with sequence numbers that are no
longer in the resequencing window shall be forwarded to the
XDCE except that an incomplete S-bit sequence shall be
discarded; and
c)
the Tq timer associated with any released packets shall
be stopped.
(7)
Mode S specific services processing
Mode S specific services shall be processed by an entity in the
XDLP termed the Mode S specific services entity (SSE). Trans-
ponder registers shall be used to convey the information specified
in Table 5-24 of Schedule 5. The data structuring of the registers
in Table 5-24 of Schedule 5 shall be implemented in such a way
that interoperability is ensured.
Note 1.— The data formats and protocols for messages trans-
ferredviaModeSspecificservicesarespecifiedintheTechnical

CIVIL AVIATION
S.R.O. 32
Provisions for Mode S Services and Extended Squitter (Doc
9871)(in preparation).
Note 2.— Uniform implementation of the data formats and
protocols for messages transferred via Mode S specific services
will ensure interoperability.
Note 3.— This section describes the processing of control and
message data received from the Mode S specific services
interface.
Note 4.— Control data consists of information permitting the
determination of, for example, message length, BDS code used to
access the data format for a particular register, and aircraft
address.
(1)
ADLP PROCESSING
(a) DOWNLINK PROCESSING
(i) Specific services capability. The ADLP shall
be capable of receiving control and message
data from the Mode S specific services
interface(s) and sending delivery notices to
this interface. The control data shall be proc-
essed to determine the protocol type and the
length of the message data. When the mes-
sage or control data provided at this interface
are erroneous (i.e. incomplete, invalid or in-
consistent), the ADLP shall discard the mes-
sage and deliver an error report at the inter-
face.
Note.— The diagnostic content and error reporting mechanism
are a local issue.

CIVIL AVIATION
S.R.O. 32
(ii) Broadcast processing. The control and mes-
sage data shall be used to format the Comm-
B broadcast message as specified in Sub-
paragraph (7)(5) and transferred to the trans-
ponder.
(iii) GICB processing. The 8-bit BDS code shall
be determined from the control data. The 7-
byte register content shall be extracted from
the received message data. The register con-
tent shall be transferred to the transponder,
along with an indication of the specified reg-
ister number. A request to address one of the
air-initiated Comm-B registers or the air-
borne collision avoidance system (ACAS)
active resolution advisories register shall be
discarded. The assignment of registers shall
be as specified in Table 5-24 of Schedule 5.
Note.— Provision of the data available in transponder registers
40, 50 and 60 {HEX} has been mandated in some ICAO Regions
in support of ATM applications.
(iv) MSP processing
(aa) The MSP message length, channel
number (M/CH) and optionally the
interrogator identifier (II) code
shall be determined from the
control data. The MSP message
content shall be extracted from the
received message data. If the
message length is 26 bytes or less,
the SSE shall format an air-initiated
Comm-B message for transfer to
the transponder using the short
form MSP packet. If the message

CIVIL AVIATION
S.R.O. 32
length is 27 to 159 bytes and the
transponder has adequate downlink
ELM capability, the SSE shall
format an ELM message for
transfer using the short form MSP
packet. If the message length is 27
to 159 bytes and the transponder
has a limited downlink ELM
capability, the SSE shall format
multiple long form MSP packets
using ELM messages, as required
utilizing the L-bit and M/SNfields
for association of the packets. If
the message length is 27 to 159
bytes and the transponder does not
have downlink ELM capability, the
SSE shall format multiple long form
MSP packets using air initiated
Comm-B messages, as required
utilizing the L-bit and M/SN fields
for association of the packets.
Different frame types shall never
be used in the delivery of an MSP
message. Messages longer than
159 bytes shall be discarded. The
assignment of downlink MSP
channel numbers shall be as
specified in Table 5-25 of Schedule
5.
(bb) For an MSP, a request to send a
packet shall cause the packet to be
multisite-directed to the interrogator
which II code is specified in control
data. If no II code is specified, the
packet shall be downlinked using
the air-initiated protocol. A mes-

CIVIL AVIATION
S.R.O. 32
sage delivery notice for this packet
shall be provided to the Mode S
specific interface when the corre-
sponding close-out(s) have been
received from the transponder. If a
close-out has not been received
from the transponder in Tz sec-
onds, as specified in Table 5-1 of
Schedule 5, the MSP packet shall
be discarded. This shall include the
cancellation in the transponder of
any frames associated with this
packet. A delivery failure notice for
this message shall be provided to
the Mode S specific services
interface.
(b) UPLINK PROCESSING
Note.—ThissectiondescribestheprocessingofModeSspecific
services messages received from the transponder.
(i) Specific services capability. The ADLP shall
be capable of receiving Mode S specific
services messages from the transponder via
frame processing. The ADLP shall be capa-
ble of delivering the messages and the asso-
ciated control data at the specific services
interface. When the resources allocated at
this interface are insufficient to accommo-
date the output data, the ADLP shall discard
the message and deliver an error report at this
interface.
Note.— The diagnostic content and the error reporting mecha-
nism are a local issue.

CIVIL AVIATION
S.R.O. 32
(ii) Broadcast processing. If the received mes-
sage is a broadcast Comm-A, as indicated by
control data received over the transponder/
ADLP interface, the broadcast ID and user
data shall be forwarded to the Mode S spe-
cific services interface along with the control
data that identifies this as a broadcast mes-
sage. The assignment of uplink broadcast
identifier numbers shall be as specified in
Table 5-23 of Schedule 5.
(iii) MSP processing. If the received message is
an MSP, as indicated by the packet format
header, the user data field of the received
MSP packet shall be forwarded to the Mode
S specific services interface together with
the MSP channel number (M/CH), the IIS
subfield together with control data that iden-
tifies this as an MSP message. L-bit process-
ing shall be performed as specified in Sub-
paragraph (7)(4). The assignment of uplink
MSP channel numbers shallbe as specified in
Table 5-25 of Schedule 5.
(2) GDLP PROCESSING
(a) UPLINK PROCESSING
(i) Specific services capability. The GDLP shall
be capable of receiving control and message
data from the Mode S specific services
interface(s) and sending delivery notices to
the interface(s). The control data shall be
processed to determine the protocol type and
the length of the message data.

CIVIL AVIATION
S.R.O. 32
(ii) Broadcast processing. The GDLP shall de-
termine the interrogator(s), broadcast azi-
muths and scan times from the control data
and format the broadcast message for trans-
fer to the interrogator(s) as specified in (7)(5).
(iii) GICB processing. The GDLP shall deter-
mine the register number and the aircraft
address from the control data. The aircraft
address and BDS code shall be passed to the
interrogator as a request for a ground-initi-
ated Comm-B.
(iv) MSP processing. The GDLP shall extract
from the control data the message length, the
MSP channel number (M/CH) and the air-
craft address, and obtain the message con-
tent from the message data. If the message
lengthis 27bytes or less, the SSE shall format
a Comm-A message for transfer to the inter-
rogator using the short form MSP packet. If
the message length is 28 to 151 bytes and the
transponder has uplink ELM capability, the
SSE shall format an ELM message for trans-
fer to the interrogator using the short form
MSP packet. If the message length is 28 to
151 bytes and the transponder does not have
uplink ELM capability, the SSE shall format
multiple long form MSP packets utilizing the
L-bit and the M/SN fields for association of
the packets. Messages longer than 151 bytes
shall be discarded. The interrogator shall
provide a delivery notice to the Mode S
specific services interface(s) indicating suc-
cessful or unsuccessful delivery, for each
uplinked packet.

CIVIL AVIATION
S.R.O. 32
(b) DOWNLINK PROCESSING
(i) Specific services capability. The GDLP shall
be capable of receiving Mode S specific
services messages from the interrogator via
frame processing.
(ii) Broadcast processing. If the received mes-
sage is a broadcast Comm-B, as indicated by
the interrogator/GDLP interface, the GDLP
shall:
(aa) generate control data indicating the
presence of a broadcast message
and the 24-bit address of the
aircraft from which the message
was received;
(bb) append the 7-byte MB field of the
broadcast Comm-B; and
(cc)   forward this data to the Mode S
specific services interface(s).
(iii) GICB processing. If the received message is
a GICB, as indicated by the interrogator/
GDLP interface, the GDLP shall:
(aa) generate control data indicating the
presence of a GICB message, the
register number and the 24-bit
address of the aircraft from which
the message was received;
(bb) append the 7-byte MB field of the
GICB; and

CIVIL AVIATION
S.R.O. 32
(cc) forward this data to the Mode S
specific services interface(s).
(iv) MSP processing. If the received message is
an MSP as indicated by the packet format
header, the GDLP shall:
(aa) generate control data indicating the
transfer of an MSP, the length of
the message, the MSP channel
number (M/CH) and the 24-bit
address of the aircraft from which
the message was received;
(bb) append the user data field of the
received MSP packet; and
(cc) forward this data to the Mode S
specific services interface(s).
L-bitprocessingshallbeperformedasspecifiedin Sub-paragraph
(7)(4).
(3) MSP PACKET FORMATS
(a) Short form MSP packet. The format for this
packet shall be as follows:
DP:1 MP:1 M/CH:6 FILL1:0 or 6
UD:v
(i) Data packet type (DP). This field shall be set
to 0.
(ii) MSPpackettype(MP).Thisfieldshallbeset
to 0.

CIVIL AVIATION
S.R.O. 32
(iii) MSP channel number (M/CH). The field
shall be set to the channel number derived
from the SSE control data.
(iv) Fill field (FILL1:0 or 6). The fill length shall be
6 bits for a downlink SLM frame. Otherwise
the fill length shall be 0.
(v) User data (UD). The user data field shall
contain message data received from the Mode
S specific services interface.
(b) Long form MSP packet. The format for this
packet shall be as follows:
DP:1
MP:1
SP:2 L:1
M/SN:3
FILL2:0 or 2 M/CH:6
UD:v
Fields shown in the packet format and not specified in the
following paragraphs shall be set as specified in (5)(2)(a) and
(7)(3)(a).
(c) Data packet type (DP). This field shall be set to
0.
(i) MSP packet type (MP). This field shall be set
to 1.
(ii)   Supervisorypacket (SP). This field shall be
set to 0.
(iii) L field (L). A value of 1 shall indicate that the
packet is part of an L-bit sequence with more
packets in the sequence to follow. A value of
0 shall indicate that the sequence ends with
this packet.

CIVIL AVIATION
S.R.O. 32
(iv) MSP sequence number field (M/SN). This
field shall be used to detect duplication in the
delivery of L-bit sequences. The first packet
in an L-bit sequence shall be assigned a
sequence number of 0. Subsequent packets
shall be numbered sequentially. A packet
received with the same sequence number as
the previously received packet shall be dis-
carded.
(4) L-bitprocessing.L-bitprocessingshallbeperformed
only on the long form MSP packet and shall be performed as
specified for M-bit processing except as specified in the following
paragraphs.
(a) Upon receipt of a long form MSP packet, the
XDLP shall construct the user data field by:
(i) verifyingthatthepacketorderiscorrectusing
the M/SN field;
(ii) assuming that the user data field in the MSP
packet is the largest number of integral bytes
that is contained within the frame;
(iii) associating each user data field in an MSP
packet received with a previous user data
field in an MSP packet that has an Lbit value
of 1; and
Note.— Truncation of the user data field is not permitted as this
is treated as an error condition.
(v) if an error is detected in the processing of an
MSP packet, the
packetshallbe discarded.

CIVIL AVIATION
S.R.O. 32
(b) In the processing of an L-bit sequence, the XDLP
shall discard any MSP packets that have dupli-
cate M/SN values. The XDLP shall discard the
entire L-bit sequence if a long form MSP packet
is determined to be missing by use of the M/SN
field.
(c) The packets associated with any L-bit sequence
whose reassembly is not completed in Tm sec-
onds (Tables 5-1 and 5-13 of Schedule 5) shall be
discarded.
(5) BROADCAST FORMAT
(a) Uplink broadcast. The format of the broadcast
Comm-A shall be as follows: The 83-bit uplink
broadcast shall be inserted in an uplink Comm-A
frame. The MA field of the Comm-A frame shall
contain the broadcast identifier specified in Table
5-23 of Schedule 5 in the first 8 bits, followed by
the first 48 user data bits of the broadcast mes-
sage. The last 27 user data bits of the broadcast
message shall be placed in the 27 bits immediately
following the UF field of the Comm-A frame.
(b) Downlink broadcast. The format of broadcast
Comm-B shall be as follows: The 56-bit downlink
broadcast message shall be inserted in the MB
field of the broadcast Comm-B. The MB field
shall contain the broadcast identifier specified in
Table 5-23 of Schedule 5 in the first 8 bits,
followed by the 48 user data bits.
(8)
Mode S subnetwork management
(1) INTERROGATOR LINK DETERMINATION FUNCTION

CIVIL AVIATION
S.R.O. 32
Note.— The ADLP interrogator link determination function
selects the II code of the Mode S interrogator through which a
Mode S subnetwork packet may be routed to the desired destina-
tion ground DTE.
(a) II code-DTE address correlation. The ADLP
shall construct and manage a Mode S interroga-
tor-data terminal equipment (DTE) cross-refer-
encetablewhoseentriesareModeSinterrogator
identifier (II) codes and ground DTE addresses
associated with the ground ATN routers or other
ground DTEs. Each entry of the II code-DTE
cross-reference table shall consist of the 4-bit
Mode S II code and the 8-bit binary representa-
tion of the ground DTE.
Note 1.— Due to the requirement for non-ambiguous addresses,
a DTE address also uniquely identifies a GDLP.
Note 2.— An ATN router may have more than one ground DTE
address.
(b) Protocol.Thefollowingproceduresshallbe used:
(i) when the GDLP initially detects the presence
of an aircraft, or detects contact with a
currently acquired aircraft through an inter-
rogator with a new II code, the appropriate
fields of the DATA LINK CAPABILITY
report shall be examined to determine if, and
to what level, the aircraft has the capability to
participate in a data exchange. After positive
determination of data link capability, the GDLP
shall uplink one or more Mode S ROUTE
packets as specified in (5)(3)(c). This infor-
mation shall relate the Mode S II code with

CIVIL AVIATION
S.R.O. 32
the ground DTE addresses accessible through
that interrogator.The ADLPshall updatethe
II code-DTE cross-reference table and then
discard the Mode S ROUTE packet(s);
(ii) a II code-DTE cross-reference table entry
shall be deleted when commanded by a Mode
S ROUTE packet or when the ADLP recog-
nizes that the transponder has not been selec-
tively interrogated by a Mode S interrogator
with a given II code for Ts seconds by
monitoring the IIS subfield in Mode S surveil-
lance or Comm-A interrogations (Table 5-1
of Schedule 5);
(iii) when the GDLP determines that modifica-
tion is required to the Mode S interrogator
assignment, it shall transfer one or more
Mode S ROUTE packets to the ADLP. The
update information contained in the Mode S
ROUTE packet shall be used by the ADLP
to modify its cross-reference table. Additions
shall be processed before deletions;
(iv) when the GDLP sends the initial ROUTE
packetafteracquisitionofaModeSdatalink-
equipped aircraft, the IN bit shall be set to
ONE. This value shall cause the ADLP to
perform the procedures as specified in
(6)(3)(c)(iii). Otherwise, the IN bit shall be
set to ZERO;
(v) when the ADLP is initialized (e.g. after a
power-up procedure), the ADLP shall issue
a search request by sending a broadcast
Comm-B message with broadcast identifier
equal to 255 (FF16, as specified in Table 5-23

CIVIL AVIATION
S.R.O. 32
of Schedule 5) and the remaining 6 bytes
unused. On receipt of a search request, a
GDLP shall respond with one or more Mode
S ROUTE packets, clear all SVCs associ-
atedwiththeADLP,asspecifiedin(6)(3)(c),
and discard the search request. This shall
cause the ADLP to initialize the II code-DTE
cross-reference table; and
(vi) onreceiptofanupdaterequest(Table5-23 of
Schedule 5), a GDLP shall respond with one
or more Mode S ROUTE packets and dis-
card the update request. This shall cause the
ADLP to update the II code-DTE cross-
reference table.
Note.— The update request may be used by the ADLP under
exceptional circumstances (e.g. changeover to standby unit) to
verify the contents of its II codeDTE crossreference table.
(C) PROCEDURES FOR DOWNLINKING MODE S PACKETS
(i) When the ADLP has a packet to downlink,
thefollowingproceduresshall apply:
(aa) CALL REQUEST packet. If the
packet to be transferred is a Mode
S CALL REQUEST, the ground
DTE address field shall be exam-
ined and shall be associated with a
connected Mode S interrogator
using the II code-DTE cross-
reference table. The packet shall
be downlinked using the multisite-
directed protocol. A request to
transfer a packet to a DTE address
not in the cross-reference table

CIVIL AVIATION
S.R.O. 32
shall result in the action specified in
(6)(3)(c)(i).
(bb) Other SVC packets. For an SVC, a
request to send a packet to a
ground DTE shall cause the packet
to be multisite- directed to the last
Mode S interrogator used to
successfully transfer (uplink or
downlink) a packet to that DTE,
provided that this Mode S interro-
gator is currently in the II code-
DTE cross-reference table. Other-
wise, an SVC packet shall be
downlinked using the multisite-
directed protocol to any other
Mode S interrogator associated
with the specified ground DTE
address.
Level 5 transponders shall be permitted to use additional interro-
gators for downlink transfer as indicated in the II code-DTE
cross-reference table.
(ii) A downlink frame transfer shall be defined to be
successful if its Comm-B or ELM close-out is
received from the transponder within Tz seconds
as specified in Table 5-1 of Schedule 5. If the
attempt is not successful and an SVC packet is
to be sent, the II code-DTE cross-reference
table shall be examined for another entry with the
same called ground DTE address and a different
Mode S II code. The procedure shall be retried
using the multisite-directed protocol with the new
Mode S interrogator. If there are no entries for
the required called DTE, or all entries result in a
failed attempt, a link failureshall be declared.

CIVIL AVIATION
S.R.O. 32
(2) SUPPORT FOR THE DTE(S)
(a) GDLP connectivity reporting. The GDLP shall
notify the ground DTE(s) of the availability of a
Mode S data link-equipped aircraft (“join event”).
The GDLP shall also inform the ground DTEs
when such an aircraft is no longer in contact via
that GDLP (“leave event”). The GDLP shall
provide for notification (on request) of all Mode
S data link- equipped aircraft currently in contact
with that GDLP. The notifications shall provide
the ground ATN router with the subnetwork point
of attachment (SNPA) address of the mobile
ATN router, with the position of the aircraft and
quality of service as optional parameters. The
SNPA of the mobile ATN router shall be the
DTE address formed by the aircraft address and
a sub-address of 0.
(b) ADLP connectivity reporting. The ADLP shall
notify all aircraft DTEs whenever the last re-
maining entry for a ground DTE is deleted from
the II code-DTE cross-reference table. This
notification shall include the address of this DTE.
(c) Communications requirements. The mechanism
for communication of changes in subnetwork
connectivity shall be a confirmed service, such as
the join/leave events that allow notification of the
connectivity status.
(3) ERROR PROCEDURES
(a) Link failure. The failure to deliver a packet to the
referenced XDLP after an attempt has been
made to deliver this packet via all available
interrogators shall be declared to be a link level

CIVIL AVIATION
S.R.O. 32
failure. For an SVC, the XDCE shall enter the
state p1 and release all resources associated with
that channel. This shall include the cancellation in
the transponder of any frames associated with
this SVC. A Mode S CLEAR REQUEST packet
shall be sent to the DCE via the reformatting
process and shall be forwarded by the DCE as an
ISO 8208 packet to the local DTE as described in
(6)(3)(c). On the aircraft side, the channel shall
not be returned to the ADCE channel pool, i.e.
does not return to the state p1, until Tr seconds
after the link failure has been declared (Table 5-
1 of Schedule 5).
(b) ACTIVE CHANNEL DETERMINATION
(i) Procedure for d1 state. The XDLP shall
monitor the activity of all SVCs, not in a
READY state (p1). If an SVC is in the
(XDCE) FLOW CONTROL READY state
(d1) for more than Tx seconds (the active
channel timer, Tables 5-1 and 5-13 of Sched-
ule 5) without sending a Mode S RR, RNR,
DATA, or REJECT packet, then:
(aa) if the last packet sent was a Mode
S REJECT packet to which a
response has not been received,
then the XDLP shall resend that
packet;
(bb) otherwise, the XDLP shall send a
Mode S RR or RNR packet as
appropriate to the peer XDLP.
(ii) Procedure for other states. If an XDCE
SVC is in the p2, p3, p6, p7, d2 or d3 state for

CIVIL AVIATION
S.R.O. 32
more than Tx seconds, the link failure proce-
dure of 5.2.8.3.1 shall be performed.
(iii) Link failure shall be declared if either a failure to deliver,
or a failure to receive, keep-alive packets has occurred. In
which case the channel shall be cleared.
(9)
The data link capability report
The data link capability report shall be as specified in Annex 10,
Volume IV, 3.1.2.6.10.2.
(10) System timers
(1) The values for timers shall conform to the values
given in Tables 5-1 and 5-13 of Schedule 5.
(2) Toleranceforalltimersshallbeplusorminusoneper
cent.
(3) Resolution for all timers shall be one second.
(11) System requirements
(1) Data integrity. The maximum bit error rates for data
presented at the ADLP/transponder interface or the GDLP/
interrogator interface measured at the local DTE/XDLP inter-
face (and vice versa) shall not exceed 10-9 for undetected errors
and 10-7 for detected errors.
Note.— The maximum error rate includes all errors resulting
from data transfers across the interfaces and from XDLP internal
operation.
(2) TIMING

CIVIL AVIATION
S.R.O. 32
(a) ADLP timing. ADLP operations shall not take
longer than 0.25 seconds for regular traffic and
0.125 seconds for interrupt traffic. This interval
shall be defined as follows:
(i) Transponders with downlink ELM capability.
The time that the final bit of a 128-byte data
packet is presented to the DCE for downlink
transfer to the time that the final bit of the first
encapsulating frame is available for delivery
to the transponder.
(ii) Transponders with Comm-B capability. The
time that the final bit of a user data field of 24
bytes is presented to the DCE for downlink
transfer to the time that the final bit of the last
of the four Comm-B segments that forms the
frame encapsulating the user data is available
for delivery to the transponder.
(iii) Transponders with uplink ELM capability.
The time that the final bit of the last segment
of an ELM of 14 Comm-C segments that
contains a user data field of 128 bytes is
received by the ADLP to the time that the
final bit of the corresponding packet is avail-
able for delivery to the DTE.
(iv) Transponders with Comm-A capability. The
time that the final bit of the last segment of
four linked Comm-A segments that contains
a user data field of 25 bytes is received by the
ADLP to the time that the final bit of the
corresponding packet is available for delivery
to the DTE.

CIVIL AVIATION
S.R.O. 32
(b) GDLP TIMING
(i) The totaltimedelayacrossthe GDLP,exclu-
sive of transmission delay, should not be
greater than seconds.
(c) Interface rate. The physical interface between
the ADLP and the transponder shall have a
minimum bit rate of 100 kilobits per second.
SCHEDULE 3:
DCE AND XDCE STATE TABLES
(Regulation 18)
(1) State table requirements. The DCE and XDCE shall
function as specified in state Tables 5-3 to 5-22 of Schedule 5.
State Tables 5-15 through 5-22 of Schedule 5 shall be applied
to:
a)
ADLP state transitions when the XDCE or XDLP
terms in parenthesis are omitted; and
b)
GDLP state transitions when the terms in parenthesis
are used and the XDCE or XDLP preceding them are omitted.
(2) Diagnostic and cause codes. The table entries for
certain conditions indicate a diagnostic code that shall be included
in the packet generated when entering the state indicated. The
term, “D = ,” shall define the diagnostic code. When “A = DIAG
“, the action taken shall be to generate an ISO 8208 DIAGNOS-
TIC packet and transfer it to the DTE; the diagnostic code
indicated shall define the entry in the diagnostic field of the packet.
The cause field shall be set as specified in (6)(3)(c). The reset
cause field shall be set as specified in ISO 8208.

CIVIL AVIATION
S.R.O. 32
Note 1.— The tables provided below specify state requirements
inthe followingorder:
5-3
DCE special cases
5-4
DTE effect on DCE restart states
5-5
DTE effect on DCE call setup and clearing states
5-6
DTE effect on DCE reset states
5-7
DTE effect on DCE interrupt transfer states
5-8
DTE effect on DCE flow control transfer states
5-9
XDCE effect on DCE restart states
5-10 XDCE effect on DCE call setup and clearing states
5-11 XDCE effect on DCE reset states
5-12 XDCE effect on DCE interrupt transfer states
5-15 GDLP (ADLP) effect on ADCE (GDCE) packet layer
ready states
5-16 GDLP (ADLP) effect on ADCE (GDCE) call setup and
clearing states
5-17 GDLP (ADLP) effect on ADCE (GDCE) reset states
5-18 GDLP (ADLP) effect on ADCE (GDCE) interrupt
transfer states
5-19 GDLP (ADLP) effect on ADCE (GDCE) flow control
transfer states

CIVIL AVIATION
S.R.O. 32
5-20 DCE effect on ADCE (GDCE) call setup and clearing
states
5-21 DCE effect on ADCE (GDCE) reset states
5-22 DCE effect on ADCE (GDCE) interrupt transfer states
Note 2.— All tables specify both ADLP and GDLP actions.
Note 3.— Within the Mode S subnetwork, states p6 and d2 are
transient states.
Note 4.— References to “notes” in the state tables refer to table-
specific notes that follow each state table.
Note 5.— All diagnostic and cause codes are interpreted as
decimal numbers.
Note 6.— An SVC between an ADCE and a GDCE may be
identified by a temporary and/or permanent channel number, as
defined in (5)(1)(b) of Schedule 5.
SCHEDULE 4:
MODE S PACKET FORMATS
(Regulation 19)
(1) Formats. The Mode S packet formats shall be as
specified in Figures 6-3 to 6-22 of Schedule 6.
(2) Significance of control fields. The structure of the
formatcontrol fieldsusedinModeSpacketsshallbeas specified
in Figure 6-23 of Schedule 6. The significance of all control fields
used in these packet formats shall be as follows:

CIVIL AVIATION
S.R.O. 32
Field symbol
Definition
AG
Address, Ground; the 8-bit binary repre
sentation of the ground DTE address
AM
Address, Mobile; the 4-bit binary repre
sentation of the last two BCD digits of the
mobile DTE address
CC
Clearing cause as defined in ISO 8208
CH
Channel number (1 to 15)
DC
Diagnostic code as defined in ISO 8208
DP
Data packet type (Figure 6-23 of Sched
ule 6)
F
S-bit sequence, first packet flag
FILL
Fill field
FILL1
Has a length of 6 bits for a non-
multiplexed packet in a downlink SLM
frame; otherwise it is 0 bit
FILL2
Has a length of 0 bit for a non-multiplexed
packet in a downlink SLM frame and for
a multiplexing header; otherwise it is 2
bits
FIRST PACKET
The contents of the first of themultiplexed
packets
FS
Fast select present

CIVIL AVIATION
S.R.O. 32
IN
Initializationbit
L
“More bit” for long-form MSP packets as
specified in Sub-paragraph (7)(4) of
Schedule 4.
LAST PACKET
The contents of the last of the multiplexed
packets
LENGTH
The length of a multiplexed packet in
bytes expressed as an unsigned binary
number
LV
User data field length; number of user
bytes as specified in (2)(3)(a) of Schedule
M
“More bit” for SVC DATA packets as
specified in (5)(1)(d)(i) of Schedule 5
M/CH
MSP channel number
MP
MSP packet type (Figure 6-23 of Sched
ule 6)
M/SN
Sequence number; the sequence number
for the long form MSP packet
OD
Optional data
ODL
Optionaldata length
OF
Option flag
P
Priority field

CIVIL AVIATION
S.R.O. 32
PR
Packet receive sequence number
PS
Packet send sequence number
RC
Resetting cause code as defined in ISO
RT
Route table as defined in (5)(3)(c)(viii)
RTL
Route table length expressed in bytes
S
“More bit” for CALL REQUEST, CALL
ACCEPT, CLEAR REQUEST and IN
TERRUPT packets as specified in
(5)(1)(d)(ii)
SN
Sequence number; the sequence number
for this packet type
SP
Supervisory packet (Figure 6-23 of
Schedule 6)
SS
Supervisory subset number (Figure 6-23
of Schedule 6)
ST
Supervisory type (Figure 6-23 of Sched
ule)
TC
Temporary channel number (1 to 3)
UD
User data field

CIVIL AVIATION
S.R.O. 32
SCHEDULE 5:
TABLES FOR PART IV
Table 5-1.  ADLP Mode S subnetwork timers
Timer name
Timer label
Nominal value
Reference
Channel retirement
Tr
600 s
(8)(3)(a)
Active channel-ADLP
Tx
420 s
(8)(3)(b)
Interrogator interrogation
Ts
60 s
(8)(1)(b)
Interrogator link
Tz
30 s
(7)(1)(a)(iv)
(bb),(8)(1)(c)(ii)
Link frame cancellation
Tc
60 s
(2)(1)(a)(iv)(ee)
L-bit delivery-ADLP
Tm
120 s
(7)(4)(c)
Packet resequencing and S-bit delivery
Tq
60 s
(6)(9)

CIVIL AVIATION
S.R.O. 32
Table 5-2.  DCE actions at state transition
DCE
State definition
Action that shall be taken when entering the state
state
r1
PACKET LEVEL READY
Return all SVCs to the p1 state (see p1 state
explanation).
r2
DTE RESTART REQUEST
Return each SVC to the p1 state (see p1 state
explanation). Issue a RESTART CONFIRMA
TION to the DTE.
r3
DCE RESTART REQUEST
Issue a RESTART REQUEST to the DTE.
Unless entered via the r2 state, send a RE
START REQUEST to the reformatting process.
p1
READY
Release all resources assigned to SVC. Break
the correspondence between the DTE/DCE
SVC and the ADCE/GDCE SVC (the ADCE/
GDCE SVC may not yet be in the p1 state).
p2
DTE CALL REQUEST
Determine if sufficient resources exist to
support request; if so, allocate resources and
forward CALL REQUEST packet to
reformatting process; if not, enter DCE CLEAR
REQUEST to DTE state (p7). Determination of
resources and allocation is as defined in ISO
8208.
p3
DCE CALL REQUEST
Determine if sufficient resources exist to
support request; if so allocate resources and
forward CALL REQUEST packet to DTE; if not,
send a CLEAR REQUEST packet to the
reformatting process. Determination of re
sources and allocation is as defined in ISO
8208.
p4
DATA TRANSFER
No action.

CIVIL AVIATION
S.R.O. 32
p5
CALL COLLISION
Reassign outgoing call to another SVC (the
DTE in its call collision state ignores the
\incoming call) and enter the DCE CALL
REQUEST state (p3) for that new SVC. Enter
the p2 state to process the CALL REQUEST
from the DTE.
p6
DTE CLEAR REQUEST
Release all resources assigned to SVC, send a
CLEAR CONFIRMATION packet to the DTE
and enter p1 state.
p7
DCE CLEAR REQUEST to DTE Forward CLEAR REQUEST packet to DTE.
d1
FLOW CONTROL READY
No action.
d2
DTE RESET REQUEST
Remove DATA packets transmitted to DTE
from window; discard any DATA packets that
represent partially transmitted M-bit se
quences and discard any INTERRUPT packet
awaiting transfer to the DTE; reset all window
counters to 0; set any timers and
retransmission parameters relating to DATA
and INTERRUPT transfer to their initial value.
Send RESET CONFIRMATION packet to DTE.
Return SVC to d1 state.
d3
DCE RESET REQUEST to DTE  Remove DATA packets transmitted to DTE
from window; discard any DATA packets that
represent partially transmitted M-bit se
quences and discard any INTERRUPT packet
awaiting transfer to the DTE; reset all window
counters to 0; set any timers and
retransmission parameters relating to DATA
and INTERRUPT transfer to their initial value.
Forward RESET  REQUEST packet to DTE.

CIVIL AVIATION
S.R.O. 32
DCE
State definition
Action that shall be taken when entering the state
state
i1
DTE INTERRUPT
No action.
READY
i2
DTE INTERRUPT
Forward INTERRUPT packet received from DTE
SENT
to reformatting process.
jl
DCE INTERRUPT
No action.
 READY
j2
DCE INTERRUPT
Forward INTERRUPT packet received from
SENT
reformatting process to DTE.
f1
DCE RECEIVE
No action.
READY
f2
DCE RECEIVE NOT No action.
READY
g1
DTE RECEIVE
No action.
READY
g2
DTE RECEIVE
No action.
 NOT READY

CIVIL AVIATION
S.R.O. 32
Table 5-3.  DCE special cases
Received from DTE
DCE special cases
Any state
Any packet less than 2 bytes in length (including a valid
A=DIAG
 data link level frame containing no packet)
D=38
Any packet with an invalid general format identifier
A=DIAG
D=40
Any packet with a valid general format identifier and
an assigned logical channel identifier (includes a
See Table 5-4
logical channel identifier of 0)
Table 5-4.  DTE effect on DCE restart states
DCE restart states (see Note 5)
 PACKET LEVEL
DTE RESTART DCE RESTART
READY (see Note 1)
REQUEST
REQUEST
Packet received from DTE
r1
r2
r3
Packets having a packet
See Table 5-5
A=ERROR
A=DISCARD
type identifier shorter than
S=r3D=38
1 byte and logical channel
(see Note 4)
identifier not equal to 0
Any packet, except RESTART,
A=DIAG
A=DIAG
A=DIAG
 REGISTRATION(if supported) D=36
D=36
D=36
with alogical channel identifier
of 0
Packet with a packet type
See Table 5-5
A=ERROR
A=DISCARD
identifier which is undefined
S=r3
 or not supported by DCE
D=33
(see Note 4)

CIVIL AVIATION
S.R.O. 32
RESTART REQUESt,
See Table 5-5
A=ERROR
A=DISCARD
 RESTART ,
S=r3
CONFIRMATIONor
D=41
REGISTRATION
(see Note 4)
(if supported) packet
 with a logical channel
identifier unequal to 0
RESTART REQUEST
A=NORMAL
A=DISCARD
A=NORMAL
(forward)
S=p1 or d1
S=r2
(see Note2)
RESTART
A=ERROR
A=ERROR
A=NORMAL
CONFIRMATION
S=r3
S=r3
S=p1 ord1
D=17
D=18
(see Note 2)
(see Note 6)
(see Note 4)
RESTART REQUEST
A=DIAG
A=DISCARD
A=ERROR
OR RESTART
D=38, 39, 81 or 82
D=38, 39, 81 or 82
CONFIRMATION packet
with a format error
REGISTRATION
A=NORMAL
A=NORMAL
A=NORMAL
REQUEST or
REGISTRATION
CONFIRMATION packets
(see Note 3)
REGISTRATION REQUEST
A=DIAG
A=ERROR
A=ERROR
or REGISTRATION
D=38, 39, 81 or 82
S=r3
D=38, 39, 81 or 82
CONFIRMATION
D=38, 39, 81 or 82
 packet with a format error
 (see Note 4)
(see Note 3)
Call setup, call clearing,
See Table 5-5
A=ERROR
A=DISCARD
DATA, interrupt, flow control,
S=r3
or resetpacket
D=18

CIVIL AVIATION
S.R.O. 32
NOTES:
1. The Mode S subnetwork has no restart states. Receipt of a RESTART REQUEST causes
 the DCE to respond with a RESTART CONFIRMATION. The RESTART REQUEST
packet is forwarded to the reformatting process, which issues clear requests for all SVCs
associated with the DTE. The DCE enters the r3 state only as a result of an error detected
on the DTE/DCE interface.
2.The SVC channels are returned to state p1, the permanent virtual circuits (PVC)
channels are returned to state d1.
3.The use of the registration facility is optional on the DTE/DCE interface.
4.No action is taken within the Mode S subnetwork.
5.Table entries are defined as follows: A = action to be taken, S = the state to be entered,
D = the diagnostic code to be used in packets generated as a result of this action,
DISCARD indicates that the received packet is to be cleared for the XDLP buffers, and
INVALID indicates that the packet/state combination cannot occur.
6.The error procedure consists of entering the r3 state, and sending a RESTART
REQUEST to the reformatting process.

CIVIL AVIATION
S.R.O. 32
Table 5-5.  DTE effect on DCE call setup and clearing states
DCE call setup and clearing states (see Note 5)
CALL
COLLISION
DCE CLEAR
DTE CALLDCE CALLDATA
p5
DTE
REQUEST to
Packet received READYp1 REQUEST REQUEST TRANSFER(see Notes 1
CLEAR  DTE p7
from DTE
p2
p3
p4
and 4)
REQUEST
p6
Packets having A=ERROR A=ERROR
A=ERROR See Table A=ERROR
A=ERROR A=DISCARD
 a packet
S=p7
S=p7
S=p7
 5-6
S=p7
S=p7
type identifier D=38
D=38
D=38
D=38
D=38
shorter
(see Note 2) (see Note 2)
(see Note 2) (see Note 2)
than 1 byte
Packets having A=ERROR A=ERROR
A=ERROR See Table A=ERROR
A=ERRORA=DISCARD
 a packet
5-6
type identifier S=p7
S=p7
S=p7
S=p7
S=p7
which is
D=33
D=33
D=33
D=33
D=33
undefined or
(see Note 2) (see Note 2)
(see Note 2) (see Note 2)
notsupported
 by DCE
RESTART
A=ERROR A=ERROR
A=ERROR See Table A=ERROR
A=ERRORA=DISCARD
REQUEST,
5-6
RESTART
S=p7
S=p7
S=p7
S=p7
S=p7
CONFIRMA- D=41
D=41
D=41
D=41
D=41
TION or
(see Note 2) (see Note 2)
(see Note 2)
(see Note 2)
REGISTRA-
TIONpacket
with logical
channel
 identifier
unequal to 0
CALL
A=NORMALA=ERROR
A=NORMALA=ERROR A=ERROR
A=ERROR A=DISCARD
REQUEST
S=p2
S=p7
S=p5
S=p7
S=p7
S=p7
(forward) D=21
D=23
D=24
D=25
(see Note 2)
(see Note 2)(see Note 2)
(see Note 2)

CIVIL AVIATION
S.R.O. 32
CALL
A=ERROR A=ERROR
A=NORMALA=ERRORA=ERROR
A=ERROR
A=DISCARD
ACCEPT
S=p7
S=p7
S=p4
S=p7
S=p7
S=p7
D=20
D=21
(Forward) D=23
D=24
D=25
(see Note 2)
or
(see Note 2)(see Notes 2
(see Note 2)
A=ERROR
and 4)
S=p7
D=42
(see Notes 2
and 3)
CLEAR
A=NORMALA=NORMAL A=NORMALA=NORMALA=NORMAL A=DISCARD A=NORMAL
REQUEST
S=p6
S=p6
S=p6
S=p6
S=p6
S=p1
(forward) (forward)
(forward) (forward)
(do not
 forward)
CLEAR
A=ERROR A=ERROR
A=ERROR A=ERROR A=ERROR
A=ERROR
A=NORMAL
CONFIRM-
S=p7
S=p7
S=p7
S=p7
S=p7
S=p7
S=p1
-ATION
D=20
D=21
D=22
D=23
D=24
D=25
(do not
(see Note 2)
(see Note 2) (see Note 2)(see Note 2)(see Note 2)
forward)
DATA,
 interrupt, flow A=ERROR
A=ERROR
A=ERROR
See Table 5-6A=ERROR
A=ERROR
A=DISCARD
control or resetS=p7
S=p7
S=p7
S=p7
S=p7
 packets
D=20
D=21
D=22
D=24
D=25
(see Note 2)
(see Note 2)
(see Note 2) (see Note 2)
DCE call setup and clearing states (see Note 5)
CALL
COLLISION
DCE CLEAR
 DTE CALLDCE CALL DATA
p5
DTECLEAR REQUEST
Packet received READY
REQUEST REQUEST TRANSFER (see Notes 1 REQUEST
 to DTE
 from DTE
p1
p2
p3
p4
and 4)
p6
p7
NOTES:
1.
On entering the p5 state, the DCE reassigns the outgoing call to the DTE to
another channel (no CLEAR REQUEST is issued) and responds to incoming DTE call as
appropriate with a CLEAR REQUEST or CALL ACCEPT packet.
2.
The error procedure consists of performing the actions specified when entering
the p7 state (including sending a CLEAR REQUEST packet to the DTE) and addition-

CIVIL AVIATION
S.R.O. 32
ally sending a CLEAR REQUEST packet to the XDCE (via the reformatting process).
3.
The use of the fast select facility with a restriction on the response prohibits the
DTE from sending a CALL ACCEPT packet.
4.
The DTE in the event of a call collision must discard the CALL REQUEST packet
received from the DCE.
5.
Table entries are defined as follows: A = action to be taken, S = the state to be
entered, D = the diagnostic code to be used in packets generated as a result of this
action, DISCARD indicates that the received packet is to be cleared from the XDLP
buffers, and INVALID indicates that the packet/state combination cannot occur.
Table 5-6.  DTE effect on DCE reset states
DCE reset states (see Note 2)
FLOWCONTROLRESETREQUEST DCE RESETREQUEST
READY
by DTE
to DTE
Packet received from DTE
d1
d2
d3
Packet with a packet type identifier A=ERROR
A=ERROR
A=DISCARD
shorter than 1 byte
S=d3
S=d3
D=38
D=38
(see Note 1)
(see Note 1)
Packet with a packet type identifier
A=ERROR
A=ERROR
A=DISCARD
which is undefined or not DCE
S=d3
S=d3
supported by
D=33
D=33
(see Note 1)
(see Note 1)RE
START REQUEST, RESTART
A=ERROR
A=ERROR
A=DISCARD
CONFIRMATION, or
S=d3
S=d3
REGISTRATION (if supported)
D=41
D=41
packet with logical channel
(see Note 1)
(see Note 1)
identifier unequal to 0
RESET
A=NORMAL
A=DISCARD
A=NORMAL
REQUEST
S=d2
S=d1
(forward)
(do not forward)
RESET CONFIRMATION
A=ERROR
A=ERROR
A=NORMAL
S=d3
S=d3
S=d1
D=27
D=28
(do not forward)
(see Note 1)
(see Note 1)

CIVIL AVIATION
S.R.O. 32
INTERRUPT packet
See Table 5-7
A=ERROR
A=DISCARD
S=d3
D=28
(see Note 1)
INTERRUPT
 CONFIRMATION packet
See Table 5-7
A=ERROR
A=DISCARD
S=d3
D=28
(see Note 1)
DATA or flow control packet
See Table 5-8
A=ERROR
A=DISCARD
S=d3
D=28
(see Note 1)
REJECT supported but not
A=ERROR
A=ERROR
A=DISCARD
subscribed to
S=d3
S=d3
D=37
D=37
(see Note 1)
(see Note 1)
NOTES:1.The error procedure consists of performing the specified actions when entering the d3
state (which includes forwarding a RESET REQUEST packet to the DTE) and sending a RESET
REQUEST packet to the XDCE (via the formatting function).
2.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared for the XDLP buffers, and INVALID indicates
that the packet/state combination cannot occur.

CIVIL AVIATION
S.R.O. 32
Table 5-7.  DTE effect on DCE interrupt transfer states
DTE/DCE interrupt transfer states (see Note 2)
Packet received from DTE
DTE INTERRUPT READY
DTE INTERRUPT SENT
              i1
          i2
INTERRUPT
A=NORMAL
A=ERROR
(see Note 1)
S=i2
S=d3
(forward)
D=44(see Note 3)
DTE/DCE interrupt transfer states (see Note 2)
Packet received from DTE
DCE INTERRUPT READY
DCE INTERRUPT SENT
j1
j2
INTERRUPT CONFIRMATION
A=ERROR
A=NORMAL
(see Note 1)
S=d3
S=j1
D=43
(forward)
(see Note 3)
NOTES:
1.If the packet has a format error, then the error procedure applies (see Note 3). Interrupt
packets with user data greater than 32 bytes should be treated as a format error.
2.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID
indicates that the packet/state combination cannot occur.
3.The error procedure consists of performing the specified actions when
entering the d3 state (which includes forwarding a RESET REQUEST packet
to the DTE) and sending a RESET REQUEST packet to the XDCE (via the
reformatting process).

CIVIL AVIATION
S.R.O. 32
Table 5-8.  DTE effect on DCE flow control transfer states
DCE flow control transfer states (see Notes 2 and 3)
DCE RECEIVE READY
DCE RECEIVE NOT READY
Packet received from DTE
f1
f2
DATA packet with less than 4
A=ERROR
A=DISCARD
bytes when using modulo 128
S=d3
numbering
D=38
(see Note 4)
DATA packet with invalid PR
A=ERROR
A=ERROR
S=d3
S=d3
D=2
D=2
(see Note 4)
(see Note 4)
DATA packet with valid PR but
A=ERROR
A=DISCARD
invalid PS or user data field with
S=d3
(process PR data)
 improper format
D=1 (invalid PS)
D=39 (UD > max negotiated
length)D=82 (UD unaligned)
(see Note 4)
DATA packet with valid PR with A=ERROR
A=DISCARD
M-bit setto 1 when the user data
S=d3
(process PR data)
 field is partially full
D=165
(see Note 4)
DATA packet with valid PR, PS
A=NORMAL
A=DISCARD
and userdata field format
(forward)
(process PR data)
DCE flow control transfer states (see Notes 2 and 3)
DTE RECEIVE READY
DTE RECEIVE NOT READY
Packet received from DTE
g1
g2
RR, RNR, or REJECT packet
A=DISCARD
A=DISCARD
 with less than3 bytes when using
modulo 128 numbering
 (see Note 1)

CIVIL AVIATION
S.R.O. 32
RR, RNR, or REJECT
A=ERROR
A=ERROR
 packet with an invalid
S=d3
S=d3
PR
D=2
D=2
(see Note 4)
(see Note 4)
RR packet with a valid PR
A=NORMAL
A=NORMAL
S=g1
RNR packet with a valid PR
A=NORMAL
A=NORMAL
S=g2
REJECT packet with a valid PR
A=NORMAL
A=NORMAL
S=g1
NOTES:
1.The reject procedures are not required.
2.The RR, RNR and REJECT procedures are a local DTE/DCE matter and the corresponding
packets are not forwarded to the XDCE
3.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
4.The error procedure consists of performing the specified actions when entering the d3 state (which
includes forwarding a RESET REQUEST packet to the DTE) and sending a RESET REQUEST
packet to the XDCE (via the reformatting process).
Table 5-9.  XDCE effect on DCE restart states
DCE restart states (see Note)
PACKET LEVEL
DTE RESTART
DCE RESTART
READY
REQUEST
 REQUEST
Packet received from
r1
r2
r3
XDCE
CALL REQUEST
See Table 5-10
Send CLEAR
Send CLEAR
REQUEST to
REQUEST to
reformatting
reformatting
process with
process with
D=244
D=244

CIVIL AVIATION
S.R.O. 32
CALL ACCEPT, CLEAR
See Table 5-10
A=DISCARD
A=DISCARD
 REQUEST, DATA, I
NTERRUPT,INTERRUPT
CONFIRMATION,
RESET REQUEST
Note.— Table entries are defined as follows: A = action to be taken, S = the state to be entered, D =
the diagnostic code to be used in packets generated as a result of this action, DISCARD indicates
that the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the
packet/state combination cannot occur.
Table 5-10.  XDCE effect on DCE call setup and clearing states
DCE call setup and clearing states (see Note)
DCE CLEAR
 DTE CALLDCE CALL DATA
CALL
DTE CLEAR REQUESTto
Packet received READY
REQUESTREQUEST
TRANSFER COLLISIONREQUEST DTE
from XDCE
p1
p2
p3
p4
p5
p6
p7
CALL
A=NORMALINVALID
INVALID
INVALID
INVALID INVALID
INVALID
REQUEST
S=p3
(forward)
CALL
A=DISCARDA=NORMALINVALID
INVALID
INVALID A=DISCARD A=DISCARD
ACCEPT
S=p4
(forward)
CLEAR
 REQUEST
A=DISCARDA=NORMALA=NORMAL A=NORMAL INVALID A=DISCARD A=DISCARD
S=p7
S=p7
S=p7
(forward) (forward)
(forward)
DATA,
A=DISCARDINVALID INVALID
See Table 5-11 INVALID A=DISCARD A=DISCARDI
 INTERRUPT,
NTERRUPT
CONFIRMAT
ION, or RESET
REQUEST
Note.— Table entries are defined as follows: A = action to be taken, S = the state to be entered, D =
the diagnostic code to be used in packets generated as a result of this action, DISCARD indicates
that the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the
packet/state combination cannot occur.

CIVIL AVIATION
S.R.O. 32
Table 5-11.  XDCE effect on DCE reset states
DCE reset states (see Note)
FLOW CONTROL
DCE RESET
DTE RESET
READY
REQUEST
REQUEST to DTE
Packet received from XDCE
d1
d2
d3
RESET REQUEST
A=NORMAL
A=NORMAL
A=DISCARD
S=d3
S=d1
(forward)
(forward)
INTERRUPT
See Table 5-12
A=DISCARD
A=DISCARD
INTERRUPT
See Table 5-12
A=DISCARD
INVALID
CONFIRMATION
DATA
A=NORMAL
A=DISCARD
A=DISCARD
(forward)
Note.— Table entries are defined as follows: A = action to be taken, S = the state to be entered, D
= the diagnostic code to be used in packets generated as a result of this action, DISCARD indicates
that the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the
packet/state combination cannot occur.
Table 5-12.  XDCE effect on DCE interrupt transfer states
DCE interrupt transfer states (see Note)
DTE INTERRUPT READY
DTE INTERRUPT SENT
Packet received from XDCE
i1
i2
INTERRUPT CONFIRMATION
INVALID
A=NORMAL
      S=i1
 (forward)
DCE interrupt transfer states (see Note)
DCE INTERRUPT READY
DCE INTERRUPT SENT
Packet received from XDCE
j1
j2

CIVIL AVIATION
S.R.O. 32
INTERRUPT
A=NORMAL
INVALID
S=j2
(forward)
Note.— Table entries are defined as follows: A = action to be taken, S = the state to be entered, D =
the diagnostic code to be used in packets generated as a result of this action, DISCARD indicates
that the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the
packet/state combination cannot occur.
Table 5-13.  GDLP Mode S subnetwork timers
Timer name
Timer label
Nominal value
Reference
Active channel-GDLP
Tx
300 s
5.2.8.3.2
L-bit delivery-GDLP
Tm
120 s
5.2.7.4.3
Packet resequencing and S-bit
Tq
60 s
5.2.6.9
delivery
Table 5-14.  XDCE actions at state transition
XDCE
State definition
 Action that shall be taken when entering the state
state
r1
PACKET LEVEL READY Return all SVCs to the p1 state.
p1
READY
Release all resources assigned to the SVC. Break the
correspondence between the ADCE/GDCE SVC and the
DTE/DCE SVC (the DTE/DCE SVC may not yet be in a p1
state).
p2
GDLP
Determine if sufficient resources exist to support request; if
(ADLP) CALL REQUEST so allocate resources and forward Mode S CALL REQUEST
packet to reformatting process; if not, enter ADCE(GDCE)
CLEAR REQUEST to GDLP(ADLP) state (p7).
p3
ADCE(GDCE) CALL
Determine if sufficient resources exist to support request; if
REQUEST
so, allocate resources and forward Mode S CALL RE
QUEST packet to frame processing; if not, send Mode S
CLEAR REQUEST to reformatting process and go to state
p1. Do not forward the Mode S CALL REQUEST to the
peer XDCE.

CIVIL AVIATION
S.R.O. 32
p4
DATA TRANSFER
No action.
p6
GDLP(ADLP) CLEAR
Release all resources, send a Mode S CLEAR
REQUEST
CONFIRMATlON packet to the peer XDCE and enter the
p1 state.
p7
ADCE(GDCE) CLEAR
Forward Mode S CLEAR REQUEST packet to the peer
REQUEST to GDLP(ADLP) XDCE via frame processing.
d1
FLOW CONTROL READY No action.
d2
GDLP(ADLP) RESET
Remove Mode S DATA packets transmitted to peer
XDCE
REQUEST
from window; discard any DATA packets
that represent
partially transmitted M-bit sequences and
discard any Mode
S INTERRUPT packets awaiting transfer
to the peer XDCE;
reset all flow control window counters to
0. Send Mode S
RESET CONFIRMATION packet to the
peer XDCE.
Return SVC to d1 state. Forward
Mode S RESET REQUEST
packet to reformatting process.
d3
ADCE(GDCE) RESET
Remove Mode S DATA packets transmitted to peer
XDCE
REQUEST to GDLP(ADLP)
from window; discard any
DATA packets that represent
partially transmitted M-bit sequences and
discard any Mode
S INTERRUPT packets awaiting transfer
to the peer XDCE;
reset all flow control window counters to
0. Forward Mode
S RESET REQUEST packet to peer
XDCE via frame
processing.
i1
GDLP(ADLP) INTERRUPT No action.
READY
i2
GDLP(ADLP) INTERRUPT Forward Mode S INTERRUPT packet received from peer
SENT
XDCE to the reformatting process.
j1
ADCE(GDCE) INTERRUPT No action.
j2
ADCE(GDCE) INTERRUPT SENTForward Mode S INTERRUPT packet received
from the reformatting process.
f1
ADCE(GDCE) RECEIVE READY No action.
f2
ADCE(GDCE) RECEIVE NOT READY
No action.
g1
GDLP(ADLP) RECEIVE READY
No action.
g2
GDLP(ADLP) RECEIVE NOT READY
No action.

CIVIL AVIATION
S.R.O. 32
Table 5-15.  GDLP (ADLP) effect on ADCE (GDCE) packet layer ready states
ADCE (GDCE) states
(see Notes 1 and 3)
Packet received from GDLP (ADLP)
PACKET LEVEL READY
(see Note 2)
r1
CH=0 with no TC present (see Note 4) or
A=DISCARD
CH=0 in a CALL ACCEPT by ADLP packet
Unassigned packet header
A=DISCARD
Call setup, call clearing, DATA, interrupt, flow
See Table 5-16
control, or reset
NOTES:
1.The XDCE state is not necessarily the same state as the DTE/DCE interface.
2.All packets from the peer XDLP have been checked for duplication before evaluation as
   represented by this table.
3.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
   diagnostic code to be used in packets generated as a result of this action, DISCARD indicates
   that the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the
   packet/state combination cannot occur.
4.Where CH=0 and a valid TC is present in a CLEAR REQUEST by ADLP or GDLP packet or a
   CLEAR CONFIRMATION by ADLP or GDLP packet, it is handled as described in (5)(1)(b)(iii)
    and Table 5-16.
Table 5-16.  GDLP (ADLP) effect on ADCE (GDCE) call setup and clearing states
ADCE (GDCE) call setup and clearing States
 (See Notes 1, 7 and 8)
ADCE (GDCE)
GDLP (ADLP) ADCE (GDCE)
GDLP (ADLP) CLEAR
Packet received
CALL
CALL
DATA
CLEAR
REQUEST  to
from
READY
REQUEST
REQUEST
TRANSFER REQUEST
GDLP (ADLP)
GDLP (ADLP) p1
p2
p3
p4
p6
p7
(seeNote 2)
Format error
A=ERROR A=ERROR
A=ERROR
See Table 5-17 A=ERROR
A=DISCARD
(see Note 3)
(see Note 10) S=p7
S=p7
S=p7
S=p7
D=33
D=33
D=25
D=33
(see Note 6)
(see Notes 6 and 9)
(see Note 6)
(see Note 9)

CIVIL AVIATION
S.R.O. 32
CALL REQUEST A=NORMAL A=ERROR
Not applicable Not applicable A=ERROR
 A=DISCARD
(5.2.6.3.1)
S=p7
(see Note 4)
(see Note 4)
S=p7
S=p2
D=21
D=25
(forward
(see Note 6)
(see Note 6)
request
to DCE)
CALL ACCEPTA=ERROR
A=ERROR
A=NORMAL A=ERROR
A=ERROR A=DISCARD
S=p7
 S=p7
(5.2.6.3.1)
S=p7
 S=p7
D=20
D=21
S=p4 (forwardD=23
D=25
(see Note 10) (see Note 6)
 to DCE), or (see Note 6)
(see Note 6)
A=ERROR(see
S=p7
D=42
Note 6)
ADCE (GDCE) call setup and clearing States
 (See Notes 1,7 and 8)
ADCE (GDCE)
GDLP (ADLP) ADCE (GDCE)
GDLP (ADLP) CLEAR
Packet received
CALL
CALL
DATA
CLEAR
REQUESTto
from GDLP
READY
REQUEST
REQUEST
TRANSFER
REQUEST GDLP (ADLP)
 (ADLP)(see
p1
p2
p3
p4
p6
p7
 Note 2)
CLEAR RE
A=NORMAL A=NORMAL A=NORMAL A=NORMAL A=DISCARD A=NORMAL
QUEST
((6)(3)(c))
((6)(3)(c))
((6)(3)(c))
((6)(3)(c))
((6)(3)(c))
S=p6
S=p6
S=p6
S=p6
S=p1
(do not forward) (forward to DCE) (forward to DCE) (forward to DCE)
(do not forward)
CLEAR
A=ERROR
A=ERROR
A=ERROR
A=ERROR
A=ERROR
A=NORMAL
CONFIRMATIONS=p7
S=p7
S=p7
S=p7
S=p7
(5.2.6.3.3)
D=20
D=21
D=22
D=23
D=25
S=p1
(see Note 10) (see Note 6)
(see Note 6) (see Note 6)
(see Note 6) (do notforward)
DATA, interrupt, A=ERROR
A=ERROR
A=ERROR
See Table 5-17A=ERROR
A=DISCARD
 flowcontrol or S=p7
S=p7
S=p7
S=p7
reset packets
D=20
D=21
D=22
D=25
(see Note 10) (see Notes 6
(see Notes 5
and 9)
 and 6)
(see Note 6)

CIVIL AVIATION
S.R.O. 32
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.All packets from the peer XDLP have been checked for duplication before evaluation as repre-
sented by this table.
3.A format error may result from an S-bit sequence having a first or intermediate packet shorter
than the maximum length, or else from an invalid LV field in a CALL REQUEST, CALL ACCEPT,
CLEAR REQUEST or INTERRUPT packet. There are no other detectable Mode S format errors.
4.The ADCE assigns all channel numbers used between the ADLP and GDLP, hence call collisions
are not possible. When a CALL REQUEST by GDLP packet is received bearing a temporary
channel number associated with an SVC in the p4 state, the association of the temporary to perma-
nent channel number is broken.
5.Not applicable to the GDLP.
6.The error procedure consists of performing the actions specified when entering the p7 state
(including sending a CLEAR REQUEST packet to the peer XDLP) an
d additionally sending a CLEAR REQUEST packet to the DCE (via the reformatting process).
7.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
8.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received
packet. If no paragraph number is referenced, the normal processing is defined in the table entry.
9.An error condition is declared and transfer to the p7 state is possible only if the ground DTE
address is known unambiguously. Otherwise the action is to discard the packet.
10.The error procedure consists of performing the action when entering the p7 state (including
sending a CLEAR REQUEST packet to the XDLP) but without sending a CLEAR REQUEST packet
to the local DCE.

CIVIL AVIATION
S.R.O. 32
Table 5-17.  GDLP (ADLP) effect on ADCE (GDCE) reset states
ADCE (GDCE) reset states (see Notes 1, 4 and 5)
FLOW CONTROL
GDLP (ADLP) RESET ADCE (GDCE) RESET REQUEST
Packet received
READY
REQUEST
to GDLP (ADLP)
from GDLP
d1
d2
d3
(ADLP) (see Note 2)
RESET
A=NORMAL
A=DISCARD
A=NORMAL
REQUEST
((6)(7))
((6)(7))
S=d2
S=d1
(forward to DCE)
(do not forward)
RESET
A=ERROR
A=ERROR
A=NORMAL
CONFIRMATION
S=d3
S=d3
(5.2.6.7)
D=27
D=28
S=d1
(see Note 3)
(see Note 3)
(do not forward)
INTERRUPT
See Table 5-18
A=ERROR
A=DISCARD
S=d3
D=28
(see Note 3)
INTERRUPT
See Table 5-18
A=ERROR
A=DISCARD
CONFIRMATION
S=d3
D=28
(see Note 3)
DATA or flow
See Table 5-19
A=ERROR
A=DISCARD
control packet
S=d3
D=28
(see Note 3)
Format error
A=ERROR
A=ERROR
A=DISCARD
(see Note 6)
S=d3
S=d3
D=33
D=33
(see Note 3)
(see Note 3)

CIVIL AVIATION
S.R.O. 32
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface
2.All packets from the peer XDLP have been checked for duplication before evaluation as repre-
sented by this table.
3.The error procedure consists of performing the specified actions when entering the d3 state (which
includes forwarding a RESET REQUEST packet to the peer XDLP) and sending a RESET RE-
QUEST packet to the DCE (via the formatting function).
4.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared for the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
5.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received
packet. If no paragraph number is referenced, the normal processing is defined in the table entry
6.A format error may result from an S-bit sequence having a first or intermediate packet shorter
than the maximum length, or else from an invalid LV field in a CALL REQUEST, CALL ACCEPT,
CLEAR REQUEST, or INTERRUPT packet. There are no other detectable Mode S format
errors.
Table 5-18.  GDLP (ADLP) effect on ADCE (GDCE) interrupt transfer states
ADCE/GDCE interrupt transfer states
(see Notes 1, 3 and 4)
GDLP (ADLP) INTERRUPT GDLP (ADLP) INTERRUPT
Packet received from GDLP
READY
SENT
 (ADLP) (see Note 2)
i1
i2
INTERRUPT
A=NORMAL
A=ERROR
(see Note 6)
((6)(4)(e))
S=d3
S=i2
D=44
(forward to DCE)
(see Note 5)
ADCE (GDCE) interrupt transfer states
 (see Notes 1, 3 and 4)
ADCE (GDCE) INTERRUPT ADCE (GDCE) INTERRUPT
Packet received from GDLP
READY
SENT
 (ADLP) (see Note 2)
j1
j2

CIVIL AVIATION
S.R.O. 32
INTERRUPT CONFIRMATION A=ERROR
A=NORMAL
S=d3
((6)(4)(e))
D=43
S=j1
(see Note 5)
(forward confirmation to DCE)
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.All packets from the peer XDLP have been checked for duplication before evaluation as repre-
sented by this table.
3.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared for the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
4.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received
packet. If no paragraph number is referenced, the normal processing is defined in the table entry.
5.The error procedure consists of performing the specified actions when entering the d3 state (which
includes forwarding a RESET REQUEST packet to the peer XDLP) and sending a RESET RE-
QUEST packet to the DCE (via the reformatting process).
6.User data length for INTERRUPT packets greater than 32 bytes, or an out of sequence INTER-
RUPT packet, are considered as errors.
Table 5-19.  GDLP (ADLP) effect on ADCE (GDCE) flow control transfer states
ADCE (GDCE) flow control transfer states
(see Notes 1, 6 and 7)
ADCE (GDCE)
ADCE (GDCE)
Packet received from GDLP
 RECEIVE READY
RECEIVE NOT READY
(ADLP) (see Note 2)
f1
f2
DATA packet with invalid PR
A=ERROR
A=ERROR
(see Note 3)
S=d3
S=d3
D=2
D=2
(see Note 8)
(see Note 8)
DATA packet with valid PR,
A=DISCARD,
A=DISCARD, but process the
invalid PS or LV subfield
but process the PR value and
PR value and send REJECTpacket
(see Notes 4 and 5)
 send REJECT packet containing
containing the expected PS
the expected  PS value
value when busy condition ends
(see Note 5)

CIVIL AVIATION
S.R.O. 32
DATA packet with valid PR,
A=NORMAL
A=PROCESS, if possible; or
 PS and LV subfield
((6)(4)(d))
A=DISCARD, but process the
(forward)
PR value and send REJECT
containing the expected PS
value whenbusy condition ends
ADCE (GDCE) flow control transfer states
(see Notes 1, 6 and 7)
GDLP (ADLP)
GDLP (ADLP)
Packet received from GDLP
RECEIVE READY
RECEIVE NOT READY
(ADLP) (see Note 2)
g1
g2
RR, RNR, REJECT packet with A=ERROR
A=ERROR
invalid PR(see Note 3)
S=d3
S=d3
D=2
D=2
(see Note 8)
(see Note 8)
RR with valid PR field
A=NORMAL
A=NORMAL
(see Note 9)
((6)(5))
((6)(5))
S=g1
RNR with valid PR value
A=NORMAL
A=NORMAL
(see Note 9)
((6)(5))
((6)(6))
S=g2
REJECT with valid PR
A=NORMAL
A=NORMAL
(see Note 9)
((6)(5))
((6)(6))
S=g1
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.All packets from the peer XDLP have been checked for duplication before evaluation as repre-
sented by this table.
3.An invalid PR value is one which is less than the PR value (modulo 16) of the last packet sent by
the peer XDLP, or greater than the PS value of the next data packet to be transmitted by the XDLP.
4.An invalid PS value is one which is different from the next expected value for PS.
5.An invalid LV subfield is one which represents a value that is too large for the size of the segment
received. In the event of an LV field error which gives rise to a loss of confidence in the correctness
of the other fields in the packet, the packet is discarded without any further action.
6.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
7.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received

CIVIL AVIATION
S.R.O. 32
packet. If no paragraph number is referenced, the normal processing is defined in the table entry.
8.The error procedure consists of performing the specified actions when entering the d3 state (which
includes forwarding a RESET REQUEST packet to the peer XDLP) and sending a RESET RE-
QUEST packet to the DCE (via the reformatting process).
9.RR, RNR, and REJECT packets have no end-to-end significance and are not forwarded to the
DCE.
10.The receipt of a packet smaller than the maximum packet size with M-bit = 1 will cause a reset to
be generated and the remainder of the sequence will be discarded.
Table 5-20.  DCE effect on ADCE (GDCE) call setup and clearing states
ADCE (GDCE) call setup and clearing states
 (see Notes 1, 7 and 8)
ADCE (GDCE)
GDLP
to GDLP
GDLP (ADLP)ADCE (GDCE)
(ADLP)
(ADLP)
Packet received
CALL
CALL
DATA
CLEAR
CLEAR
from DCE(see READY
REQUEST
REQUEST TRANSFER REQUEST
REQUEST
Notes 2 and 4)
p1
p2
p3
p4
p6
p7
CALL
A=NORMAL
INVALID
INVALID
INVALID
INVALID
INVALID
REQUEST
((6)(3)(a))
(see Note 5)
(see Note 3) (see Note 3)(see Note 3)
(see Note 3)
(see Note 6)
S=p3(forward)
CALL ACCEPTA=DISCARD
A=NORMAL INVALID
INVALID
A=DISCARDA=DISCARD
(see Note 4)
S=P4
(see Note 3) (see Note 3)
 (forward)
CLEAR
A=DISCARD
A=NORMAL A=NORMAL A=NORMALA=DISCARDA=DISCARD
REQUEST
((6)(3)(c))
((6)(3)(c))
((6)(3)(c))
(see Note 4)
S=p7
S=p7
S=p7
(forward)
(forward)
(forward)
DATA,
A=DISCARD
INVALID
INVALID
See Table
A=DISCARDA=DISCARD
INTERRUPT
(see Note 3)
(see Note 3) 5-21
or RESET
packets
(see Note 4)
 NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.This is the DTE packet received via the DCE after all DTE/DCE processing has occurred.
Procedures local to the DTE/DCE interface (such as RR, RNR, and REJECT if in effect), do not affect

CIVIL AVIATION
S.R.O. 32
the XDCE directly. All error procedures as documented in ISO 8208 have been performed. Hence
certain packets are rejected by the interface and are not represented in this table.
3.The DCE in its protocol operation with the DTE will detect this error condition, hence the errone-
ous packet can be said never to “reach” the XDCE; see also Note 2.
4.The channel number for the DTE/DCE need not be the same channel number used for the ADCE/
GDCE; a packet from the DTE which contains a channel number is associated with an air/ground
channel by means of a previously established cross-reference table. If none exists then the DTE/DCE
channel by definition references an air/ground channel in the p1 state.
5.The ADCE assigns all channel numbers used between the ADLP and GDLP; hence call collisions
(denoted p5 ISO 8208) are not possible; see also Note 4.
6.A CALL REQUEST from the DTE can never be associated with an XDCE channel number which
is not in the p1 state.
7.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that
the packet/state combination cannot occur.
8.The number in parentheses below an “A = NORMAL” table entry is the
paragraph number in this document that defines the actions to be taken to
perform normal processing on the received packet. If no paragraph number
is referenced, the normal processing is defined in the table entry.
Table 5-21.  DCE effect on ADCE (GDCE) reset states
ADCE (GDCE) reset states
(see Notes 1, 4 and 5)
ADCE (GDCE)
RESET
FLOW CONTROL
GDLP (ADLP)
REQUEST
READY
RESET REQUEST
to GDLP (ADLP)
Packet received from
d1
d2
d3
DCE
RESET REQUEST
A=NORMAL
A=NORMAL
A=DISCARD
((6)(7))
((6)(7))
S=d3
S=d1
(forward)
(forward)
RESET
INVALID
INVALID
INVALID
CONFIRMATION
(see Note 3)
(see Note 3)
(see Note 3)
INTERRUPT
See Table 5-22
A=DISCARD
Hold interrupt until
Mode S reset complete

CIVIL AVIATION
S.R.O. 32
INTERRUPT
See Table 5-22
A=DISCARD
INVALID
CONFIRMATION
(see Note 3)
DATA (see Note 2)
A=NORMAL
A=DISCARD
Hold data until ModeS
((6)(4))
reset complete
(forward)
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.This is the DTE packet received via the DCE after all DTE/DCE processing has occurred.
Procedures local to the DTE/DCE interface (such as RR, RNR, and REJECT if in effect), do not affect
the XDCE directly. All error procedures as documented in ISO 8208 have been performed. Hence
certain packets are rejected by the interface and are not represented in this table
3.The DCE in its protocol operation with the DTE will detect this error condition, hence the errone-
ous packet can be said never to “reach” the XDCE; see also Note 2.
4.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
5.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received
packet. If no paragraph number is referenced, the normal processing is defined in the table entry
.
Table 5-22.  DCE effect on ADCE (GDCE) interrupt transfer states
ADCE (GDCE) interrupt transfer state
 (see Notes 1, 4 and 5)
GDLP (ADLP)
GDLP (ADLP)
Packet received from DCE
INTERRUPT READY
INTERRUPT SENT
 (see Note 2)
i1
i2
INTERRUPT
INVALID
A=NORMAL
CONFIRMATION
(See Note 3)
((6)(4)(e))
S=i1
(forward)

CIVIL AVIATION
S.R.O. 32
 ADCE (GDCE) interrupt transfer states
       (see Notes 1, 4 and 5)
ADCE (GDCE)
ADCE (GDCE)
Packet received
 INTERRUPT READY
 INTERRUPT SENT
from DCE (see Note 2)
j1
j2
INTERRUPT
A=NORMAL
INVALID
((6)(4)(e))
(see Note 3)
S=j2
(forward)
NOTES:
1.The XDCE is not necessarily in the same state as the DTE/DCE interface.
2.This is the DTE packet received via the DCE after all DTE/DCE processing has occurred.
Procedures local to the DTE/DCE interface (such as RR, RNR, and REJECT if in effect), do not affect
the XDCE directly. All error procedures as documented in ISO 8208 have been performed. Hence
certain packets are rejected by the interface and are not represented in this state.
3.The DCE in its protocol operation with the DTE will detect this error condition, hence the errone-
ous packet can be said never to “reach” the XDCE; see also Note 2.
4.Table entries are defined as follows: A = action to be taken, S = the state to be entered, D = the
diagnostic code to be used in packets generated as a result of this action, DISCARD indicates that
the received packet is to be cleared from the XDLP buffers, and INVALID indicates that the packet/
state combination cannot occur.
5.The number in parentheses below an “A = NORMAL” table entry is the paragraph number in
this document that defines the actions to be taken to perform normal processing on the received
packet. If no paragraph number is referenced, the normal processing is defined in the table entry.
Table 5-23.  Broadcast identifier number assignments
Uplink broadcast identifier
Assignment
Not valid
Reserved (differential GNSS correction)
Not valid
Reserved for ACAS (RA broadcast)
Reserved for ACAS (ACAS broadcast)
Others
Unassigned

CIVIL AVIATION
S.R.O. 32
Downlink broadcast identifier
Assignment
Not valid
Reserved (traffic information service)
Data link capability report
Aircraft identification
FE16
Update request
FF16
Search request
Others
Unassigned
Table 5-24.  Register number assignments
Transponder register No.
Assignment
Not valid
Unassigned
Linked Comm-B, segment 2
Linked Comm-B, segment 3
Linked Comm-B, segment 4
Extended squitter airborne position
Extended squitter surface position
Extended squitter status
Extended squitter identification and type
Extended squitter airborne velocity
0A16
Extended squitter event-driven information
0B16
Air/air information 1 (aircraft state)
0C16
Air/air information 2 (aircraft intent)
0D16-0E16
Reserved for air/air state information
0F16
Reserved for ACAS
Data link capability report
1116-1616
Reserved for extension to data link capability reports
Common usage GICB capability report
1816-1F16
Mode S specific services capability reports
Aircraft identification
Aircraft and airline registration markings
Antenna positions
Reserved for antenna position
Reserved for aircraft parameters

CIVIL AVIATION
S.R.O. 32
Aircraft type
2616-2F16
Unassigned
ACAS active resolution advisory
3116-3F16
Unassigned
Selected vertical intention
Next waypoint identifier
Next waypoint position
Next waypoint information
Meteorological routine air report
Transponder register No.
Assignment
Meteorological hazard report
Reserved for flight management system Mode 1
Reserved for flight management system Mode 2
VHF channel report
4916-4F16
Unassigned
Track and turn report
Position report coar
Position report fine
Air-referenced state vector
Waypoint 1
Waypoint 2
Waypoint 3
5716-5E16
Unassigned
5F16
Quasi-static parameter monitoring
Heading and speed report
Extended squitter emergency/priority status
Reserved for target state and status information
Reserved for extended squitter
Reserved for extended squitter
Aircraft operational status
6616-6F16
Reserved for extended squitter
7016-7516
Reserved for future aircraft downlink parameters
7616-E016
Unassigned
E116-E216
Reserved for Mode S BITE
E316
Transponder type/part number
E416
Transponder software revision number
E516
ACAS unit part number
E616
ACAS unit software revision number
E716-F016
Unassigned
F116
Military applications
F216
Military applications
F316-FF16
Unassigned

CIVIL AVIATION
S.R.O. 32
Note.— In the context of Table 5-24 of Schedule 5, the term “aircraft” can be understood as
“transponder carrying aircraft”, “pseudo-aircraft (e.g. an obstacle)” or “vehicle”.
Table 5-25.  MSP channel number assignments
Uplink channel
Assignment
 number
Not valid
Reserved (specific services management)
Reserved (traffic information service)
Reserved (ground-to-air alert)
Reserved (ground derived position)
ACAS sensitivity level control
Reserved (ground-to-air service request)
Reserved (air-to-ground service response)
8–63
Unassigned
Downlink channel
Assignment
number
Not valid
Reserved (specific services management)
Unassigned
Reserved (data flash)
Reserved (position request)
Unassigned
Reserved (ground-to-air service response)
Reserved (air-to-ground service request)
8–63
Unassigned

CIVIL AVIATION
S.R.O. 32
SCHEDULE 6: FIGURES FOR PART IV
For DI = 1
TMS
IIS
MBS
MES
LOS
RSS
SPARE
LAS
For DI = 7
TMS
IIS
  MBS
   MES
  LOS
   RSS
  SPARE
    LAS
Figure 6-1.  The SD field structure
Ready and restart
r1
r2
r3
Call setup and clearing
p1
p2
p3
p4
p5
p6
p7
Data transfer
d1
d2
d3
Interrupt and control
f 1
f 2
g1
g2
i1
i2
j1
j2
Note.— States r1, p4 and d1 (shown circled) are states that provide access to
the lower levels of the DCE substate hierarchy.

CIVIL AVIATION
S.R.O. 32
Figure 6-2.  DCE substate hierarchy
4 5
6 7
DP=0
MP=1
SP=1
ST=0
FILL2
P
FILL
SN
CH
LAM
AG
S
FS
F
LV
UD
Figure 6-3.  CALL REQUEST by ADLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=0
FILL
P
FILL
SN
FILL
TC
AM
AG
S
FS
F
LV
UD

CIVIL AVIATION
S.R.O. 32
Figure 6-4.  CALL REQUEST by GDLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=1
FILL2
TC
SN
CH
AM
AG
S
FILL
F
LV
UD
Figure 6-5.  CALL ACCEPT by ADLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=1
FILL
FILL
SN
CH
AM
AG
S
FILL
F
LV
UD

CIVIL AVIATION
S.R.O. 32
Figure 6-6.  CALL ACCEPT by GDLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=2
FILL2
TC
SN
CH
AM
AG
CC
DC
S
FILL
F
LV
UD
Figure 6-7.  CLEAR REQUEST by ADLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=2
FILL
TC
SN
CH
AM
AG
CC
DC
S
FILL
F
LV
UD

CIVIL AVIATION
S.R.O. 32
Figure 6-8.  CLEAR REQUEST by GDLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=3
FILL2
TC
SN
CH
AM
AG
Figure 6-9.  CLEAR CONFIRMATION by ADLP packet
4 5
6 7
DP=0
MP=1
SP=1
ST=3
FILL
TC
SN
CH
AM
AG

CIVIL AVIATION
S.R.O. 32
Figure 6-10.  CLEAR CONFIRMATION by GDLP packet
4 5
6 7
DP=1
M
SN
FILL1
PS
PR
CH
LV
UD
Figure 6-11.  DATA packet
4 5
6 7
DP=0
MP=1
SP=3
ST=1
FILL2
S
F
SN
CH
LV
UD
Figure 6-12.  INTERRUPT packet
4 5
6 7
DP=0
MP=1
SP=3
ST=3
SS=0
FILL2
SN
CH
FILL

CIVIL AVIATION
S.R.O. 32
                 Figure 6-13.  INTERRUPT CONFIRMATION packet
4 5
6 7
DP=0
MP=1
SP=3
ST=3
SS=1
FILL2
SN
CH
PR
                          Figure 6-14.  REJECT packet
4 5
6 7
DP=0
MP=1
SP=2
ST=0
FILL2
FILL
SN
CH
PR
                  Figure 6-15.  RECEIVE READY packet
4 5
6 7
DP=0
MP=1
SP=2
ST=1
FILL2
FILL
SN
CH
PR

CIVIL AVIATION
S.R.O. 32
Figure 6-16.  RECEIVE NOT READY packet
4 5
6 7
DP=0
MP=1
SP=2
ST=2
FILL2
FILL
SN
CH
FILL
RC
DC
Figure 6-17.  RESET REQUEST packet
4 5
6 7
DP=0
MP=1
SP=2
ST=3
FILL2
FILL
SN
CH
FILL
Figure 6-18.  RESET CONFIRMATION packet
4 5
6 7
DP=0
MP=1
SP=3
ST=0
OF IN
RTL
RT
ODL
OD

CIVIL AVIATION
S.R.O. 32
Figure 6-19.  ROUTE packet
4 5
6 7
DP=0
MP=1
SP=3
ST=2
FILL2
LENGTH
FIRST PACKET
LENGTH
LAST PACKET
LENGTH = 0
Figure 6-20.  MULTIPLEX packet
4 5
6 7
DP=0
MP=0
M/CH
FILL1
UD
Figure 6-21.  SHORT FORM MSP packet
4 5
6 7
DP=0
MP=1
SP=0
L
M/SN
FILL2
M/CH
UD

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32
Figure 6-23.  Control fields used in MODE S packets
SCHEDULE 7: PHYSICAL LAYER PROTOCOLS
AND SERVICES
(Regulation 23)
The aircraft and ground stations shall access the physical medium
operating in simplex mode
(1) Functions
(a) The physical layer shall provide the following
functions:
a)
transmitter and receiver frequency control;
b)
digital reception by the receiver;
c)
digital transmission bythe transmitter; and
d)
notification services.
(i) Transmitter/receiver frequency control.
The VDL physical layer shall set the trans-
mitter or receiver frequency as commanded
by the link management entity (LME).
Note.— The LME is a link layer entity as contained in the
Manuals on VDL Mode 2 and VDL Mode 3 Technical Specifi-
cations.
(ii) Digital reception by the receiver. The re-
ceiver shall decode input signals and forward
them to the higher layers for processing.

CIVIL AVIATION
S.R.O. 32
(iii) Digital transmission. The VDL physical
layer shall appropriately encode and transmit
information received from higher layers over
the RF channel.
(2)Modes 2 and 3 common physical layer
(a) Modulation scheme. Modes 2 and 3 shall use
differentially encoded 8 phase shift keying
(D8PSK), using a raised cosine filter with á = 0.6
(nominal value). The information to be transmit-
ted shall be differentially encoded with 3 bits per
symbol (baud) transmitted as changes in phase
rather than absolute phase. The data stream to be
transmitted shall be divided into groups of 3
consecutive data bits, least significant bit first.
Zeros shall be padded to the end of the transmis-
sions if needed for the final channel symbol.
(i) Data encoding. A binary data stream enter-
ing a differential data encoder shall be con-
verted into three separate binary streams X,
Y, and Z so that bits 3n form X, bits 3n + 1
form Y, and bits 3n + 2 form Z. The triplet at
time k (Xk, Yk, Zk) shall be converted to a
change in phase as shown in Table 8-1, and
the absolute phase ök is the accumulated
series of Äök, that is:
ök = ök-1 + Äök
(ii) Transmitted signal form. The phase-modu-
lated baseband signal as defined in Sub-
paragraph (2)(a)(i) of this Schedule shall
excite the pulse shape filter.

CIVIL AVIATION
S.R.O. 32
h is the complex impulse response of the pulse shape filter;
k is defined in (2)(a)(i);
ö is defined by the equation in (2)(a)(i);
t is time;
Tsis time duration of each symbol.
The output (function of time) of the pulse shape filter (s(t)) shall
modulate the carrier frequency. The pulse shape filter shall have
a nominal complex frequency response of a raised-cosine filter
with á =0.6.
(b) Modulation rate. The symbol rate shall be 10
500 symbols/second, resulting in a nominal bit
rate of 31 500 bits/s. The modulation stability
requirements for Modes 2 and 3 are provided in
Table 8-2.
(3) Mode 2 specific physical layer
Note.—TheMode2specificphysicallayerspecificationincludes
a description of the Mode 2 training sequence, forward error
correction (FEC), interleaving, bit scrambling, channel sensing,
and physical layer system parameters.
(a) To transmit a sequence of frames, a station shall
insert the bit numbers and flags (per the data link
service descriptionforMode2ascontainedinthe
Manual on VDL Mode 2 Technical Specifica-
tions), compute the FEC (per (3)(a)(ii)), inter-
leave (per (3)(a)(iii)), prepend the training se-
quence (per (3)(a)(i)), carry out bit scrambling
(per (3)(a)(iv)) and finally encode and modulate
the RF signal (per (2)(a)).

CIVIL AVIATION
S.R.O. 32
(i) Training sequence. Data transmission shall
begin with a demodulator training sequence
consisting of five segments:
a)
transmitter ramp-up and power stabilization;
b)
synchronizationandambiguity resolution;
c)
reserved symbol;
d)
transmissionlength; and
e)
header FEC.
Note.— Immediately after these segments follows an AVLC
frame with the format as contained in the data link service
description in the Manual on VDL Mode 2 Technical Specifica-
tions.
(aa) Transmitter ramp-up and power
stabilization. The purpose of the
first segment of the training se-
quence, called the ramp-up, is to
provide for transmitter power
stabilization and receiver AGC
settling, and it shall immediately
precede the first symbol of the
unique word. The duration of the
ramp-up shall be five symbol
periods. The time reference point
(t), for the following specification is
the centre of the first unique word
symbol, a point that occurs half a
symbol period after the end of the
ramp-up. Conversely stated, the
beginning of the ramp-up starts at t

CIVIL AVIATION
S.R.O. 32
= –5.5 symbol periods. The trans-
mitted power shall be less than –40
dBc prior to time t = –5.5 symbol
periods. The ramp-up shall provide
that at time t = –3.0 symbol periods
the transmitted power is 90 per
cent of the manufacturer’s stated
output power or greater (see Figure
6-1*). Regardless of the method
used to implement (or truncate) the
raised cosine filter, the output of
the transmitter between times t = –
3.0 and t = –0.5 will appear as if
‘000’ symbols were transmitted
during the ramp-up period.
Note. 1.— For Mode 3, the timing reference point is the same as
the “power reference point”.
Note 2.— It is desirable to maximize the time allowed for the AGC
settling time. Efforts should be made to have power above 90 per
cent of nominal output power at t – 3.5 symbol periods.
(bb) Synchronization and ambiguity
resolution. The second segment of
the training sequence shall consist
of the unique word:
000 010 011 110 000 001 101 110 001 100 011 111 101 111 100
and shall be transmitted from left to right.
.
(cc) Reserved symbol. The third seg-
ment of the training sequence shall
consist of the single symbol repre-
senting 000.

CIVIL AVIATION
S.R.O. 32
Note.— This field is reserved for future definition.
(dd) Transmission length. To allow the
receiver to determine the length of
the final Reed-Solomon block, the
transmitter shall send a 17-bit word,
from least significant bit (lsb) to
most significant bit (msb), indicating
the total number of data bits that
follow the header FEC.
Note.— The length does not include those bits transmitted for: the
Reed Solomon FEC, extra bits padded to ensure that the interleaver
generates an integral number of 8-bit words, or the extra bits
padded to ensure that the data encoder generates an integral
number of 3-bit symbols.
(ee) Header FEC. To correct bit errors
in the header, a (25, 20) block code
shall be computed over the re-
served symbol and the transmission
length segments. The block code
shall be transmitted as the fifth
segment. The encoder shall accept
the header in the bit sequence that
is being transmitted. The five parity
bits to be transmitted shall be
generated using the following
equation:
[
P
1 , ... , P5] = [R1 , ... , R3 , TL1 , ... , TL17] HT
where:
P
is the parity symbol (P1 shall be transmitted first);
R
is the reserved symbol;

CIVIL AVIATION
S.R.O. 32
TL
is the transmission Length symbol;
T
is the matrix transpose function; and
H
is the parity matrix defined below:
0 0000 0 00 1 1 11 1 1 11 1 1 11
H = 0 0111 1 11 0 0 00 1 1 11 1 1 11
1 1000 1 11 0 0 11 0 0 00 1 1 11
1 1011 0 11 0 1 01 0 0 11 0 0 11
0 1101 0 01 1 1 10 0 1 01 0 1 01
(ff) Bit transmission order. The five
parity bits of the resultant vector
product shall be transmitted from
the left bit first.
(ii) Forward error correction. In order to im-
prove the effective channel throughput by
reducing the number of
required
retransmissions, FEC shall be applied after
the training sequence, regardless of frame
boundaries.
(aa) FEC calculation. The FEC coding
shall be accomplished by means of
a systematic fixed-length Reed-
Solomon (RS)(255,249) 28-ary
code.
Note 1.— This code is capable of correcting up to
three octets for data blocks of 249 octets (1992 bits).
Longer transmissions must be divided up into 1992 bit
transmissions and shorter transmissions must be
extended by virtual fill with trailing zeros. Six RS-check
octets are appended for a total block of 255 octets.

CIVIL AVIATION
S.R.O. 32
The field defining the primitive polynomial of the code shall be
as follows:
p(x) = (x8 + x7 + x2 + x + 1)
   The generator polynomial shall be as follows:
where:
á is a primitive element of GF(256);
GF(256) is a Galois field (GF) of size 256.
Note 2.— The Reed-Solomon codes are described in the Recom-
mendation for Space Data System Standards Telemetry Channel
Coding, by the Consultative Committee for Space Data Systems
(see the Appendix to this chapter).
(bb) Block lengths. The six RS-check
octets shall be calculated on blocks
of 249 octets. Longer transmissions
shall be split into blocks of 249
octets, per (3)(a)(iii). Blocks of
shorter length shall be extended to
249 octets by a virtual fill of trailing
zeros. The virtual fill shall not be
transmitted. Blocks shall be coded
according to (3)(a)(ii)(cc) through
(3)(a)(ii)(cc)(C).
(cc) No error correction. For blocks
with 2 or fewer non-fill octets, no
error correction shall be used.
(A) Single-byte error correction. For
blocks with 3 to 30 non-fill octets,

CIVIL AVIATION
S.R.O. 32
all six RS-check octets shall be
generated, but only the first two
shall be transmitted. The last four
RS-check octets shall be treated as
erasures at the decoder.
(B) Two-byte error correction. For
blocks with 31 to 67 non-fill octets,
all six RS-check octets shall be
generated, but only the first four
shall be transmitted. The last two
RS-check octets shall be treated as
erasures at the decoder.
(C) Three-byte error correction. For
blocks with 68 or more non-fill
octets, all six RS-check octets shall
be generated and transmitted.
(iii) Interleaving. To improve the performance
of the FEC, an octet-based table-driven
interleaver shall be used. The interleaver
shall create a table having 255 octets per row
and c rows, where
 transmissionlength (bits)
c =
1992 (bits)
where:
a)
the transmission length is as defined in (3)(a)(i)(ee); and
b)
c = the smallest integer greater than or equal to the
value of the fraction.

CIVIL AVIATION
S.R.O. 32
After extending the data to an even multiple of 1992 bits, the
interleaver shall write the transmission stream into the first 249
octets of each row by taking each consecutive group of eight bits
and storing them from the first column to the 249th. The first bit
in each group of eight bits shall be stored in the eighth bit position;
the first group of 1992 bits shall be stored in the first row, the
second group of 1992 bits in the second row, etc. After the FEC
is computed on each row, the FEC data (or erasures) shall be
stored in columns 250 through 255. The interleaver shall then pass
the data to the scrambler by reading out column by column,
skipping any octet which contains erasures or all fill bits. All of the
bits in an octet shall be transmitted from bit 8 to bit 1.
On reception, the de-interleaver shall calculate the number of
rows and size of the last (potentially partial) row from the length
field in the header. It shall only pass valid data bytes to the higher
layer.
(iv) Bit scrambling. To aid clock recovery and to
stabilize the shape of the transmitted spec-
trum, bit scrambling shall be applied. The
pseudo noise (PN) sequence shall be a 15-
stage generator (see Figure 9-2) with the
characteristicpolynomial:
X15 + X + 1
The PN-sequence shall start after the frame synchronization
pattern with the initial value 1101 0010 1011 001 with the left- most
bit in the first stage of the register as per Figure 9-2. After
processing each bit, the register shall be shifted one bit to the right.
For possible encryption in the future this initial value shall be
programmed. The sequence shall be added (modulo 2) to the data
at the transmit side (scrambling) and to the scrambled data at the
receive side (descrambling) per Table 8-3.

CIVIL AVIATION
S.R.O. 32
(b) MODE 2 CHANNEL SENSING
(i) Channel busy to idle detection. When a
station receives on-channel power of at least
–87 dBm for at least 5 milliseconds, then:
a)
with a likelihood of 0.9, it shall continue to consider the
channel occupied if the signal level is attenuated to below -92
dBm for less than 1 millisecond; and
b)
with a likelihood of 0.9, it shall consider the channel
unoccupied if the signal level is attenuated to below –92 dBm
for at least 1.5 milliseconds.
Note.— The maximum link throughput available to all users is
highly sensitive to the RF channel sense delay (from the time
when the channel actually changes state until a station detects and
acts on that change) and RF channel seizure delay (from the time
when a station decides to transmit until the transmitter is suffi-
ciently ramped up to lock out other stations). Accordingly, it is
imperative that all efforts are made to reduce those times as the
state-of-the-art advances.
(ii) Channel idle to busy detection. With a
likelihood of at least 0.9, a station shall con-
sider the channel occupied within 1 millisec-
ond after on-channel power rises to at least –
90 dBm.
(iii) The detection of an occupied channel
shall occur within 0.5 milliseconds.
Note.— A higher probability of false alarm is acceptable on the
idle to busy detection than the busy to idle detection because of the
effects of the two different errors.

CIVIL AVIATION
S.R.O. 32
(c) MODE 2 RECEIVER/TRANSMITTER INTERACTION
(i) Receiver to transmitter turnaround time. A
station shall transmit the training sequence
such that the centre of the first symbol of the
unique word will be transmitted within 1.25
milliseconds after the result of an access
attempt is successful (see Figure 9-3). The
total frequency change during the transmis-
sion of the unique word shall be less than 10
Hz. After transmission of the unique word,
the phase acceleration shall be less than 500
Hz per second.
(ii) Transmitter to receiver turnaround time.
The transmitter power shall be –20 dBc
within 2.5 symbol periods ofthemiddleofthe
final symbol of the burst. The transmitter
power leakage when the transmitter is in the
“off” state shall be less than –83 dBm. A
station shall be capable of receiving and
demodulating with nominal performance, an
incoming signal within 1.5 milliseconds after
transmission of the final information symbol.
Note.— Reference DO-160D section 21, category H for antenna
radiated signals.
(d) MODE 2 PHYSICAL LAYER SYSTEM PARAMETERS
(i) The physical layer shall implement the sys-
tem parameters as defined in Table 8-4.
(aa) Parameter P1 (minimum trans-
mission length). Parameter P1
defines the minimum transmission
length that a receiver shall be

CIVIL AVIATION
S.R.O. 32
capable of demodulating without
degradation of BER.
(4) Mode 3 specific physical layer
Note.— The Mode 3 specific physical layer specification includes
a description of Mode 3 management (M) burst and handoff
check message (H) burst uplink, M burst downlink, voice/data (V/
D) burst, and bit scrambling.
(a) Management (M) burst and handoff check
message (H) burst uplink. The M uplink burst
(as contained in the Manual on VDL Mode 3
Technical Specifications) shall consist of three
segments, the training sequence followed by the
system data and the transmitter ramp down. The
H uplink burst (as contained in the Manual on
VDL Mode 3 Technical Specifications) shall
consist of three segments, the training sequence
followed by the handoff check message and the
transmitter ramp down.
(i) Training sequence. Uplink M burst and H
burst training sequences shall consist of two
componentsas follows:
a)
transmitter ramp up and power stabilization; and
b)
synchronizationandambiguity resolution.
(aa) Transmitter ramp-up and power
stabilization. This shall be as
defined in Section (3)(a)(i)(aa).
(bb) Synchronization and ambiguity resolution. The
second component of the training sequence shall consist of the
synchronization sequence, known as S2*, as follows:

CIVIL AVIATION
S.R.O. 32
000 001 101 100 110 010 111 100 010 011 101 000 111 000 011
and shall be transmitted from left to right.
Note.— The sequence S2* is very closely related to the sequence
S2 (Section (4)(c)(i)(bb)) . The 15 phase changes between the 16
symbols of S2* are each exactly 180o out of phase from the 15
phase changes associated with S2 . This relationship can be used
to simplify the process of simultaneously searching for both
sequences.
System data and handoff check message. The non-3T configu-
ration (as contained in the Manual on VDL Mode 3 Technical
Specifications) system data shall consist of 32 transmitted sym-
bols. The 96 transmitted bits shall include 48 bits of information
and 48 parity bits, generated as 4 Golay (24, 12) code words. The
3T configuration as contained
in the Manual on VDL Mode 3
Technical Specifications shall consist of 128 transmitted symbols.
The 384 transmitted bits shall include192bits of information and
192 parity bits, generated as 16 Golay (24, 12) code words. The
3T configuration handoff check message shall consist of 40
transmittedsymbols.The120transmittedbitsshallinclude60bits
of information and 60 parity bits, generated as 5 Golay (24,12)
code words.
The specific definition of the Golay encoder shall be as follows:
If the 12 bit input bit sequence is written as a row vector x, then
the 24 bit output sequence can be written as the row vector y,
where y = x G, and the matrix G shall be given by

CIVIL AVIATION
S.R.O. 32
1 1 0 1 0 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0 1 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0
1 1 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 1 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0
1 1 1 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0
G =
1 0 1 1 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0 0
1 0 0 1 1 0 0 1 1 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0
0 1 0 1 1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0
0 0 1 0 1 1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 1 0 1 1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0
1 1 0 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1 0
1 0 1 0 1 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 1
Note.— The extended Golay code allows for the correction of
any error pattern with 3 or fewer bit errors and the detection of
any 4-bit error pattern.
(iii) Transmitter ramp-down. The transmitter
power shall be –20 dBc within 2.5 symbol
periods of the middle of thefinalsymbolofthe
burst. The transmitter power leakage when
the transmitter is in the “off” state shall be
less than -83 dBm.
Note.— Reference RTCA/DO-160D section 21, category H for
antenna radiated signals.
(b) Management (M) burst downlink. The M
downlink burst (as contained in the Manual on
VDL Mode 3 Technical Specifications) shall
consist of three segments, the training sequence
followed by the system data and the transmitter
ramp down.
(i) Training sequence. The M downlink burst
trainingsequenceshallconsistoftwocompo-
nents as follows:

CIVIL AVIATION
S.R.O. 32
a)
transmitter ramp up and power stabilization; and
b)
synchronizationandambiguity resolution.
(aa) Transmitter ramp-up and power
stabilization. This shall be as
defined in (4)(a)(i)(aa).
(bb) Synchronization and ambiguity
resolution. Three separate syn-
chronization sequences shall be
used for this burst type. The
standard sequence, known as S1,
shall be as follows:
000 111 001 001 010 110 000 011 100 110 011 111 010 101 100
and shall be transmitted from left to right. The special sequence
usedtoidentifypollresponsesshallbeasdefinedin(4)(a)(i)(bb).
The special sequence used to identify net entry requests (S1*)
shall use the following sequence:
000 001 111 111 100 000 110 101 010 000 101 001 100 011 010
and shall be transmitted from left to right.
Note.— The sequence S1* is very closely related to the sequence
S1. The 15 phase changes between the 16symbols of S1* are each
exactly 180o out of phase from the 15 phase changes associated
with S1 . This relationship can be used to simplify the process of
simultaneously searching for both sequences.
(ii) System data. The system data segment shall
consist of 16 transmitted symbols. The 48
transmitted bits shallbe encoded as 24 bits of
system data and 24 bits of parity bits gener-

CIVIL AVIATION
S.R.O. 32
ated as two consecutive (24, 12) Golay code
words. The encoding of the (24, 12) Golay
code words should be as defined in (4)(a)(ii).
(iii) Transmitter ramp-down. This shall be as
defined in (4)(a)(iii).
(c) Voice or data (V/D) burst. The V/D burst (as
contained in the Manual on VDL Mode 3 Tech-
nical Specifications) shall consist of four seg-
ments: the training sequence followed by the
header, the user information segment and the
transmitter ramp down. The same V/D burst
format shall be used for both uplink and downlink.
(i) Training sequence. V/D burst training se-
quence shall consist of two components as
follows:
a)
transmitter ramp-up and power stabilization; and
b)
synchronizationandambiguity resolution.
(aa) Transmitter ramp-up and power
stabilization. This shall be as
specified in (4)(a)(i)(aa).
(bb) Synchronization and ambiguity
resolution. The second component
of the training sequence shall
consist of the synchronization
sequence, known as S2, as follows:
000 111 011 010 000 100 001 010 100 101 011 110 001 110 101
and shall be transmitted from left to right.

CIVIL AVIATION
S.R.O. 32
(ii) Header. The header segment shall consist of
8 transmitted symbols. The 24 transmitted
bits shall be encoded as 12 bits of header
informationand12paritybits,generatedasa
single (24, 12) Golay code word. The encod-
ing of the (24, 12) Golay code word shall be
as defined in (4)(a)(ii).
(iii) User information. The user information seg-
ment shall consist of 192 3-bit symbols. When
transmitting voice, FEC shall be applied to the
analysis output of the vocoder specified in
6.8. The vocoder shall provide satisfactory
performance in a BER environment of 10–3
(with a design goal of 10–2). The overall bit
rate of the vocoder including FEC is 4 800
bits/s (except when in the truncated mode in
which the bit rate is 4 000 bits/s).
(aa) When transmitting user data, the
576 bits shall be encoded as a
single Reed-Solomon (72, 62) 28–
ary code word. For user data input
to the Reed-Solomon encoder of
length less than 496 bits, input data
shall be padded with zeroes at the
end to a full length of 496 bits. The
fielddefining the primitive polyno-
mial of the code shall be as de-
scribed in (3)(a)(ii)(aa). The
generator polynomial shall be as
follows:

CIVIL AVIATION
S.R.O. 32
Note.—TheReed-Solomon(72,62)codeiscapableofcorrecting
up to five 28-ary (code word) symbol errors in the received word.
(iv) Transmitter ramp-down. This shall be as
defined in (4)(a)(iii).
(d) Interleaving. There shall be no interleaving in
Mode 3 operation.
(e) Bit scrambling. Under Mode 3 operation, bit
scrambling, as specified in (3)(a)(iv) shall be
performed on each burst, starting after the train-
ing sequence. The scrambling sequence shall be
reinitialized on each bursteffectivelyproviding a
constant overlay for each of the Mode 3 fixed
length bursts.
(f) Receiver/transmitter interaction. The switch-
ing times in this subsection will be defined as the
time between the middle of the last information
symbol of one burst and the middle of the first
symbol of the synchronization sequence of the
subsequent burst.
Note.— This nominal time will be shortened by considerations
such as the finite width of each symbol due to Nyquist filteringand
the ramp up and power stabilization sequence. Such alternative
definitions could yield switching times up to 8 symbol periods
shorter.
(i) Receiver to transmitter switching time. An
aircraft radio shall be capable of switching
from reception to transmission within 17 sym-
bol periods. This time can be relaxed to 33

CIVIL AVIATION
S.R.O. 32
symbol periods for aircraft radios which do
not implement functions requiring discrete
addressing.
Note 1.— The shortest R/T switching time for an aircraft radio
occurs when the reception of an uplink M channel beacon is
followed by a V/D transmission in the same slot. In certain
instances where aircraft radios do not implement functions
requiring discrete addressing, the R/T switching time can be
increased since the last two Golay words of the uplink M channel
beacon need not be read.
Note 2.— The minimum turnaround time assumes that in
configurations 3V1D, 2V1D, and 3T (as contained in Section
5.5.2.4 of the Manual on VDL Mode 3 Technical Specifica-
tions), the aircraft radios will be provided with software that
will prevent them from transmitting a downlink M channel
message in a slot following the reception of a voice message
from another aircraft with a long time delay.
(ii) Transmitter to receiver switching time. An
aircraft radio shall be capable of switching
from transmission to reception within 32 sym-
bol periods.
Note.— The worst case T/R switching time for an aircraft radio
occurs when it transmits a downlink M channel message and
receives a V/D message in the same slot.
(g) Fringe coverage indication
(i) Indication of near edge-of-coverage shall
be provided to the VDL Mode 3 aircraft
.

CIVIL AVIATION
S.R.O. 32
SCHEDULE 8: Tables for PART V
(PART V)
Table 8-1. Modes 2 and 3 data encoding
Xk
Y
Zk
ÄÖk
0 ð / 4
1 ð / 4
2 ð / 4
3 ð / 4
4 ð / 4
5 ð / 4
6 ð / 4
7 ð / 4
Table 8-2. Modes 2 and 3 modulation stability
VDL Mode
Aircraft
Ground
 Modulation
Modulation
 Stability
Stability
Mode 2
± 0.0050 per cent
± 0.0050 per cent
Mode 3
± 0.0005 per cent
± 0.0002 per cent
Table 8-3. Scrambler functions
Function
Data in
Data out
scrambling
clean data
scrambled data
descrambling
scrambled data
clean data

CIVIL AVIATION
S.R.O. 32
Table 8-4. Physical services system parameters
Symbol
Parameter name
Mode 2 value
P1
Minimumtransmission
131071 bits
length
Table 8-5. VDL Mode 4 operating on frequencies
between
112.0–117.975 MHz
Frequency (MHz)
Maximum level of unwanted
signal at receiver input (dBm)
88–104
+15
+10
+5
107.9
Note.— The relationship is linear between adjacent points desig-
nated by the above frequencies.

CIVIL AVIATION
S.R.O. 32
SCHEDULE 9: Figures for PART V
(PART V)
Power at 90 per cent
by t = -3
Major divisions are
symbol periods
Centre of first symbol of unique word
-5.5
-5
-4
-3
-2
-1

CIVIL AVIATION
S.R.O. 32
Figure 9-1. Transmitter power stabilization
⊕
T
T
T
T
T
T
T
(1)
(1)
(0)
(1)
Data in
Data out
(0)
(0)
(1)
⊕
Legend:
1 clock period delay
stage number
initial value
module 2 adder (exclusive OR): ⊕

CIVIL AVIATION
S.R.O. 32
Figure 9-2. PN-generator for bit scrambling sequence
Figure 9-3. Receive to Transmit turnaround time
SCHEDULE 10: RADIO FREQUENCY (RF) CHARACTERISTICS
(Regulation 30)

CIVIL AVIATION
S.R.O. 32
(1) General radio characteristics
(a) AeroMACSshalloperateintimedivisionduplex
(TDD) mode.
(b) AeroMACS shall operate with a 5 MHz channel
bandwidth.
(c) AeroMACS MS antenna polarization shall be
vertical.
(d) AeroMACSBSantennapolarizationshallhavea
vertical component.
(e) AeroMACS shall operate without guard bands
between adjacent AeroMACS channels.
(f) AeroMACS shall operate according to the
orthogonal frequency division multiple access
method.
(g) AeroMACS shall support both segmented partial
usage sub-channelization (PUSC) and PUSC
with all carriers as subcarrier permutation meth-
ods.
(2) Frequency bands
(a) AeroMACS equipment shall operate in the band
from 5 030 MHz to 5 150 MHz in channels of 5
Mhation 21zbandwidth.
Note 1.— Some States may, on the basis of national regula-
tions, have additional allocations to support AeroMACS.
Information on the technical characteristics and operational
performance of AeroMACS is contained in the AeroMACS
Minimum Operational Performance Specification (MOPS)

CIVIL AVIATION
S.R.O. 32
(EUROCAE ED-223 / RTCA DO-346) and AeroMACS Mini-
mum Aviation System Performance Standard (MASPS)
(EUROCAE ED-227).
Note 2.— The last centre frequency of 5 145 MHz is selected as
the reference frequency for the numbering of AeroMACS
channels. AeroMACS nominal centre frequencies are numbered
downward from the reference frequency in 5 MHz steps.
(b) The mobile equipment shall operate at centre
frequencies offset from the preferred frequen-
cies, with an offset of 250 kHz step size.
Note.— The nominal centre frequencies are the preferred centre
frequencies for AeroMACS operations. However, the base
stations should have the capability to deviate from the preferred
centre frequencies to satisfy potential nationalspectrum authority
implementation issues (i.e. to allow AeroMACS operations with-
out receiving or causing interference to other systems operating
in the band such as MLS and AMT).
(3) Radiated power
(a) Themaximummobilestationequivalentisotropic
radiated power (EIRP) shall not exceed 30 dBm.
(b) ThemaximumbasestationEIRPinasectorshall
not exceed 39.4 dBm.
(c) In order to meet ITU requirements, the total
base station EIRP in a sector should be de-
creased from that peak, considering the an-
tenna characteristics, at elevations above the
horizon. Further information is provided in
the guidance material.

CIVIL AVIATION
S.R.O. 32
Note 1.— EIRP — defined as antenna gain in a specified
elevation direction plus the average AeroMACS transmitter
power. While the instantaneous peak power from a given trans-
mitter may exceed that level when all of the subcarriers randomly
align in phase, when the large number of transmitters assumed in
the analysis is taken into account, average power is the appropri-
ate metric.
Note 2.— If a sector contains multiple transmit antennas (e.g.,
multiple input multiple output (MIMO) antenna), the specified
power limit is the sum of the powers from each antenna.
(4) Minimumreceiver sensitivity
(a) AeroMACSreceiversensitivityshallcomplywith
Table 10-1, AeroMACS receiver sensitivity val-
ues.
Note 1.— The computation of the sensitivity level for
AeroMACS is described in the Aeronautical Mobile Airport
Communications System (AeroMACS) Manual (Doc 10044).
Note 2.— AeroMACS receiver would be 2 dB more sensitive
than indicated if Convolutional Turbo Codes (CTC) is used.
Note 3.— The sensitivity level is defined as the power level
measured at the receiver input when the bit error rate (BER) is
equal to 1 × 10-6 and all active subcarriers are transmitted in the
channel. In general, the requisite input power depends on the
number of active subcarriers of the transmission.
Note4.—ThevaluesinTable10-1assumeareceivernoisefigure
of 8 dB.
Note 5.— The sensitivity values in Table 10-1 assume absence of
any source of interference except for thermal and receiver noise.

CIVIL AVIATION
S.R.O. 32
Table 10-1. AeroMACS receiver sensitivity values
M
o
d
u
l
a
t
i
o
n
 s
c
h
e
m
e
R
e
p
.

F
a
c
t
o
r
M
S
 S
e
n
s
i
t
i
v
i
t
y
B
S
 S
e
n
s
i
t
i
v
i
t
y
u
s
i
n
g
 c
o
n
v
o
l
u
t
i
o
n
a
l
c
o
d
e
s

(
C
C
)
e
n
c
o
d
i
n
g

s
c
h
e
m
e
Q
A
M

/
-
.

d
B
m
-
.

d
B
m
Q
A
M

/
-
.

d
B
m
-
.

d
B
m
Q
A
M

/
-
.

d
B
m
-
.

d
B
m
Q
A
M

/
-
.

d
B
m
-
.

d
B
m
Q
P
S
K

/
-
.

d
B
m
-
.

d
B
m
Q
P
S
K

/
-
.

d
B
m
-
.

d
B
m
Q
P
S
K
/

w
i
t
h
-
.

d
B
m
-
.

d
B
m
r
e
p
e
t
i
t
i
o
n
N
o
t
e
.
—
A
Q
A
M
t
r
a
n
s
m
i
s
s
i
o
n
i
s
o
p
t
i
o
n
a
l
f
o
r

M
S
.
(
)

S
p
e
c
t
r
a
l
m
a
s
k
a
n
d

e
m
i
s
s
i
o
n
s
(a) The power spectral density of the emissions
when all active subcarriers are transmitted in the
channel shall be attenuated below the maximum
power spectral density as follows:
a)
on any frequency removed from the assigned frequency
between 50 and 55 per cent of the authorized bandwidth: 26 +
145 log (per cent of BW/50) dB;
b)
on any frequency removed from the assigned frequency
between 55 and 100 per cent of the authorized bandwidth: 32 +
31 log (per cent of (BW)/55) dB;
c)
on any frequency removed from the assigned frequency
between 100 and 150 per cent of the authorized bandwidth: 40
+57 log (per cent of (BW)/100) dB; and
d)
on any frequency removed from the assigned frequency
beyond 150 per cent of the authorized bandwidth: 50 dB.

CIVIL AVIATION
S.R.O. 32
Note.— The power spectral density at a given frequency is the
power within a bandwidth equal to 100 kHz centred at this
frequency, divided by this measurement bandwidth. It is made
clear that the measurement of the power spectral density should
encompass the energy over at least one frame period.
(b) AeroMACS shall implement power control.
(c) AeroMACSminimumrejectionforadjacent(+/–
5MHz) channel, measured at BER=10-6 level for
a victim signal power 3 dB higher than the
receiver sensitivity, shall be 10 dB for 16 QAM 3/
4.
(d) AeroMACSminimumrejectionforadjacent(+/–
5MHz) channel, measured at BER=10-6 level for
a victim signal power 3 dB higher than the
receiver sensitivity, shall be 4 dB for 64 QAM 3/
4.
(e) AeroMACS minimum rejection for second adja-
cent (+/–10MHz) channel and beyond, measured
at BER=10-6 level for a victim signal power 3 dB
higher than the receiver sensitivity, shall be 29 dB
for 16 QAM 3/4.
(f) AeroMACS minimum rejection for second adja-
cent (+/–10MHz) channel and beyond, measured
at BER=10-6 level for a victim signal power 3 dB
higher than the receiver sensitivity, shall be 23 dB
for 64 QAM 3/4.
Note.— For additional clarification to the requirements stated in
Sub-paragraphs (5)(c), (5)(d), (5)(e) and (5)(f) of this Schedule,
refer to IEEE 802.16-2009 section 8.4.14.2.

CIVIL AVIATION
S.R.O. 32
(6) Frequency tolerance
(a) AeroMACS BS transmitter frequency tolerance
shallbebetterthan+/-2×10-6ofnominalchannel
frequency.
(b) AeroMACS MS transmitter centre frequency
shall be locked to that of the BS transmission
centre frequency with a tolerance better than 2
per cent of the subcarrier spacing.
(c) AeroMACS MS shall track the frequency of the
BS and shall defer any transmission if synchroni-
zation is lost or exceeds the tolerances given
above.
SCHEDULE 11: AFTN NETWORK
(1) TECHNICAL PROVISIONS RELATING TO
TELETYPEWRITER APPARATUS AND CIRCUITS
USED IN THE AFTN
(Regulation 34)
(a) In international teletypewriter circuits of the
AFTN, using a 5-unit code, the International
Telegraph Alphabet No. 2 (see Table 11-1) shall
be used only to the extent prescribed in 4.1.2 of
Annex 10 Volume II.
(b) The modulation rate shall be determined by bilat-
eral or multilateral agreement between adminis-
trations concerned, taking into account primarily
traffic volume.
(c) The nominal duration of the transmitting cycle shall be
at least 7.4 units (preferably 7.5), the stop element
lasting for at least 1.4 units (preferably 1.5).

CIVIL AVIATION
S.R.O. 32
(i) The receiver shall be able to translate cor-
rectly in service the signals coming from a
transmitter with a nominal transmitting cycle
of 7 units.
(d) Apparatus in service shall be maintained and
adjusted in such a manner that its net effective
margin is never less than 35 per cent.
(e) The number of characters which the textual line
of the page-printing apparatus may contain shall
be fixed at 69.
(f) In start-stop apparatus fitted with automatic time
delay switches, the disconnection of the power
supply to the motor shall not take place before the
lapse of at least 45 seconds after the reception of
the last signal.
(g) Arrangements should be made to avoid the muti-
lation of signals transmitted at the head of a
message and received on start-stop reperforating
apparatus.
(i) If the reperforating apparatus is provided
with local means for feeding the paper, not
more than one mutilated signal should be
tolerated.
(h) Complete circuits should be so engineered and
maintained that their degree of standardized test
distortion does not exceed 28 per cent on the
standardized text:
THE QUICK BROWN FOX
JUMPS OVER THE LAZY DOG

CIVIL AVIATION
S.R.O. 32
or
VOYEZ LE BRICK GEANT
QUE JEXAMINE PRES DU
WHARF
(i) Thedegreeofisochronousdistortiononthestand-
ardized text of each of the parts of a complete
circuit shall be as low as possible, and in any case
should not exceed 10 per cent.
(j) The overall distortion in transmitting equipment
used on teletypewriter channels shall not exceed
5 per cent.
(k) AFTNcircuitsshallbeequippedwithasystemof
continuouscheckofchannelcondition. Addition-
ally, controlled circuit protocols shall be applied.
(2) TERMINAL EQUIPMENT ASSOCIATED WITH
AERONAUTICAL RADIOTELETYPEWRITER CHAN-
NELS OPERATING IN THE BAND 2.5 – 30 MHz
(Regulation 35)
(a) Selection of type of modulation and code
(i) Frequency shift modulation (F1B) should be
employed in radioteletypewriter systems used
in the aeronautical fixed service (AFS), ex-
cept where the characteristics of the inde-
pendent sideband (ISB) method of operation
are of advantage.
Note.— F1B type of modulation is accomplished by shifting a
radio frequency carrier between two frequencies representing
“position A” (start signal polarity) and “position Z” (stop signal
polarity) of the start-stop 5-unit telegraphic code.

CIVIL AVIATION
S.R.O. 32
(b) System characteristics
(i) The characteristics of signals from
radioteletypewriter transmitters utilizing
F1B modulation should be as follows:
a)
Frequency shift: the lowest possible value.
b)
Frequency shift tolerance: within plus or minus 3 per
cent of the nominal value of the frequency shift.
c)
Polarity: single channel circuits: the higher frequency
corresponds to “position A” (start signal polarity).
(ii) The variation of the mean between the
radio frequencies representing respec-
tively “position A” and “position Z” should
not exceed 100 Hz during any two-hour
period.
(iii) The overall distortion of the teletypewriter
signal, as monitored at the output of the
radio transmitter or in its immediate vicin-
ity, should not exceed 10 per cent.
Note.— Such distortion means the displacement in time of the
transitions between elements from their proper positions, ex-
pressed as a percentage of unit element time.
(iv) Radioteletypewriter receivers concerned
with F1B modulation should be capable of
operating satisfactorily on signals having
the characteristics set out in (2)(b)(i) and
(2)(b)(ii).
(v)
The characteristics of multichannel transmis-
sion of teletypewriter signals over a radio circuit should

CIVIL AVIATION
S.R.O. 32
be established by agreement between the Administrations
concerned.
(3) CHARACTERISTICSOFINTERREGIONALAFS
CIRCUITS
(Regulation 36)
(a) Interregional AFS circuits being implemented or
upgraded shall employ high quality telecommuni-
cations service. Modulation rate shall take into
account traffic volumes expected under both
normal and alternate route conditions.
(4) TECHNICAL PROVISIONS RELATING TO ATS
MESSAGE TRANSMISSION
(Regulation 37)
(a) Interconnectionbydirectoromnibuschannels—
low modulation rates — 5-unit code.
Note.— See 8.6 for medium modulation rates.
(i) AFTN techniques (cf. 8.2) shall be used.
(5) TECHNICAL PROVISIONS RELATING TO IN-
TERNATIONAL GROUND-GROUND DATA INTER-
CHANGE AT MEDIUM AND HIGHER SIGNALLING
RATES
(Regulation 38)
Note.—Throughoutthissectioninthecontextofcodedcharacter
sets, the term “unit” means the unit of selective information and
is essentially equivalent to the term “bit”.
(a) General

CIVIL AVIATION
S.R.O. 32
(i) In international data interchange of charac-
ters, a 7-unit coded character set providing a
repertoire of 128 characters and designated
asInternationalAlphabetNo.5(IA-5)should
be used. Compatibility with the 5-unit coded
character set of International Telegraph Al-
phabet No. 2 (ITA-2) shall be ensured where
applicable.
(ii) When the provisions of Sub-paragraph
(5)(a)(i) are applied, International Alphabet
No. 5 (IA-5) contained in Table 11-2 shall be
used.
(aa) The serial transmission of units
comprisinganindividualcharacter
of IA-5 shall be with the low order
unit (b1) transmitted first.
(bb) When IA-5 is used, each charac-
ter should include an additional
unit for parity in the eighth level
position.
‘(cc) When the provisions of
(5)(a)(ii)(bb) are applied, the sense
of the character parity bit shall
produce even parity in links which
operate on the start-stop principle,
and odd parity in links using end-to-
end synchronous operations.
(dd) Character-for-character conversion shall
be as listed in Tables 11-3 and 11-4 for
all characters which are authorized in the
AFTN format for transmission on the
AFS in bothIA-5 and ITA-2.

CIVIL AVIATION
S.R.O. 32
(ee) Characters which appear in only
one code set, or which are not
authorized for transmission on the
AFS shall be as depicted in the
code conversion tables.
(b) Data transmission characteristics
(i) The data signaling rate shall be chosen from
amongthefollowing:
ts/s
4 800 bits/s
bits/s 9 600 bits/s
bits/s
(ii) Thetypeoftransmissionforeachdatasignal-
ling rate shall be chosen as follows:
Data signalling rate
Type of transmission
600 bits/s
Synchronous or asynchronous serial
transmission
1200 bits/s
Synchronous or asynchronous serial
transmission
2400 bits/s
Synchronousserial transmission
4800 bits/s
Synchronousserial transmission
9600 bits/s
Synchronousserial transmission
(iii) The type of modulation for each data signal-
ling rate shall be chosen as follows:
Data signaling rate
Typeof modulation
600 bits/s
Frequency
1 200 bits/s
Frequency
2 400 bits/s
Phase
4 800 bits/s
Phase
9 600 bits/s
Phase-amplitude

CIVIL AVIATION
S.R.O. 32
Note.— This recommendation does not necessarily apply to
ground-groundextensionsofair-groundlinksusedexclusively for
the transfer of air-ground data, inasmuch as such circuits may be
considered as part of the air-ground link.
(iv) CHARACTER STRUCTURE ON DATA LINKS
(aa) Character parity shall not be used
for error checking on CIDIN links.
Parity appended to IA-5 coded
characters per (5)(a)(ii)(bb), prior
to entry to the CIDIN shall be
ignored. For messages exiting the
CIDIN, parity shall be generated in
accordance with (5)(a)(ii)(cc).
(bb) Characters of less than eight bits in
length shall be padded out to eight
bits in length before transmission
over any octet-based or bit-oriented
communications network. The
padding bits shall occupy the higher
order end of the octet, i.e. bit 8, bit
7 as required, and shall have the
binary values 0.
(v) When exchanging data over CIDIN links
using bit-oriented procedures, the entry cen-
tre address, exit centre addresses and desti-
nation addresses in the Transport and CIDIN
Packet Headers shall be in the IA-5 charac-
ter set contained in Table 11-2.
(vi) When transmitting messages in AFTN for-
mat over CIDIN links using bit-oriented pro-
cedures, the messages should be in the IA-5
character set contained in Table 11-2.

CIVIL AVIATION
S.R.O. 32
(c) Ground-groundcharacter-orienteddatalinkcon-
trol procedures
Note.— The provisions of this section pertain to ground-ground
data interchange applications using IA-5 prescribed by 8.6.1 and
which employ the ten transmission control characters (SOH,
STX, ETX, EOT, ENQ, ACK, DLE, NAK, SYN, and ETB) for
data link control, over synchronous or asynchronous transmission
facilities.
(i) Descriptions.Thefollowingdescriptionsshall
applytodatalinkapplicationscontainedinthis
section:
a)
A master station is that station which has control of the
data link at a given instant.
b)
A slave station is one that has been selected to receive
a transmission from the master station.
c)
A control station is the single station on a multipoint link
that is permitted to assume master status and deliver messages
to one or more individually selected (non-control) tributary
stations, or it is permitted to assign temporary master status to
any of the other tributary stations.
(ii) MESSAGE COMPOSITION
a)
A transmission shall consist of characters from IA-5
transmitted in accordance with (5)(a)(ii)(bb) and shall be either
an information message or a supervisory sequence.
b)
An information message used for the exchange of data
shall take one of the following forms:

CIVIL AVIATION
S.R.O. 32
1)
S
E
B
T
—TEXT—- T
C
X
X
C
2)
S
E
B
T
—TEXT—- T
C
X
B C
3)
S
S
E B
O
—HEADIN---
T
—TEXT—-T C
H
X
X C
4)
S
S
E B
O
—HEADIN--
T
—TEXT—-T C
H
X
B C
5)
S
E
B
O
—HEADING— T
C
H
B
C
B
Note 1.—
C is a block check character (BCC).
C
Note 2.— In formats 2), 4), and 5) above which end with ETB,
some continuationis required.
c)
A supervisory sequence shall be composed of either a
single transmission control character (EOT, ENQ, ACK or
NAK) or a single transmission control (ENQ) preceded by a
prefix of up to 15 non-control characters, or the character
DLE used in conjunction with other graphic and control char-
acters to provide additional communication control functions.

CIVIL AVIATION
S.R.O. 32
(iii) Three system category A: two-way alter-
nate, multipoint allowing either centralized or
non-centralized operation and single or multi-
ple message-oriented information transfers
without replies (but with delivery verifica-
tion).
System category B: two-way simultaneous, point-to-point em-
ployingmessageassociatedblockingandmodulo8 numbering of
blocks and acknowledgements.
System category C: two-way alternate, multipoint allowing only
centralized (computer-to-terminal) operation, single or multiple
message transfers with replies.
(aa) In addition to the characteristics
prescribed in the paragraphs that
follow for both system categories
A and B, other parameters that
shall be accounted for in order to
ensure viable, operationally reliable
communications include:
a)
the number of SYN characters required to establish and
maintain synchronization;
Note.—Normallythetransmittingstationsendsthreecontiguous
SYN characters and the receiving station detects at least two
before any action is taken.
b)
the values of system time-outs for such functions as
“idle line” and “no response” as well as the number of auto-
matic retries that are to be attempted before manual interven-
tion is signalled;
c)
the composition of prefixes within a 15 character maxi-
mum.

CIVIL AVIATION
S.R.O. 32
Note.— By agreement between the administrations concerned,
it is permissible for supervisory signals to contain a station
identification prefix using characters selected from columns 4
through 7 of IA-5.
(bb) For multipoint implementations
designed to permit only central-
ized (computer-to- terminal)
operations, the provisions of
(5)(c)(vii) should be employed.
(iv) BLOCK CHECK CHARACTER
(aa) Both system category A and B
shall utilize a block check character
to determine the validity of a
transmission.
(bb) The block check character shall be
composed of 7 bits plus a parity bit.
(cc) Each of the first 7 bits of the block
check character shall be the
modulo 2 binary sum of every
element in the same bit 1 to bit 7
column of the successive charac-
ters of the transmitted block.
(dd) The longitudinal parityofeach
column oftheblock,includingthe
block check character, shall be
even.
(ee) The sense of the parity bit of the
block check character shall be the
same as for the information char-
acters.

CIVIL AVIATION
S.R.O. 32
(ff) SUMMATION
(A) The summation to obtain the block
check character shall be started by
the first appearance of either SOH
(start of heading) or STX (start of
text).
(B) The starting character shall not be
includedinthe summation.
(C) If an STX character appears after
the summation has been started by
SOH, then the STX character shall
be included in the summation as if it
were a text character.
(D) With the exception of SYN (syn-
chronous idle), all the characters
which are transmitted after the
start of the block check summation
shall be included in the summation,
including the ETB (end of transmis-
sion/block) or ETX (end of text)
control character which signals that
the following character is the block
check character.
(E) No character, SYN or otherwise,
shall be inserted between the ETB
or ETX character and the block
check character.
(v) DESCRIPTION OF SYSTEM CATEGORY A

CIVIL AVIATION
S.R.O. 32
System category A is one in which a number of stations are
connected by a multipoint link and one station is permanently
designated as the control station which monitors the link at all
times to ensure orderly operation.
(aa) LINK ESTABLISHMENT PROCEDURE
(A) To establish the link for transmis-
sion,thecontrol stationshall either:
a)
poll one of the tributary stations to assign it master
status; or
b)
assume master status and select one or more tributary
(slave) stations to receive a transmission.
(B) Polling shall be accomplished by the
control station sending a polling
supervisory sequence consisting of
a prefix identifying a single tribu-
tary station and ending in ENQ.
(C) A tributary station detecting its
assignedpollingsupervisoryse-
quence shall assume master status
and respond in one of two ways:
a)
if the station has a message to send, it shall initiate a
selection supervisory sequence as described in
(5)(c)(v)(aa)(E);
b)
if the station has no message to send, it shall send EOT,
and master status shall revert to the control station.
(D) If the control station detects an
invalid or no response resulting
from a poll, it shall terminate by

CIVIL AVIATION
S.R.O. 32
sending EOT prior to resuming
polling or selection.
(E) Selection shall be accomplished by
the designated master station
sending a selection supervisory
sequence consisting of a prefix
identifying a single station and
ending in ENQ.
(F) A station detecting its assigned
selection supervisory sequence
shall assume slave status and send
one of two replies:
a)
if the station is ready to receive, it shall send a prefix
followed by ACK. Upon detecting this reply, the master station
shall either select another station or proceed with message
transfer;
b)
if the station is not ready to receive, it shall send a prefix
followed by NAK and thereby relinquish slave status. If the
master station receives NAK, or no reply, it shall either select
another or the same tributary station or terminate;
c)
it shall be permissible for N retries (N e” 0) to be made
to select a station for which NAK, an invalid reply, or no
response has been received.
(G) If one or more stations have been
selected and have properly re-
sponded with ACK, the master
station shall proceed with message
transfer.
(bb) MESSAGE TRANSFER PROCEDURE

CIVIL AVIATION
S.R.O. 32
(A) The master station shall send a
message or series of messages,
with or without headings to the
selected slave station(s).
(B) The transmission of a message
shall:
a)
begin with:
—
SOH if the message has a heading,
—
STX if the message has no heading;
b)
becontinuous,endingwithETX,immediatelyfollowed
by a block check character (BCC).
(C) After transmitting one or more
messages, the master station shall
verify successful delivery at each
selected slave station.
(CC) DELIVERY VERIFICATION PROCEDURE
(A) The master station shall send a
delivery verification supervisory
sequence consisting of a prefix
identifying a single slave station and
ending in ENQ.
(B) A slave station detecting its as-
signed delivery verification supervi-
sory sequence shall send one of
tworeplies:
a)
if the slave station properly received all of the transmis-
sion, it shall send an optional prefix followed by ACK;

CIVIL AVIATION
S.R.O. 32
b)
if the slave station did not receive all of the transmission
properly, it shall send an optional prefix followed by NAK.
(C) If the master station receives no
reply or an invalid reply, it shall
request a reply from the same or
another slave station until all
selected stations have been prop-
erly accounted for.
(D) If the master station receives a
negative reply (NAK) or, after N
e” 0 repeat attempts, no reply, it
shall repeat that transmission to the
appropriate slave stations at a later
opportunity.
(E) After all messages have been sent
and delivery verified, the master
station shall proceed with link
termination.
(dd) LINK TERMINATION PROCEDURE
(A) The terminate function, negating
the master or slave status of all
stations and returning master status
to the control station, shall be
accomplished by the master station
transmitting EOT.
(vi) DESCRIPTION OF SYSTEM CATEGORY B
System category B is one in which two stations are on a point-
to-point, full-duplex link and each station has the capability to
maintain concurrent master and slave status, i.e. master status

CIVIL AVIATION
S.R.O. 32
on its transmit side and slave status on its receive side and both
stations can transmit simultaneously.
(aa) LINK ESTABLISHMENT PROCEDURE
(A) To establish the link for message
transfers (from the calling to the
called station), the calling station
shall request the identity of the
called station by sending an identifi-
cation supervisory sequence
consisting of a DLE character
followed by a colon character, an
optional prefix, and ENQ.
(B) The called station, upon detecting
ENQ, shall send one of two replies:
a)
if ready to receive, it shall send a sequence consisting of
a DLE followed by a colon, a prefix which includes its identity
and ended by ACK0 (see (5)(c)(vi)(bb)(E). This establishes
the link for message transfers from the calling to the called
station;
b)
if not ready to receive, it shall send the above sequence
with the ACK0 replaced by NAK.
(C) Establishment of the link for mes-
sage transfers in the opposite
direction can be initiated at any
time following circuit connection in
a similar manner to that described
above.
(bb) MESSAGE TRANSFER PROCEDURE

CIVIL AVIATION
S.R.O. 32
(A) System category B message
transfer provides for message
associated blocking with longitudi-
nal checking and modulo 8 num-
bered acknowledgements.
(B) It is permissible for a transmission
block to be a complete message or
a portion of a message. The send-
ing station shall initiate the trans-
mission with SOTB N followed by:
a)
SOH if it is the beginning of a message that contains a
heading;
b)
STX if it is the beginning of a message that has no
heading;
c)
SOH if it is an intermediate block that continues a
heading;
d)
STX if it is an intermediate block that continues a text.
Note.— SOTB N is the two-character transmission control
sequence DLE = (characters 1/0, and 3/13) followed by the block
number, N, where N is one of the IA-5 characters 0, 1 ... 7
(characters 3/0, 3/1 ... 3/7).
(C) A block which ends at an interme-
diate point within a message shall
be ended with ETB; a block which
ends at the end of a message shall
be ended with ETX.
(D) It shall be permissible for each
station to initiate and continue to
send messages to the other concur-

CIVIL AVIATION
S.R.O. 32
rentlyaccording to the following
sequence.
a)
It shall be permissible for the sending station (master
side) to send blocks, containing messages or parts of mes-
sages, continuously to the receiving station (slave side) without
waiting for a reply.
b)
It shall be permissible for replies, in the form of slave
responses, to be transmitted by the receiving station while the
sending station is sending subsequent blocks.
Note.— By use of modulo 8 numbering of blocks and replies, it
shall be permissible for the sending station to send as many as
seven blocks ahead of the received replies before being
required to stop transmission until six or less blocks are
outstanding.
c)
If a negative reply is received, the sending station
(master side) shall start retransmission with the block following
the last block for which the proper affirmative acknowledge-
ment was received.
(E) Slave responses shall be according
to one of the following:
a) if a transmission block is received without error and the
station is ready to receive another block, it shall send DLE, a
colon, an optional prefix, and the appropriate acknowledgement
ACKN (referring to the received block beginning with SOTB
N, e.g. ACK0, transmitted as DLE0 is used as the affirmative
reply to the block numbered SOTB0, DLE1 for SOTB1, etc.);
b)
if a transmission block is not acceptable, the receiving
station shall send DLE, a colon, an optional prefix, and NAK.

CIVIL AVIATION
S.R.O. 32
(F) Slave responses should be inter-
leaved between message blocks
and transmitted at the earliest
possible time.
(cc) LINK TERMINATION PROCEDURE
(A) If the link has been established for
message transfers in either or both
directions, the sending of EOT by a
station shall signal the end of
message transfers in that direction.
To resume message transfers after
sending EOT, the link shall be re-
established in that direction.
(B) EOT shall only be transmitted by a
station after all outstanding slave
responses have been received or
otherwise accounted for.
(dd) CIRCUIT DISCONNECTION
(A) On switched connections, the data
links in both directions shall be
terminated before the connection is
cleared. In addition, the station
initiating clearing of the connection
shall first announce its intention to
do so by transmitting the two-
character sequence DLE EOT,
followed by any other signals
required to clear the connection.
(vii) DESCRIPTION OF SYSTEM CATEGORY C (CEN-
TRALIZED)

CIVIL AVIATION
S.R.O. 32
System category C (centralized) is one (like system category A)
in which a number of stations are connected by a multipoint link
and one station is designated as the control station but (unlike
system category A) provides only for centralized (computer-to-
terminal) operations where message interchange (with replies)
shall be constrained to occur only between the control and a
selected tributary station.
(aa) LINK ESTABLISHMENT PROCEDURE
(A) To establish the link for transmis-
sion the control station shall either:
a)
poll one of the tributary stations to assign it master
status; or
b)
assume master status and select a tributary station to
assume slave status and receive a transmission according to
either of two prescribed selection procedures:
1)
selection with response (see (5)(c)(vii)(aa)(E)); or
2)
fast select (see (5)(c)(vii)(aa)(G)).
(B) Polling is accomplished by the
control station sending a polling
supervisory sequence consisting of
a prefix identifying a single tribu-
tary station and ending in ENQ.
(C) A tributary station detecting its
assigned polling supervisory se-
quence shall assume master status
and respond in one of two ways:
a)
if the station has a message to send, it shall initiate
message transfer. The control station assumes slave status;

CIVIL AVIATION
S.R.O. 32
b)
if the station has no message to send, it shall send EOT
and master status shall revert to the control station.
(D) If the control station detects an
invalid or no response resulting
from a poll, it shall terminate by
sending EOT prior to resuming
polling or selection.
(E) Selection with response is accom-
plished by the control station
assuming master status and sending
a selection supervisory sequence
consisting of a prefix identifying a
single tributary station and ending in
ENQ.
(F) A tributary station detecting its
assigned selection supervisory
sequence shall assume slave status
and send one of two replies:
a)
if the station is ready to receive, it shall send an optional
prefix followed by ACK. Upon detecting this reply, the master
station shall proceed with message transfer;
b)
if the station is not ready to receive, it shall send an
optional prefix followed by NAK. Upon detecting NAK, it
shall be permissible for the master station to again attempt
selecting the same tributary station or initiate termination by
sending EOT.
Note.— If the control station receives an invalid or no reply,
it is permitted to attempt again to select the same tributary or
after N retries (N e
0) either to exit to a recovery procedure
or to initiate termination by sending EOT.

CIVIL AVIATION
S.R.O. 32
(G) Fast select is accomplished by the
control station assuming master
status and sending a selection
supervisory sequence, and without
ending this transmission with ENQ
or waiting for the selected tributary
to respond, proceeding directly to
message transfer.
(bb) MESSAGE TRANSFER PROCEDURE
(A) The station with master status shall
send a single message to the station
with slave status and wait for a
reply.
(B) The message transmission shall:
a)
begin with:
—
SOH if the message has a heading,
—
STX if the message has no heading; and
b)
becontinuous,endingwithETX,immediatelyfollowed
by BCC.
(C) The slave station, upon detecting
ETX followed by BCC, shall send
one of two replies:
a)
if the messages were accepted and the slave station is
ready to receive another message, it shall send an optional
prefix followed by ACK. Upon detecting ACK, the master
station shall be permitted either to transmit the next message
or initiate termination;

CIVIL AVIATION
S.R.O. 32
b)
if the message was not accepted and the slave station is
ready to receive another message, it shall send an optional
prefix followed by NAK. Upon detecting NAK, the master
station may either transmit another message or initiate termina-
tion. Following the NAK reply, the next message transmitted
need not be a retransmission of the message that was not
accepted.
(D) If the master station receives an
invalid or no reply to a message, it
shall be permitted to send a deliv-
ery verification supervisory se-
quence consisting of an optional
prefix followed by ENQ. Upon
receipt of a delivery verification
supervisory sequence, the slave
station repeats its last reply.
(E) N retries (N e 0) may be made
by the master station in order to get
a valid slave reply. If a valid reply
is not received after N retries, the
master station exits to a recovery
procedure.
(cc) LINK TERMINATION PROCEDURE
(A) The station with master status shall
transmit EOT to indicate that it has
no more messages to transmit.
EOT shall negate the master/slave
status of both stations and return
master status to the control station.
(d) Ground-groundbit-orienteddatalinkcontrol pro-
cedures

CIVIL AVIATION
S.R.O. 32
Note.— The provisions of this section pertain to ground-ground
data interchange applications using bit-oriented data link control
procedures enabling transparent, synchronous transmission that
is independent of any encoding; data link control functions are
accomplished by interpreting designated bit positions in the trans-
mission envelope of a frame.
(i) Thefollowingdescriptionsshallapplytodata
linkapplicationscontainedinthis section:
a)
Bit-oriented data link control procedures enable trans-
parent transmission that is independent of any encoding.
b)
A data link is the logical association of two intercon-
nected stations, including the communication control capability
of the interconnected stations.
c)
A station is a configuration of logical elements, from or
to which messages are transmitted on a data link, including
those elements which control the message flow on the link via
communication control procedures.
d)
A combined station sends and receives both commands
and responses and is responsible for control of the data link.
e)
Data communication control procedures are the means
used to control and protect the orderly interchange of informa-
tion between stations on a data link.
f)
A component is defined as a number of bits in a pre-
scribed order within a sequence for the control and supervision
of the data link.
g)
An octet is a group of 8 consecutive bits.
h)
A sequence is one or more components in prescribed
order comprising an integral number of octets.

CIVIL AVIATION
S.R.O. 32
i)
A field is a series of a specified number of bits or
specified maximum number of bits which performs the func-
tions of data link or communications control or constitutes data
to be transferred.
j)
A frame is a unit of data to be transferred over the data
link, comprising one or more fields in a prescribed order.
k)
A common ICAO data interchange network (CIDIN)
switching centre is that part of an automatic AFTN switching
centre which provides for the entry, relay, and exit centre
functions using the bit-oriented link and CIDIN network
procedures specified in this section and includes the appropri-
ate interface(s) with other parts of the AFTN and with other
networks.
(ii) BIT-ORIENTED DATA LINK CONTROL PROCEDURES
FOR POINT-TO-POINT, ROUND-GROUND DATA IN-
TERCHANGE APPLICATIONS EMPLOYING SYNCHRO-
NOUS TRANSMISSION FACILITIES
Note.— The following link level procedures are the same as the
LAPB link level procedures described in ITU CCITT Recom-
mendation X.25, Section 2, Yellow Book (1981 version). Later
versions of Recommendation X.25 will be reviewed as they are
released to ascertain whether or not they should be adopted.
(aa) Frame format. Frames shall
contain not less than 32 bits, ex-
cluding the opening and closing
flags, and shall conform to the
following format:
FLAG ADDRESS CONTROL INFORMATION FCS
FLAG
F
A
 C
I
 F

CIVIL AVIATION
S.R.O. 32
(A) A frame shall consist of an opening
flag (F), an address field (A), a
control field (C), an optional infor-
mation field (I), a frame check
sequence (FCS), and a closing flag
sequence (F), and shall be transmit-
ted in that order.
Note.— In relation to CIDIN, the opening flag, the fields A and
C, the FCS and the closing flag form together the Data Link
Control Field (DLCF). The field I is denoted as the Link Data Field
(LDF).
(I) The flag (F) shall be the 8-bit sequence
01111110 which delimits the beginning and
ending of each frame. It shall be permissible
for the closingflagof a frame to also serve as
the opening flag of the next frame.
(II) The address (A) field shall consist of one
octet,excluding0bitsaddedtoachievetrans-
parent transmission, which shall contain the
link address of the combined station.
(III) Thecontrol(C)fieldshallconsistofoneoctet,
excluding0bitsaddedtoachievetransparent
transmission, and shall contain the commands,
responses, and frame sequence number com-
ponents for the control of the data link.
(IV) The information (I) field shall contain digital
data which may be presented in any code or
sequence but shall not exceed a maximum of
259 octets, excluding 0 bits added to achieve
transparent transmission. The I field shall
always be a multiple of 8 bits in length.

CIVIL AVIATION
S.R.O. 32
(V) The frame check sequence (FCS) shall con-
sist of two octets, excluding 0 bits added to
achieve transparent transmission, and shall
contain the error detecting bits.
(bb) A frame check sequence (FCS)
shall be included in each frame for
the purpose of error checking.
(A) The error checking algorithm shall
be a cyclic redundancy check
(CRC).
(B) The CRC polynomial (P(x)) shall
be
x16 + x12 + x5 + 1.
(C) The FCS shall be a 16-bit se-
quence. This FCS shall be the
ones’ complement of the remain-
der, R(x), obtained from the modulo
2 division of
x16[G(x)] + xK(x15 + x14 + x13 + ... + x2 + x1 + 1)
by the CRC polynomial, P(x).
G(x) shall be the contents of the frame existing between, but
including neither, the final bit of the opening flag nor the first bit
of the FCS, excluding bits inserted for transparent transmission.
K shall be the length of G(x) (number of bits).
(D) The generation and checking of the
FCS accumulation shall be as
follows:

CIVIL AVIATION
S.R.O. 32
a)
the transmitting station shall initiate the FCS accumula-
tion with the first (least significant) bit of the address (A) field
and shall include all bits up to and including the last bit preced-
ing the FCS sequence, but shall exclude all 0 bits (if any)
inserted to achieve transparent transmission;
b)
upon completion of the accumulation the FCS shall be
transmitted, starting with bit b1 (highest order coefficient) and
proceeding in sequence to bit b16 (lowest order coefficient)
as shown below;
First bit transmitted “!
b16
b15
b14
b3
b2
b1
x0
x1
x2
x13
x14
x15
c)
the receiving station shall carry out the cyclic redun-
dancy check (CRC) on the content of the frame commencing
with the first bit received following the opening flag, and shall
include all bits up to and including the last bit preceding the
closing flag, but shall exclude all 0 bits (if any) deleted accord-
ing to the rules for achievement of transparency;
d)
upon completion of the FCS accumulation, the receiving
station shall examine the remainder. In the absence of trans-
mission error, the remainder shall be 1111000010111000 (x0
through x15, respectively).
(cc) Achievement of transparency.
The frame format contents (A, C,
link data field, and FCS) shall be
capable of containing any bit
configuration.
(A) The followingrulesshall applytoall
frame contents, except flag se-
quences:

CIVIL AVIATION
S.R.O. 32
a)
the transmitting station shall examine the frame contents
before transmission, and shall insert a single 0 bit immediately
following each sequence of 5 consecutive 1 bits;
b)
the receiving station shall examine the received frame
contents for patterns consisting of 5 consecutive 1 bits immedi-
ately followed by one (or more) 0 bit(s) and shall remove the 0
bit which directly follows 5 consecutive 1 bits.
()
Special transmission sequences and related link
states. In addition to employing the prescribed repertoire of
commands and responses to manage the interchange of data
and control information, stations shall use the following con-
ventions to signal the indicated conditions:
a)
Abort is the procedure by which a station in the process
of sending a frame ends the frame in an unusual manner such
that the receiving station shall ignore the frame. The conven-
tions for aborting a frame shall be:
1)
transmitting at least seven, but less than fifteen, one bits
(with no inserted zeros);
2)
receiving seven one bits.
b)
Active link state. A link is in an active state when a
station is transmitting a frame, an abort sequence, or
interframe time fill. When the link is in the active state, the
right of the transmitting station to continue transmission shall
be reserved.
c)
Interframe time fill. Interframe time fill shall be accom-
plished by transmitting continuous flags between frames.
There is no provision for time fill within a frame.
d)
Idle link state. A link is in an idle state when a continu-
ous one condition is detected that persists for 15 bit times, or

CIVIL AVIATION
S.R.O. 32
longer. Idle link time fill shall be a continuous one condition on
the link.
e)
Invalid frame. An invalid frame is one that is not
properly bounded by two flags or one which is shorter than 32
bits between flags.
(ee) MODES
(A) Operational mode. The opera-
tional mode shall be the asynchro-
nous balanced mode (ABM).
(I) It shall be permissible for a combined station
in ABM to transmit without invitation from
the associated station.
(ii) A combined station in ABM shall be permit-
ted to transmit any command or response
type frame except DM.
(B) Non-operational mode. The non-
operational mode shall be the
asynchronous disconnected mode
(ADM) in which a combined
station is logically disconnected
from the data link.
(i) It shall be permissible for a combined station
in ADM to transmit without invitation from
the associated station.
(ii) A combined station in ADM shall transmit
only SABM, DISC, UA and DM frames.
(See (5)(d)(ii)(gg) for a description of the
commands and responses to which these
frame types refer.)

CIVIL AVIATION
S.R.O. 32
(iii) A combined station in ADM shall transmit a
DM when a DISC is received, and shall
discard all other received command frames
except SABM. If a discarded command
frame has the P bit set to “1”, the combined
station shall transmit a DM with the F bit set
to “1”.
(ff) Control field functions and
parameters. Control fields contain
a command or a response and
sequence numbers where applica-
ble. Three types of control fields
shall be used to perform:
a)
numbered information transfer (I-frames);
b)
numbered supervisory functions (S-frames); and
c)
unnumbered control functions (U-frames).
The control field formats shall be as shown in Table 11-5. The
functional frame designation associated with each type control
field as well as the control field parameters employed in perform-
ing these functions shall be described in the followingparagraphs.
(A) The I-frame type is used to per-
form information transfers. Except
for some special cases it is the only
format which shall be permitted to
contain an information field.
(B) The S-frame type is used for
supervisory commands and re-
sponses that perform link supervi-
sory control functions such as
acknowledge information frames,

CIVIL AVIATION
S.R.O. 32
request transmission or
retransmission of information
frames, and to request a temporary
suspension of transmission of I-
frames. No information field shall
be contained in the S-frame.
(C) The U-frame type is used for
unnumbered commands and
responses that provide additional
link control functions. One of the
U-frame responses, the frame
reject (FRMR) response, shall
contain an information field; all
other frames of the U-frame type
shall not contain an information
field.
(D) The station parameters associated
with the three control field types
shall be as follows:
a)
Modulus. Each I-frame shall be sequentially numbered
with a send sequence count, N(S), having value 0 through
modulus minus one (where modulus is the modulus of the
sequence numbers). The modulus shall be 8. The maximum
number of sequentially numbered I-frames that a station shall
have outstanding (i.e. unacknowledged) at any given time shall
never exceed one less than the modulus of the sequence
numbers. This restriction on the number of outstanding frames
is to prevent any ambiguity in the association of transmission
frames with sequence numbers during normal operation and/or
error recovery.
b)
The send state variable V(S) shall denote the sequence
number of the next in-sequence I-frame to be transmitted.

CIVIL AVIATION
S.R.O. 32
1)
The send state variable shall take on the value 0 through
modulus minus one (modulus is the modulus of the sequence
numbering and the numbers cycle through the entire range).
2)
The value of V(S) shall be incremented by one with
each successive in-sequence I-frame transmission, but shall
not exceed the value of N(R) contained in the last received
frame by more than the maximum permissible number of
outstanding I-frames (k). See i) below for the definition of k.
c)
Prior to transmission of an in-sequence I-frame, the
value of N(S) shall be updated to equal the value of V(S).
d)
The receive state variable V(R) shall denote the se-
quence number of the next in-sequence I-frame to be re-
ceived.
1)
V(R) shall take on the values 0 through modulus minus
one.
2)
The value of V(R) shall be incremented by one after the
receipt of an error-free, in-sequence I-frame whose send
sequence number N(S), equals V(R).
e)
All I-frames and S-frames shall contain N(R), the
expected sequence number of the next received frame. Prior
to transmission of either an I or an S type frame, the value of
N(R) shall be updated to equal the current value of the receive
state variable. N(R) indicates that the station transmitting the
N(R) has correctly received all I-frames numbered up to and
including N(R) – 1.
f)
Each station shall maintain an independent send state variable,
V(S), and receive state variable,V(R), on the I-frames it sends and
receives. That is, each combined station shall maintain aV(S) count on
the I-frames it transmits and a V(R) count on the I-frames it has
correctly received from theremote combined station.

CIVIL AVIATION
S.R.O. 32
g)
The poll (P/F) bit shall be used by a combined station to
solicit (poll) a response or sequence of responses from the
remote combined station.
h)
The final (P/F) bit shall be used by the remote combined
station to indicate the response frame transmitted as the result
of a soliciting (poll) command.
i)
The maximum number (k) of sequentially numbered I-
frames that a station may have outstanding (i.e. unacknowl-
edged) at any given time is a station parameter which shall
never exceed the modulus.
Note.— k is determined by station buffering limitations and
should be the subject of bilateral agreement at the time of
circuit establishment.
(gg) Commands and responses. It shall
be permissible for a combined
station to generate either com-
mands or responses. A command
shall contain the remote station
address while a response shall
contain the sending station address.
The mnemonics associated with all
of the commands and responses
prescribed for each of the three
frame types (I, S, and U) and the
corresponding encoding of the
control field are as shown in Table
11-6.
(A) The I-frame command provides the
means for transmitting sequentially
numbered frames, each of which
shall be permitted to contain an

CIVIL AVIATION
S.R.O. 32
information field.
(B) The S-frame commands and responses
shall be used to perform numbered
supervisory functions (such as
acknowledgement, polling, tempo-
rary suspension of information
transfer, or error recovery).
(I) The receive ready command or response
(RR) shall be used by a station to:
a)
indicate that it is ready to receive an I-frame;
b)
acknowledge previously received I-frames numbered up
to and including N(R) – 1;
c)
clear a busy condition that was initiated by the transmis-
sion of RNR.
Note.— It is permissible for a combined station to use the RR
command to solicit a response from the remote combined
station with the poll bit set to “1”.
(II) It shall be permissible to issue a reject com-
mand or response (REJ) to request
retransmission of frames starting with the I-
frame numbered N(R) where:
a)
I-frames numbered N(R) – 1 and below are acknowl-
edged;
b)
additional I-frames pendinginitial transmission are to be
transmitted following the retransmitted I-frame(s);
c)
only one REJ exception condition, from one given station
to another station, shall be established at any given time:

CIVIL AVIATION
S.R.O. 32
another REJ shall not be issued until the first REJ exception
condition has been cleared;
d)
the REJ exception condition is cleared (reset) upon the
receipt of an I-frame with an N(S) count equal to the N(R) of
the REJ command/response.
(III) The receive not ready command or response
(RNR) shall be used to indicate a busy con-
dition,i.e.temporaryinabilitytoacceptaddi-
tional incomingI-frames, where:
a)
frames numbered up to and including N(R) – 1 are
acknowledged;
b)
frame N(R) and any subsequent I-frames received, if
any, are not acknowledged (the acceptance status of these
frames shall be indicated in subsequent exchanges);
c)
the clearing of a busy condition shall be indicated by the
transmission of an RR, REJ, SABM, or UA with or without
the P/F bit set to “1”.
(AA)
a)
A station receiving an RNR frame when in the proc-
ess of transmitting should stop transmitting I-frames at the
earliest possible time.
b)
Any REJ command or response which was received
prior to the RNR should be actioned before the termination
of transmission.
c)
It should be permissible for a combined station to
use the RNR command with the poll bit set to “1” to obtain
a supervisory frame with the final bit set to “1” from the
remote combined station.

CIVIL AVIATION
S.R.O. 32
(IV) Itshallbepermissiblefortheselectivereject
command or response (SREJ) to be used to
request retransmission of the single I-frame
numbered N(R) where:
a)
frames numbered up to N(R) – 1 are acknowledged;
frame N(R) is not accepted; the only I-frames accepted are
those received correctly and in sequence following the I-frame
requested; the specific I-frame to be retransmitted is indicated
by the N(R) in the SREJ command/response;
b)
the SREJ exception condition is cleared (reset) upon
receipt of an I-frame with an N(S) count equal to the N(R) of
the SREJ;
c)
after a station transmits a SREJ it is not permitted to
transmit SREJ or REJ for an additional sequence error until the
first SREJ error condition has been cleared;
d)
I-frames that have been permitted to be transmitted
following the I-frame indicated by the SREJ are not
retransmitted as the result of receiving a SREJ; and
e)
itispermissibleforadditionalI-framespendinginitial
transmission to be transmitted following the retransmission of
the specific I-frame requested by the SREJ.
(C) The U-frame commands and
responses shall be used to extend
the number of link control func-
tions. Transmitted U-frames do not
increment the sequence counts at
either the transmitting or receiving
station.
a)
The U-frame mode-setting commands (SABM, and
DISC) shall be used to place the addressed station in the

CIVIL AVIATION
S.R.O. 32
appropriate response mode (ABM or ADM) where:
1)
upon acceptance of the command, the station send and
receive state variables, V(S) and V(R), are set to zero;
2)
the addressed station confirms acceptance at the earli-
est possible time by transmission of a single unnumbered
acknowledgement, UA;
3)
previously transmitted frames that are unacknowledged
when the command is actioned remain unacknowledged;
4)
the DISC command is used to perform a logical discon-
nect, i.e. to inform the addressed combined station that the
transmitting combined station is suspending operation. No
information field shall be permitted with the DISC command.
b)
The unnumbered acknowledge response (UA) shall be
used by a combined station to acknowledge the receipt and
acceptance of an unnumbered command. Received unnum-
bered commands are not actioned until the UA response is
transmitted. No information field shall be permitted with the
UA response.
c)
The frame reject response (FRMR), employing the
information field described below, shall be used by a combined
station in the operational mode (ABM) to report that one of the
following conditions resulted from the receipt of a frame
without an FCS error:
1)
a command/response that is invalid or not implemented;
2)
a frame with an information field that exceeds the size
of the buffer available;
3)
a frame having an invalid N(R) count.

CIVIL AVIATION
S.R.O. 32
Note.— An invalid N(R) is a count which points to an I-frame
which has previously been transmitted and acknowledged or
to an I-frame which has not been transmitted and is not the
next sequential I-frame pending transmission.
d)
The disconnected mode response (DM) shall be used to
report a non-operational status where the station is logically
disconnected from the link. No information field shall be
permitted with the DM response.
Note.— The DM response shall be sent to request the remote
combined station to issue a mode-setting command or, if sent
in response to the reception of a mode-setting command, to
inform the remote combined station that the transmitting station
is still in ADM and cannot action the mode-setting command.
(iii) EXCEPTION CONDITION REPORTING AND RECOV-
ERY
This section specifies the procedures that shall be employed to
effect recovery following the detection or occurrence of an
exception condition at the link level. Exception conditions de-
scribed are those situations that may occur as the result of
transmission errors, station malfunction, or operational situations.
(aa) Busy condition. A busy condition
occurs when a station temporarily
cannot receive or continue to
receive I-frames due to internal
constraints, e.g. due to buffering
limitations. The busy condition shall
be reported to the remote combined
station by the transmission of an
RNR frame with the N(R) number
of the next I-frame that is ex-
pected. It shall be permissible for
traffic pending transmission at the

CIVIL AVIATION
S.R.O. 32
busy station to be transmitted prior
to or following the RNR.
Note.— The continued existence of a busy condition must be
reported by retransmission of RNR at each P/F frame ex-
change.
(A) Upon receipt of an RNR, a com-
bined station in ABM shall cease
transmitting I-frames at the earliest
possible timebycompletingor
aborting the frame in process. The
combined station receiving an RNR
shall perform a time-out operation
before resuming asynchronous
transmission of I-frames unless the
busy condition is reported as
cleared by the remote combined
station. If the RNR was received
as a command with the P bit set to
“1”, the receiving station shall
respond with an S-frame with the F
bit set to “1”.
(B) The busy condition shall be cleared
at the station which transmitted the
RNR when the internal constraint
ceases. Clearance of the busy
condition shall be reported to the
remote station by transmission of
an RR, REJ, SABM, or UA frame
(with or without the P/F bit set to
“1”).
(bb) N(S) sequence error. An N(S)
sequence exception shall be estab-
lished in the receiving station when
an I-frame that is received error

CIVIL AVIATION
S.R.O. 32
free (no FCS error) contains an
N(S) sequence number that is not
equal to the receive variable V(R)
at the receiving station. The receiv-
ing station shall not acknowledge
(shall not increment its receive
variable V(R)) the frame causing
the sequence error, or any I-frames
which may follow, until an I-frame
with the correct N(S) number is
received. A station that receives
one or more I-frames having
sequence errors, but which are
otherwise error free, shall accept
the control information contained in
the N(R) field and the P/F bit to
perform link control functions, e.g.
to receive acknowledgement of
previously transmitted I-frames (via
the N(R)), to cause the station to
respond (P bit set to “1”).
(A) The means specified in
 (5) (d) (iii) (bb) (A) (I) and (5)
(d) (iii) (bb)(A) (II) shall be
available for initiating the
retransmission of lost or errored I-
frames following the occurrence of
a sequence error.
(I) Where the REJ command/response is used to
initiate an exception recovery following the
detection of a sequence error, only one “sent
REJ” exception condition,fromone station to
another station, shall be established at a time.
A “sent REJ” exception shall be cleared
when the requested I-frame is received. A

CIVIL AVIATION
S.R.O. 32
stationreceivingREJshallinitiatesequential (re)transmission of
I-frames starting with the I-frame indicated by the N(R) con-
tained in the REJ frame.

CIVIL AVIATION
S.R.O. 32
(II) In the event a receiving station, due to a
transmission error, does not receive (or re-
ceives and discards) a single I-frame or the
last I-frame(s) in a sequence of I-frames, it
shall not detect an out-of-sequence exception
and, therefore, shall not transmit REJ. The
station which transmitted the unacknowl-
edged I-frame(s) shall, following the comple-
tion of a system-specified time-out period,
take appropriate recovery action to deter-
mine the sequence number at which
retransmission must begin.
(III) A combined station which has timed out
waiting for a response should not
retransmit all unacknowledged frames
immediately. The station may enquire about
status with a supervisory frame.
Note 1.— If a station does retransmit all unacknowledged I-
frames after a time-out, it must be prepared to receive a
subsequent REJ frame with an N(R) greater than its send
variable V(S).
Note 2.— Since contention may occur in the case of two-way
alternate communications in ABM or ADM, the time-out interval
employed by one combined station must be greater than that
employed by the other combined station so as to permit contention
to be resolved.
(cc) FCS error. Any frame with an
FCS error shall not be accepted by
the receiving station and will be
discarded. No action shall be taken
by the receiving station as the
result of that frame.

CIVIL AVIATION
S.R.O. 32
(dd) Frame reject exception condi-
tion. A frame reject exception
condition shall be established upon
the receipt of an error-free frame
which contains an invalid or
unimplemented control field, an
invalid N(R), or an information field
which has exceeded the maximum
established storage capability. If a
frame reject exception condition
occurs in a combined station, the
station shall either:
a)
take recovery action without reporting the condition to
the remote combined station; or
b)
report the condition to the remote combined station with
a FRMR response. The remote station will then be expected to
take recovery action; if, after waiting an appropriate time, no
recovery action appears to have been taken, the combined
station reporting the frame reject exception condition may take
recovery action.
Recovery action for balanced operation includes the transmission
of an implemented mode-setting command. Higher level func-
tions may also be involved in the recovery.
(ee) Mode-setting contention. A
mode-setting contention situation
exists when a combined station
issues a mode- setting command
and, before receiving an appropri-
ate response (UA or DM), re-
ceives a mode-setting command
from the remote combined station.
Contention situations shall be
resolved in the following manner:

CIVIL AVIATION
S.R.O. 32
a)
when the send and receive mode-setting commands are
the same, each combined station shall send a UA response at
the earliest respond opportunity. Each combined station shall
either enter the indicated mode immediately or defer entering
the indicated mode until receiving a UA response. In the latter
case, if the UA response is not received:
1)
the mode may be entered when the response timer
expires; or
2)
the mode-setting command may be reissued;
b)
when the mode-setting commands are different, each
combined station shall enter ADM and issue a DM response at
the earliest respond opportunity. In the case of DISC conten-
tion with a different mode-setting command, no further action
is required.
(ff) Time-out functions. Time-out
functions shall be used to detect
that a required or expected ac-
knowledging action or response to
a previously transmitted frame has
not been received. Expiration of the
time-out function shall initiate
appropriate action, e.g. error
recovery or reissuance of the P bit.
The duration of the following time-
out functions is system dependent
and subject to bilateral agreement:
a)
combined stations shall provide a time-out function to
determine that a response frame with F bit set to “1” to a
command frame with the P bit set to “1” has not been re-
ceived. The time-out function shall automatically cease upon
receipt of a valid frame with the F bit set to “1”;

CIVIL AVIATION
S.R.O. 32
b)
a combined station which has no P bit outstanding, and
which has transmitted one or more frames for which re-
sponses are anticipated shall start a time-out function to detect
the no-response condition. The time-out function shall cease
when an I- or S-frame is received with the N(R) higher than
the last received N(R) (actually acknowledging one or more I-
frames).
(e) Common ICAO data interchange network
(CIDIN)
(i) INTRODUCTION
Note 1.— The common ICAO data interchange network (CIDIN)
is an element of the aeronautical fixed service (AFS) which uses
bit-oriented procedures, store and forward techniques and packet
switching techniques based on CCITT Recommendation X.25 to
carry messages of specific applications of the AFS such as AFTN
and operational meteorological information (OPMET).
Note 2.— The CIDIN provides a reliable common network
service for the conveyance of application messages in binary or
text form to air traffic service providers and aircraft operating
agencies.
(aa) CIDIN entry and exit centres or
stations shall be used to connect
application entities to the CIDIN.
Note.— The interfacingbetween CIDINand application entities
is a matter for local implementation.
(bb) CIDIN relay centres shall be used
to forward packets between
CIDIN entry and exit centres or
stations which are not directly
connected.

CIVIL AVIATION
S.R.O. 32
(ii) GENERAL
(aa) There shall be four protocol levels
defined to control the transfer of
messages between CIDIN switch-
ingcentres:
—
the data link protocol level
—
the X.25 packet protocol level
—
the CIDIN packet protocol level
—
the CIDIN transport protocol level.
Note 1.— The relationship of the terms used is shown in Figures
11-1 and 11-2.
Note 2.— The details of CIDIN communication procedures
and system specifications, as implemented in Europe, are
shown in the EUR CIDIN Manual (EUR Doc 005).
(bb) THE DATA LINK PROTOCOL LEVEL
(A) X.25 packets to be transferred
between two CIDIN switching
centres or a CIDIN switching
centre and a packet switched data
network, shall be formatted into
data link frames.
(B) Each data link frame shall consist
of a data link control field (DLCF),
possibly followed by a link data
field, and shall be terminated by a
frame check sequence and flag
(being the second part of the

CIVIL AVIATION
S.R.O. 32
DLCF). If a link data field is
present, the frame shall be denoted
as an information frame.
(C) X.25 packets shall be transmitted
within the link data field of informa-
tion frames. Only one packet shall
be contained in the link data field.
(cc) THE X.25 PACKET PROTOCOL LEVEL
(A) Each CIDIN packet to be trans-
ferred on CIDIN circuits between
CIDIN switching centres shall be
formatted into one X.25 packet.
When a packet switched data
network is used, it shall be permis-
sible to format the CIDIN packet
into more than one X.25 packet.
(B) The integrity of each CIDIN
packet shall be preserved by the
X.25 packet protocol by mapping
each CIDIN packet onto one
complete X.25 packet sequence, as
defined in CCITT Recommenda-
tion X.25.
(C) Each X.25 packet shall consist of
an X.25 packet header, possibly
followed by a user data field
(UDF).
(D) The X.25 packet protocol is based
on the application of virtual circuit
procedures. A virtual circuit shall
be defined as a logical path be-

CIVIL AVIATION
S.R.O. 32
tween two CIDIN switching
centres. If a packet switched data
network is used to interconnect two
CIDIN switching centres, the
procedure shall provide full compat-
ibility with the procedures to be
followed for virtual circuits accord-
ing to CCITT Recommendation
X.25.
(dd) THE CIDIN PACKET PROTOCOL LEVEL
(A) Each transport header and the
associated segment shall be pre-
ceded by a CIDIN packet header.
No further segmentation of the
CIDIN message shall be used
between transport protocol level
and CIDIN packet protocol level.
Both headers, therefore, shall be
used in combination. Together they
shall be referred to as the commu-
nicationscontrol field(CCF).
Together with the message seg-
ment they form CIDIN packets that
shall be transmitted from entry
centre to exit centre(s), when
necessary through one or more
relay centres, as an entity.
(B) CIDIN packets of one CIDIN
message shall be relayed independ-
ently via predetermined routes
through the network thus allowing
alternative routing on a CIDIN
packet basis as necessary.

CIVIL AVIATION
S.R.O. 32
(C) The CIDIN packet header shall
contain information to enable relay
centres to handle CIDIN packets in
the order of priority, to transmit the
CIDIN packets on the proper
outgoing circuit(s) and to duplicate
or multiplicate CIDIN packets
when required for multiple dissemi-
nation purposes. The information
shall be sufficient to apply address
stripping on the exit addresses as
well as on the addressee indicators
of messages in AFTN format.
(ee) THE TRANSPORT PROTOCOL LEVEL
(A) Information exchanged over the
CIDIN shall be transmitted as
CIDIN messages.
(B) The length of a CIDIN message
shall be defined by the CIDIN
packet sequence number (CPSN).
The maximum permissible length is
215 packets which in effect results
in no practical limitation.
(C) If the length of a CIDIN message
and its transport and packet head-
ers (as defined below) exceeds 256
octets, the message shall be divided
into segments and placed in the
CIDIN user data field of CIDIN
packets. Each segment shall be
preceded by a transport header
containing information to enable the

CIVIL AVIATION
S.R.O. 32
re-assembly of the CIDIN mes-
sage at the exit centre(s) from
individually received segments and
to determine further handling of the
received complete CIDIN mes-
sage.
(D) All segments of one CIDIN mes-
sage shall be provided with the
same message identification
information in the transport header.
Only the CPSN and final CIDIN
packet (FCP) indicator shall be
different.
(E) Recovery of messages shall be
performed at the transport level.

CIVIL AVIATION
S.R.O. 32
