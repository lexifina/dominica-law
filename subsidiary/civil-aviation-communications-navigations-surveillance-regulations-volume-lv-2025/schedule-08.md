SCHEDULE 8
COORDINATION AND COMMUNICATION RE-
LATED TO ACAS II AND ACAS III
1.
PROVISIONS FOR COORDINATION WITH ACAS-
EQUIPPED THREATS
(1) Multi-aircraft coordination. In a multi-aircraft situa-
tion, ACAS shall coordinate with each equipped threat individu-
ally.
(2) Data protection during coordination. ACAS shall
prevent simultaneous access to stored data by concurrent proc-
esses, in particular, during resolution message processing.
(3) Coordination interrogation. Each cycle ACAS shall
transmit a coordination interrogation to each equipped threat,
unless generation of an RA is delayed because it is not possibleto
select an RAthat can be predicted to provide adequate separation
(Regulation33(1)). The resolution message transmitted to a threat
shall include an RAC selected for that threat. If an RAC has been
received from the threat before ACAS selects an RAC for that
threat, the selected RAC shall be compatible with the received
RAC unless no more than three cycles have elapsed since the
RAC was received, theRACisaltitude-crossing,andownaircraft
address is lower in value than that of the threat in which case

CIVIL AVIATION
S.R.O. 31
ACAS shall select its RA independently. If an RAC received
from an equipped threat is incompatible with the RAC own ACAS
has selected for that threat,ACAS shall modify the selected RAC
to be compatible with the received RAC if own aircraft address
is higher in value than that of the threat.
Note.— The RAC included in the resolution message is in the
form of a vertical RAC (VRC) for ACAS II and a vertical RAC
(VRC) and/or horizontal RAC (HRC) for ACAS III.
(a) Coordination termination. Within the cycle during
which an intruder ceases to be a reason for maintain-
ing the RA, ACAS shall send a resolutionmessageto
thatintruderbymeansofacoordinationinterrogation.
Theresolutionmessageshallincludethecancellation
codeforthelastRAC sent to that intruder while it was
a reason for maintaining the RA.
Note.— During an encounter with a single threat, the threat
ceases to be a reason for the RA when the conditions for
cancelling the RA are met. During an encounter with multiple
threats, a threat ceases to be a reason for the RA when the
conditions for cancelling the RA are met in respect of that threat,
even though the RA may have to be maintained because of other
threats.
(b) ACAS coordination interrogations shall be transmit-
ted until a coordination reply is received from the
threat, up to a maximum of not less than six and not
more than twelve attempts. The successive interro-
gations shall be nominally equally spaced over a
period of 100 ±5 ms. If the maximum number of
attempts is made and no reply is received, ACAS
shall continue its regular processing sequence.
(c) ACAS shall provide parity protection for all fields in the
coordination interrogation that convey RAC information.

CIVIL AVIATION
S.R.O. 31
Note.— This includes the vertical RAC (VRC), the cancel
vertical RAC (CVC), the horizontal RAC (HRC) and the cancel
horizontal RAC (CHC).
(d) Whenever own ACAS reverses its sense against an
equipped threat, the resolution message that is sent on
the current and subsequent cycles to that threat shall
contain both the newly selected RAC and the cancel-
lation code for the RAC sent before the reversal.
(e) When a vertical RA is selected, the vertical RAC
(VRC) that own ACAS includes in a resolution
message to the threat shall be as follows:
(1) “do not pass above” when the RA is intended to
provide separation above the threat;
(2) “do not pass below” when the RA is intended to
provide separation below the threat.
(4) Resolution message processing. Resolution messages
shall be processed in the order in which they are received and with
delay limited to thatrequiredtopreventpossibleconcurrentaccess
to stored data and delays due to the processing of previously
receivedresolutionmessages.Resolution messages that are being
delayed shall be temporarily queued to prevent possible loss of
messages. Processing a resolution message shall include decoding
the message and updating the appropriate data structures with the
information extracted from the message.
Note.— According to paragraph subparagraph 1(2) resolution
message processing must not access any data whose usage is not
protected by the coordination lock state.
(a) An RAC or an RAC cancellation received from
another ACAS shall be rejected if the encoded sense
bits indicate the existence of a parity error or if

CIVIL AVIATION
S.R.O. 31
undefined value(s) are detected in the resolution
message. An RAC or an RAC cancellation received
withoutparityerrorsandwithoutundefined resolution
message values shall be considered valid.
(b) RAC storage. A valid RAC received from another
ACAS shall be stored or shall be used to update the
previouslystored RACcorresponding to that ACAS.
A valid RAC cancellation shall cause the previously
stored RAC to be deleted. A stored RAC that has not
been updated for an interval of 6 s shall be deleted.
(c) RAC record update. A valid RAC or RAC cancella-
tion received from another ACAS shall be used to
update the RAC record. If a bit in the RAC record has
not been refreshed for an interval of 6 s by any threat,
that bit shall be set to 0.
(5)
PROVISIONS FOR ACAS COMMUNICATION
WITH GROUND STATIONS
(1)
Air-initiated downlink of ACAS RAs. When an
ACAS RA exists, ACAS shall:
(a)
transfer to its Mode S transponder
an RA report for transmission to the
ground in a Comm-B reply ; and
(b)
transmit periodic RA broadcasts.
(2)
Sensitivity level control (SLC) command.
ACAS shall store SLC commands from Mode S
ground stations. An SLC command received from
a Mode S ground station shall remain effective
until replaced by an SLC command from the
same ground station as indicated by the site
number contained in the IIS subfield of the inter

CIVIL AVIATION
S.R.O. 31
rogation. If an existing stored command from a
Mode S ground station is not refreshed within 4
minutes, or if the SLC command received has the
value 15, the stored SLC command for that Mode S ground
station shall be set to 0.
(6)
PROVISIONS FOR DATA TRANSFER BETWEEN
ACAS AND ITS MODE S TRANSPONDER
(1)
Data transfer from ACAS to its Mode S trans
ponder:
(a) ACAS shall transfer RA information
to its Mode S transponder for
transmission in an RA report and in
acoordinationreply;
(b) ACAS shall transfer current sensi
tivity level to its Mode S transponder
for transmission ina sensitivitylevel
report; and
(c) ACAS shall transfer capability
information to its Mode S trans
ponder for transmission in a data link
capability report.
(2)
Data transfer from Mode S transponder to its
ACAS:
(a) ACAS shall receive from its Mode S
transponder sensitivity level control
commands transmitted by Mode S
groundstations;
(b) ACAS shall receive from its Mode S
transponder ACAS broadcast

CIVIL AVIATION
S.R.O. 31
messages transmitted by other
ACAS; and
(c) ACAS shall receive from its Mode S
transponder resolution messages
transmitted by other ACAS for air-
air coordinationpurposes.
