TABLES FOR SCHEDULE 11
Table 11-1.
International Telegraph Alphabets No. 2 and No. 3

CIVIL AVIATION
S.R.O. 32
Table 11-2. International Alphabet No.5 (IA-5)

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32

CIVIL AVIATION
S.R.O. 32
Table 11-3. Conversion from the International Telegraph Alphabet No. 2 (ITA-2)
to the International Alphabet No. 5 (IA-5)
ITA-2
ITA-2
        letter case
IA-5                           figure case
IA-5
      of signal No.                     column/row                   of  signal No.                       column/row
A
4/1
A
–
2/13
–
B
4/2
B
?
3/15
?
C
4/3
C
:
3/10
:
D
4/4
D
3/15
?
E
4/5
E
3/3
F
4/6
F
3/15
?
G
4/7
G
3/15
?
H
4/8
H
3/15
?
I
4/9
I
3/8
10 J
4/10 J
10 Attention Signal(Note 3)
0/7
Bel
11 K
4/11 K
11 (
2/8
(
12 L
4/12 L
12 )
2/9
)
13 M
4/13 M
13 .
2/14
.
14 N
4/14 N
14 ,
2/12
,
15 O
4/15 O
15 9
3/9
16 P
5/0
P
16 0
3/0
17 Q
5/1
Q
17 1
3/1
18 R
5/2
R
18 4
3/4
19 S
5/3
S
19 ’
2/7
’
20 T
5/4
T
20 5
3/5
21 U
5/5
U
21 7
3/7
22 V
5/6
V
22 =
3/13
=
23 W
5/7
W
23 2
3/2
24 X
5/8
X
24 /
2/15
/
25 Y
5/9
Y
25 6
3/6
26 Z
5/10 Z
26 +
2/11
+
27 CR
0/13 CR
27 CR
0/13
CR

CIVIL AVIATION
S.R.O. 32
28 LF
0/10 LF
28 LF
0/10
LF
29 LTRS
*
29 LTRS
*
30 FIGS
*
30 FIGS
*
31 SP
2/0
SP
31 SP
2/0
SP
*
*
* No conversion shall be made for these positions and the signal/character shall be
removed from the data.
Note 1.— The end-of-message signal NNNN(in letter and figure case) shallconvert
toETX(0/3). Note 2.— The start-of-message signal ZCZC (in letter and figure case)
shall convert to
SOH (0/1).
Note3.—FigurescaseofSignalNo.10shallonlybeconvertedupondetectionofthe
AFTN priority alarm which shall convert to five occurrences of BEL (0/7).
Note 4.—When converting from ITA-2, a STX (0/2) character shall be inserted once
at the beginning of the next line following detection of CR LF or LF CR at the end
of the Origin Line.
Note 5.— The sequence of seven signal 28 (LF) shall convert to one VT (0/11)
character.

CIVIL AVIATION
S.R.O. 32
Table 11-4. Conversion from the International Alphabet No. 5 (IA-5) to the
International Telegraph Alphabet No. 2 (ITA-2)
Col.Row
*
*
31FL
16F
2F
16L
2F
16L
Note 5
*
2F
17F
1L
17L
1L
17L
*
*
2F
23F
2L
18L
2L
18L
Note 1
*
2F
5F
3L
19L
3L
19L
*
*
2F
18F
4L
20L
4L
20L
*
*
2F
20F
5L
21L
5L
21L
*
*
2F
25F
6L
22L
6L
22L
Note 2
*
19F
21F
7L
23L
7L
23L
*
*
11F
9F
8L
24L
8L
24L
*
*
12F
15F
9L
25L
9L
25L
28 FL
*
2F
3F
10L
26L
10L
26L
Note 3
*
26F
2F
11L
2F
11L
2F
*
*
14F
2F
12L
2F
12L
2F
27FL
*
1F
22F
13L
2F
13L
2F
*
*
13F
2F
14L
2F
14L
2F
*
*
24F
2F
15L
2F
15L
*
* No conversion shall be made for these positions and the signal/character shall be removed from the
data.
Example:
To find the ITA-2 signal to which the character 3/6 of IA-5 is to be converted, look
at column 3, row 6.
25F means figure case of signal No. 25
(L = letter case, FL = either case designation).
Note 1.—
  The character 0/3 (ETX) shall convert to the ITA-2 sequence signals 14L, 14L,
14L, 14L (NNNN).
Note 2. — The signal 0/7 (BEL) shall only be converted when a sequence of 5 occurrences is
detected, which shall convert to the ITA-2 sequence signals 30, 10F, 10F, 10F, 10F,
10F, 29.
Note 3. — The character sequence CR CR LF VT (0/11) ETX (0/3) shall convert to the ITA-2
sequence signals 29, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 14L, 14L, 14L, 14L.
Note 4. — To prevent redundant generation of figure and letter characters in ITA-2 when convert
ing from IA-5, no case designation shall be assigned to ITA-2 non-printing functions
(signals No. 27, 28, 29, 30, 31).
Note 5. —   The character 0/1 (SOH) shall convert to the ITA-2 sequence signals 26L, 3L, 26L, 3L
(ZCZC).

CIVIL AVIATION
S.R.O. 32
Table 11-5. Control field formats
Control field bits
Control field format for
Information transfer (I frame)
N(S)
P
N(R)
Supervisory commands
S
S
P/F
N(R)
/responses (S frame)
Unnumbered commands/
M
M
P/F
M
M
M
responses
where:
N(S) = send sequence count (bit 2 = low order bit)
N(R) = receive sequence count (bit 6 = low order bit)
S = supervisory function bits
M = modifier function bits
P = poll bit (in commands)
F = final bit (in responses)
Table 11-6. Commands and responses

CIVIL AVIATION
S.R.O. 32
