31. (1)AeroMACS communications service provider
Radio frequency (RF)
characteristics.
Performance
requirements.

CIVIL AVIATION
S.R.O. 32
(a) Themaximumunplannedserviceoutageduration
on a per aerodrome basis shall be 6 minutes.
(b) The maximum accumulated unplanned service
outagetimeonaperaerodromebasisshallbe240
minutes/year.
(c) The maximumnumber ofunplanned serviceout-
ages shall not exceed 40 per year per aerodrome.
(d) Connection resilience. The probability that a trans-
action will be completed once started shall be at
least 0.999 for AeroMACS over any one-hour
interval.
(2) Doppler shift
(a) AeroMACS shall operate with a Doppler shift
inducedbythemovementoftheMSuptoaradial
speedof92.6km(50NM)perhour,relativetothe
BS.
(3) Delay
(a) Subnetwork entry time shall be less than 90
seconds.
(b) Subnetwork entry time should be less than 20
seconds.
(c) The from-MS data transit delay (95th percentile)
for the highest priority data service, shall be less
than or equal to 1.4 seconds over a window of 1
hour or 600 SDUs, whichever is longer.
(d) The to-MS data transit delay (95th percentile) for
thehighestprioritydataservice,shallbelessthan

CIVIL AVIATION
S.R.O. 32
or equal to 1.4 seconds over a window of 1 hour
or 600 SDUs, whichever is longer.
(4) Integrity
(a) AeroMACS BS and MS shall support mecha-
nisms to detect and correct corrupt SNSDUs.
(b) AeroMACS BS and MS shall only process
SNSDUs addressed to themselves.
(c) The residual error rate, to/from MS should be
less than or equal to 5 × 10-8 per SNSDU.
(d) The maximum bit error rate shall not exceed 10-
6 after CTC-FEC, if the received signal is equal
to or greater than the minimum sensitivity level
for the modulations scheme used, as given in
Table 10-1 of Schedule 10 of these regulations.
(5) Security
(a) AeroMACS shall provide a capability to protect
the integrity of messages in transit.
(b) AeroMACS shall provide a capability to protect
the availability of the system.
(c) AeroMACS shall provide a capability to protect
the confidentiality of messages in transit.
(d) AeroMACS shall provide an authentication ca-
pability.
(e) AeroMACS shall provide a capability to ensure
the authenticity of messages in transit.

CIVIL AVIATION
S.R.O. 32
(f) AeroMACS shall provide a capability to author-
ize the permitted actions of users of the system.
(g) If AeroMACS provide interfaces to multiple
domains, AeroMACS shall provide capability to
prevent intrusion from lower integrity domain to
higher integrity domain.
