"""This is the code for my project!"""

import random

amend1_desc = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."
amend2_desc = "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."
amend3_desc = "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law."
amend4_desc = "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."
amend5_desc = "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation."
amend6_desc = "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence."
amend7_desc = "In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law."
amend8_desc = "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."
amend9_desc = "The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people."
amend10_desc = "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people."

required_amend_terms = {
    1: ["speech", "religion", "press", "assembly", "petition"],
    2: ["bear arms"],
    3: ["no quartering soliders", "peace"],
    4: ["no unreasonable search and seizure", "search warrant", "probable cause"],
    5: ["right to remain silent", "no self-incrimination", "substantive due process"],
    6: ["right to counsel", "speedy trial", "confront witnesses"],
    7: ["right to a jury trial", "federal civil cases"],
    8: ["no cruel or unusual punishment", "excessive fines", "excessive bail"],
    9: ["rights beyond text"],
    10: ["powers not dedicated to the federal government are reserved to the states"]
}

bor_rat_date = 1791

scotus_cases_by_amend = {
    1: ["citizens united v. fec", 
        "wisconsin v. yoder", 
        "new york times vs. us", 
        "tinker v. des moines", 
        "engel v. vitale", 
        "schenck v. us"],
    2: ["mcdonald v. chicago"],
    6: ["gideon v. wainwright"]
}

correct_responses = [
    "🦅 GovBot: Go USA! You've earned one freedom point.",
    "🦅 GovBot: Outstanding! An eagle just screeched in celebration.",
    "🦅 GovBot: Correct! James Madison nods approvingly.",
    "🦅 GovBot: Correct! George Washington nods approvingly.",
    "🦅 GovBot: Correct! Alexander Hamilton nods approvingly.",
    "🦅 GovBot: Nice work! The Constitution remains secure.",
    "🦅 GovBot: Outstanding! The eagle has awarded you one patriot point.",
    "🦅 GovBot: Nice work! Madison is updating your stats.",
    "🦅 GovBot: Perfect! *Hamilton soundtrack plays triumphantly*",
    "🦅 GovBot: Correct! The eagle has certified this answer as constitutional."
]
    
incorrect_responses = [
    "🦅 GovBot: Incorrect. The Supreme Court has ruled against that answer.",
    "🦅 GovBot: That's not it. Even the eagle looks confused.",
    "🦅 GovBot: Nice try, but no. The eagle has placed you under academic review.",
    "🦅 GovBot: Nice try. Madison has scheduled a remedial civics lesson.",
    "🦅 GovBot: Incorrect. Time for a quick trip back to the notes.",
    "🦅 GovBot: Incorrect. I'm going to have to 'Say No to This.'",
    "🦅 GovBot: Incorrect. Remember, history has its eyes on you...",
    "🦅 GovBot: Not quite. Alexander Hamilton is writing a strongly worded Federalist Paper about this.",
    "🦅 GovBot: Not quite. Aaron Burr recommends talking less and studying more.",
    "🦅 GovBot: Not quite. This answer is helpless... but not hopeless."
]


class StudyingBillOfRights():
    """
    A study tool that quizzes users on the Bill of Rights.

    The class tracks a user's score and provides methods for
    reviewing amendment descriptions, ratification date,
    and important Supreme Court cases that relate to a specified amendment.
    """

    def __init__(self):
        """
        Initialize a StudyingBillOfRights object.

        Creates a new study session and sets the user's score to zero.

        Returns
        -------
        None
            This method does not return a value.
        """
        self.score = 0

    def amend_description(self, num, desc):  # desc is the user's own string description of the amendment they are trying to study
        """
        Check whether a user's amendment description contains all required concepts.
    
        Compares the user's description against a list of required keywords
        associated with the specified amendment. If all required concepts are
        present, the user's score is increased by one and a random success
        message is returned. Otherwise, a random failure message and the
        missing concepts are returned.
    
        Parameters
        ----------
        num : int
            Amendment number used to retrieve the required concepts.
        desc : str
            User-provided description of the amendment.
    
        Returns
        -------
        str
            A formatted message indicating whether the response was correct,
            any missing concepts, and the current score.
        """

        desc = desc.lower()
        
        keywords = required_amend_terms[num]
        missing = []
        
        for phrase in keywords: 
            if phrase not in desc:
                missing.append(phrase)
                
        if len(missing) == 0:
            self.score += 1
            return (
                f"{random.choice(correct_responses)}\n"
                f"Score: {self.score}"
            )

        return (
            f"{random.choice(incorrect_responses)}\n"
            f"Missing Concepts: {', '.join(missing)}\n"
            f"Score: {self.score}"
        )

    def amend_date(self, date):
        """
        Check whether the user correctly identifies the Bill of Rights ratification year.

        Compares the provided year against the Bill of Rights ratification
        year. If the answer is correct, the user's score is increased by one
        and a random success message is returned. Otherwise, a random failure
        message is returned.

        Parameters
        ----------
        date : int or str
            User-provided year to compare against the ratification date.

        Returns
        -------
        str
            A formatted message indicating whether the response was correct
            and the current score.
        """

        if int(date) == bor_rat_date:
            self.score += 1

            return (
                f"{random.choice(correct_responses)}\n"
                f"Score: {self.score}"
            )

        else:
            return (
                f"{random.choice(incorrect_responses)}\n"
                f"Score: {self.score}"
            )

    def amend_scotus_cases(self, num, case_name):  # case_name is the user's string input of court case names they are trying to study
        """
        Check whether a user's response includes all AP-Gov-required Supreme Court cases for an amendment.

        Compares the user's input against a list of AP-Gov-required Supreme Court
        cases associated with the specified amendment. If all required cases
        are included, the user's score is increased by one and a random
        success message is returned. Otherwise, a random failure message and
        the missing cases are returned.

        Parameters
        ----------
        num : int
            Amendment number used to retrieve the associated Supreme Court cases.
        case_name : str
            User-provided Supreme Court case name(s).

        Returns
        -------
        str
            A formatted message indicating whether the response was correct,
            any missing cases, and the current score.
        """
        
        case_name = case_name.lower()

        key_cases = scotus_cases_by_amend[num]
        case_missing = []

        for case in key_cases:
            if case not in case_name:
                case_missing.append(case)
            
        if len(case_missing) == 0:
            self.score += 1
            return (
                f"{random.choice(correct_responses)}\n"
                f"Score: {self.score}"
            )

        return (
            f"{random.choice(incorrect_responses)}\n"
            f"Missing Concepts: {', '.join(case_missing)}\n"
            f"Score: {self.score}"
        )

    