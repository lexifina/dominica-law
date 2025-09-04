SCHEDULE 12
PERFORMANCE OF THE ACAS II COLLISION
AVOIDANCE LOGIC
1.
CONDITIONS UNDER WHICH THE REQUIRE-
MENTS APPLY

CIVIL AVIATION
S.R.O. 31
(1) The followingassumed conditions shall applyto the
performance requirements specified in paragraph 2. and para-
graph 3. of this schedule.
(a) range and bearing measurements and an altitude
report are available for the intruder each cycle as long
as it is within 14 NM, but not when the range exceeds
14 NM;
(b) the errors in the range and bearing measurements
conform to standard range and bearing error models;
(c) the intruder’s altitude reports, which are its Mode C
replies, are expressed in 100 ft quanta;
(d) an altitude measurement that has not been quantised
and is expressed with a precision of 1 ft or better is
available for own aircraft;
(e) errors in the altitude measurements for both aircraft
are constant throughout any particular encounter;
(f) the errors in the altitude measurements for both
aircraft conform to a standard altimetry error model;
(g) the pilot responses to RAs conform to a standard pilot
model;
(h) the aircraft operate in an airspace in which close
encounters, including those in which ACAS gener-
ates an RA, conform to a standard encounter model;
(i) ACAS-equipped aircraft are not limited in their ability
to perform the manoeuvres required by their RAs;
and

CIVIL AVIATION
S.R.O. 31
(j) as specified in Sub-paragraph 1.(8).
(i) the intruder involved in each encounter is not
equipped;or
(ii) the intruder is ACAS-equipped but follows a
trajectory identical to that in the unequipped
encounter; or
(iii) the intruder is equipped with an ACAS having a
collision avoidance logic identical to that of own
ACAS.
Note.— The phrase “altitude measurement” refers to a measure-
ment by an altimeter prior to any quantization.
(2)
The performance of the collision avoidance logic shall not
degrade abruptly as the statistical distribution of the altitude errors
or the statistical distributions of the various parameters that
characterize the standard encounter model or the response of
pilots to the advisories are varied, when surveillance reports are
not available on every cycle or when the quantisation of the
altitude measurements for the intruder is varied or the altitude
measurements for own aircraft are quantised.
(3)
STANDARD RANGE ERROR MODEL
The errors in the simulated range measurements shall be taken
from a Normaldistributionwithmean0ftandstandarddeviation
50 ft.
(4)
STANDARD BEARING ERROR MODEL
The errors in the simulated bearing measurements shall be taken
from a Normal distribution with mean 0.0 degrees and standard
deviation 10.0 degrees.
(5)
STANDARD ALTIMETRY ERROR MODEL

CIVIL AVIATION
S.R.O. 31
(a) The errors in the simulated altitude measurements
shall be assumed to be distributed as a Laplacian
distribution with zero mean havingprobability density
(b) The parameter ë required for the definition of the
statistical distribution of altimeter error for each
aircraft shall have one of two values, ë1 and ë2, which
depend on the altitude layer of the encounter as
follows:
(c) For an aircraft equipped with ACAS the value of λ
shall be λ1.
(d) For aircraft not equipped with ACAS, the value of ë
shall be selected randomly usingthe followingprob-
abilities:
(6)
STANDARD PILOT MODEL
The standard pilot model used in the assessment of the perform-
ance of the collision avoidance logic shall be that:
(a) any RA is complied with by accelerating to the

CIVIL AVIATION
S.R.O. 31
required rate (if necessary) after an appropriate
delay;
(b) when the aircraft’s current rate is the same as its
original rate and the original rate complies with the
RA, the aircraft continues at its original rate, which is
not necessarily constant due to the possibility of
acceleration in the original trajectory;
(c) when the aircraft is complying with the RA, its current
rate is the same as the original rate and the original
rate changes and consequently becomes inconsistent
with the RA, the aircraft continues to comply with the
RA;
(d) when an initial RA requires a change in altitude rate,
the aircraft responds with an acceleration of 0.25 g
after a delay of 5 s from the display of the RA;
(e) whenanRAismodifiedandtheoriginalratecomplies
with the modified RA, the aircraft returns to its
original rate (if necessary) with the acceleration
specified in g) after the delay specified in h);
(f) when an RA is modified and the original rate does not
comply with the modified RA, the aircraft responds to
comply with the RA withtheaccelerationspecifiedin
g) after the delay specified in h);
(g) the acceleration used when an RAis modified is 0.25
g unless the modified RA is a reversed sense RA or
an increased rate RA in which case the acceleration
is 0.35 g;
(h) the delay used when an RAis modified is 2.5 s unless
this results in the acceleration starting earlier than 5
s from the initial RA in which case the acceleration

CIVIL AVIATION
S.R.O. 31
starts 5 s from the initial RA; and
(i) when an RA is cancelled, the aircraft returns to its
original rate (if necessary) with an acceleration of
0.25 g after a delay of 2.5 s.
(7)
STANDARD ENCOUNTER MODEL
(a) ELEMENTS OF THE STANDARD ENCOUN-
TER MODEL
(i) In order to calculate the effect of ACAS on the
risk of collision and the compatibility of ACAS
with air traffic management (ATM), sets of
encounters shall be created for each of:
(a) the two aircraft address orderings;
(b) the six altitude layers;
(c) nineteen encounter classes; and
(d) nine or ten vmd bins as specified in sub paragraph
1(7)(b)(iv).
The results for these sets shall be combined using the relative
weightings given in sub paragraph 1.(7)(b).
(aa)
Each set of encounters shall contain at least 500
independent, randomly generated encounters.
(bb)
The two aircraft trajectories in each encounter
shall be constructed with the following randomly selected
characteristics:
(a)
in the vertical plane:

CIVIL AVIATION
S.R.O. 31
(i)
a vmd from within the appropriate
vmdbin;
(ii)
a vertical rate for each aircraft at the
beginning of the encounter window,
ż1, and at the end of the encounter
window, ż2;
(iii)
a vertical acceleration; and
(iv)
a start time for the vertical accelera
tion; and
(b)
and in the horizontal plane:
(i)
an hmd;
(ii)
an approach angle;
(iii)
a speed for each aircraft at closest
approach;
(iv)
a decision for each aircraft whether
or not it turns;
(v)
the turn extent; the bank angle; and
the turn end time;
(vi)
a decision for each aircraft whether
or not its speed changes; and
(vii)
the magnitude of the speed change.
Note.— It is possible for the selections made for the various
characteristics of an encounter to be irreconcilable. When this
occurs, the problem can be resolved by discarding either the
selection for a particular characteristic or the whole encounter,

CIVIL AVIATION
S.R.O. 31
as most appropriate.
(cc) Two models shall be used for the statistical
dis
tribution of hmd. For calculations of the effect of
ACAS on the risk of collision, hmd shall be
constrained to be less than 500 ft. For calculations
of the compatibility of ACAS with ATM, hmd
shall be selected from a larger range of values.
Note.— Sub paragraphs 1.(7)(b) and (c) specify vertical
characteristics for the aircraft trajectories in the standard
encounter model that depend on whether the hmd is con-
strained to be small (“for calculating risk ratio”) or can take
larger values (“for ATM compatibility”). Otherwise, the
characteristics of the encounters in the vertical and horizon-
tal planes are independent.
(c)
ENCOUNTER CLASSES AND WEIGHTS
(i)
Aircraft address. Each aircraft shall be equally
likely to have the higher aircraft address.
(ii)
Altitude layers. The relative weights of the
altitude layers shall be as follows:
(iii)
Encounter classes
(ba) The encounters shall be classified according to
whether the aircraft are level (L) or transitioning
(T) at the beginning (before tca) and end (after
tca) of the encounter window and whether or not
the encounter is crossing, as follows

CIVIL AVIATION
S.R.O. 31
(bb) The relative weights of the encounter classes shall
depend on layer as follows:

CIVIL AVIATION
S.R.O. 31
(iv)
vmd bins
(aa)
The vmd of each encounter shall be taken
from one of ten vmd bins for the non-
crossing encounter classes, and from one of
nine or ten vmd bins for the crossing
encounter classes. Each vmd bin shall have
an extent of 100 ft for calculating risk ratio,
or an extent of 200 ft for calculating
compatibility with ATM. The maximum
vmd shall be 1 000 ft for calculatingrisk
ratio, and 2 000 ft otherwise.
(bb)
For non-crossing encounter classes, the

CIVIL AVIATION
S.R.O. 31
relative weights of the vmd bins shall be as
follows:
Note.— The weights for the vmd bins do not sum to 1.0. The
weights specified are based on an analysis of encounters
captured in ATC ground radar data. The missing proportion
reflects the fact that the encounters captured included some
with vmd exceeding the maximum vmd in the model.
(cc) For the crossing classes, the relative
weights of the vmd bins shall be as follows:
Note.— For the crossing classes, vmd must exceed 100 ft so
that the encounter qualifies as a crossing encounter. Thus,
for the calculation of risk ratio there is no vmd bin 1, and for

CIVIL AVIATION
S.R.O. 31
calculations of the compatibility with ATM vmd bin 1 is
limited to [100 ft, 200 ft].
(d)
CHARACTERISTICS OF THE AIRCRAFT TRAJEC-
TORIES IN THE VERTICAL PLANE
(i)
vmd. The vmd for each encounter shall be se
lected randomly from a distribution that is uniform
in the interval covered by the appropriate vmd bin.
(ii)
Vertical rate
(aa)
For each aircraft in each encounter, either
the vertical rate shall be constant (ż) or the
vertical trajectory shall be constructed so
that the vertical rate at tca – 35 s is ż1 and
the vertical rate at tca+ 5 s is ż2. Each
vertical rate, ż, ż1or ż2, shall be determined
by first selecting randomly an interval
within which it lies and then selecting the
precise value from a distribution that is
uniform over the interval selected.
(bb)
The intervals within which the vertical rates
lie shall depend on whether the aircraft is
level, i.e. marked “L” in sub paragraph 1(7)
(c)(iii)(ba), or transitioning, i.e. marked “T”
in sub paragraph 1(7)(c)(ii)(ba),, and shall
be as follows:

CIVIL AVIATION
S.R.O. 31
(cc) For aircraft that are level over the entire
encounter window, the vertical rate ż shall
be constant. The probabilities for the
intervals within which ż lies shall be as
follows:
(dd)
For aircraft that are not level over the entire en
counter window, the intervals for ¿1 and ¿2 shall
be determined jointly by random selection using
joint probabilities that depend on altitude layerand
on whether the aircraft is transitioning at the
beginning of the encounter window (Rate-to-
Level), at the end of the encounter window
(Level-to-Rate) or at both the beginning and the
end (Rate-to-Rate). The joint probabilities for the
vertical rate intervals shall be as follows:

CIVIL AVIATION
S.R.O. 31
for aircraft with Rate-to-Level trajectories in layers 1 to 3,
for aircraft with Rate-to-Level trajectories in layers 4 to 6,
for aircraft with Rate-to-Rate trajectories in layers 1 to 3,
for aircraft with Rate-to-Rate trajectories in layers 4 to 6,
for aircraft with Rate-to-Rate trajectories in layers 1 to 3,

CIVIL AVIATION
S.R.O. 31
for aircraft with Rate-to-Rate trajectories in layers 4 to 6,
(ee)
For a Rate-to-Rate track, if line |ż2 – ż1| <
566 ft/min then the track shall be con
structed with a constant rate equal to ż1.
(iii)
Vertical acceleration
(aa)
Subject to (d)(ii)(ee) immediately above for
aircraft that are not level over the entire
encounter window, the rate shall be con
stant and equal to ż1 over at least the
interval [tca – 40 s,tca– 35 s] at the begin
ning of the encounter window, and shall
be constant and equal to ż2 over at least the
interval [tca+ 5 s, [tca+ 10 s] at the end of
the encounter window. The vertica accel
eration shall be constant in the intervening
period.
(bb) The vertical acceleration shall be modelled as
         follows:

CIVIL AVIATION
S.R.O. 31
where the parameter A is case-dependent as follows:
and the error ε is selected randomly using the following prob-
abilitydensity:
Where µ = 0.3 ft s -2
Note.— The sign of the acceleration
is determined by ż1 and
ż2. An error å that reverses this sign must be rejected and the error
reselected.
(iv)
Acceleration start time. The acceleration start
time shall be distributed uniformly in the time
interval [tca– 35 s, tca– 5 s] and shall be such that
ż2 is achieved no later than tca+ 5 s.
(e)
CHARACTERISTICS OF THE AIRCRAFT TRAJEC-
TORIES IN THE HORIZONTAL PLANE
(i)
Horizontalmissdistance
(aa)
For calculations of the effect of ACAS on
theriskofcollision,hmdshall beuniformly
distributed in the range [0, 500 ft].

CIVIL AVIATION
S.R.O. 31
(bb)
For calculations concerning the compatibil
ity of ACAS with ATM, hmd shall be
distributed so
that the values of hmd have
the following cumulative
probabilities:
(ii)
Approach angle. The cumulative distribution for the hori
zontal ap-
proach angle shall be as follows:

CIVIL AVIATION
S.R.O. 31
(iii)
Aircraft speed. The cumulative distribution for each aircraft’s
horizontal ground speed at closest approach shall be as follows:
(iv)
Horizontal manoeuvre probabilities. For each aircraft in each encounter, the
probability of a turn, the probability of a speed change given a turn, and the
probability of a speed change given no turn shall be as follows:
(aa)
Given a speed change, the probability of a
speed increase shall be 0.5 and the prob
ability of a speed decrease shall be 0.5.

CIVIL AVIATION
S.R.O. 31
(v)
Turn extent. The cumulative distribution for the
extent of any turn shall be as follows:
(aa)
The direction of the turn shall be random,
with the probability of a left turn being 0.5
and the probability of a right turn being 0.5.
(vi)
Bank angle. An aircraft’s bank angle during a
turn shall not be less than 15 degrees. The prob
ability that it equals 15 degrees shall be 0.79 in
layers 1-3 and 0.54 in layers 4-5. The cumulative
distribution for larger bank angles shall be follows:
Turn end time. The cumulative distribution for each aircraft’s turn
end time shall be as follows:

CIVIL AVIATION
S.R.O. 31
(vii)
Speed change. A constant acceleration or decel
eration shall be randomly selected for each air
craft performing a speed change in a given en
counter, and shall be applied for the duration of
the encounter. Accelerations shall be uniformly
distributed between 2 kt/s and 6 kt/s.
Decelerations shall be uniformly distributed
between 1 kt/s and 3 kt/s.
(8)
ACAS EQUIPAGE OF THE INTRUDER
The performance requirements specified in Paragraphs 2. and 3.
of this scheduleeach apply to three distinct situations in which the
following conditions concerningtheintruder’sACASandtrajec-
toryshallapply:
(a) where the intruder involved in each encounter is not
equipped,it follows a trajectory identical to that which
it follows when own aircraft is not equipped;
(b) where the intruder is ACAS-equipped but follows a
trajectory identical to that in the unequipped encoun-
ter:
(i)
it follows the identical trajectory regardless of
whether or not there is an RA;

CIVIL AVIATION
S.R.O. 31
(ii)
the intruder ACAS generates an RA and trans
mits an RAC that is received immediately after
any RA is first announced to the pilot of own
aircraft;
(iii)
the sense of the RAC generated by the intruder
ACAS and transmitted to own aircraft is opposite
to the sense of the first RAC selected and trans
mitted to the intruder by own aircraft;
(iv)
the RAC transmitted by the intruder is received
by own
aircraft; and
(v)
the requirements apply both when own aircraft
has the lower aircraft address and when the
intruder aircraft has the lower aircraft address;
and
(c) where the intruder is equipped with an ACAS having
a collision avoidance logic identical to that of own
ACAS:
(i)
the conditions relating to the performance of own
aircraft, ACAS and pilot apply equally to the
intruder aircraft, ACAS and pilot;
(ii)
RACs transmitted by one aircraft are
received by the other; and
(iii)
the requirements apply both when own aircraft
has the lower aircraft address and when the
intruder aircraft has the lower aircraft address.
(9)
COMPATIBILITY
BETWEEN DIFFERENT
COLLISION AVOIDANCE LOGIC DESIGNS

CIVIL AVIATION
S.R.O. 31
Whenconsideringalternativecollisionavoidancelogicdesigns,
certificationauthoritiesshallverify that:
(a) theperformances ofthealternativedesignareaccept-
able in encounters involving ACAS units that use
existingdesigns;and
(b) the performances of the existing designs are not
degraded by the use of the alternative design.
Note.— To address the compatibility between different collision
avoidance logic designs, the conditions described in
sub paragraph 1(8)(b) are the most severe that can be
anticipated in this respect.
2.
Reduction in the risk of collision
Undertheconditionsofparagraph1.thecollisionavoidancelogic
shall be such that the expected number of collisions is reduced to
the following proportions of the number expected in the absence
of ACAS:
(a) when the intruder is not ACAS equipped 0.18;
(b) when the intruder is equipped but does not respond
0.32; and
(c) when the intruder is equipped and responds 0.04.
3.
Compatibility with air traffic management (ATM)
(1)
NUISANCE ALERT RATE
(a) Under the conditions of Paragraph 1., the collision
avoidance logic shall be such that the proportion of
RAs which are a “nuisance” shall not exceed:

CIVIL AVIATION
S.R.O. 31
.06 when own aircraft’s vertical rate at the time the RA is first
issued is less than 400 ft/min; or
.08 when own aircraft’s vertical rate at the time the RA is first
issued exceeds 400 ft/min.
Note.—Thisrequirement isnotqualifiedbytheACASequipage
of the intruder since it has negligible effect on the occurrence and
frequency of nuisance RAs.
(b) An RA shall be considered a “nuisance” for the
purposes of Sub-paragraph 3.(1)(a) unless, at some
point in the encounter in the absence of ACAS, the
horizontal separation and the vertical separation are
simultaneously less than the following values:
(2)
COMPATIBLE SENSE SELECTION
Under the conditions of Paragraph 1., the collision avoidance
logic shall be such that the proportion of encounters in which
following the RA results in an altitude separation at closest
approach with the opposite sign to that occurring in the ab-
sence of ACAS shall not exceed the following values:
(a) when the intruder is not ACAS equipped 0.08;
(b) when the intruder is equipped but does not respond
0.08; and
(c) when the intruder is equipped and responds
0.12.
(3)
DEVIATIONS CAUSED BY ACAS

CIVIL AVIATION
S.R.O. 31
(a) Under the conditions of Paragraph 1. the collision avoidance logic shall
be such that the number of RAs resulting in “deviations” greater than the
values indicated shall not exceed the following proportions of the total
number of RAs:
For the purposes of sub-paragraph (3)(a), the “deviation” of the equipped aircraft
from the original trajectory shall be measured in the interval from the time at which
the RA is first issued until the time at which, following cancellation of the RA, the
equipped aircraft has recovered its original altitude rate. The deviation shall be
calculated as the largest altitude difference at any time in this interval between the
trajectory followed by theequippedaircraftwhenrespondingtoitsRAanditsoriginal
trajectory.
4.
Relative value of conflicting objectives
The collision avoidance logic shall be such as to reduce the risk of collision (measured
as defined in paragraph 2.) and limit the disruption to ATM (measured as defined in
paragraph 3.).

CIVIL AVIATION
S.R.O. 31
