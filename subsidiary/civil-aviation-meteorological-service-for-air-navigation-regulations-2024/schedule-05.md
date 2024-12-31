SCHEDULE 5
(Regulation 45(1) and entire Part VIII)
TECHNICAL SPECIFICATIONS RELATED TO
SIGMET AND AIRMET INFORMATION, AERO-
DROME WARNINGS AND WIND SHEAR WARN-
INGS AND ALERTS
PART I
SPECIFICATIONS RELATED TO SIGMET
INFORMATION
1. (1) The content and order of elements in a SIGMET
messageshallbe in accordance with the template shown in Table
A6-1A.
(2) MessagescontainingSIGMET informationshallbe
identifiedas:
“SIGMET”.
(3) The sequence number referred to in the template in
Table A6- 1A shall correspond with the number of SIGMET
messages issued for the flight information region (FIR) since
0001 UTC on the day concerned. The meteorological watch
offices whose area of responsibility encompasses more than one
FIR and/or control area (CTA) shall issue separate SIGMET
messages for each FIR and/or CTA within their area of respon-
sibility.
(4) In accordance with the template in Table A6-1A,
only one of the following phenomena shall be included in a
SIGMET message, using the abbreviations as indicated below—
(5) thunderstorm
(a) Reporting thunderstorms at cruising levels irre-
spective of altitude—
Format of SIGMET
messages.

CIVIL AVIATION
SRO 35
(i) obscured
OBSC TS
(ii) embedded
      EMBD TS
(iii) frequent
FRQ TS
(iv) squall line
SQL TS
(v) obscured with hail
OBSC TSGR
(vi) embeddedwith hail
EMBD TSGR
(vii) frequent,with hail
FRQ TSGR
(viii) squalllinewith hail
SQL TSGR
(b) Reportingtropicalcycloneatcruisinglevelsirre-
spective of altitude—
(i) tropical cyclone with 10-minute mean
(ii) TC (+ cyclone name) surface wind speed of
17 m/s (34 kt) or more
(c) Reporting turbulence at cruising levels irrespec-
tive of altitude-
(i) severe turbulence
SEV TURB
(d) reporting icing at cruising levels irrespective of
altitude—
(i) severe icing
SEV ICE
(ii) severe icing due to
SEV ICE
(iii) freezing rain
FZRA

CIVIL AVIATION
SRO 35
(e) reportingotherphenomenaatcruisinglevelsirre-
spective of altitude—
(i) severe mountain wave SEV MTW
(ii) heavy duststorm
HVY DS
(iii) heavy sandstorm
HVY SS
(iv) volcanic ash
VA (+ volcano
name, if known)
(v) radioactive cloud
RDOACT CLD
(f) SIGMET information shall not contain unneces-
sary descriptive material. In describing the
weather phenomena for which the SIGMET is
issued, no descriptive material additional to that
given in paragrapg (5) shall be included. SIGMET
information concerningthunderstormsoratropi-
cal cyclone shall not include references to asso-
ciated turbulence and icing.
(g) Meteorological watch offices should issue
SIGMET informationin digital form, in addition to
the issuance of this SIGMET information in
abbreviated plain language.
(h) SIGMET if disseminated in digital form shall be
formatted in accordance with a globally
interoperable information exchange model and
shall use extensible markup language (XML)/
geography markup language (GML).
(i) SIGMET if disseminated in digital form shall be
accompanied by the appropriate metadata

CIVIL AVIATION
SRO 35
2. (1)SIGMET messages shall be disseminated to meteoro-
logicalwatch offices, WAFCs and to other meteorological offices
in accordance with regional air navigation agreement. SIGMET
messages for volcanic ash shall also be disseminated to volcanic
ash advisory centres.
(2) SIGMET messages shall be disseminated to interna-
tional OPMET databanks and the centres designated by regional
air navigation agreement for the operation of aeronautical fixed
service Internet-based services, in accordance with regional air
navigation agreement.
PART II
DETAILED CRITERIA RELATED TO SIGMET AND
SPECIAL AIR-REPORTS (UPLINK)
1. (1) In cases where the airspace is divided into an FIR and
an upper flight information region (UIR), the SIGMET should be
identified by the location indicator of the air traffic services unit
serving the FIR.
(2) The SIGMET message applies to the whole airspace
within the lateral limits of the FIR, i.e. to the FIR and to the UIR.
The particular areas and/or flight levels affected by the meteoro-
logical phenomena causing the issuance of the SIGMET are given
in the text of the message.
2. (1) An area of thunderstorms and cumulonimbus clouds
should be considered—
(a) obscured (OBSC) if it is obscured by haze or
smoke or cannot be readily seen due to darkness;
(b) embedded (EMBD) if it is embedded within cloud
layers and cannot be readily recognized;
(c) isolated (ISOL) if it consists of individual features
Identification of the
flight information region.
 Criteria related to
phenomena included in
SIGMET and AIRMET
messages and special air-
reports (uplink).
Dissemination of
SIGMET messages.

CIVIL AVIATION
SRO 35
which affect, or are forecast to affect, an area
withamaximumspatial coveragelessthan50per
cent of the area concerned (at a fixed time or
during the period of validity); and
(d) occasional (OCNL) if it consists of well-sepa-
rated features which affect, or are forecast to
affect, an area with a maximum spatial coverage
between 50 and 75 per cent of the area con-
cerned (at a fixed time or during the period of
validity).
(2) An area of thunderstorms should be considered
frequent (FRQ) if within that area there is little or no separation
between adjacent thunderstorms with a maximum spatial cover-
age greater than 75 per cent of the area affected, or forecast to
be affected, by the phenomenon (at a fixed time or during the
period of validity).
(3) Squall line (SQL) should indicate a thunderstorm
along a line with little or no space between individual clouds.
(4) Hail (GR) should be used as a further description of
the thunderstorm, as necessary.
(5) Severe and moderate turbulence (TURB) should
refer only to: low-level turbulence associated with strong surface
winds; rotor streaming; or turbulence whether in cloud or not in
cloud (CAT). Turbulence should not be used in connection with
convectiveclouds.
(6) Turbulence shall be considered—
(a) severe whenever the peak value of the cube root
of EDR exceeds 0.7; and
(b) moderate whenever the peak value of the cube

CIVIL AVIATION
SRO 35
root of EDR is above 0.4 and below or equal to
0.7.
(7) Severe and moderate icing (ICE) should refer to icing
in other than convective clouds. Freezing rain (FZRA) should
refer to severe icing conditions caused by freezing rain.
(8) A mountain wave (MTW) should be considered—
(a) severe whenever an accompanying downdraft of
3.0 m/s (600 ft/min) or more and/or severe
turbulence is observed or forecast; and
(b) moderate whenever an accompanying downdraft
of 1.75–3.0 m/s (350–600 ft/min) and/or moder-
ate turbulence is observed or forecast.
(9) Sandstorm/duststorm should be considered—
(a) heavy whenever the visibility is below 200 m and
the sky is obscured; and
(b) moderate wheneverthevisibility is:
(i) below 200 m and the sky is not obscured; or
(ii) between 200 m and 600 m.
PART III
SPECIFICATIONS RELATED TO
AERODROME WARNINGS
1. (1)The aerodrome warnings shall be issued in accordance
with the template in Table A6-2 where required by operators or
aerodrome services, and shall be disseminated in accordance
with local arrangements to those concerned.
Format and dissemina-
tion of aerodrome
warnings.

CIVIL AVIATION
SRO 35
(2) The sequence number referred to in the template in
Table A6-2 shall correspond with the number of aerodrome
warnings issued for the aerodrome since 0001 UTC on the day
concerned.
(3) In accordance with the template in Table A6-2,
aerodrome warnings should relate to the occurrence or expected
occurrence of one or more of the following phenomena:
(a) tropical cyclone (to be included if the 10-minute
mean surface wind speed at the aerodrome is
expected to be 17 m/s (34 kt) or more)
(b) thunderstorm
(c) hail
(d) snow (including the expected or observed snow
accumulation)
(e) freezing precipitation
(f) hoar frost or rime
(g) sandstorm
(h) duststorm
(i) rising sand or dust
(j) strong surface wind and gusts
(k) squall
(l) frost
(m) volcanic ash

CIVIL AVIATION
SRO 35
(n) tsunami
(o) volcanicash deposition
(p) toxic chemicals
(q) other phenomena as agreed locally.
(4) Aerodrome warnings related to the occurrence or
expected occurrence of tsunami are not required where a national
public safety plan for tsunami is integrated with the “at risk”
aerodrome concerned.
(5) The use of text additional to the abbreviations listed in
the template in Table A6-2 should be kept to a minimum. The
additional text should be prepared in abbreviated plain language
using approved ICAO abbreviations and numerical values. If no
ICAO approved abbreviations are available for any weather
phenomena, English plain language text should be used.
2.When quantitative criteria are necessary for the issue of
aerodrome warnings covering, for example, the expected maxi-
mum wind speed or the expected total snowfall, the criteria used
should be as agreed between the aerodrome meteorological
office and the users concerned.
PART IV
SPECIFICATIONS RELATED TO
WIND SHEAR WARNINGS
1. (1) Evidence of the existence of wind shear should be
derived from
(i) ground-based, wind shear remote-sensing
equipment, for example, Doppler radar;
(ii) ground-based, wind shear detection equip-
Quantitative criteria for
aerodrome warnings.
Detection of wind shear
Recommendation.

CIVIL AVIATION
SRO 35
ment, for example, a system of surface wind
and/or pressure sensors located in an array
monitoring a specific runway or runways and
associated approach and departure paths;
(iii) aircraft observations during the climb-out or
approach phases of flight to be made in
accordance with provisions of Part VI of
these Regulations; or
(iv) other meteorological information, for exam-
ple, from appropriate sensors located on ex-
isting masts or towers in the vicinity of the
aerodrome or nearby areas of high ground.
(2) Wind shear conditions are normally associated with
the followingphenomena—
(i) thunderstorms, microbursts, funnel cloud
(tornado or waterspout), and gust fronts
(ii) frontal surfaces
(iii) strong surface winds coupled with local to-
pography
(iv) sea breeze fronts
(v) mountainwaves(includinglow-levelrotorsin
the terminal area)
(vi) low-leveltemperature inversions.
2. (1) The wind shear warnings shall be issued in accord-
ance with the template in Table A6-3 and shall be disseminated
in accordance with local arrangements to those concerned.
Format and dissemina-
tion of wind shear
warnings and alerts.

CIVIL AVIATION
SRO 35
(2) The Sequence number referred to in the template in
Table A6-3 shall correspond with the number of wind shear
warnings issued for the aerodrome since 0001 UTC on the day
concerned.
(3) Theuseoftextadditionaltotheabbreviationslistedin
the template in Table A6-3 should be kept to a minimum. The
additional text should be prepared in abbreviated plain language
using approved ICAO abbreviations and numerical values. If no
ICAO approved abbreviations are available, English plain lan-
guage text should be used.
(4) When an aircraft report is used to prepare a wind
shear warning, or to confirm a warning previously issued, the
corresponding aircraft report, including the aircraft type, should
be disseminated unchanged in accordance with local arrange-
ments to those concerned.
(5) Following reported encounters by both arriving and
departing aircraft, two different wind shear warnings may exist:
one for arriving aircraft and one for departing aircraft.
(6) Specifications for reporting the intensity of wind
shear recognizes that pilots, when reporting wind shear, may use
the qualifying terms “moderate”, “strong” or “severe”, based to
a large extent on their assessment of the intensity of the wind
shear encountered.
(7) The wind shear alerts shall be disseminated from
automated, ground- based, wind shear remote-sensing or detec-
tion equipment in accordance with local arrangements to
thoseconcerned.
(8) Where microbursts are observed, reported by pilots
or detected by ground-based, wind shear detection or remote-
sensing equipment, the wind shear warning and wind shear alert
should include a specific reference to microburst.

CIVIL AVIATION
SRO 35
(9) Where information from ground-based, wind shear
detection or remote-sensing equipment is used to prepare a wind
shear alert, the alert shall, if practicable, relate to specific sections
of the runway and distances along the approach  path or  take-off
path  as agreed between the meteorological authority, the appro-
priate ATS authority and the operators concerned.
(10) Information on wind shear is also to be included as
supplementary information in local routine reports, local special
reports, METAR and SPECI in accordance with the templates in
Appendix 3, Tables A3-1 and A3-2.
Table A6-1A. Template for SIGMET and AIRMET
messages
Key: M = inclusion mandatory, part of every message;
C
= inclusion conditional, included whenever applicable;
=
= a double line indicates that the text following it
should be placed on the subsequent  line.
Note 1.— The ranges and resolutions for the numerical
elements included in SIGMET messages are shown in
Table A6-4 of this Schedule.
Note 2.— Severe or moderate icing and severe or moder-
ate turbulence (SEV ICE, MOD ICE, SEV TURB, MOD
TURB) associated with thunderstorms, cumulonimbus
clouds or tropical cyclones should not be included.

CIVIL AVIATION
SRO 35
Element
Detailed content
SIGMET
AIRMET*
SIGMET
AIRMET*
template
template
message             message example
examples
Location
ICAO location
 indicator of
 indicator of the
FIR/CTA (M)1 ATS unit serving
nnnn
YUCC2 YUDD2
the FIR or CTA to
 which theSIGMET
/AIRMETrefers
Identification
 Message identifi-
SIGMET AIRMET
SIGMET 1
AIRMET* 9
 (M)
cationandsequence [n][n]n
 [n][n]n
SIGMET 01
AIRMET * 19
number3
 SIGMET A01
AIRMET B19
Validity period Day-time groups
VALID
VALID 010000/010400 VALID
 (M)
indicating the
nnnnnn
221215/221600  VALID 101520/101800
period of validity in /nnnnnn
VALID  251600/252200  VALID
UTC
152000/160000 VALID 192300/
200300
Location
Location  indicator
indicator  of
of  MWO
MWO (M)
originating the
nnnn–
YUDO–2 YUSO–2
 message  with a
 separating  hyphen
Name of the
 Location  indicator nnnn
YUCC
FIR/ CTA (M) and name of  the
 nnnnnnn
AMSWELL
FIR/CTA4  for
nnn  or
 FIR2 YUDD
which the SIGMET/UIRor FIR/
SHANLON2
YUCC
AIRMET is issued UIR or
UIR
AMSWELL
nnnn
nnnn
FIR/UIR
FIR/22 YUDD
nnnnnn n nnnnn
YUDD
SHANLON FIR2
nnnn
nnnn FIR[/n] SHANLON
CTA
CTA2
IF THE SIGMET OR AIRMET MESSAGE IS TO BE CANCELLED, SEE DETAILS AT THE
END OF THE TEMPLATE.
Status
Indicator of  test
TEST or
TEST or
TEST EXER
TEST EXE
 in dicator (C)5 or  exercise
EXER
EXER

CIVIL AVIATION
SRO 35
phenomenon
Description  of OBSC7 TS
SFC WIND
OBSC  TS
SFC WIND
(M)6
phenomenon
[GR8]
nnn/nn[n]
OBSC  TSGR
040/40MPS
causing  the
EMBD9
MPS (or SFC EMBD TS
SFC WIND
 issuance of
TS[GR8]
WIND  nnn/ EMBD  TSGR
310/20KT
SIGMET/
FRQ10
  nn[n] KT)
FRQ TS
SFC VIS 1500M
AIRMET
TS[GR8]
SFC VIS [n]
FRQ  TSGR
(BR)ISOL TS
SQL11
 [n]nnM(nn) SQL  TS
ISOL TSGR
TS[GR8] TC
16  ISOL 17
SQL  TSGR
OCNL TS
 nnnnnnnnnn
  TS [GR8]
TC GLORIA
OCNL TSGR
PSN  Nnn[nn] OCNL 18  TSPSN   N10
 MT OBSC
or Snn[nn]
 [GR8] MT
W060  CB
BKN CLD
Wnnn[nn] or
OBSC  BKN TC  NN  PSN
120/900M
Ennn[nn]CB
  CLD  nnn/
S2030
BKN CLD
or TC  NN12 [ABV][n]nnn E06030  CB
400/3000FT
 PSN Nnn[nn]  M (or BKN
SEV  TURB
 BKN CLD
or Snn[nn]
CLD [n]nnn/ SEV ICE
1000/5000FT
 Wnnn[nn]or
[ABV][n]
SEV ICE (FZRA) BKN CLD
Ennn[nn] CB
 nnnnFT)or
SEV MTW
SFC/3000M
SEV  TURB13  BKN CLD
HVY DS
BKN CLD SFC/
SEV   ICE 14
SFC/[ABV[n] HVY SS
ABV10000FT
SEV ICE
nnnM (or
VA
OVC CLD 270/
 (FZRA)14
BKN  CLD
ERUPTION
ABV3000M
SEV  MTW15  SFC/[ABV]
MT ASH VAL
OVC CLD 900/
HVY  DS
 [n]nnnnFT) 2 PSN S15
ABV10000FT
HVY  SS [VA OVC  CLD
E073 VA CLD
OVC
ERUPTION]
nnn/[ABV]
RDOACT CLD
CLD1000/5000FT
[MT  nnnnnnn [n]nnnM (or
OVC CLD
nnn] [PSN
OVC CLD[n]
SFC/3000M
Nnn[nn] or
nnn/[ABV]
OVC CLD SFC/
Snn[nn]Ennn
[n] nnnnFT)
ABV10000FT
[nn] or Wnnn or OVC CLD
ISOL CB
[nn]] VA CLD SFC/[ABV]
OCNL CB
RDO ACT
[n]nnnM (or
FRQ CB
CLD
OVC  CLD
ISOL TCU
SFC/[ABV]
OCNL TCU
[n]nnnnFT)
FRQ TCU
 ISOL17
MOD TURB
CB19 OCNL
MOD ICE
18  CB19
MOD MTW
FRQ10 CB19
ISOL17
TCU19
OCNL18
TCU19
FRQ10
TCU19

CIVIL AVIATION
SRO 35
 MOD TURB
13 MOD  ICE
14  MOD
MTW 15
Observed or
Indication
OBS [AT nnnnZ] or
OBS
forecast
whether  the
FCST [AT nnnnZ]
OBS AT 1210Z
 phenomenon
information
FCST
 (M)
is observed  and
FCST AT 1815Z
 expected to
continue, or
 forecast
Location (C)Location
Nnn[nn] Wnnn[nn] or
N2020 W07005
(referring to
Nnn[nn] Ennn[nn] or
N48 E010
latitude and
Snn[nn] Wnnn[nn] or
S60 W160
longitude  (in
Snn[nn] Ennn[nn]orN   OF
S0530 E16530
degrees and
Nnn[nn] or S OF   Nnn
N OF N50
minutes))
[nn] or N OF Snn[nn]
 S OF N5430
or S OF Snn [nn] [AND]
N OF S10
W  OF  Wnnn[nn] or E OF
S OF S4530
Wnnn[nn] or W  OF
W OF W155
Ennn[nn] or E   OF Ennn
E OF W45
[nn]orN   OF  Nnn[nn]
W OF E15540
or N OF  Snn[nn] AND
 E OF E09015
S OF Nnn[nn] orS  OF
 N OF N1515 AND W OF E13530
Snn[nn]orW   OF Wnnn
S OF N45 AND N OF N40
[nn] or W OF Ennn
N OF LINE S2520 W11510 – S2520
[nn] AND E OF Wnnn
W12010
[nn] or E OF Ennn[nn]
SW OF LINE N50 W005 – N60 W020
orN OF LINE21 or NE
SW OF LINE N50 W020 – N45 E010
OF LINE21 or E  OF
AND NE OF LINE N45 W020 – N40
 LINE21 or SE  OF
E010
 LINE21 or S OF   LINE
WI N6030E02550 – N6055 E02500 –
21 or SW  OF  LINE21
N6050 E02630 – N6030 E02550
or W OF  LINE21 or
APRX 50KM WID LINE BTN N64
NW  OF LINE21 Nnn[nn]
W017 – N60 W010 – N57 E010
or Snn[nn] Wnnn[nn]
ENTIRE   FIR
or Ennn[nn] – Nnn[nn] ENTIRE  UIR
or Snn[nn] Wnnn[nn]
ENTIRE FIR/UIR
or Ennn[nn][– Nnn[nn] ENTIRE  CTA

CIVIL AVIATION
SRO 35
or Snn[nn] Wnnn[nn] or WI 400KM OF TC CENTRE
Ennn[nn]] [– Nnn[nn] or Snn WI 250NM OF TC CENTRE
[nn] Wnnn[nn] or Ennn[nn]] WI 30KM OF N6030 E02550†
[AND N OF LINE21 or NE
OF LINE21 or E OF LINE
21 or SE OF LINE21 or S
 OF LINE21 or SW OF LINE
21 or W OF LINE21 or NW
OF  LINE21 Nnn[nn] orSnn
[nn] Wnnn[nn] or Ennn[nn]
– Nnn[nn]or Snn[nn] Wnnn
[nn] or Ennn[nn] [– Nnn[nn]
orSnn[nn] Wnnn[nn]orEnnn
[nn]] [– Nnn[nn] or Snn[nn]
Wnnn[nn]orEnnn[nn]]]
orWI21, 22 Nnn[nn] or Snn
[nn] Wnnn[nn] orEnnn[nn] –
Nnn[nn] or Snn[nn] Wnnn
[nn] or Ennn[nn] –
Nnn[nn] or Snn[nn] Wnnn
[nn] or Ennn[nn] –
[Nnn[nn] or Snn[nn] Wnnn
[nn] or Ennn[nn] –
Nnn[nn] or Snn[nn] Wnnn
[nn] or Ennn[nn]]orAPRX
 nnKM WID LINE21 BTN
(or nnNMWID LINE21 BTN)
Nnn[nn] or Snn[nn] Wnnn
[nn] or Ennn[nn]
– Nnn[nn] or Snn[nn] Wnnn
[nn] orEnnn[nn]
[– Nnn[nn] or Snn[nn] Wnnn
[nn]orEnnn[nn]]
[– Nnn[nn] or Snn[nn] Wnnn
[nn] orEnnn[nn]] or
ENTIRE UIRorENTIRE FIR
orENTIRE FIR/UIRor
ENTIRE CTAor23 WI nnn
KM (or nnnNM) OF TC
 CENTREor24WI nnKM
 (or nnNM) OF  Nnn[nn] or
Snn[nn] Wnnn[nn] or Ennn[nn]

CIVIL AVIATION
SRO 35
Element
Detailed content SIGMET
AIRMET
SIGMET
AIRMET
template
 template
message
message
examples
examples
Level (C)20, 24Flight level or
[SFC/]FLnnn or
FL180
altitude
[SFC/]nnnnM (or [SFC/][n]
SFC/FL070
nnnnFT) or
SFC/3000M
FLnnn/nnn or
SFC/10000FT
TOP FLnnn or
FL050/080
[TOP] ABV FLnnn (or [TOP] TOP FL390
ABV [n]nnnnFT)
ABV FL250
[nnnn/]nnnnM (or [[n]nnnn/] TOP ABV FL100
[n]nnnnFT)
ABV 7000FT
or [nnnnM/]FLnnn (or [
TOP ABV 9000FT
[n]nnnnFT/] FLnnn)
TOP ABV 10000FT
or 23
3000M
TOP [ABV or BLW]
2000/3000M
FLnnn
8000FT
6000/12000FT
2000M/FL150
10000FT/FL250
TOP FL500
TOP ABV FL500
TOP BLW FL450
Movement or Movement or
MOV N [nnKMH] or MOV MOV SE
expected
expected
NNE[nnKMH] or
MOV NNW
movement
movement
MOV NE [nnKMH] or
MOV E 40KMH
(C)20, 25
(direction and
MOV ENE[nnKMH] or
MOV E 20KT
speed) with
MOV E [nnKMH] or MOV MOV WSW 20KT
reference to one  ESE[nnKMH] or
STNR
of the sixteen
MOV SE [nnKMH] or MOV
points of
SSE[nnKMH] or
compass, or
MOV S [nnKMH] or MOV
stationary
SSW[nnKMH] or
MOV SW [nnKMH] or
MOV WSW[nnKMH] or
MOV W [nnKMH] or MOV
WNW[nnKMH] or
MOV NW [nnKMH] or
MOV NNW [nnKMH]
(or MOV N [nnKT] or MOV
NNE[nnKT] or
MOV NE [nnKT] or MOV
ENE [nnKT]or

CIVIL AVIATION
SRO 35
MOV E [nnKT] or MOV
ESE [nnKT] or
MOV SE [nnKT] or MOV
SSE [nnKT]or
MOV S [nnKT] or MOV
SSW [nnKT] or
MOV SW [nnKT] or MOV
WSW[nnKT] or
MOV W [nnKT] or MOV
WNW [nnKT]or
MOV NW [nnKT] or MOV
NNW [nnKT]) or
STNR
Changes  in
Expected
INTSF or
INTSF
intensity (C)
changes  in
 WKN or
WKN
intensity
 NC
NC
Forecast
Indication  of
time
the f ore cast
(C)25
time of
FCST AT
—
FCST AT 2200Z —
phenomenon
nnnnZ
TC forecast
Forecast
 TC  CENTRE —
TC  CENTRE
—
position (C)
position of  TC PSN  Nnn[nn]
PSN   N1030  TC
centre  at the
or Snn[nn]
CENTRE  PSN
end of the
Wnnn[nn]or
E1600015
 validity
Ennn[nn]
period  of  the
SIGMET
message
Forecast
Forecast
 Nnn[nn] Wnnn —
N30 W170
—
position
 position of
 [nn]orNnn
N OF N30
(C)20, 25, 26
 phenomenon
[nn] Ennn[nn]
S OF S50 AND W
at the end of  the  or Snn[nn]
OF
validity period
Wnnn[nn] or
E170
of the SIGMET Snn[nn] Ennn
S OF N46 AND
 message
[nn]orN OF
N OF N39
 Nnn[nn] or S
NE OF LINE N35
OF Nnn[nn] or
W020 —

CIVIL AVIATION
SRO 35
N OF Snn[nn]
N45 W040
orS OF Snn[nn] SW OF LINE
[AND]W OF
N 48 W020
Wnnn[nn] or E  – N43 E010
OF Wnnn[nn]
AND NE OF
or W OF Ennn
LINE N43
[nn] or E OF
W020  – N38
Ennn[nn]orN
E010
OF Nnn[nn] or WI N20
N OF Snn[nn]
W090 – N05
AND S OF Nnn W090 – N10
[nn] or S OF
W100 – N20
Snn[nn]orW OF W090
Wnnn[nn] or W APRX50KM
OF Ennn[nn]
WID LINE
AND E OF
 BTN N64
Wnnn[nn] or E W017 – N57
 OF Ennn[nn]or W005 – N55
N OF LINE21
 E010 – N55
or NE OF LINE  E030
21 or E OF
ENTIRE FIR
LINE21 or SE
ENTIRE UIR
OF LINE21orS  ENTIRE FIR
OF LINE21 or
 /UIR
SW OF LINE21ENTIRE CTA
or W OF LINE NO VA EXP
21 or NW OF
WI 30KM
LINE21Nnn[nn] OF N6030
or Snn[nn]
E02550†
Wnnn[nn] or
Ennn[nn] –Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn][– Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn]][AND
N OF LINE21or
NE OF LINE21
or E OF LINE21
or SE OF LINE
21 or S OF
LINE21 or SW
OF LINE21 or
W OF LINE21

CIVIL AVIATION
SRO 35
 or NW OF LINE
21Nnn[nn] or
Snn[nn] Wnnn
[nn] or Ennn[nn]
 –Nnn[nn] or
Snn[nn] Wnnn
 [nn] or Ennn
[nn][– Nnn[nn]
or Snn[nn]
Wnnn[nn] or
Ennn[nn]]]
orWI21, 22 Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn]–Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn]–Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn] – Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn]or
APRX nnKM
WID LINE21
 BTN (nnNM
WID LINE21
BTN)Nnn[nn]
 or Snn[nn]
Wnnn[nn] or
Ennn[nn] –Nnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn][–
 Nnn[nn] or Snn
[nn] Wnnn[nn]
or Ennn[nn]][
 – Nnn[nn] or
Snn[nn] Wnnn
[nn] or Ennn[nn]
]orENTIRE FIR
orENTIRE UIR
orENTIRE FIR
/UIRorENTIRE

CIVIL AVIATION
SRO 35
CTAor27NO
VA EXPor24
WI nnKM (or
nnNM) OFNnn
[nn] or Snn[nn]
Wnnn[nn] or
Ennn[nn]
Repetition
Repetition
[AND]28
—
 AND
—
of elements
of elements
(C)28
included in
 a SIGMET
message for
volcanic ash
 cloud or
tropical
 cyclone
OR
Cancellation
Cancellation
CNL SIGMET CNL
CNL SIGMET
CNL
 of  SIGMET/  of   SIGMET/
[n][n]n
AIRMET
2101200/
AIRMET 05
AIRMET
AIRMET
nnnnnn
[n][n]n
101600
151520/151800
(C)29
referring  to
/nnnnnn
nnnnnn/
CNL SIGMET
 itsidentification Or 27 CNL.
nnnnnn
A13 251030
 SIGMET[n][n]/
251430 VA
  n nnnnnn/ /
MOV TO YUDO
 nnnnnnVA
FIR2
 MOV TO nnnn
FIR
Notes.—
1.
Fictitiouslocation.
2.
Used only when the message issued to indicate that a test or an exercise
is taking place. When the word “TEST” or the abbreviation “EXER” isin
cluded, the message may contain information that should not be used
operationally or will otherwise end immediately after the word “TEST”.
[Applicable 7 November 2020]

CIVIL AVIATION
SRO 35
3.
The use of cumulonimbus (CB) and towering cumulus (TCU) is restricted
to AIRMETs.
4.
In the case of volcanic ash cloud or cumulonimbus clouds associated with a
tropical cyclone covering more than one area within the FIR, these ele
ments can be repeated, as necessary.
5.
A straight line is to be used between two points drawn on a map in the
Mercator projection or between two points which crosses lines of longitude
at a constant angle.
6.
The number of coordinates should be kept to a minimum and should not
normally exceed seven.
7.
Only for SIGMET messages for tropical cyclones.
8.
Only for SIGMET messages for radioactive cloud. When detailed informat
ion on the release is not available, a radius of up to 30 kilometres (or 16
nautical miles) from the source may be applied; and a vertical extent from
surface (SFC) to the upper limit of the flight information region/upper flight
information region (FIR/UIR) or control area (CTA) is to be applied.
[Applicable 7 November 2020]
9.
The elements “forecast time” and “forecast position” are  not  to be used in
conjunction with the element “movement or expected movement”.
10.
The levels of the phenomena remain fixed throughout the forecast period.
11.
Only for SIGMET messages for volcanic ash.
12.
To be used for two volcanic ash clouds or two centres of tropical cyclones
 simultaneously affecting the FIR concerned..
13.
End of the essage (as the SIGMET/AIRMET message is being cancelled
AIRMET*- Not applicable in accordance with AFI Regional Air Navigation
Agreement

CIVIL AVIATION
SRO 35
Table A6-1B. Template for special air-reports (uplink)
Key: M
=
inclusion mandatory, part of every message;
C
=
inclusionconditional,includedwheneverapplicable;
=
=
a double line indicates that the text following it should be
placedon the subsequent line.
Note. — The ranges and resolutions for the numerical elements included in
special air-reports are shown in Table A6-4 of this appendix.
Element
Detailed content
Template1,2
Examples
Identification (M)
Message identification
ARS
ARS
Aircraft identification
Aircraft radiotelephony
nnnnnn
VA8123
(M)
 call sign
Observed phenomenon
Description of   observed TS TSGR
TS TSGR
(M)
phenomenon  causing the SEV  TURB SEV ICE SEV TURB SEV ICE
 issuance of the special air SEV MTW HVY SS
SEV MTW HVY SS
- report4
VA CLD
VA CLD VA
VA [MT nnnnnn
VA MT ASHVAL5
nnnn] MOD
MOD TURB MOD
TURB MOD ICE
ICE
Observation time (M)
Time  of  observation  of
OBS AT nnnnZ
OBS AT 1210Z
observed phenomenon
Location (C)
Location (referring to
NnnnnWnnnnn
or
N2020W07005
latitude and longitude (in
NnnnnEnnnnn
or
S4812E01036
degrees and minutes)) of
SnnnnWnnnnn
or
observed phenomenon
SnnnnEnnnnn
Level (C)
Flight level or altitude of
FLnnn or
FL390 FL180/
observed  phenomenon
FLnnn/nnn  or
210 3000M
nnnnM (or
12000FT
[n]nnnnFT)

CIVIL AVIATION
SRO 35
Notes.
1.
No wind and temperature to be uplinked to other aircraft in flight.
2.
Fictitious call sign.
3.
In the case of special air-report for volcanic ash cloud, the vertical extent (if observed) and
name of the volcano (if known) can be used.
4.
Fictitious location.
Table A6-2. Template for aerodrome warnings
Key:
M =
inclusion mandatory, part of every message;
C
=
inclusion conditional, included wheneverapplicable.
Note1.— The ranges and resolutions for the numerical elements included in aerodrome warnings
are shown in Table A6-4 of this schedule.
Note2.— TheexplanationsfortheabbreviationscanbefoundintheProcedures for Air Navigation
Services — ICAO Abbreviations and Codes (PANS-ABC, Doc 8400).
Element
Detailed content
Templates
Examples
Location
Location  indicator  of
 indicator of the the aerodrome
nnnn
YUCC1
 aerodrome (M)
Identification of
Type of  message
 the type of
message (M)
and  sequence number
AD WRNG [n]n
AD WRNG 2
Validity period
Day and time of  validity
VALID nnnnnn/nnnnnn
VALID
 (M)
period in UTC
211230/211530
IF THE AERODROME WARNING IS TO BE CANCELLED, SEE DETAILS AT THE END OF
THE TEMPLATE.
  Phenomenon
Description  of
TC3 nnnnnnnnnn or
TC ANDREW
(M)2
phenomenon causing  the
 HVY] TS or GR or
 HVY SN
issuance  of  the aerodrome
 [[HVY] SN [nnCM]3 or
25CM
warning
[HVY] FZRAor
SFC WSPD
[HVY] FZDZ or RIME4 or 20MPS MAX
[HVY] SS or [HVY] DS or
30  VA
SA or DU or
TSUNAMI
SFC  WSPD nn[n]MPS
MAX nn[n]

CIVIL AVIATION
SRO 35
(SFC WSPD nn[n]KT
MAX nn[n]) or
SFC WIND nnn/nn[n]MPS
MAX nn[n]
(SFC WIND nnn/nn[n]
KT MAX nn[n]) or
SQ or FROST or
TSUNAMI orVA[DEPO]
or TOX  CHEM or
Free text up to 32
 characters5
Observed or
Indication whether the
OBS [AT nnnnZ] or
 forecast
  information  is observed and FCST
phenomenon (M)
 expected to continue, or
forecast
OBS AT 1200Z
OBS
Changes in intensity(C)
Expected changes inintensity INTSF
orWKN orNC WKN
OR
Cancellation of Cancellation of
CNL AD WRNG [n]n CNL AD
aerodrome
aerodrome warning
nnnnnn/ nnnnnn
WRNG 2
warning6
referring to its
211230/2115306
identification
Notes.—
1.
Fictitious location.
2.
One phenomenon or a combination thereof phenomena.
3.
Hoar frost or rime.
4.
End of the message (as the aerodrome warning is being cancelled).
Table A6-3. Template for wind shear warnings
Key: M = inclusion mandatory, part of every message;
C =
inclusionconditional,included wheneverapplicable.
Note 1. —
The ranges and resolutions for the numerical elements included in wind shear
warnings are shown in Table A6-4 of this Schedule.
Note 2. —
The explanations for the abbreviations can be found in the PANS-ABC (Doc 8400).

CIVIL AVIATION
SRO 35
Element
Detailed  content
Template(s)
Example
Location
Location  indicator  of  the
nnnn
YUCC1
indicator of  the
 aerodrome
aerodrome (M)
Identification  of
Type of  message  and
WS WRNG [n]n
WS WRNG 1
the type of
sequence  number
 message (M)
Time  of  origin and Day and time of  issue and,
nnnnnn [VALID  TL
211230 VALID TL
validity period (M) where applicable, validity
 nnnnnn] or[VALID
211330221200
 period in UTC
nnnnnn/nnnnnn]
   VALID
 221215/221315
IF THE WIND SHEAR WARNING IS TO BE CANCELLED, SEE DETAILS AT THE END OF
THE TEMPLATE.
Phenomenon (M)
Identification  of  the
[MOD] or [SEV] WS IN
WS APCH RWY12
phenomenon and its location APCHor[MOD] or [SEV]
MOD WS RWY34
WS [APCH] RWYnnnor
[MOD] or [SEV] WS IN
WS IN CLIMB-
CLIMB-OUTor[MOD] or OUT MBST
[SEV] WS CLIMB-
APCH RWY26
OUT RWYnnn orMBST
MBST IN
IN APCH orMBST
CLIMB-OUT
 [APCH] RWYnnnor
MBST IN CLIMB-OUT or
MBST CLIMB-OUT RWY
nnn
Observed, reported Identification  whether  the
REP AT nnnn nnnnnnnn or REP AT 1510
or forecast
phenomenon is observed or
OBS [AT nnnn] orFCST
B747 OBSAT 1205
phenomenon (M)
reported and expected to
FCST
continue, or forecast
Details  of  the
Description of  phenomenon SFC WIND: nnn/nnMPS
SFC WIND: 320/
 phenomenon (C)2 causing the is suance of  the
(ornnn/nnKT) nnnM (nnn
5MPS60M-WIND:
 wind shear warning
FT)- WIND: nnn/nnMPS
360/13MPS (SFC
(or nnn/ nnKT)ornnKMH
WIND: 320/10KT
(or nnKT) LOSS nnKM (or 200FT-WIND:
nnNM)FNA RWYnnornn
360/26KT)60KMH
KMH (or nnKT) GAIN nn LOSS 4KM FNA
KM (or nnNM) FNA
RWY13 (30KT
RWYnn
 LOSS 2NM FNA
RWY13)

CIVIL AVIATION
SRO 35
OR
Cancellation  of
Cancellation  of   wind
CNL WS WRNG [n]
CNL WS WRNG 1
wind  shear
shear  warning referring  to
n nnnnnn/nnnnnn
211230/2113303
 warning3
 its  identification
Notes.—
1.
Fictitious location.
2.
Additional provisions.
3.
End of the message (as the wind shear warning is being cancelled).
Table A6-4. Ranges and resolutions for the numerical elements included in volcanic ash
and tropical cyclone advisory messages, SIGMET/AIRMET messages and aerodrome and
wind shear warnings
Element as specified in Appendices 2 and 6
Range
Resolution
Summit elevation:
M
000 – 8 100
FT
000 – 27 000
Advisory number:
for VA (index)*
000 – 2 000
for TC (index)*
00 – 99
Maximum  surface wind:
MPS
00 – 99
KT
00 – 199
Central  pressure:
hPa
850 – 1 050
Surface wind speed:
MPS
15 – 49
KT
30 – 99
Surface  visibility:
M
0000 – 0750
M
0800 – 5 000
Cloud: height of   base:
M
000 – 300
FT
000 – 1 000
Cloud: height  of   top:
M
000 – 2 970
M
3 000 – 20 000
FT
000 – 9 900
FT
10 000 – 60 000
1 000
Latitudes:
° (degrees)
00 – 90
´ (minutes)
00 – 60

CIVIL AVIATION
SRO 35
Longitudes:
° (degrees)
000 – 180
´ (minutes)
00 – 60
Flight levels:
000 – 650
Movement:
KMH
0 – 300
KT
0 – 150
* Non-dimensional
Example A6-1. SIGMET and AIRMET message and the corresponding
cancellations
SIGMET
Cancellation of SIGMET
YUDD SIGMET 2 VALID 101200/
YUDD SIGMET 3 VALID 101345
101600 YUSO – YUDD SHANLON
/101600 YUSO – YUDD
 FIR/UIR OBSC TS FCST
SHANLON FIR/UIR CNL
SIGMET 2 101200 /101600
S OF N54 AND E OF W012 TOP FL390
MOV E 20KT WKN
Cancellation of SIGMET
Cancellation of AIRMET
YUDD SIGMET 3 VALID
YUDD AIRMET 2 VALID
101345/101600 YUSO – YUDD
151650/151800 YUSO – YUDD
SHANLON FIR/UIR CNL SIGMET
 SHANLON FIR CNL AIRMET 1
 2 101200/101600
 151520/151800
Example A6-2. SIGMET message for tropical cyclone
YUCC SIGMET 3 VALID 251600/252200 YUDO –
YUCC AMSWELL FIR TC GLORIA PSN N2706 W07306 CB OBS AT 1600Z
WI 250NM OF TC CENTRE TOP FL500 NC FCST AT 2200Z TC CENTRE
PSN N2740 W07345

CIVIL AVIATION
SRO 35
Meaning:
The third SIGMET message issued for the AMSWELL* flight
information region (identified by YUCC Amswell area control
centre) by the Donlon/International* meteorologicalwatchoffice
(YUDO) since 0001 UTC; the message is valid from 1600 UTC
to 2200 UTC on the 25th of the month; tropical cyclone Gloria at
27 degrees 6 minutes north and 73 degrees 6 minutes west;
cumulonimbus was observed at 1600 UTC within 250 nautical
miles of the centre of the tropical cyclone with top at flight level
500;nochangesinintensityareexpected;at2200 UTC the centre
of the tropical cyclone is forecast to be located at 27 degrees 40
minutes north and 73 degrees 45 minutes west.
*Fictitious location
Example A6-3. SIGMET message for volcanic ash
YUDD SIGMET 2 VALID 211100/211700 YUSO –
YUDD SHANLON FIR/UIR VA ERUPTION MT ASHVAL
PSN S1500 E07348 VA CLD OBS AT 1100Z APRX 50KM
WID LINE BTN S1500 E07348 – S1530 E07642 FL310/450
INTSF FCST AT 1700Z APRX 50KM WID LINE BTN S1506
E07500 – S1518 E08112 – S1712 E08330
Meaning:
The second SIGMET message issued for the SHANLON* flight
information region (identified by YUDD Shanlon area control
centre/upper flight information region) by the Shanlon/ Interna-
tional* meteorological watch office (YUSO) since 0001 UTC;
the message is valid from 1100 UTC to 1700 UTC on the 21st of
the month; volcanic ash eruption of Mount Ashval* located at 15
degrees south and 73 degrees 48 minutes east; volcanic ash cloud
observed at 1100 UTC in an approximatly 50 km wide line
between 15 degrees south and 73 degrees 48 minutes east, and
15 degrees 30 minutes south and 76 degrees 42 minutes east;

CIVIL AVIATION
SRO 35
between flight levels 310 and 450, intensifying at 1700 UTC the
volcanic ash cloud is forecast to be located in an approximate 50
km wide line between 15 degrees 6 minutes south and 75 degrees
east, 15 degrees 18 minutes south and 81 degrees 12 minutes
east, and 17 degrees 12 minutes south and 83 degrees 30 minutes
east.
*Fictitious location
Example A6-4. SIGMET message for radioactive cloud
YUCC SIGMET 2 VALID 201200/201600 YUDO –
YUCC AMSWELL FIR RDOACT CLD OBS AT 1155Z WI
S5000 W14000 – S5000 W13800 – S5200 W13800 – S5200
W14000 – S5000 W14000 SFC/FL100 WKN FCST AT 1600Z
WI S5200 W14000 – S5200 W13800 – S5300 W13800 – S5300
W14000 – S5200 W14000
Meaning:
The second SIGMET message issued for the AMSWELL* flight
information region (identified by YUCC Amswell area control
centre) by the Donlon/International* meteorological watch office
(YUDO) since 0001 UTC; the message is valid from 1200 UTC
to 1600 UTC on the 20th of the month; radioactive cloud was
observed at 1155 UTC within an area bounded by 50 degrees 0
minutessouth140degrees0minuteswestto50degrees0minutes
south138
degrees0minuteswestto52degrees0minutessouth138degrees
0 minutes west to
52 degrees 0 minutes south 140 degrees 0 minutes west to 50
degrees 0 minutes south 140 degrees 0 minutes west and between
the surface and flight level 100; the radioactive cloud is expected
to weaken in intensity; at 1600 UTC the radioactive cloud is
forecast to be located within an area bounded by 52 degrees 0
minutes south 140 degrees0 minuteswestto52 degrees0 minutes
south 138 degrees 0 minutes west to 53 degrees 0 minutes south

CIVIL AVIATION
SRO 35
138 degrees 0 minutes west to 53 degrees 0 minutes south 140
degrees0minuteswestto52 degrees0minutessouth140degrees
0 minutes west.
*Fictitious location
Example A6-5. SIGMET message for severe turbulence
YUCC SIGMET 5 VALID 221215/221600 YUDO –
YUCC AMSWELL FIR SEV TURB OBS AT 1210Z N2020
W07005FL250INTSFFCST AT 1600Z S OF N2020 AND E OF
W06950
Meaning:
The fifth SIGMET message issued for the AMSWELL* flight
information region (identified by YUCC Amswell area control
centre) by the Donlon/International* meteorological watch office
(YUDO) since 0001 UTC; the message is valid from 1215 UTC
to 1600 UTC on the 22nd of the month; severe turbulence was
observed at 1210 UTC 20 degrees 20 minutes north and 70
degrees 5 minutes west at flight level 250; the turbulence is
expected to strengthen in intensity; at 1600 UTC the severe
turbulence is forecast to be located south of 20 degrees 20 minutes
north and east of 69 degrees 50 minutes west.
*Fictitious location
Example A6-6. AIRMET message for moderate moun-
tain wave
YUCC AIRMET 2 VALID 221215/221600 YUDO –
YUCC AMSWELL FIRMOD MTW OBS AT 1205ZN48 E010
FL080 STNR NC

CIVIL AVIATION
SRO 35
Meaning:
The second AIRMET message issued for the AMSWELL* flight
information region (identified by YUCC Amswell area control
centre) by the Donlon/International* meteorological watch office
(YUDO) since 0001 UTC; the message is valid from 1215 UTC
to 1600 UTC on the 22nd ofthemonth; moderatemountainwave
was observed at 1205 UTC at 48 degrees north and 10 degrees
east at flight level 080; the mountain wave is expected to remain
stationary and not to undergo any changes inintensity.
*Fictitious location
