<!-- ards for a given Aim: P ; . iat repare a SRS document in line with the IEEE recommended stand
Problem.
Pre-Experiment Questions:
l. Define Software. bo
Define Software engineering.
What does requirement gathering and analysis mean?
Bw
Howmini project topic was selected.
nn
What analysis you have done beforefinalizing the topic.
n
Whatis scope of project?
Procedure:
Step 1:
Introduction:
Purpose
Identify the product whose software requirements are specified in this document. Describe the
scope of the productthat is covered by this SRS, particularly if this SRS describes only part of
the system or a single subsystem.Describe the different types of user that the documentis
intended for, such as developers, project managers, marketing staff, users, testers, and
riters. Describe what the rest of this SRS contains and how it is organized. documentation w
g the document, beginning with the overview sections and Suggest a sequence for readin
proceeding through the sections that are mostpertinent to each readertype.
Project Scope
Provide a short description of the software being specified and its purpose, including relevant
benefits, objectives, and goals. Relate the software to corporate goals or businessstrategies. Ifa
separate vision and scope document is available, refer to it rather than duplicating its contents
here. An SRSthai-specifies the nextrelease of an evolving product should contain its own
scope statement as a subset of the long-term strategic productvision.
em
hUpre
Aer
Software Engineering Lab (RCS-452) Manual(CS, IV SEM) Page 18
TUT Oe UE eee Oe OB MC HPAIUIIUITLES Y 5 SPB eS rR ee Denurine CPE CEN alee “top 2; ¢ Mupiler science & Knpineering
( Way Vorall Description
byTodos. Poospective
Doseni SUEDE (He Contes Tain of
OULENT ane Origin of the product being specified in this SRS, Por example, state rola product family, a replacement for certain
Whether (his np NAS prodiel is a follow-on membe
eloontained product, If the SRS defines a component of a larger
ONIgti —
Nisting AVSlOMS, ap anew, §
r system to the functionality of this software and
AVale ‘ah ; lOM, relate (he requirements of the large
simple diagram that shows the major componentsof the Wontintorioos between (he two, A
and external interfaces can be helpful. OVOR Vorall system, We subsystem , iimoreonnections,
¥
Product nN Koatures
‘es the product contains or the significant functions that it performs
\ : Summarize the major fear
Or lots lets the usersean perform, fan Only a high level summary : , . is needed here, Organize the functions to makethem understandable to any reader of the SRS, A picture of the major groups of related requirements and howtheyrelate, such as a top level data flow diagram or a class diagram,is ofteneffective,
User Classes and Characteristics
Identify the various user classes that youanticipate will use this product. User classes may be
differentiated based on frequency of use, subset of product functions used, technical expertise,
security or privilege levels, educational level, or experience. Describe the pertinent
characteristics of each userclass, Certain requirements may pertain only to certain userclasses.
Distinguish the favoreduserclasses from those whoare less importantto satisfy.
Operating Environment
Describe the environmentin whichthe software will operate, including the hardwareplatform,
operating system and versions, and any other software components or applications with which
it must peacefully coexist.
Design and Implementation Constraints
Describe any items or issuesthat will limit the options available to the developers. These might
include: corporate or regulatory policies; hardware limitations (timing requirements, memory
requirements); interfaces to other applications; specific technologies, tools, and databases to be
used; parallel operations; language requirements; communications protocols; security
Page 19 Software Engineering Lab (RCS-452) Manual (CS, IV SEM)
RajJ Kumar Kk @Goel ; lustitute of Vechnolopy, De $s ae .
Cihaviahwd Sion Partment of ¢ MUPULEE Nelonoe & f ilneeriig CONSiderar: MU tions: a as OVanizatic ry US] "i ‘ ; .
_ OPUW TH
,
he
S8
pac
CONVentions
4 .
or PrOBTANIN trig standards (ley example, if the customer's © Fesponsible ; toy Maintaining the delivered sofware) Ste 3:
Q.- “*stem Features
This template {te illustrates j oroanie: ‘ates Organizing the finetional requirements for the product by system feature. . S. the maio Arya :
‘ UOP services Provided by the product, You May prefer to organize this section by usec sss Sse, modede ofof peration, operat; user:
class, Object :
class, functional ;
hierarchy, —
Ofthese Ww ,
or combinations - » Whatever makes the most logical sense for your product,
System Feature ]
Dont ; 76a, j Teally say “System Feature 1.” State the feature hame in just a few words,
1 Description and Priority
Provide a Short description
Priority.
of the feature and indicate whetherit is of High, Medium, or Low You could also include specific priority componentratings, such as benefit, penalty, Cost, andrisk (each rated onarelative scale from a low of 1 toa high of 9). 2 Stimulus/Response Sequences
List the Sequencesofuseractions and system responsesthat stimulate the behavior defined for this feature. These will correspondto the dialog elements associated with use cases. 3 Functional Requirements
Itemize the detailed functional requirements associated with this feature. These are the software capabilities that must be presentin orderfor the userto carry out the services provided bythe feature, or to execute the use case. Include how the product should respondto anticipated error conditions or invalid inputs. Requirements should be concise, complete, unambiguous, verifiable, and necessary,
<Lach requirement should be uniquelyidentified with a sequence numberor a meaningful lag ofsome kind,>
REQ-1: REQ-2:
7 ¢ pyar pe
r Goel Institute of Technology: Ghar Raj Kuma ence & Engineering Department of Computer Sci
External Interface Requirements
gers.
e software product and the ¥
i that are
duct family style
netions (€-8+ hel
UserInterfaces
of eachinterface guides between th
p) that will Describe the logical characteristics
any GUI standards or pro
standard buttons and fu
ror message display stan
e is needed. Details of t
This mayinclude sample screen images,
avout constraints, :
Define the
dards, and so on.
e design to be followed, screen|
screen, keyboard shortcuts, er he user interfac appear on every
software components for which a userinterfac
mented in a separate user interface specification. should be docu
tween the software product
d device types: the
ardware, and
HardwareInterfaces
stics of each interface be
may include the supporte
e software and the h
Describe the logical and physical characteri
and the hardware components of the system. This
nature of the data and control interactions between th
communication protocols to be used.
Software Interfaces
fiware components (name
n this product and other specific so
ms, tools, libraries, and integrated ¢
e system and going out and
nications.
Describe the connections betwee ommercial
including databases, operating syste
data items or messages coming into th
e services needed and the nature of commu
g interface protocols. Identify
and version),
components. Identify the
describe the purpose of each. Describe th
hat describe detailed application programmin
omponents. If the data sharing mechanism must be
multitasking operating
Refer to documentst
data that will be shared across software ¢
implemented in a specific way (for example, use of a global data area in a
system), specify this as an implementation constraint.
Communications Interfaces
Describe the requirements associated with any communications functions required by this product
including e-mail, web browser, network server communications protocols, electronic forms,9 and
so on. Define any pertinent message formatting. Identify any communication standards that will
be used, such as FTP or HTTP. Specify any communication security or encryption issues, data
transferrates, and synchronization mechanisms.
eeee ___o&x@x@O&je&5e“- 25 eg . .
pao Fi mE ok ee Oy Se La RK /(NMO AFA\ At awmwnl (MC IWaAPMKRAYN nN...
Ghaziaper
Institute of Technology:
r Science & engineering
Raj Kumar Goel
Department of Compute
Nonfunctional Requirements
Performance Requirements
ct under various circu ple design
derstand the intent 4
e such re
ndividual fun
nd make guita If there are performance requirements for the produ
quire ale, to help the developers un
al tim
ments as
and explaintheirration
the timing relationships for re ‘
ctional
need to state performance choices. Specify e systems. Mak
specific as possible. You may requirements for |
requirements orfeatures.
at could
ell as
Safety Requirements damage, or harm th
ust be taken, as W
at state safety issues
atisfied.
with possible loss,
quirements that are concerned
rds or actions that m
he product. Define any safegua
d. Refer to any external polic
se. Define any safety certifi
Specify those re
result from the use of tl
actions that must be prevente es or regulations th
cations that must be s
that affect the product’s design or u
Security Requirements
ts regarding security or privac of the product or
r created by the product. De
olicies or regulations containin
fications that must be satisfied.
y issues surrounding use
fine any user identity auth
g security issues that affect the Specify any requiremen entication
protection of the data used 0
ements. Refer to any external p requir
ne any security or privacy certi product. Defi
Software Quality Attributes portant to either the
teristics for the product that will be im
ability, availability, correctness,
robustness,
fy any additional quality charac
+ the developers. Some to consider are: adapt
portability, reliability, reusability,
and verifiable when possible. At
Speci
customers 0
flexibility, interoperability, maintainability,
testability, and usability. Write these to be specific, quantitative,
t, clarify the relative preferences for various attributes, such as ease of use over ease of
the leas
learning.
Other Requirements
Define any other requirements not covered elsewhere in the SRS. This might include databas e . e . . .
: ¢ eC
requirements, internationalization requirements, legal requirements, reuse objectives for th ? or the
project, and so on. Add any new sections that are pertinentto the project -->


 <!-- the following is the prompt for the 1st assignment of the software engineering course. the fist assigment is to make a srs document on movie recommneder system -->


<!-- # Introduction
#1 Purpose
#2 Product Scope
# Overall Description
#1 Product Perspective
#2 Product Features
#3 User Classes and Characteristics
#4 Operating Environment
#5 Design and Implementation Constraints
# System Features( it contains multiple features)
#1 Feature 1 (don't use the number 1, use the name of the feature)
#1.1 Description and Priority
#1.2 User Classes and Characteristics
#1.3 Functional Requirements
# External Interface Requirements
#1 User Interfaces
#2 Hardware Interfaces
#3 Software Interfaces
#4 Communications Interfaces
# Nonfunctional Requirements
#1 Performance Requirements
#2 Safety Requirements
#3 Security Requirements
#4 Software Quality Attributes
#5 Other Requirements
# -->


Prepare a Software Requirements Specification (SRS) document for a content-based recommender system that recommends movies similar to the movie the user likes and analyses the sentiments of the reviews given by the user. The document should contain the following sections:

# Introduction
## Purpose
## Product Scope
# Overall Description
## Product Perspective
## Product Features
## User Classes and Characteristics
## Operating Environment
## Design and Implementation Constraints
# System Features( it contains multiple features)
## Feature 1 (don't use the number 1, use the name of the feature)
### Description and Priority
### User Classes and Characteristics
### Functional Requirements
# External Interface Requirements
## User Interfaces
## Hardware Interfaces
## Software Interfaces
## Communications Interfaces
# Nonfunctional Requirements
## Performance Requirements
## Safety Requirements
## Security Requirements
## Software Quality Attributes
## Other Requirements
