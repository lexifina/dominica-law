28. (1) AMode4stationshallconformtotherequirements
defined in sub-regulations 20.(1)(c), 20.(3)(b), 21.(1)(a), 21.(3)(a),
21.(4), 22.(1), 22.(3)(a), 22.(4), 22.(5)(a), 22.(5)(b), 22.(5)(c),
22.(5)(d)(i) and this regulation.
(2) VDL Mode 4 radio channels
(a) VDL MODE 4 STATION FREQUENCY
RANGE
(i) Transmitter/receiver tuning range. A VDL
Mode 4 transmitter/receiver shall be capable
of tuning to any of the 25 kHz channels from
112 MHz to 137 MHz.
(ii) Simultaneous reception. A VDL Mode 4
station shall be capable of receiving two
channels simultaneously.
(iii) A VDL Mode 4 station shall be capable of
receiving additional channels simultane-
ously as required by operational services.
(b) GLOBAL SIGNALING CHANNELS
(i) VDL Mode 4 stations shall use two assigned
frequencies as global signaling channels
(GSC), to support user communications and
link management functions.
(3) System capabilities
VDL mode 4.

CIVIL AVIATION
S.R.O. 32
(a) ATN compatibility. The VDL Mode 4 system
shall support ATN/IPS-compliant subnetwork
services.
(b) Data transparency. The VDL Mode 4 system
shall provide code-independent, byte-independ-
ent transfer of data.
(c) Broadcast. The VDL Mode 4 system shall pro-
vide link layer broadcast services.
(d) Point-to-point. The VDL Mode 4 system shall
providelinklayerpoint-to-point services.
(e) Air-air communications. The VDL Mode 4
system shall provide air-air communications, with-
out ground support, as well as air-ground commu-
nications.
(f) Connection management. When supporting air-
ground operations, the VDL Mode 4 system shall
establish and maintain a reliable communications
path between the aircraft and the ground system
while allowing, but not requiring, manual inter-
vention.
(g) Ground network transition. A mobile VDL
Mode 4 DLS station shall transition from one
ground VDL Mode 4 DLS station to another as
required.
(h) Derived time capability. VDL Mode 4 shall
providethecapabilityforderivingtimefromtime-
of-arrival measurements of received VDL Mode
4 transmissions whenever externally derived es-
timates of time are unavailable.
(i) Simplex operations. Mobile and ground VDL

CIVIL AVIATION
S.R.O. 32
Mode 4 stations shall access the physical medium
operating insimplex mode.
(4) Coordinationofchannel utilization
(a) Onaregionalbasis,transmissionsshallbesched-
uled relative to UTC, to ensure efficient use of
sharedchannels and to avoid unintentional slot re-
use.
(5) Physical layer protocols and services
(a) FUNCTIONS
(i) TRANSMITTED POWER
(aa) Airborne installation. The effec-
tive radiated power shall be such as
to provide a field strength of at
least 35 microvolts per metre
(minus 114.5 dBW/m2) on the basis
of free space propagation, at
ranges and altitudes appropriate to
the conditions pertaining to the
areas over which the aircraft is
operated.
(bb) Ground installation.The effective
radiated power shall be such as to
provide a field strength of at least
75 microvolts per metre (minus 109
dBW/m2) within the defined opera-
tional coverage of the facility, on
the basis of free-space propaga-
tion.

CIVIL AVIATION
S.R.O. 32
(ii) TRANSMITTER AND RECEIVER FRE-
QUENCY CONTROL
(aa) The VDL Mode 4 physical layer
shall set the transmitter or receiver
frequency as commanded by the
link management entity (LME).
Channel selection time shall be less
than 13 ms after the receipt of a
command from a VSS user.
(iii) DATA RECEPTION BY RECEIVER
(aa) The receiver shall decode input
signals and forward them to the
higher layers for processing.
(IV) DATA TRANSMISSION BY TRANSMITTER
(aa) Data encoding and transmission.
The physical layer shall encode the
data received from the data link
layer and transmit it over the RF
channel. RF transmission shall take
place only when permitted by the
MAC.
(bb) Order of transmission. The
transmission shall consist of the
followingstagesinthefollowing
order:
a) transmitterpower stabilization;
b) bit synchronization;

CIVIL AVIATION
S.R.O. 32
c) ambiguityresolutionanddata
transmission; and
d) transmitter decay.
(cc) Automatic transmitter shutdown.
A VDL Mode 4 station shall
automatically shut-down power to
any final stage amplifier in the
event that output power from that
amplifier exceeds –30 dBm for
more than 1 second. Reset to an
operational mode for the affected
amplifier shall require a manual
operation.
(v) NOTIFICATION SERVICES
(aa) Signal quality. The operational
parameters of the equipment shall
be monitored at the physical layer.
Signal quality analysis shall be
performed in the demodulator
process and in the receive process.
(bb) Arrival time. The arrival time of
each received transmission shall be
measured with a two-sigma error
of 5 microseconds.
(cc) The receiver shall be capable of
measuring the arrival time within
a two-sigma error of 1 microsec-
ond.

CIVIL AVIATION
S.R.O. 32
(b) PROTOCOL DEFINITION FOR GFSK
(i) Modulation scheme. The modulation scheme
shall be GFSK. The first bit transmitted (in the
training sequence) shall be a high tone and the
transmitted tone shall be toggled before trans-
mitting a 0 (i.e. non-return to zero inverted
encoding).
(ii) Modulation rate. Binary ones and binary ze-
ros shall be generated with a modulation
index of 0.25 ± 0.03 and a BT product of 0.28
± 0.03, producing data transmission at a bit
rate of 19 200 bits/s ± 50 ppm.
(iii) STAGES OF TRANSMISSION
(aa) Transmitter power stabilization.
The first segment of the training
sequence is the transmitter power
stabilization, which shall have a
duration of 16 symbol periods. The
transmitter power level shall be no
less than 90 per cent of the steady
state power level at the end of the
transmitter power stabilization
segment.
(bb) Bit synchronization. The second
segment of the training sequence
shall be the 24-bit binary sequence
0101 0101 0101 0101 0101 0101,
transmitted from left to right
immediately before the start of the
data segment.
(cc) Ambiguity resolution and data
transmission. The transmission of

CIVIL AVIATION
S.R.O. 32
the first bit of data shall start 40 bit
intervals (approximately 2 083.3
microseconds) ± 1 microsecond
after the nominal start of transmis-
sion.
(dd) Transmitter decay. The transmitted
power level shall decay at least by
20 dB within 300 microseconds
after completing a transmission.
The transmitter power level shall
be less than -90 dBm within 832
microseconds after completing a
transmission.
(c) CHANNEL SENSING
(i) Estimation of noise floor. A VDL Mode 4
stationshallestimatethe noisefloorbasedon
power measurements of the channel when-
ever a valid training sequence has not been
detected.
(ii) The algorithm used to estimate the noise floor
shall be such that the estimated noise floor
shall be lower than the maximum power value
measured on the channel over the last minute
when the channel is regarded as idle.
(iii) Channel idle to busy detection. A VDL
Mode 4 station shall employ the following
means to determine the channel idle to busy
transition at the physical layer.
(aa) Detection of a training sequence.
The channel shall be declared busy
if a VDL Mode 4 station detects a

CIVIL AVIATION
S.R.O. 32
valid training sequence followed by
a frame flag.
(bb) Measurement of channel power.
Regardless of the ability of the
demodulator to detect a valid
training sequence, a VDL Mode 4
station shall consider the channel
busy with at least a 95 per cent
probability within 1 ms after on-
channel power rises to the equiva-
lent of at least four times the
estimated noise floor for at least
0.5 milliseconds.
(iv) CHANNEL BUSY TO IDLE DETECTION
(aa) A VDL Mode 4 station shall
employ the following means to
determine the channel busy to idle
transition.
(bb) Measurement of transmission
length. When the training se-
quence has been detected, the
channel busy state shall be held for
a period of time at least equal to 5
milliseconds,andsubsequently
allowed to transition to the idle
state based on measurement of
channel power.
(cc) Measurement of channel power.
When not otherwise held in the
channel busy state, a VDL Mode 4
station shall consider the channel
idle with at least a 95 per cent

CIVIL AVIATION
S.R.O. 32
probability if on-channel power falls
below the equivalent of twice the
estimated noise floor for at least
0.9 milliseconds.
(d) RECEIVER/TRANSMITTER INTERACTION
(i) Receiver to transmitter turnaround time. A
VDL Mode 4 station shall be capable of
beginningthe transmission of the transmitter
power stabilization sequence within 16 mi-
croseconds after terminating the receiver
function.
(ii) Frequency change during transmission.
The phase acceleration of the carrier from
the start of the synchronization sequence to
the data end flag shall be less than 300 Hz per
second.
(iii) Transmitter to receiver turnaround time.
A VDL Mode 4 station shall be capable of
receivingand demodulating with nominal per-
formance an incoming signal within 1 ms
after completing a transmission.
(e) PHYSICAL LAYER SYSTEM PARAM-
ETERS
(i) PARAMETER P1 (MINIMUM TRANS-
MISSION LENGTH)
(aa) A receiver shall be capable of
demodulating a transmission of
minimum length P1 without degra-
dation of BER.

CIVIL AVIATION
S.R.O. 32
(bb) The value of P1 shall be 19 200
bits.
(ii) PARAMETER P2 (NOMINAL CO-CHANNEL INTERFER-
ENCE PERFORMANCE)
(aa) The parameter P2 shall be the
nominal co-channel interference at
which a receiver shall be capable
of demodulating without degrada-
tion in BER.
(bb) The value of P2 shall be 12 dB.
(f) FM BROADCAST INTERFERENCE IMMUNITY PERFORM-
ANCE FOR VDL MODE 4 RECEIVING SYSTEMS
(i) A VDL Mode 4 station shall conform to the
requirementsdefinedinsection6.3.5.4when
operating in the band 117.975–137 MHz.
(ii) A VDL Mode 4 station shall conform to the
requirements defined below when operating
in the band 108-117.975 MHz.
(aa) The VDL Mode 4 receiving system
shall meet the requirements speci-
fied in Sub-regulation 22.(5)(a) in
the presence of two- signal, third-
order intermodulation products
caused by VHF FM broadcast
signals having levels in accordance
with thefollowing:
2N1 + N2 + 72 d” 0

CIVIL AVIATION
S.R.O. 32
for VHF FM sound broadcasting
signals in the range 107.7–108.0
MHz
 and
where the frequencies of the two
VHF FM sound broadcasting
signals produce, within the receiver,
a two-signal, third-order
intermodulation product on the
desired VDL Mode 4 frequency.
N1 and N2 are the levels (dBm) of
the two VHF FM sound broadcast-
ing signals at the VDL Mode 4
receiver input. Neither level shall
exceed the desensitization criteria
set forth in Sub-regulation
28.(5)(f)(ii)(bb)
Äf = 108.1 – f1, where f1 is the
frequency of N1, the VHF FM
sound broadcasting signal closer to
108.1 MHz.
(bb) The VDL Mode 4 receiving system
shall not be desensitized in the
presence of VHF FM broadcast
signals having levels in accordance
with Table 6-5.
(6) Link layer
(a) Details on link layer functions are contained
intheManualonVHFDigitalLink(VDL)Mode

CIVIL AVIATION
S.R.O. 32
4 (Doc 9816).
(7) Subnetwork layer and SNDCF
(a) Details on subnetwork layer functions and
SNDCF are contained in the Manual on VHF
Digital Link (VDL) Mode 4 (Doc 9816).
(8) ADS-B applications
(a) Details on ADS-B application functions are
contained in the Manual on VHF Digital Link
(VDL) Mode 4 (Doc 9816).
PART VI
AERONAUTICAL MOBILE AIRPORT
COMMUNICATIONS SYSTEM (AEROMACS)
