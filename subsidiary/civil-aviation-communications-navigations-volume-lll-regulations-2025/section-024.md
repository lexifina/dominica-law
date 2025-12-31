24. (1) General information
Physical layer protocals
and services.
Link layer protocols and
services.

CIVIL AVIATION
S.R.O. 32
(a) Functionality. The VDL link layer shall provide
thefollowingsublayer functions:
a)
media access control (MAC) sublayer, which re-
quires the use of the carrier sense multiple access (CSMA)
algorithm for Mode 2 or TDMA for Mode 3;
b)
a data link service (DLS) sublayer:
1)
for Mode 2, the DLS sublayer provides connection-
oriented point-to-point links using data link entities (DLE) and
connectionless broadcast link over the MAC sublayer; and
2)
for Mode 3, the DLS sublayer provides acknowl-
edgedconnectionlesspoint-to-pointandpoint-to-multipoint links
over a MAC sublayer that guarantees sequencing; and
c)
a VDL management entity (VME), which estab-
lishes and maintains DLEs between the aircraft and the ground-
based systems using link management entities (LME).
(b) SERVICE
(i) Connection-oriented. The VDL Mode 2
link layer shall provide a reliable point-to-
point service using a connection-oriented DLS
sublayer.
(ii) Connectionless. The VDL Mode 2 and 3
link layers shallprovide anunacknowledged
broadcastserviceusing a connectionless DLS
sublayer.
(iii) Acknowledged connectionless. The VDL
Mode 3 link layer shall provide an acknowl-
edged point-to-point service using a
connectionless DLS sublayer that relies upon

CIVIL AVIATION
S.R.O. 32
the MAC sublayer to guarantee sequencing.
(2) MAC sublayer
(a) The MAC sublayer shall provide for the transpar-
ent acquisition of the shared communications
path. It makes invisible to the DLS sublayer the
way in which supporting communications re-
sources are utilized to achieve this.
(3) Data link service sublayer
(a) For Mode 2, the DLS shall support bit-oriented
simplex air-ground communications using the
aviation VHF link control (AVLC) protocol.
(b) For Mode 3, the DLS shall support bit-oriented,
priority based, simplex air-ground communica-
tions using the acknowledged connectionless data
link (A-CLDL) protocol.
(4) VDL management entity
(a) Services. The VME shall provide link establish-
ment,maintenanceanddisconnectionservicesas
wellassupport parameter modification. Specific
VME services, parameter formats and proce-
dures for Modes 2 and 3 are contained in the
Manuals on VDL Mode 2 and Mode 3 Technical
Specifications.
