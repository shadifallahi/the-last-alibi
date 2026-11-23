
# ==================================================
# THE LAST ALIBI
# A Terminal-Based Detective Mystery Game
# ==================================================


# ==================================================
# GAME DATA
# ==================================================

notebook = []
interviewed_suspects = []
analyzed_evidence = []
contradictions = []

murderer = "James Carter"


# ==================================================
# 1. CRIME SCENE INVESTIGATION
# ==================================================

def crime_scene():

    print("\n========== EDWARD BLACKWOOD'S ROOM ==========")
    print("You enter Edward Blackwood's bedroom.")
    print("The room is dark, and something feels suspicious...")

    clues = {
        "1": (
            "Desk",
            "You discover a partially burned letter hidden inside the desk."
        ),

        "2": (
            "Bookshelf",
            "You find a photograph of Edward with an unknown person."
        ),

        "3": (
            "Window",
            "You notice scratches around the window lock."
        ),

        "4": (
            "Body",
            "You discover a small puncture wound on Edward's neck."
        ),

        "5": (
            "Fireplace",
            "You find a partially burned piece of paper."
        )
    }

    while True:

        print("\nWhat would you like to investigate?")
        print("1. Desk")
        print("2. Bookshelf")
        print("3. Window")
        print("4. Body")
        print("5. Fireplace")
        print("6. Return to main menu")

        choice = input("\nYour choice: ")

        if choice in clues:

            object_name, clue = clues[choice]

            print(f"\n[CLUE DISCOVERED] {object_name}")
            print(clue)

            if clue not in notebook:

                notebook.append(clue)
                print("\nAdded to your detective notebook!")

            else:

                print("\nYou have already discovered this clue.")

        elif choice == "6":

            print("\nYou leave Edward's bedroom.")
            break

        else:

            print("\nInvalid choice. Try again.")


# ==================================================
# 2. INTERVIEW SUSPECTS
# ==================================================

def interview_suspects():

    suspects = {

        "1": {
            "name": "Victoria Blackwood",
            "description": "Edward's wife.",

            "questions": {
                "1": "Edward and I had dinner together at 8 PM.",
                "2": "He had many business enemies. I don't know who would want him dead.",
                "3": "I was in the living room after dinner.",
                "4": "I have never seen that photograph before."
            }
        },

        "2": {
            "name": "James Carter",
            "description": "Edward's personal assistant.",

            "questions": {
                "1": "I last saw Edward around 8:30 PM.",
                "2": "Edward was a private man. He didn't discuss his enemies with me.",
                "3": "I left the mansion at 9 PM. I had somewhere important to be.",
                "4": "I don't know anything about that photograph."
            }
        },

        "3": {
            "name": "Dr. Henry Wilson",
            "description": "Edward's personal doctor.",

            "questions": {
                "1": "I examined Edward earlier that evening.",
                "2": "He seemed anxious, but he didn't tell me why.",
                "3": "I left shortly before 9 PM.",
                "4": "I noticed Edward was keeping some old photographs."
            }
        }
    }

    print("\n========== SUSPECT INTERVIEWS ==========")

    while True:

        print("\nWho would you like to interview?")

        for number, suspect in suspects.items():

            print(f"{number}. {suspect['name']}")

        print("4. Return to main menu")

        choice = input("\nYour choice: ")

        if choice in suspects:

            suspect = suspects[choice]

            print(f"\nInterviewing {suspect['name']}")
            print(suspect["description"])

            if suspect["name"] not in interviewed_suspects:

                interviewed_suspects.append(suspect["name"])

                print("\nSuspect added to your interview records.")

            while True:

                print("\nWhat would you like to ask?")

                print("1. When did you last see Edward?")
                print("2. Did Edward have any enemies?")
                print("3. What were you doing that evening?")
                print("4. Do you know anything about the photograph?")
                print("5. End interview")

                question = input("\nYour choice: ")

                if question in ["1", "2", "3", "4"]:

                    print(f"\n{suspect['name']}:")
                    print(f"\"{suspect['questions'][question]}\"")

                    # Evidence-based dialogue with James Carter

                    if suspect["name"] == "James Carter" and question == "4":

                        photograph = (
                            "You find a photograph of Edward with an unknown person."
                        )

                        if photograph in notebook:

                            print("\nYou show James the photograph.")

                            print("\nJames looks nervous.")

                            print('"I... I may have seen that photograph before."')

                            print("\n[NEW INFORMATION]")

                            print("James has changed his original statement.")

                            contradiction = (
                                "James initially denied knowing about the photograph, "
                                "but changed his statement when confronted with it."
                            )

                            if contradiction not in contradictions:

                                contradictions.append(contradiction)

                                print("\n[CONTRADICTION DISCOVERED]")
                                print(contradiction)

                                print("\nAdded to your detective notebook!")

                        else:

                            print("\nYou haven't discovered the photograph yet.")
                            print("Perhaps you should investigate the crime scene first.")

                elif question == "5":

                    print("\nYou ended the interview.")
                    break

                else:

                    print("\nInvalid choice. Try again.")

        elif choice == "4":

            break

        else:

            print("\nInvalid choice. Try again.")


# ==================================================
# 3. DETECTIVE NOTEBOOK
# ==================================================

def detective_notebook():

    print("\n========== DETECTIVE NOTEBOOK ==========")

    print("\n--- DISCOVERED CLUES ---")

    if notebook:

        for index, clue in enumerate(notebook, start=1):

            print(f"{index}. {clue}")

    else:

        print("No clues discovered yet.")

    print("\n--- INTERVIEWED SUSPECTS ---")

    if interviewed_suspects:

        for suspect in interviewed_suspects:

            print(f"- {suspect}")

    else:

        print("You haven't interviewed anyone yet.")

    print("\n--- ANALYZED EVIDENCE ---")

    if analyzed_evidence:

        for evidence in analyzed_evidence:

            print(f"- {evidence}")

    else:

        print("No evidence analyzed yet.")

    print("\n--- CONTRADICTIONS ---")

    if contradictions:

        for contradiction in contradictions:

            print(f"- {contradiction}")

    else:

        print("No contradictions discovered yet.")


# ==================================================
# 4. EVIDENCE ANALYSIS
# ==================================================

def evidence_analysis():

    print("\n========== EVIDENCE ANALYSIS ==========")

    evidence_options = {

        "1": "You find a photograph of Edward with an unknown person.",

        "2": "You discover a partially burned letter hidden inside the desk.",

        "3": "You notice scratches around the window lock.",

        "4": "You discover a small puncture wound on Edward's neck.",

        "5": "You find a partially burned piece of paper."
    }

    if not notebook:

        print("\nYou haven't discovered any evidence yet.")
        print("Visit the crime scene first.")

        return

    available_evidence = {}

    for number, evidence in evidence_options.items():

        if evidence in notebook:

            available_evidence[number] = evidence

    while True:

        print("\nWhich evidence would you like to analyze?")

        for number, evidence in available_evidence.items():

            print(f"{number}. {evidence}")

        print("6. Return to main menu")

        choice = input("\nYour choice: ")

        if choice == "6":

            break

        if choice not in available_evidence:

            print("\nInvalid choice. Try again.")
            continue

        evidence = available_evidence[choice]

        if evidence in analyzed_evidence:

            print("\nYou have already analyzed this evidence.")
            continue

        analyzed_evidence.append(evidence)

        # Photograph analysis

        if choice == "1":

            print("\n--- PHOTOGRAPH ANALYSIS ---")

            print("You carefully examine the photograph.")
            print("You notice something unusual...")

            print("\nThe unknown person appears to be James Carter!")

            print("This is interesting because James claimed")
            print("he knew nothing about the photograph.")

            if "James Carter" in interviewed_suspects:

                contradiction = (
                    "James Carter denied knowing about the photograph, "
                    "but evidence connects him to it."
                )

                if contradiction not in contradictions:

                    contradictions.append(contradiction)

                    print("\n[CONTRADICTION DISCOVERED]")
                    print(contradiction)

                    print("\nAdded to your detective notebook!")

            else:

                print("\nYou should interview James Carter")
                print("to compare this evidence with his statement.")

        # Letter analysis

        elif choice == "2":

            print("\n--- LETTER ANALYSIS ---")

            print("You carefully examine the burned letter.")
            print("You can make out a few words:")

            print('"Meet me tonight. Nobody can know."')

            print("\nSomeone was hiding a secret from Edward.")

        # Window analysis

        elif choice == "3":

            print("\n--- WINDOW ANALYSIS ---")

            print("You examine the scratches around the lock.")

            print("The scratches appear to be on the inside.")
            print("Someone may have tried to make it look")
            print("like an intruder entered through the window.")

        # Body analysis

        elif choice == "4":

            print("\n--- BODY ANALYSIS ---")

            print("You examine the puncture wound more closely.")

            print("The wound appears consistent with a small")
            print("sharp instrument.")

            print("You suspect the murderer may have used")
            print("a medical instrument.")

        # Fireplace analysis

        elif choice == "5":

            print("\n--- FIREPLACE ANALYSIS ---")

            print("You carefully examine the burned paper.")

            print("You discover part of a handwritten name:")
            print('"...Carter"')

            print("\nThis could be an important discovery!")

        print("\nEvidence analysis completed.")


# ==================================================
# 5. FINAL ACCUSATION
# ==================================================

def make_accusation():

    suspects = [
        "Victoria Blackwood",
        "James Carter",
        "Dr. Henry Wilson"
    ]

    print("\n========== FINAL ACCUSATION ==========")

    if len(notebook) < 3:

        print("\nYou don't have enough evidence!")
        print("Discover at least 3 clues before making an accusation.")

        return

    if len(interviewed_suspects) < 1:

        print("\nYou must interview at least one suspect first!")

        return

    if not analyzed_evidence:

        print("\nYou must analyze at least one piece of evidence first!")

        return

    print("\nYou have gathered enough evidence.")
    print("Who do you believe is responsible for Edward's death?")

    for index, suspect in enumerate(suspects, start=1):

        print(f"{index}. {suspect}")

    print("4. Return to main menu")

    choice = input("\nYour choice: ")

    if choice == "4":

        return

    if choice in ["1", "2", "3"]:

        accused = suspects[int(choice) - 1]

        print(f"\nYou accuse {accused}!")

        if accused == murderer:

            print("\n================================")
            print("          CASE SOLVED!")
            print("================================")

            print("Congratulations, Detective!")
            print("You correctly identified James Carter.")
            print("Edward Blackwood's murderer has been caught.")

        else:

            print("\n================================")
            print("       WRONG ACCUSATION!")
            print("================================")

            print("The real murderer is still free.")
            print("You need to reconsider the evidence.")

    else:

        print("\nInvalid choice. Try again.")


# ==================================================
# 6. MAIN MENU
# ==================================================

def main():

    print("\n================================")
    print("       THE LAST ALIBI")
    print("================================")

    print("A murder mystery awaits...")
    print("Edward Blackwood has been found dead.")
    print("Can you uncover the truth?")

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Crime scene")
        print("2. Interview suspects")
        print("3. Notebook")
        print("4. Evidence analysis")
        print("5. Final accusation")
        print("6. Exit")

        choice = input("\nYour choice: ")

        if choice == "1":

            crime_scene()

        elif choice == "2":

            interview_suspects()

        elif choice == "3":

            detective_notebook()

        elif choice == "4":

            evidence_analysis()

        elif choice == "5":

            make_accusation()

        elif choice == "6":

            print("\nThank you for playing The Last Alibi!")
            print("Goodbye, Detective.")

            break

        else:

            print("\nInvalid choice. Please select 1-6.")


# ==================================================
# START THE GAME
# ==================================================

if __name__ == "__main__":

    main()

