import json
import re

from pathlib import Path

# This is a hacked up script with the goal of converting the plaintext data from
# DICTLINE.txt and INFLECTIONS.txt to a JSON format. The benefits of using JSON 
# are twofold: handling data is much easier and handing out data (through an API) 
# requires nothing more than just sending the appropriate JSON entry.

# The script shall open the DICTLINE.txt/INFLECTIONS.txt file as provided by the DICTLINE_PATH/INFLECTS_PATH filepath.
# It shall then do some preparatory formatting before running through the entire file
# line by line. Each line shall be analysed and its content shall be put in a Python dictionary object.
# Any lines that can not be analysed (although very unlikely) shall be noted and displayed appropriately.
# Once all lines have been analysed, each dictionary object shall be turned into JSON and
# saved to a file as provided by the DICTLINE_JSON_PATH/INFLECTS_JSON_PATH filepath.

# This script's code should mostly be self-explanatory, but I have nevertheless commented
# areas which might require further explanation.

# Getting things done was the first priority while writing this. Also, I'm not very well versed
# in Python. Please take that in account before calling thousands of curses upon me.

DICTLINE_PATH = Path(__file__).parent / "DICTLINE.TXT"
DICTLINE_JSON_PATH = Path(__file__).parent / "DICTLINE.json"

INFLECTS_PATH = Path(__file__).parent / "INFLECTS.txt"
INFLECTS_JSON_PATH = Path(__file__).parent / "INFLECTS.json"

# Used for internal representation
NO_STEM = "NO_STEM"
NO_ENDING = "NO_ENDING"

# Remove all unnecessary whitespace from the JSON file
COMPACT_JSON = True

with open(DICTLINE_PATH, "r") as dictline_file:
    dictline_data = dictline_file.readlines()

    # Removes unnecessary whitespace, leaving exactly one space between each part of the entry.
    dictline_formatted = [re.sub("\s\s+", " ", s) for s in dictline_data]

    # Replaces all "zzz" with NO_STEM, making its meaning clearer
    dictline_formatted = [re.sub("zzz", NO_STEM, s) for s in dictline_formatted]

    lines = []
    
    for entry in dictline_formatted:
        lines.append(entry)

    ERROR_LINES = []
    ERROR_COUNT = 0

    NOUN_COUNT = 0
    PRONOUN_COUNT = 0
    VERB_COUNT = 0
    ADJECTIVE_COUNT = 0
    ADVERB_COUNT = 0
    PREPOSITION_COUNT = 0
    INTERJECTION_COUNT = 0
    NUMBER_COUNT = 0
    CONJUNCTION_COUNT = 0
    PACKON_COUNT = 0

    json_lines = []

    for line in lines:
        sline = line.split()

        # Check if the split line is a specific type of word and handle appropriately.
        #
        # Always check based on POS (part of speech) which comes after all the stems.
        #
        # Specifics:
        # - Nouns:
        #    - one stem
        #    - two stems
        # - Pronoun:
        #    - two stems
        # - Verbs:
        #    - one stem
        #    - four stems
        # - Adjectives:
        #    - one stem
        #    - two stems
        #    - four stems
        # - Adverbs:
        #    - one stem
        #    - three stems
        # - Preposition
        #    - one stem
        # - Interjection:
        #    - one stem
        # - Numbers:
        #    - one stem
        #    - four stems
        # - Conjunction:
        #    - one stem
        # - Packon:
        #    - two stems

        if sline[1] == 'N':
            # Entry is a noun with one stem (usually abbreviations and letters etc.)
            json_noun_one = {
                "stem1": sline[0],
                "stem2": NO_STEM,
                "pos": sline[1],
                "declension": sline[2],
                "declension_variant": sline[3],
                "gender": sline[4],
                "noun_kind": sline[5],
                "age": sline[6],
                "area": sline[7],
                "geography": sline[8],
                "frequency": sline[9],
                "source": sline[10],
                "senses": " ".join(sline[11:]) # Definition string was split at first, but now needs to be returned to normal
            }
            json_lines.append(json_noun_one)
            NOUN_COUNT += 1
            continue
        
        if sline[2] == 'N':
            # Entry is a noun with two stems
            json_noun_two = {
                "stem1": sline[0],
                "stem2": sline[1],
                "pos": sline[2],
                "declension": sline[3],
                "declension_variant": sline[4],
                "gender": sline[5],
                "noun_kind": sline[6],
                "age": sline[7],
                "area": sline[8],
                "geography": sline[9],
                "frequency": sline[10],
                "source": sline[11],
                "senses": " ".join(sline[12:])
            }
            json_lines.append(json_noun_two)
            NOUN_COUNT += 1
            continue

        if sline[2] == 'PRON':
            # Entry is a pronoun
            json_pronoun = {
                "stem1": sline[0],
                "stem2": sline[1],
                "pos": sline[2],
                "declension": sline[3],
                "declension_variant": sline[4],
                "pronoun_kind": sline[5],
                "age": sline[6],
                "area": sline[7],
                "geography": sline[8],
                "frequency": sline[9],
                "source": sline[10],
                "senses": " ".join(sline[11:])
            }
            json_lines.append(json_pronoun)
            PRONOUN_COUNT += 1
            continue

        if sline[1] == 'V':
            # Entry is a verb with one stem (a few Biblical/Aramaic verbs)
            json_verb_one = {
                "stem1": sline[0],
                "stem2": NO_STEM,
                "stem3": NO_STEM,
                "stem4": NO_STEM,
                "pos": sline[1],
                "conjugation": sline[2],
                "conjugation_variant": sline[3],
                "verb_kind": sline[4],
                "age": sline[5],
                "area": sline[6],
                "geography": sline[7],
                "frequency": sline[8],
                "source": sline[9],
                "senses": " ".join(sline[10:])
            }
            json_lines.append(json_verb_one)
            VERB_COUNT += 1
            continue

        if sline[4] == 'V':
            # Entry is a verb with four stems
            json_verb_four = {
                "stem1": sline[0],
                "stem2": sline[1],
                "stem3": sline[2],
                "stem4": sline[3],
                "pos": sline[4],
                "conjugation": sline[5],
                "conjugation_variant": sline[6],
                "verb_kind": sline[7],
                "age": sline[8],
                "area": sline[9],
                "geography": sline[10],
                "frequency": sline[11],
                "source": sline[12],
                "senses": " ".join(sline[13:])
            }
            json_lines.append(json_verb_four)
            VERB_COUNT += 1
            continue

        if sline[1] == 'ADJ':
            # Entry is an adjective with one stem
            json_adjective_one = {
                "stem1": sline[0],
                "stem2": NO_STEM,
                "stem3": NO_STEM,
                "stem4": NO_STEM,
                "pos": sline[1],
                "declension": sline[2],
                "declension_variant": sline[3],
                "comparison": sline[4],
                "age": sline[5],
                "area": sline[6],
                "geography": sline[7],
                "frequency": sline[8],
                "source": sline[9],
                "senses": " ".join(sline[10:])
            }
            json_lines.append(json_adjective_one)
            ADJECTIVE_COUNT += 1
            continue

        if sline[2] == 'ADJ':
            # Entry is an adjective with two stems
            json_adjective_two = {
                "stem1": sline[0],
                "stem2": sline[1],
                "stem3": NO_STEM,
                "stem4": NO_STEM,
                "pos": sline[2],
                "declension": sline[3],
                "declension_variant": sline[4],
                "comparison": sline[5],
                "age": sline[6],
                "area": sline[7],
                "geography": sline[8],
                "frequency": sline[9],
                "source": sline[10],
                "senses": " ".join(sline[11:])
            }
            json_lines.append(json_adjective_two)
            ADJECTIVE_COUNT += 1
            continue

        if sline[4] == 'ADJ':
            # Entry is an adjective with four stems
            json_adjective_four = {
                "stem1": sline[0],
                "stem2": sline[1],
                "stem3": sline[2],
                "stem4": sline[3],
                "pos": sline[4],
                "declension": sline[5],
                "declension_variant": sline[6],
                "comparison": sline[7],
                "age": sline[8],
                "area": sline[9],
                "geography": sline[10],
                "frequency": sline[11],
                "source": sline[12],
                "senses": " ".join(sline[13:])
            }
            json_lines.append(json_adjective_four)
            ADJECTIVE_COUNT += 1
            continue

        if sline[1] == 'ADV':
            # Entry is an adverb with one stem
            json_adverb_one = {
                "stem1": sline[0],
                "stem2": NO_STEM,
                "stem3": NO_STEM,
                "pos": sline[1],
                "comparison": sline[2],
                "age": sline[3],
                "area": sline[4],
                "geography": sline[5],
                "frequency": sline[6],
                "source": sline[7],
                "senses": " ".join(sline[8:])
            }
            json_lines.append(json_adverb_one)
            ADVERB_COUNT += 1
            continue

        if sline[3] == 'ADV':
            # Entry is an adverb with three stems
            json_adverb_three = {
                "stem1": sline[0],
                "stem2": sline[1],
                "stem3": sline[2],
                "pos": sline[3],
                "comparison": sline[4],
                "age": sline[5],
                "area": sline[6],
                "geography": sline[7],
                "frequency": sline[8],
                "source": sline[9],
                "senses": " ".join(sline[10:])
            }
            json_lines.append(json_adverb_three)
            ADVERB_COUNT += 1
            continue

        if sline[1] == 'PREP':
            # Entry is a preposition
            json_preposition = {
                "stem1": sline[0],
                "pos": sline[1],
                "case": sline[2],
                "age": sline[3],
                "area": sline[4],
                "geography": sline[5],
                "frequency": sline[6],
                "source": sline[7],
                "senses": " ".join(sline[8:])
            }
            json_lines.append(json_preposition)
            PREPOSITION_COUNT += 1
            continue

        if sline[1] == 'INTERJ':
            # Entry is an interjection
            json_interjection = {
                "stem1": sline[0],
                "pos": sline[1],
                "age": sline[2],
                "area": sline[3],
                "geography": sline[4],
                "frequency": sline[5],
                "source": sline[6],
                "senses": " ".join(sline[7:])
            }
            json_lines.append(json_interjection)
            INTERJECTION_COUNT += 1
            continue

        if sline[4] == 'NUM':
            # Entry is a number with four stems 
            json_number_four = {
                "stem1": sline[0],
                "stem2": sline[1],
                "stem3": sline[2],
                "stem4": sline[3],
                "pos": sline[4],
                "declension": sline[5],
                "declension_variant": sline[6],
                "numeral_sort": sline[7],
                "numeral_value": sline[8], # Contains value of the number (e.g 19 for undevicensum) or 0 (e.g number is an adverbial)
                "age": sline[9],
                "area": sline[10],
                "geography": sline[11],
                "frequency": sline[12],
                "source": sline[13],
                "senses": " ".join(sline[14:])
            }
            json_lines.append(json_number_four)
            NUMBER_COUNT += 1
            continue

        if sline[1] == 'NUM':
            # Entry is a number with one stem
            json_number_one = {
                "stem1": sline[0],
                "stem2": NO_STEM,
                "stem3": NO_STEM,
                "stem4": NO_STEM,
                "pos": sline[1],
                "declension": sline[2],
                "declension_variant": sline[3],
                "numeral_sort": sline[4],
                "numeral_value": sline[5],
                "age": sline[6],
                "area": sline[7],
                "geography": sline[8],
                "frequency": sline[9],
                "source": sline[10],
                "senses": " ".join(sline[11:])
            }
            json_lines.append(json_number_one)
            NUMBER_COUNT += 1
            continue

        if sline[1] == 'CONJ':
            # Entry is a conjunction
            json_conjunction = {
                "stem1": sline[0],
                "pos": sline[1],
                "age": sline[2],
                "area": sline[3],
                "geography": sline[4],
                "frequency": sline[5],
                "source": sline[6],
                "senses": " ".join(sline[7:])
            }
            json_lines.append(json_conjunction)
            CONJUNCTION_COUNT += 1
            continue

        if sline[2] == 'PACK':
            # Entry is a PACKON
            json_packon = {
                "stem1": sline[0],
                "stem2": sline[1],
                "pos": sline[2],
                "declension": sline[3],
                "declension_variant": sline[4],
                "packon_kind": sline[5], # Actually the same as pronoun_kind
                "age": sline[6],
                "area": sline[7],
                "geography": sline[8],
                "frequency": sline[9],
                "source": sline[10],
                "senses": " ".join(sline[11:])
            }
            json_lines.append(json_conjunction)
            PACKON_COUNT += 1
            continue

        # Used for debugging purposes in the event the script misses something.
        NOT_CONFORM = "Could not parse line (" + line + ")."
        ERROR_LINES.append(NOT_CONFORM)
        ERROR_COUNT += 1
    
    # We have finished storing the lines and can now begin converting to JSON.
    with open(DICTLINE_JSON_PATH, "w") as json_file:
        
        if COMPACT_JSON:
            json_file.write(json.dumps(json_lines, separators = (',', ':')))
        else:
            json_file.write(json.dumps(json_lines, indent = 4))
        
        print("Finished parsing and saved the JSON document with (" + str(ERROR_COUNT) + ") errors.")

        TOTAL = (NOUN_COUNT 
                + PRONOUN_COUNT 
                + VERB_COUNT 
                + ADJECTIVE_COUNT 
                + ADVERB_COUNT 
                + PREPOSITION_COUNT 
                + INTERJECTION_COUNT 
                + NUMBER_COUNT 
                + CONJUNCTION_COUNT 
                + PACKON_COUNT)
        
        print("Successfully parsed:")
        
        print("")
        print(str(NOUN_COUNT) + " NOUNS")
        print(str(PRONOUN_COUNT) + " PRONOUNS")
        print(str(VERB_COUNT) + " VERBS")
        print(str(ADJECTIVE_COUNT) + " ADJECTIVES")
        print(str(ADVERB_COUNT) + " ADVERBS")
        print(str(PREPOSITION_COUNT) + " PREPOSITIONS")
        print(str(INTERJECTION_COUNT) + " INTERJECTIONS")
        print(str(NUMBER_COUNT) + " NUMBERS")
        print(str(CONJUNCTION_COUNT) + " CONJUNCTIONS")
        print(str(PACKON_COUNT) + " PACKONS")
        print("")

        print("TOTAL: " + str(TOTAL))

        if ERROR_COUNT > 0:
            print("Error lines are the following: ")
            for error_line in ERROR_LINES:
                print(error_line)
        
        print("Press 'c' if you wish to parse endings. Otherwise press any other key to exit.")
        next = input("")

        if next != 'c':
            exit()


#################################
#    Inflection jsonisation     #
#################################

with open(INFLECTS_PATH) as inflections_file:
    inflections_data = inflections_file.readlines()

    # As with the dictionary, remove unnecessary whitespace
    inflections_formatted = [re.sub("\s\s+", " ", s) for s in inflections_data]

    # Some endings are merely empty strings. In the original INFLECTS file, they were
    # simply not there. For the sake of everybody's sanity, I have decided to denote
    # such endings with NULL in the INFLECTS file (as Whitaker himself did a couple of times) 
    # and NO_ENDING in the JSON variant.
    inflections_formatted = [re.sub("NULL", NO_ENDING, s) for s in inflections_formatted]

    # Removes any empty lines so it does not trigger false positive errors.
    inflections_formatted = filter(lambda empty: empty.strip(), inflections_formatted)

    lines = []
    for entry in inflections_formatted:
        lines.append(entry)

    NOUN_ENDING_COUNT = 0
    ADJECTIVE_ENDING_COUNT = 0
    ADVERB_ENDING_COUNT = 0
    PREPOSITION_ENDING_COUNT = 0
    INTERJECTION_ENDING_COUNT = 0
    VERB_ENDING_COUNT = 0
    VPAR_ENDING_COUNT = 0
    SUPINE_ENDING_COUNT = 0
    PRONOUN_ENDING_COUNT = 0
    NUMBER_ENDING_COUNT = 0
    CONJUNCTION_ENDING_COUNT = 0
    
    INFLECT_ERROR_LINES = []
    INFLECT_ERROR_COUNT = 0

    json_inflects = []
    for inflection in lines:
        sinflection = inflection.split()

        # Ignore commented lines
        if sinflection[0].startswith("--"):
            continue

        # Adverbs, prepositions, conjunctions and interjections have only a few possible "endings".
        # They all evaluate to NO_ENDING and are unique in that they have little information about them.

        if sinflection[0] == 'ADV':
            json_inflection_adverb = {
                "pos": sinflection[0],
                "comparison": sinflection[1],
                "stem": sinflection[2],
                "characters": sinflection[3],
                "ending": sinflection[4],
                "age": sinflection[5],
                "frequency": sinflection[6]
            }
            json_inflects.append(json_inflection_adverb)
            ADVERB_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'PREP':
            json_inflection_preposition = {
                "pos": sinflection[0],
                "case": sinflection[1],
                "stem": sinflection[2],
                "characters": sinflection[3],
                "ending": sinflection[4],
                "age": sinflection[5],
                "frequency": sinflection[6]
            }
            json_inflects.append(json_inflection_preposition)
            PREPOSITION_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'CONJ':
            json_inflection_conjunction = {
                "pos": sinflection[0],
                "stem": sinflection[1],
                "characters": sinflection[2],
                "ending": sinflection[3],
                "age": sinflection[4],
                "frequency": sinflection[5]
            }
            json_inflects.append(json_inflection_conjunction)
            CONJUNCTION_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'INTERJ':
            json_inflection_interjection = {
                "pos": sinflection[0],
                "stem": sinflection[1],
                "characters": sinflection[2],
                "ending": sinflection[3],
                "age": sinflection[4],
                "frequency": sinflection[5]
            }
            json_inflects.append(json_inflection_interjection)
            INTERJECTION_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'N':
            json_inflection_noun = {
                "pos": sinflection[0],
                "declension": sinflection[1],
                "declension_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "stem": sinflection[6],
                "characters": sinflection[7],
                "ending": sinflection[8],
                "age": sinflection[9],
                "frequency": sinflection[10]
            }
            json_inflects.append(json_inflection_noun)
            NOUN_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'ADJ':
            json_inflection_adjective = {
                "pos": sinflection[0],
                "declension": sinflection[1],
                "declension_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "comparison": sinflection[6],
                "stem": sinflection[7],
                "characters": sinflection[8],
                "ending": sinflection[9],
                "age": sinflection[10],
                "frequency": sinflection[11]
            }
            json_inflects.append(json_inflection_adjective)
            ADJECTIVE_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'V':
            json_inflection_verb = {
                "pos": sinflection[0],
                "conjugation": sinflection[1],
                "conjugation_variant": sinflection[2],
                "tense": sinflection[3],
                "voice": sinflection[4],
                "mood": sinflection[5],
                "person": sinflection[6],
                "number": sinflection[7],
                "stem": sinflection[8],
                "characters": sinflection[9],
                "ending": sinflection[10],
                "age": sinflection[11],
                "frequency": sinflection[12]
            }
            json_inflects.append(json_inflection_verb)
            VERB_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'VPAR':
            json_inflection_vpar = {
                "pos": sinflection[0],
                "conjugation": sinflection[1],
                "conjugation_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "tense": sinflection[6],
                "voice": sinflection[7],
                "mood": sinflection[8],
                "stem": sinflection[9],
                "characters": sinflection[8],
                "ending": sinflection[9],
                "age": sinflection[10],
                "frequency": sinflection[11]
            }
            json_inflects.append(json_inflection_vpar)
            VPAR_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'SUPINE':
            json_inflection_supine = {
                "pos": sinflection[0],
                "conjugation": sinflection[1],
                "conjugation_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "stem": sinflection[6],
                "characters": sinflection[7],
                "ending": sinflection[8],
                "age": sinflection[9],
                "frequency": sinflection[10]
            }
            json_inflects.append(json_inflection_supine)
            SUPINE_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'PRON':
            json_inflection_pronoun = {
                "pos": sinflection[0],
                "declension": sinflection[1],
                "declension_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "stem": sinflection[6],
                "characters": sinflection[7],
                "ending": sinflection[8],
                "age": sinflection[9],
                "frequency": sinflection[10]
            }
            json_inflects.append(json_inflection_pronoun)
            PRONOUN_ENDING_COUNT += 1
            continue

        if sinflection[0] == 'NUM':
            json_inflection_number = {
                "pos": sinflection[0],
                "declension": sinflection[1],
                "declension_variant": sinflection[2],
                "case": sinflection[3],
                "number": sinflection[4],
                "gender": sinflection[5],
                "numeral_sort": sinflection[6],
                "stem": sinflection[7],
                "characters": sinflection[8],
                "ending": sinflection[9],
                "age": sinflection[10],
                "frequency": sinflection[11]
            }
            json_inflects.append(json_inflection_number)
            NUMBER_ENDING_COUNT += 1
            continue

        NOT_CONFORM = "Could not parse inflection (" + inflection + ")."
        INFLECT_ERROR_LINES.append(NOT_CONFORM)
        INFLECT_ERROR_COUNT += 1

    with open(INFLECTS_JSON_PATH, "w") as endings_json_file:

        if COMPACT_JSON:
            endings_json_file.write(json.dumps(json_inflects, separators = (',', ':')))
        else:
            endings_json_file.write(json.dumps(json_inflects, indent = 4))

        print("Finished parsing and saved the JSON document with (" + str(INFLECT_ERROR_COUNT) + ") errors.")

        print("Successfully parsed:")

        TOTAL = (ADVERB_ENDING_COUNT 
                + PREPOSITION_ENDING_COUNT
                + CONJUNCTION_ENDING_COUNT
                + INTERJECTION_ENDING_COUNT 
                + NOUN_ENDING_COUNT 
                + ADJECTIVE_ENDING_COUNT 
                + VERB_ENDING_COUNT 
                + VPAR_ENDING_COUNT 
                + SUPINE_ENDING_COUNT 
                + PRONOUN_ENDING_COUNT 
                + NUMBER_ENDING_COUNT)
        
        print("")
        print(str(NOUN_ENDING_COUNT) + " NOUNS")
        print(str(ADJECTIVE_ENDING_COUNT) + " ADJECTIVES")
        print(str(ADVERB_ENDING_COUNT) + " ADVERBS")
        print(str(PREPOSITION_ENDING_COUNT) + " PREPOSITIONS")
        print(str(INTERJECTION_ENDING_COUNT) + " INTERJECTIONS")
        print(str(PRONOUN_ENDING_COUNT) + " PRONOUNS")
        print(str(VERB_ENDING_COUNT) + " VERBS")
        print(str(VPAR_ENDING_COUNT) + " VERB PARTICIPLES")
        print(str(SUPINE_ENDING_COUNT) + " SUPINES")
        print(str(NUMBER_ENDING_COUNT) + " NUMBERS")
        print(str(CONJUNCTION_ENDING_COUNT) + " CONJUNCTIONS")
        print("")

        print("Total: " + str(TOTAL))

        input("Press any key to exit.")

        if INFLECT_ERROR_COUNT > 0:
            print("Error lines are the following: ")
            for inflect_error_line in INFLECT_ERROR_LINES:
                print(inflect_error_line)
