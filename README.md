# Whitaker's WORDS JSONisator
The main purpose of this Python script is the conversion of each dictionary and inflection entry into an appropriate JSON representation.

# WORDS
The late col. William Whitaker created a large dictionary of the Latin language, which contains about 39500 entries gathered from various sources. He also made a very useful program to aid in dictionary search.

# Motivation
Whitaker wrote this program a long while ago, unaware of the technologies that we - for the better or the worse - deal with today. Thus, the original program has lots of room for improvement and modernisation, and as of this moment there are several independent projects doing exactly that. I have resolved to undertake one such project myself.

Therefore, I have found organising the data my first priority. The original version read the lines from the plaintext source files (`DICTLINE.txt` and `INFLECTS.txt`), processed them and finally saved them in a binary format for easy reading/writing from/to the disk. 

Back then, when computers used to have major memory limitations, this was perfectly reasonable. Nowadays, there is no reason not to store all this data in a widely used and supported data format like JSON. This makes it easier to build a new, modern, more powerful implementation of WORDS; easily integrated in modern languages and technologies.

# Structure
Each dictionary entry and each inflection represents a single JSON entry and each one of them has certain attributes which depend on the entry/inflection in question.

Below is a series of table documenting all entries with explanations for each attribute.

## Common attributes
But first, there is a series of attributes which are the same for all __dictionary__ entries. In the tables below, I shall omit them, but you should assume that all entries have them:

| Attribute   | Description                         |
| ----------- | ----------------------------------- |
| `pos`       | Type of word                        |
| `age`       | Approximate time of word's origin   |
| `geography` | Approximate location word's usage   | 
| `area`      | Area of study the word pertains to  |
| `frequency` | How often the word appears in texts |
| `source`    | Dictionary the word was taken from  |
| `senses`    | Word definitions and meanings       |

The same goes for attributes in the __inflection__ entries:

| Attribute    | Description                               |
| ------------ | ----------------------------------------- |
| `pos`        | Type of word the inflection is applied to |
| `stem`       | Stem the ending should be applied to      |
| `characters` | How many characters the ending has        |
| `ending`     | Ending itself                             |
| `age`        | Approximate time of inflection's origin   |
| `frequency`  | How often the inflection appears in texts |

# Dictionary entries

## Nouns

| Attribute            | Description                      |
| -------------------- | -------------------------------- |
| `stem1`              | Nominative form                  |
| `stem2`*             | Genitive stem                    |
| `declension`         | Noun declension                  |
| `declension_variant` | Specific type of noun declension |
| `gender`             | Grammatical gender of the noun   |
| `noun_kind`          | What the noun refers to          |

\* May be empty for some (rare) nouns, such as abbreviations

Example entry:

```json
    {
        "stem1": "abac",
        "stem2": "abac",
        "pos": "N",
        "declension": "2",
        "declension_variant": "1",
        "gender": "M",
        "noun_kind": "T",
        "age": "E",
        "area": "E",
        "geography": "X",
        "frequency": "C",
        "source": "E",
        "senses": "small table for cruets, credence, buffet;"
    }
```

would correspond to the noun `abacus, abaci`.

## Pronouns

| Attribute            | Description                      |
| -------------------- | -------------------------------- |
| `stem1`              | Nominative form                  |
| `stem2`*             | Genitive stem                    |
| `declension`         | Noun declension                  |
| `declension_variant` | Specific type of noun declension |
| `gender`             | Grammatical gender of the noun   |
| `pronoun_kind`       | Specific type of pronoun         |

\* May be empty for some pronouns

Example entry:

```json
{
        "stem1": "qu",
        "stem2": "NO_STEM",
        "pos": "PRON",
        "declension": "1",
        "declension_variant": "3",
        "pronoun_kind": "ADJECT",
        "age": "X",
        "area": "X",
        "geography": "X",
        "frequency": "A",
        "source": "O",
        "senses": "any; anyone/anything, any such; (after si sin/sive/ne);"
}
```

## Verbs

| Attribute             | Description                                     |
| --------------------- | ----------------------------------------------- |
| `stem1`*              | First principal part minus `-o`                 |
| `stem2`               | Second principal part (minus infinitive ending) |
| `stem3`               | Third principal part (minus `-i`)               |
| `stem4`               | Fourth principal part (minus `-us/um`)          |
| `conjugation`         | Verb conjugation                                |
| `conjugation_variant` | Specific type of conjugation                    |
| `verb_kind`           | Type of action the verb represents              |

\* May be the only stem in (rare) Biblical/Aramaic verbs

Example entry:

```json
{
    "stem1": "put",
    "stem2": "put",
    "stem3": "putav",
    "stem4": "putat",
    "pos": "V",
    "conjugation": "1",
    "conjugation_variant": "1",
    "verb_kind": "TRANS",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "X",
    "senses": "think, believe, suppose, hold; reckon, estimate, value; clear up, settle;"
}
```

would correspond to the verb `puto, putare, putavi, putatus`.

## Adjectives

| Attribute            | Description                           |
| -------------------- | ------------------------------------- |
| `stem1`              | Nominative form                       |
| `stem2`              | Genitive stem                         | 
| `stem3`*             | Comparative stem                      |
| `stem4`*             | Superlative stem                      |
| `declension`         | Adjective declension                  |
| `declension_variant` | Specific type of adjective declension |
| `gender`             | Grammatical gender of the noun        |
| `comparison`         | Comparison this adjective is in       |

\* Some adjectives are incomparable and therefore have no 3rd and 4th stems

Example form:

```json
{
    "stem1": "bon",
    "stem2": "bon",
    "stem3": "meli",
    "stem4": "opti",
    "pos": "ADJ",
    "declension": "1",
    "declension_variant": "1",
    "comparison": "X",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "O",
    "senses": "good, honest, brave, noble, kind, pleasant, right, useful; valid; healthy;"
}
```

would correspond to `bonus, boni, melior, optissimus`.

## Adverbs

| Attribute            | Description                           |
| -------------------- | ------------------------------------- |
| `stem1`*             | Positive form                         |
| `stem2`              | Comparative form                      | 
| `stem3`              | Superlative form                      |
| `declension`         | Adjective declension                  |
| `declension_variant` | Specific type of adjective declension |
| `gender`             | Grammatical gender of the noun        |
| `comparison`         | Comparison this adverb is in          |

\* Adverbs that are derived from adjectives are comparable and have all three stems. Other adverbs are incomparable and have only the 1st stem.

Example form:

```json
{
    "stem1": "bene",
    "stem2": "melius",
    "stem3": "optime",
    "pos": "ADV",
    "comparison": "X",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "O",
    "senses": "well, very, quite, rightly, agreeably, cheaply, in good style; better; best;"
}
```

## Prepositions

| Attribute | Description        |
| --------- | ------------------ |
| `stem1`   | Preposition        |
| `case`    | Case it determines |

Example form:

```json
{
    "stem1": "ad",
    "pos": "PREP",
    "case": "ACC",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "O",
    "senses": "to, up to, towards; near, at; until, on, by; almost; according to; about w/NUM;"
}
```

## Interjections

| Attribute | Description  |
| --------- | ------------ |
| `stem1`   | Interjection |

Example form:

```json
{
    "stem1": "vae",
    "pos": "INTERJ",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "B",
    "source": "X",
    "senses": "alas, woe, ah; oh dear; (Vae, puto deus fio. - Vespasian); Bah!, Curses!;"
}
```

## Numbers

| Attribute            | Description                         |
| -------------------- | ----------------------------------- |
| `stem1`*             | Cardinal number stem                |
| `stem2`              | Ordinal number stem                 | 
| `stem3`              | Distributive stem                   |
| `stem4`              | Numerical adverb stem               |
| `declension`         | Numeral declension                  |
| `declension_variant` | Specific type of numeral declension |
| `numeral_sort`       | Specific type of number             |
| `numeral_value`      | Value the number holds (an integer) |

\* Depending on the number, some may have all stems while others will lack some.

Example form:

```json
{
    "stem1": "undeviginti",
    "stem2": "undevicesim",
    "stem3": "undevicen",
    "stem4": "undevic",
    "pos": "NUM",
    "declension": "2",
    "declension_variant": "0",
    "numeral_sort": "X",
    "numeral_value": "19",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "D",
    "source": "X",
    "senses": "nineteen;"
}
```

## Conjunction

| Attribute | Description |
| --------- | ----------- |
| `stem1`   | Conjunction |

Example form:

```json
{
    "stem1": "ubi",
    "pos": "CONJ",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "X",
    "senses": "where, whereby;"
}
```

## Packons

(Artificial constructs used for the dictionary software. More specifically, they are used to represent all the `-qu-/-cu-` pronouns.)

| Attribute            | Description                       |
| -------------------- | --------------------------------- |
| `stem1`              | `-qu` packon                      |
| `stem2`*             | `-cu` packon                      |  
| `declension`         | Declension inflections required   |
| `declension_variant` | Variant of the inflections        |
| `packon_kind`        | Which pronoun type it pertains to |

\* Some packons have no `-cu` stem.

```json
{
    "stem1": "qu",
    "stem2": "cu",
    "pos": "PACK",
    "declension": "1",
    "declension_variant": "0",
    "packon_kind": "REL",
    "age": "X",
    "area": "X",
    "geography": "X",
    "frequency": "A",
    "source": "X",
    "senses": "(w/-cumque) who/whatever, no matter who/what, in any time/way, however small;"
}
```

# Inflections

## Nouns

| Attribute            | Description                                    |
| -------------------- | ---------------------------------------------- |
| `declension`         | Noun declension the ending is applied to       |
| `declension_variant` | Specific declension variant for the ending     |
| `case`               | Case the ending represents                     |
| `number`             | Number (singular/plural) the ending represents |
| `gender`             | Gender the ending represents                   |

Example form:

```json
{
    "pos": "N",
    "declension": "2",
    "declension_variant": "1",
    "case": "GEN",
    "number": "S",
    "gender": "X",
    "stem": "2",
    "characters": "1",
    "ending": "i",
    "age": "X",
    "frequency": "A"
}
```

would correspond to the `-i` ending of the 2nd declension.

## Pronouns

| Attribute            | Description                                    |
| -------------------- | ---------------------------------------------- |
| `declension`         | Pronoun declension the ending is applied to    |
| `declension_variant` | Specific declension variant for the ending     |
| `case`               | Case the ending represents                     |
| `number`             | Number (singular/plural) the ending represents |
| `gender`             | Gender the ending represents                   |

```json
{
    "pos": "PRON",
    "declension": "4",
    "declension_variant": "2",
    "case": "NOM",
    "number": "P",
    "gender": "N",
    "stem": "2",
    "characters": "1",
    "ending": "a",
    "age": "X",
    "frequency": "A"
}
```

## Verbs

| Attribute             | Description                                    |      
| --------------------- | ---------------------------------------------- |
| `conjugation`         | Conjugation the ending is applied to           |
| `conjugation_variant` | Conjugation variant for the ending             |
| `tense`               | Tense the ending represents                    |
| `voice`               | Voice the ending represents                    |
| `mood`                | Mood the ending represents                     |
| `person`              | Person the ending represents                   |
| `number`              | Number (singular/plural) the ending represents |

Example form:

```json
{
    "pos": "V",
    "conjugation": "1",
    "conjugation_variant": "1",
    "tense": "PRES",
    "voice": "ACTIVE",
    "mood": "IND",
    "person": "1",
    "number": "S",
    "stem": "1",
    "characters": "1",
    "ending": "o",
    "age": "X",
    "frequency": "A"
}
```

## Verb participles

| Attribute             | Description                                    |      
| --------------------- | ---------------------------------------------- |
| `conjugation`         | Conjugation the ending is applied to           |
| `conjugation_variant` | Conjugation variant for the ending             |
| `case`                | Case the ending represents                     |
| `tense`               | Tense the ending represents                    |
| `voice`               | Voice the ending represents                    |
| `mood`                | Mood the ending represents                     |
| `number`              | Number (singular/plural) the ending represents |

Example form:

```json
{
    "pos": "VPAR",
    "conjugation": "1",
    "conjugation_variant": "0",
    "case": "NOM",
    "number": "S",
    "gender": "X",
    "tense": "PRES",
    "voice": "ACTIVE",
    "mood": "PPL",
    "stem": "1",
    "characters": "PPL",
    "ending": "1",
    "age": "3",
    "frequency": "ans"
    }
```

## Adjectives

| Attribute            | Description                                    |
| -------------------- | ---------------------------------------------- |
| `declension`         | Adjective declension the ending is applied to  |
| `declension_variant` | Specific declension variant for the ending     |
| `case`               | Case the ending represents                     |
| `number`             | Number (singular/plural) the ending represents |
| `gender`             | Gender the ending represents                   |
| `comparison`         | Adjective comparison the ending represents     |

Example form:

```json
{
        "pos": "ADJ",
        "declension": "1",
        "declension_variant": "1",
        "case": "NOM",
        "number": "S",
        "gender": "M",
        "comparison": "POS",
        "stem": "1",
        "characters": "2",
        "ending": "us",
        "age": "X",
        "frequency": "A"
}
```

## Numbers

| Attribute            | Description                                    |
| -------------------- | ---------------------------------------------- |
| `declension`         | Number declension the ending is applied to     |
| `declension_variant` | Specific declension variant for the ending     |
| `case`               | Case the ending represents                     |
| `number`             | Number (singular/plural) the ending represents |
| `gender`             | Gender the ending represents                   |
| `numeral_sort`       | Sort of the number this ending is applied to   |

Example form:

```json
{
    "pos": "NUM",
    "declension": "1",
    "declension_variant": "1",
    "case": "NOM",
    "number": "S",
    "gender": "M",
    "numeral_sort": "CARD",
    "stem": "1",
    "characters": "2",
    "ending": "us",
    "age": "X",
    "frequency": "A"
}
```

## Supines

| Attribute             | Description                                    |      
| --------------------- | ---------------------------------------------- |
| `conjugation`         | Conjugation the ending is applied to           |
| `conjugation_variant` | Conjugation variant for the ending             |
| `case`                | Case the ending represents                     |
| `gender`              | Gender the ending represents                   |
| `number`              | Number (singular/plural) the ending represents |

Example form:

```json
{
    "pos": "SUPINE",
    "conjugation": "0",
    "conjugation_variant": "0",
    "case": "ACC",
    "number": "S",
    "gender": "N",
    "stem": "4",
    "characters": "2",
    "ending": "um",
    "age": "X",
    "frequency": "A"
}
```

## Adverbs

| Attribute    | Description                             |
| ------------ | --------------------------------------- |
| `comparison` | Adverb comparison the ending represents |

Example form:

```json
{
    "pos": "ADV",
    "comparison": "COMP",
    "stem": "1",
    "characters": "0",
    "ending": "NO_ENDING",
    "age": "X",
    "frequency": "A"
}
```

\* Adverbs, prepositions, conjunctions and interjections are not inflected. Thus they all have NO_ENDING and barely any additional attributes.

## Prepositions

| Attributes | Description                      |
| ---------- | -------------------------------- |
| `case`     | Case the prepositions determines |

Example form: 

```json
{
    "pos": "PREP",
    "case": "ACC",
    "stem": "1",
    "characters": "0",
    "ending": "NO_ENDING",
    "age": "X",
    "frequency": "A"
}
```

## Interjections

| Attributes | Description |
| ---------- | ----------- |
| N/A        | N/A         |

Example form:

```json
{
    "pos": "INTERJ",
    "stem": "1",
    "characters": "0",
    "ending": "NO_ENDING",
    "age": "X",
    "frequency": "A"
}
```

## Conjunctions

| Attributes | Description |
| ---------- | ----------- |
| N/A        | N/A         |

Example form:

```json
{
    "pos": "CONJ",
    "stem": "1",
    "characters": "0",
    "ending": "NO_ENDING",
    "age": "X",
    "frequency": "A"
}
```
