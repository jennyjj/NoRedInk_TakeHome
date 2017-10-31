import random
import csv

def my_great_app(num_of_questions):
    """Given a number of questions, will give back a comma-delimited list of 
    question ids."""

    strand1_standard1_cn = []
    strand1_standard2_an = []
    strand1_standard3_pn = []

    strand2_standard4_av = []
    strand2_standard5_tv = []
    strand2_standard6_rv = []

    strand1_standards = ["Common Nouns", "Abstract Nouns", "Proper Nouns"]
    strand2_standards = ["Action Verbs", "Transitive Verbs", "Reflexive Verbs"]

    strand1_standards_questions = {"Common Nouns": strand1_standard1_cn, "Abstract Nouns": 
    strand1_standard2_an, "Proper Nouns": strand1_standard3_pn}
    strand2_standards_questions = {"Action Verbs": strand2_standard4_av, "Transitive Verbs":
    strand2_standard5_tv, "Reflesive Verbs": strand2_standard6_rv}

    questions = []

    with open('questions.csv', 'r') as csvfile:

        CSVReader = csv.reader(csvfile)

        for row in CSVReader:

            strand_id, strand_name, standard_id, standard_name, question_id, difficulty = row
            if strand_id == 1:
                if strand_name == "Common Nouns":
                    strand1_standard1_cn.append([question_id, difficulty])
                elif strand_name == "Abstract Nouns":
                    strand1_standard2_an.append([question_id, difficulty])
                elif strand_name == "Proper Nouns":
                    strand1_standard3_pn.append([question_id, difficulty])
            else:
                if strand_name == "Action Verbs":
                    strand2_standard4_av.append([question_id, difficulty])
                elif strand_name == "Transitive Verbs":
                    strand2_standard5_tv.append([question_id, difficulty])
                elif strand_name == "Reflexive Verbs":
                    strand2_standard6_rv.append([question_id, difficulty])

    questions_chosen = []
    standards_chosen = []

    for i in range(num_of_questions):
        if i % 2 == 0:
            standard_strand1 = random.choice(strand1_standards)
            if standard_strand1 in standards_chosen and i > 6:
                question_chosen = strand1_standards_questions[standard_strand1]
                [random.choice(len(strand1_standards_questions
                    [standard_strand1])-1)][1]    
                questions_chosen.append(question_chosen)
            elif standard_strand1 == "Common Nouns":
                standards_chosen.append(standard_strand1)
                question_chosen = strand1_standards_questions[standard_strand1]
                [random.choice(len(strand1_standards_questions
                    [standard_strand1])-1)][1]        
                questions_chosen.append(question_chosen)
            elif standard_strand1 == "Abstract Nouns":
                standards_chosen.append(standard_strand1)
                question_chosen = strand1_standards_questions[standard_strand1]
                [random.choice(len(strand1_standards_questions
                    [standard_strand1])-1)][1]  
            elif standard_strand1 == "Proper Nouns":
                standards_chosen.append(standard_strand1)
                question_chosen = strand1_standard3_pn[standard_strand1]
                [random.choice(len(strand1_standard3_pn)-1)][1]      
                questions_chosen.append(question_chosen)
        else:
            standard_strand2 = random.choice(strand2_standards)
            if standard_strand2 in standards_chosen and i > 6:
                question_chosen = strand2_standards_questions[standard_strand2]
                [random.choice(len(strand2_standards_questions
                    [standard_strand2])-1)][1]    
            elif standard_strand2 == "Action Verbs":
                standards_chosen.append(standard_strand2)
                question_chosen = strand2_standards_questions[standard_strand2]
                [random.choice(len(strand2_standards_questions
                    [standard_strand2])-1)][1]  
                questions_chosen.append(question_chosen)
            elif standard_strand2 == "Transitive Verbs":
                standards_chosen.append(standard_strand2)
                question_chosen = strand2_standards_questions[standard_strand2]
                [random.choice(len(strand2_standards_questions
                    [standard_strand2])-1)][1]  
                questions_chosen.append(question_chosen)
            elif standard_strand2 == "Reflexive Verbs":
                standards_chosen.append(standard_strand2)
                question_chosen = strand2_standards_questions[standard_strand2]
                [random.choice(len(strand2_standards_questions
                    [standard_strand2])-1)][1]  
                questions_chosen.append(question_chosen)

    questions_chosen = (",").join(questions_chosen)

    return questions_chosen

num_of_questions = 5
my_great_app(5)










    
