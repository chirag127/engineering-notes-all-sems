import os
import openai
import glob


def main(file_name):
    with open(file_name, "r") as f:
        text = f.read()

    syllables = text.split(
        "-----------------------------------------------------------------------------------------------------------"
    )

    # print(syllables)

    folder_name = file_name.split(".")[0]

    folder_name = folder_name.replace("raw_s/", "")

    folder_name = "p_s/" + folder_name

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    titles = []

    for i in range(len(syllables)):
        titles.append(syllables[i].split("KCS")[0])

    titles = [i.strip() for i in titles]

    # remove the "(" and ")" from the titles
    titles = [i.replace("(", "") for i in titles]

    titles = [i.strip() for i in titles]

    print(titles)
    openai.api_key = "***REMOVED***"
    try:
        for syllable in syllables:
            file_of_syllable = f"{folder_name}/{syllables.index(syllable)}_{titles[syllables.index(syllable)]}.txt"

            if os.path.exists(file_of_syllable):
                continue

            print(file_of_syllable)
            response = openai.Completion.create(
                model="code-davinci-002",
                prompt="Real Time System (KCS-063)\nCourse Outcome ( CO) Bloom’s Knowledge Level (KL)\nAt the end of course , the student will be able:\nCO 1 illustrate the need and the challenges in the design of hard and soft real time systems. K3\nCO 2 Compare different scheduling algorithms and the schedulable criteria. K4\nCO 3 Discuss resource sharing methods in real time environment. K3\nCO 4 Compare and contrast different real time communication and medium access control \ntechniques.\nK4, K5\nCO 5 Analyze real time Operating system and Commercial databases K2, K4\nDETAILED SYLLABUS 3-0-0\nUnit Topic Proposed \nLecture \nI\nIntroduction \nDefinition, Typical Real Time Applications: Digital Control, High Level Controls, Signal \nProcessing etc., Release Times, Deadlines, and Timing Constraints, Hard Real Time Systems and \nSoft Real Time Systems, Reference Models for Real Time Systems: Processors and Resources, \nTemporal Parameters of Real Time Workload, Periodic Task Model, Precedence Constraints and \nData Dependency.\n05\nII\nReal Time Scheduling\nCommon Approaches to Real Time Scheduling: Clock Driven Approach, Weighted Round Robin \nApproach, Priority Driven Approach, Dynamic Versus Static Systems, Optimality of Effective\u0002DeadlineFirst (EDF) and Least-Slack-Time-First (LST) Algorithms, Rate Monotonic Algorithm, \nOffline Versus Online Scheduling, Scheduling Aperiodic and Sporadic jobs in Priority Driven and \nClock Driven Systems.\n09\nIII\nResources Sharing\nEffect of Resource Contention and Resource Access Control (RAC), Non-preemptive Critical \nSections, Basic Priority-Inheritance and Priority-Ceiling Protocols, Stack Based Priority-Ceiling \nProtocol, Use of Priority-Ceiling Protocol in Dynamic Priority Systems, Preemption Ceiling \nProtocol, Access Control in Multiple-Unit Resources, Controlling Concurrent Accesses to Data \nObjects.\n09\nIV\nReal Time Communication\nBasic Concepts in Real time Communication, Soft and Hard RT Communication systems, Model of \nReal Time Communication, Priority-Based Service and Weighted Round-Robin Service Disciplines \nfor Switched Networks, Medium Access Control Protocols for Broadcast Networks, Internet and \nResource Reservation Protocols\n09\nV\nReal Time Operating Systems and Databases\nFeatures of RTOS, Time Services, UNIX as RTOS, POSIX Issues, Characteristic of Temporal data, \nTemporal Consistency, Concurrency Control, Overview of Commercial Real Time databases 08\nText books:\n1. Real Time Systems by Jane W. S. Liu, Pearson Education Publication.\n2. Phillip A Laplanta,SeppoJ.Ovaska Real time System Design and Analysis Tools for practitioner, Wiley\n3. Mall Rajib, “Real Time Systems”, Pearson Education\n4. Albert M. K. Cheng , “Real-Time Systems: Scheduling, Analysis, and Verification”, Wiley\n\n\n\n# Real Time System\n## Unit 1 - Introduction of Real Time System\n### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Typical Real Time Applications for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Hard Real Time Systems for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Soft Real Time Systems for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Reference Models for Real Time Systems for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Processors and Resources for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Temporal Parameters of Real Time Workload for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Periodic Task Model for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n### Precedence Constraints and Data Dependency for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System\n## Unit 2 - Real Time Scheduling\n### Common Approaches to Real Time Scheduling for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Clock Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Weighted Round Robin Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Dynamic Versus Static Systems for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Optimality of Effective\u0002DeadlineFirst (EDF) and Least-Slack-Time-First (LST) Algorithms for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Rate Monotonic Algorithm for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Offline Versus Online Scheduling for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System\n## Unit 3 - Resources Sharing\n### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Basic Priority-Inheritance and Priority-Ceiling Protocols for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Stack Based Priority-Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Use of Priority-Ceiling Protocol in Dynamic Priority Systems for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Access Control in Multiple-Unit Resources for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n### Controlling Concurrent Accesses to Data Objects for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System\n## Unit 4 - Real Time Communication\n### Basic Concepts in Real time Communication for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n### Soft and Hard RT Communication systems for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n### Model of Real Time Communication for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n### Medium Access Control Protocols for Broadcast Networks for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n### Internet and Resource Reservation Protocols for the notes of the Unit 4 - Real Time Communication in the subject of Real Time System\n## Unit 5 - Real Time Operating Systems and Databases\n### Features of RTOS for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### UNIX as RTOS for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### POSIX Issues for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### Characteristic of Temporal data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### Temporal Consistency for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n### Overview of Commercial Real Time databases for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System\n\n################################################################################\n\n"
                + syllable
                + "# "
                + titles[syllables.index(syllable)],
                temperature=0,
                max_tokens=3000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=[
                    "\n################################################################################\n"
                ],
            )

            with open(file_of_syllable, "w") as f:
                f.write(response["choices"][0]["text"].strip())
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    for i in range(1, 100):
        # get all files of raw_s folder and sub folders of raw_s

        files = glob.glob("raw_s/**/*", recursive=True)
        for file in files:
            if os.path.isfile(file):
                main(file)
                print(file)
