SCHEDULE 16
MODE S EXTENDED SQUITTER RECEIVING SYS-
TEM CHARACTERISTICS (ADS-B IN AND TIS-B IN)
Note 1.— The paragraphs herein describe the required capabili-
ties for 1 090 MHz receivers used for the reception of Mode S
extended squitter transmissions that convey ADS-B and/or TIS-
B messages. Airborne receiving systems support ADS-B and
TIS-B reception while ground receiving systems support only
ADS-B reception.
Note 2.— Detailed technical provisions for Mode S extended
squitter receivers can be found within RTCA DO-260B/
EUROCAE ED-102A, “Minimum Operational Performance
Standards for 1 090 MHz Extended Squitter Automatic Depend-
ent Surveillance – Broadcast (ADS-B) and Traffic Information
Services – Broadcast (TIS-B).”
(1)
Mode S extended squitter receiving system func-
tional requirements
(a) Mode S extended squitter receiving systems shall
perform the message exchange function (receive)
and the report assembler function.
Note.— The extended squitter receiving system receives
ADS-B Mode S extended squitter messages and outputs ADS-
B reports to client applications. Airborne receiving systems
also receive TIS-B extended squitter messages and output
TIS-B reports to client applications. This functional model
(shown in Figure 14-1) depicts both airborne and ground 1
090 MHz ADS-B receiving systems.
(b) Mode S extended squitter receiver classes. The
required functionality and performance characteris-
tics for the Mode S extended squitter receiving

CIVIL AVIATION
S.R.O. 31
system will vary depending on the ADS-B and TIS-B client applications
to be supported and the operational use of the system. Airborne Mode S
extended squitter receivers shall be consistent with the definition of
receiving system classes shown in Table 16-1.
Table 5-3: Reception performance for airborne receiving systems

CIVIL AVIATION
S.R.O. 31
Note.— Different equipment classes of Mode S extended squitter
installations are possible. The characteristics of the receiver
associated with a given equipment class are intended to be
appropriate to support the required level of operational capability.
Equipment classes A0 through A3 are applicable to those Mode
S extended airborne installations that include a Mode S extended
squitter transmission (ADS-OUT) and reception (ADS-B IN)
capability. Equipment classes B0 through B3 are applicable to
Mode S extended installations with only a transmission (ADS-B
OUT) capability and includes equipment classes applicable to
airborne, surface vehicles and fixed obstructions. Equipment
classes C1 through C3 are applicable to Mode S extended squitter
ground receiving systems.
(2)
Message exchange function
(a) Themessageexchangefunctionshallincludethe1090
MHz receiving antenna and the radio equipment
(receiver/ demodulator/decoder/data buffer) sub-func-
tions.
(b) Message exchange functional characteristics. The
airborne Mode S extended squitter receiving system
shall support the reception and decoding of all ex-
tended squitter messages as listed in Table 16-1. The
ground ADS-B extended squitter receiving system
shall, as a minimum, support the reception and decod-
ing of all of the extended squitter message types that
convey information needed to support the generation
of the ADS-B reports of the types required by the
clientATMgroundapplications.
(c) Required message reception performance. The air-
borne Mode S extended squitter receiver/demodula-
tion/ decoder shall employ the reception techniques
and have a receiver minimum trigger threshold level
(MTL) as listed in Table 16-1 as a function of the

CIVIL AVIATION
S.R.O. 31
airborne receiver class. The reception technique and
MTL for extended squitter ground receiver shall be
selected to provide the reception performance (i.e.
range and update rates) as required by the client ATM
ground applications.
(d) Enhanced reception techniques. ClassA1,A2 andA3
airbornereceiving systems shall include the following
features to provide improved probability of Mode S
extended squitter reception
in the presence of multiple overlapping Mode A/C fruit
and/ or in the presence of an overlapping stronger
Mode S fruit, as compared to the performance of the
standard reception technique required for Class A0
airborne receiving systems:
(a) Improved Mode S extended squitter pream-
ble detection.
(b) Enhanced error detection and correction.
(c) Enhanced bit and confidence declaration
techniques applied to the airborne receiver
classes as shown below:
(i)
Class A1 – Performance equivalent
to or better than the use of the “Centre Ampli-
tude” technique.
(ii)
Class A2 – Performance equivalent
to or better than the use of the “Multiple Ampli-
tude Samples” baseline technique, where at least
8 samples are taken for each Mode S bit position
and are used in the decision process.
(iii)
Class A3 – Performance equivalent

CIVIL AVIATION
S.R.O. 31
to or better than the use of the “Multiple Ampli-
tude Samples” baseline technique, where at least
10 samples are taken for each Mode S bit position
and are used in the decision process.
Note 1.— The above enhanced reception techniques are as
defined in RTCA DO-260B/EUROCAE ED-102A, Appendix I.
Note 2.— The performance provided for each of the above
enhanced reception techniques when used in a high fruit
environment (i.e. with multiple overlapping Mode A/C fruit) is
expected to be at least equivalent to that provided by the use
of the techniques described in RTCA DO-260A, Appendix I.
Note 3.— It is considered appropriate for ground ex-
tended squitter receiving systems to employ the enhanced
reception techniques equivalent to those specified for
airborne Class A2 or A3 receiving systems.
(3)
Report assembler function
(a) The report assembler function shall include the mes-
sage decoding, report assembly, and output interface
sub-functions.
(b) When an extended squitter message is received, the
message shall be decoded and the applicable ADS-B
report(s) of the typesdefinedinsubparagraph1(3)(c)
shall be generated within 0.5 seconds.
Note 1.— Two configurations of extended squitter airborne
receiving systems, which include the reception portion of the
ADS-B message exchange function and the ADS-B/TIS-B
report assembly function, are allowed:
(a)Type I extended squitter receiving systems receive
ADS-B and TIS-B messages and produce application-

CIVIL AVIATION
S.R.O. 31
specific subsets of ADS-B and TIS-B reports. Type I
extended squitter receiving systems are customised to
the particular client applications using ADS-B and TIS-B
reports. Type I extended squitter receiving systems may
additionally be controlled by an external entity to produce
installation-defined subsets of the reports that those
systems are capable of producing.
(b)Type II extended squitter receiving systems receive
ADS-B and TIS-B messages and are capable of produc-
ing complete ADS-B and TIS-B reports in accordance
with the equipment class. Type II extended squitter
receiving systems may be controlled by an external entity
to produce installation-defined subsets of the reports that
those systems are capable of producing.
Note 2.— Extended squitter ground receiving systems receive
ADS-B messages and produce either application-specific
subsets or complete ADS-B reports based on the needs of the
ground service provider, including the client applications to
be supported.
Note 3.— The extended squitter message reception function may
be physically partitioned into hardware separate from those that
implement the report assembly function.
(c)
ADS-B REPORT TYPES
Note 1.— The ADS-B report refers to the restructuring of
ADS-B message data received from Mode S extended squitter
broadcasts into various reports that can be used directly by
a set of client applications. Five ADS-B report types are
defined by the following subparagraphs for output to client
applications. Additional information on the ADS-B report
contents and the applicable

CIVIL AVIATION
S.R.O. 31
mapping from extended squitter messages to ADS-B reports
can be found in the Technical provisions for Mode S Services
and extended squitter (Doc 9871) and RTCA DO-260B/
EUROCAE ED-102A
Note 2.— The use of precision (e.g. GNSS UTC measured
time) versus non-precision (e.g. internal receiving system
clock) time sources as the basis for the reported time of
applicability is described in Sub-paragraph (1)(3)(e).
(i)
State vector report. The state vector report shall contain
time of applicability, information about an airborne or vehicle’s
current kinematic state (e.g. position, velocity), as well as a
measure of the integrity of the navigation data, based on
information received in airborne or ground position, airborne
velocity, identification and category, aircraft operational status
and target state and status extended squitter messages. Since
separate messages are used for position and velocity, the time
of applicability shall be reported individually for the position
related report parameters and the velocity related report
parameters. Also, the state vector report shall include a time of
applicability for the estimated position and/or estimated velocity
information (i.e. not based on a message with updated position
or velocity information) when such estimated position and/or
velocity information is included in the state vector report.
Note.— Specific requirements for the customisation of this
type of report may vary according to the needs of the
client applications of each participant (ground or air-
borne). The state vector data is the most dynamic of the
four ADS-B reports; hence, the applications require
frequent updates of the state vector to meet the required
accuracy for the operational dynamics of the typical
airborne or ground operations of airborne and surface
vehicles.

CIVIL AVIATION
S.R.O. 31
(ii) Mode status report. The mode status report shall
contain time of applicability and current opera-
tional information about the transmitting partici-
pant, including airborne/ vehicle address, call sign,
ADS-B version number, airborne/vehicle length
and width information, state vector qualityinfor-
mation, and other information based on informa-
tion received aircraft in operational status, target
state and status aircraft identification and cat-
egory, airborne velocity and aircraft status ex-
tended squitter messages. Each time that a mode
status report is generated, the report assembler
functionshallupdatethe report time of applicabil-
ity. Parameters for which valid data is not avail-
ableshalleitherbeindicatedasinvalidor omitted
from the mode status report.
Note 1.— Specific requirements for the customisation of this
type of report may vary according to the needs of the client
applications of each participant (ground or airborne).
Note 2.— The age of the information being reported within
the various data elements of a mode status report may vary as
a result of the information having been received within
different extended squitter messages at different times.
(iii) Air referenced velocity report. Air referenced ve-
locity reports shall be generated when air refer-
enced velocity information is received in airborne
velocity extended squitter messages. The air refer-
enced velocity report shall contain time of applicabil-
ity, airspeed and heading information. Only certain
classes of extended squitter receiving systems, as
defined in sub paragraph 1(3)(e), are required to
generate air referenced velocity reports. Each time

CIVIL AVIATION
S.R.O. 31
that an individual mode status report is generated,
the report assembly function shall update the re-
porttime of applicability.
Note 1.— The air referenced velocity report contains velocity
information that is received in airborne velocity messages
along with additional information received in airborne iden-
tification and category extended squitter messages. Air ref-
erenced velocity reports are not generated when ground
referenced velocity information is being received in the
airborne velocity extended squitter messages.
Note 2.— Specific requirements for the customisation of this
type of report may vary according to the needs of the client
applications of each participant (ground or airborne).
(iv) Resolution advisory (RA) report. The RA report
shall containtimeofapplicabilityandthecontents
of an active ACAS resolution advisory (RA) as
received in a Type=28 and Subtype=2 extended
squitter message.
Note.— The RA report is only intended to be generated by
ground receiving subsystems when supporting a ground
ADS-B client application(s) requiring active RA information.
An RA report will nominally be generated each time a
Type=28, Subtype=2 extended squitter message is received.
(v) Target state report
Note.— The target state report will be generated when
information is received in target state and status messages,
along with additional information received in airborne iden-
tification and category extended squitter messages. The
target state and status message is defined in the Technical
Provisions for Mode S Services and Extended Squitter (Doc
9871). Specific requirements for the customisation of this

CIVIL AVIATION
S.R.O. 31
type of report may vary according to the needs of the client
applications of each participant (ground or airborne).
(d) TIS-B Report Types
(i) As TIS-B messages are received by airborne
receiving systems, the information shall be re-
ported to client applications. Each time that an
individual TIS-B report is generated, the report
assembly function shall update the report time of
applicability to the current time.
Note 1.— The TIS-B message formats are defined in the
Technical Provisions for Mode S Services and ExtendedSquitter
(Doc 9871).
Note 2.— The TIS-B report refers to the restructuring of TIS-B
message data received from ground Mode S extended squitter
broadcasts into reports that can be used by a set of client
applications. Two ADS-B report types are defined by the follow-
ing subparagraphs for output to client applications. Additional
information on the TIS-B report contents and the applicable
mapping from extended squitter messages to ADS-B reports can
be found in the Technical Provisions for Mode S Services and
Extended Squitter (Doc 9871).
Note 3.— The use of precision (e.g. GNSS UTC measured
time) versus non-precision (e.g. internal receiving system
clock) time sources as the basis for the reported time of
applicability is described in sub paragraph 1(3)(e).
(ii) TIS-B target report. All received information
elements, other than position, shall be reported
directly, including all reserved fields for the TIS-
B fine format messages and the entire message
content of any received TIS-B management mes-
sage. The reporting format is not specified in

CIVIL AVIATION
S.R.O. 31
detail, except that the information content re-
ported shall be the same as the information
content received.
(iii) When a TIS-B position message is received, it is
compared with tracks to determine whether it
can be decoded into target position (i.e. corre-
lated to an existing track). If the message is
decoded into target position, a report shall be
generated within 0.5 seconds. The report shall
contain the received position information with a
time of applicability, the most recently received
velocity measurement with a time of applicability,
the estimated position and velocity applicable to a
common time of applicability, airborne/ vehicle
address,andallotherinformationinthereceived
message. The estimated values shall be based on
the received position information and the track
history of the target.
(iv) When a TIS-B velocity message is received, if it
is correlated toa completetrack, areport shallbe
generated, within 0.5 seconds of the message
reception. The report shall contain the received
velocity information with a timeofapplicability,
theestimatedpositionandvelocity applicable to a
common time of applicability, airborne/ vehicle
address,andallotherinformationinthereceived
message. The estimated values shall be based on
the received ground reference velocity informa-
tion and the track history of the target.
(v) TIS-B management report. The entire message
content of any received TIS-B management mes-
sage shall be reported directly to the client applica-
tions. The information content reported shall be the
same as the information content received.

CIVIL AVIATION
S.R.O. 31
(vi) The contents of any received TIS-B management
message shall be reported bit-for-bit to the client
applications.
(e) Reporttimeof applicability
The receiving system shall use a local source of reference time as
the basis for reporting the time of applicability, as defined for each
specific ADS-B and TIS-B report type.
(i) Precision time reference. Receiving systems in-
tended to generate ADS-B and/or TIS-B reports
based on the reception of surface position mes-
sages, airborne position messages, and/or TIS-B
messages shall use GNSS UTC measured time
for the purpose of generating the report time
applicability for the following cases of received
messages:
(aa)
version zero (0) ADS-B messages, as de
fined in sub paragraph 8(6)(b) of the
Schedule 4, when the navigation uncer
tainty category (NUC) is 8 or 9; or
(bb)
version one (1) or version two (2) ADS-B
or TIS-B messages, as defined in sub
paragraph 8(6)(b) and 8(7) of the Schedule
4 respectively, when the navigation integrity
category (NIC) is 10 or 11;
UTC measured time data shall have a minimum range of 300
seconds and a resolution of 0.0078125 (1/128) seconds.
(ii) Non-precision local time reference
(aa)
For receiving systems not intended to

CIVIL AVIATION
S.R.O. 31
generate ADS-B and/or TIS-B reports
based on reception of ADS-B or TIS-B
messages meeting the NUC or NIC criteria
as indicated in sub paragraph(3)(e)(i) a
non- precision time source shall be allowed.
In such cases, where there is no appropri
ate precision time source available, the
receiving system shall establish an appro
priate internal clock or counter having a
maximum clock cycle or count time of 20
milliseconds. The established cycle or clock
count shall have a minimum range of 300
seconds and a resolution of 0.0078125 (1/
128) seconds.
Note.— The use of a non-precision time reference as
described above is intended to allow the report time of
applicability to accurately reflect the time intervals appli-
cable to reports within a sequence. For example, the
applicable time interval between state vector reports could
be accurately determined by a client application, even
though the absolute time (e.g. UTC measured time) would
not be indicated by the report.
(f) REPORTING REQUIREMENTS
(i) Reporting requirements for Type I Mode S ex-
tended squitter airborne receiving systems. As a
minimum, the report assembler function associ-
ated with Type I Mode S extended squitter
receiving systems, as defined in sub paragraph
1(3), shall support that subset of ADS-B and TIS-
B reports and report parameters, that are re-
quired by the specific client applications being
served by that receiving system.
(ii) Reporting requirements for Type II Mode S

CIVIL AVIATION
S.R.O. 31
extended squitter airborne receiving systems. The report assembler
function associated with Type II receiving systems, as defined in sub
paragraph 1(3),, shall generate ADS-B and TIS-B reports according
to the class of the receiving systemas shown in Table 16-2 when the
prerequisite ADS-B and/or TIS-B messages are being received.
Table 16-2: Mode S extended squitter airborne receiving system report-
ing requirements
(iii) Reporting requirements for Mode S extended squitter ground receiv-
ing systems. As a minimum, the report assembler function associated
with Mode S extended squitter ground receiving systems, as defined
sub paragraph 1(3),, shall support that subset of ADS-B reports and
report parameters, that are required by the specificclientapplications
being served by that receiving system.
(4)
Interoperability
TheModeSextendedsquitterreceivingsystemshallprovideinteroperability between
the different versions of extended squitter ADS-B message formats.

CIVIL AVIATION
S.R.O. 31
Note 1.— All defined ADS-B versions and their correspond-
ing message formats are contained in the Technical Provisions
for Mode S Services and Extended Squitter (Doc 9871) and are
identified by
a version number.
Note 2.— ADS-B message formats are defined with backward
compatibility with previous versions. An extended squitter re-
ceiver can recognize and decode signals of its own version, as well
as the message formats from lower versions. The receiver,
however, can decode the portion of messages received from a
higher version transponder according to its own capability.
(a) INITIAL MESSAGE DECODING
The Mode S extended squitter receiving system shall, upon
acquiring a new ADS-B target, initially apply the decoding
provisionsapplicabletoversion0(zero)ADS-B messages until or
unless an aircraft operational status message is received indicat-
ing that a higher version message format is in use.
(b) APPLYING VERSION NUMBER
The Mode S extended squitter receiving system shall decode the
version number information conveyed in the aircraft operational
status message and shall apply the corresponding decoding rules
for the reported version, up to the highestversion supported by the
receiving system, for the decoding of the subsequent extended
squitter ADS-B messages from that specific aircraft or vehicle.
(c) HANDLING OF RESERVED MESSAGE
SUBFIELDS
The Mode S extended squitter receiving system shall ignore the
contents of any message subfield defined as reserved.

CIVIL AVIATION
S.R.O. 31
Note.— This provision supports interoperability between
message versions by allowing the definition of additional
parameters that will be ignored by earlier receiver versions
and correctly decoded by newer receiver versions.
Note 1.— Specific MTL is referenced to the signal level at the
output terminal of the antenna, assuming a passive antenna.
If electronic amplification is integrated into the antenna
assembly, then the MTL is referenced at the input to the
amplifier. For Class A3 receivers, a second performance
level is defined at a received signal level of –87 dBm where
15 per cent of the messages are to be successfully received.
MTL values refer to reception under non-interference condi-
tions.
Note 2.— The extended squitter receiver reception tech-
niques are defined in sub paragraph 1(2)(d) of schedule 16.
“Standard” reception techniques refer to the baseline tech-
niques, as required for ACAS 1 090 MHz receivers, that are
intended to handle single overlapping Mode A/C fruit. “En-
hanced” reception techniques refer to techniques intended
to provide improved reception performance in the presence
of multiple overlapping Mode A/C fruit and improved de-
coder retriggering in the presence of overlapping stronger
Mode S fruit. The requirements for the enhanced reception
techniques that are applicable to the specific airborne re-
ceiver classes are defined in sub paragraph 1(2)(d) of
schedule 16.

CIVIL AVIATION
S.R.O. 31
