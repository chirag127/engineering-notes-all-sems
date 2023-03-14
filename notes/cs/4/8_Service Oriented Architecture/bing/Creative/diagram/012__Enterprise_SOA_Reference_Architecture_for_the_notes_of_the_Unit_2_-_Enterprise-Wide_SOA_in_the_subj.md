The following is a detailed ASCII diagram for Enterprise SOA Reference Architecture for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture. The diagram is based on the SOA Reference Architecture from The Open Group  , which consists of nine layers representing nine key clusters of considerations and responsibilities that typically emerge in the process of designing an SOA solution or defining an enterprise architecture standard. The diagram uses the following symbols:

- [ ]: A layer of the SOA RA
- < >: A capability within a layer
- - : A relationship between capabilities or layers
- / : A sub-capability within a capability

The diagram is as follows:

[ Consumer Layer ]
< Consumer Interface > - [ Services Layer ]
< Consumer Functionality > - < Consumer Interface >
< Consumer Mediation > - < Consumer Interface >
< Consumer Management > - < Consumer Mediation >

[ Services Layer ]
< Service Interface > - [ Service Component Layer ]
< Service Mediation > - < Service Interface >
< Service Orchestration > - < Service Interface >
< Service Management > - < Service Mediation >

[ Business Process Layer ]
< Business Process > - [ Services Layer ]
< Business Rules > - < Business Process >
< Business Events > - < Business Process >
< Business Management > - < Business Process >

[ Service Component Layer ]
< Service Component > - [ Operational Systems Layer ]
< Service Component Implementation > - < Service Component >
< Service Component Composition > - < Service Component >
< Service Component Management > - < Service Component >

[ Operational Systems Layer ]
< Operational System > - [ Information Layer ]
< Operational System Functionality > - < Operational System >
< Operational System Integration > - < Operational System >
< Operational System Management > - < Operational System >

[ Information Layer ]
< Information Model > - [ Services Layer ]
< Information Access > - < Information Model >
< Information Governance > - < Information Model >
< Information Management > - < Information Access >

[ Integration Layer ]
< Integration Services > - [ Services Layer ]
< Integration Patterns > - < Integration Services >
< Integration Quality of Service > - < Integration Services >
< Integration Management > - < Integration Services >

[ Quality of Service Layer ]
< Quality of Service Services > - [ Services Layer ]
< Quality of Service Characteristics > - < Quality of Service Services >
< Quality of Service Policies > - < Quality of Service Characteristics >
< Quality of Service Management > - < Quality of Service Services >

[ Governance Layer ]
< Governance Services > - [ Services Layer ]
< Governance Processes > - < Governance Services >
< Governance Roles > - < Governance Processes >
< Governance Management > - < Governance Services >