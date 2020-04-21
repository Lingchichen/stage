import nltk
class retrieveName:
    def __init__(self):
        pass

    def name_catch(self,content):
        print(content)
        tokens = nltk.tokenize.word_tokenize(content)
        """
        nltk.ne_chunk will generate a speech tree contains token with node
        """
        word = nltk.ne_chunk(nltk.pos_tag(tokens), binary = False)
        print(word)
        person_list = []
        person = []
        name = ""
        """
        get those token which nodes label is PERSON
        """
        for subtree in word.subtrees(filter=lambda t: t.label() == 'PERSON'):
            for leaf in subtree.leaves():
                person.append(leaf[0])
            if len(person) > 1:
                for part in person:
                    name += part + ' '
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
                name = ''
                person = []
        return (person_list)

content="Anthony Stephen Fauci was born on December 24, 1940, in Brooklyn, New York, the second child of first-generation Italian American parents Eugenia and Stephen. A sports nut, he spent his days playing baseball, basketball and football, when not busy working the cash register or making deliveries for his father's pharmacy."
a=retrieveName()
name_list=a.name_catch(content)
print(name_list)
