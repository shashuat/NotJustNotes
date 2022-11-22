def getSummary(text):
    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation

    if text == "":
        return ""

    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]

    punctuation = punctuation + '\n'

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    # print(word_frequencies)

    sentence_tokens = [sent for sent in doc.sents]
    # /print(sentence_tokens)

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
                    
    from heapq import nlargest
    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary

    # print(text)
    # print(len(text))
   #print(summary)
   #print(len(summary))
   #return 

#   text = """
#   Dictatorship, ‘Tyranny’, ‘Despotism’
#   In contemporary speech, dictatorship is often associated with tyranny or despotism. Terms such as dictator, tyrant, or despot are often used as synonyms or alternated between. The first students of the phenomenon of dictatorship in the interwar period, while maintaining that the concept of dictatorship is linked to the Roman model of an extraordinary, yet constitutional and temporary, magistrature, preferred to speak of a ‘new age of despots’, or of a new ‘ère des tyrannies’ (Halèvy, 1938). In more recent studies also the term ‘tyrant’ is preferred over that of dictator for defining the numerous ranks of those holding absolute personal power, dominating, in the second half of the century – and still in some cases dominating – in many countries of the so-called Third World (Rubin, 1987; Chirot, 1994). In fact, contemporary dictatorship evokes some of the characteristics of Greek tyranny, but there are also substantial differences. Above all, the origin of contemporary dictatorship is not always illegitimate. For example, Hitler came to power in 1933 through legal channels and many presidents who became dictators in Latin America were legally elected. Furthermore, the majority of modern dictatorships have a very complex structure of organization and exercise of power due to the mass dimension of the societies in which they operate, the methods they adopt and the scopes they propose. All the above makes contemporary dictatorship substantially new and different to tyranny. Therefore, the thesis that holds that the difference between tyranny and contemporary dictatorship as a form of absolute personal power is not substantive but regards solely the form, the technique and method of government should be forcefully rejected.
#   Despotism versus Democracy
#   What is the key evolved decisional structure that enables collective wisdom in honeybees and some other animals? Conradt and Roper (2003) compared two contrasting structures, despotism and democracy, in the animal kingdom. Using a stochastic model, they showed that democratic decisions usually yield better fitness outcomes to group members than despotism – even when the despot is the most experienced group member, it pays other members to accept the despot’s decision only when group size is small and the difference between their own and the despot’s information is large. These findings may be extendable to human group decision making as well. Most naturally occurring environments for humans as well as other animals are characterized by large statistical uncertainties. Given that no single individual (despot) can handle these uncertainties alone even if he or she were highly experienced, the more viable and reliable decisional structure in the long run is to use groups as an aggregation device. By aggregating members’ opinions, random errors in individual perceptions under uncertainty are canceled collectively, as implied by the law of large numbers in statistics (Surowiecki, 2004).

#   A recent study compared several decision rules, which differed in computational loads, in terms of their net efficiencies under uncertainty (Hastie and Kameda, 2005). These included the best member (‘despotism’) rule and the majority (‘democracy’) rule. Results from both computer simulations and laboratory experiments showed that the majority rule fared quite well, performing at levels comparable to much more computationally taxing rules. Furthermore, the majority rule outperformed the despotic best member rule, even when members were not forced to cooperate for group endeavor and free riding was possible (Kameda et al., 2011).

#   Checks and Balances
#   The primary, process-centered challenge for republicans has been to identify those institutions that find and secure the common good best. Popular sovereignty provides access to every citizen's interests and insights, but democracy would become an elective despotism, without checks and balances to restrain it (Pettit, 1999). Cicero blamed the Greeks' misfortunes on the turbulence of their popular assemblies, lacking internal balance or a senate to control them (Tullius Cicero Flacc.). Republics since Rome have maintained bicameral legislatures to prevent self-seeking in either assembly (Harrington, 1656: p. 22). Democracy is one of several foundation stones of liberty, not an end in itself.

#   The necessary checks and balances of republican government prevent public officials from making themselves and not the res publica the object the state (Paine, 1792: p. 168). The dispersion of power through bicameralism, federalism, and the separation of powers makes it harder for any one person or faction, including the majority, to wield arbitrary power over others (Pettit, 1997: p. 177). American republicans such as John Adams (1787–8: p. I.ii–iii) and Alexander Hamilton et al. (1787: IX) added representation and the life tenure of judges to bicameralism and checks on governmental powers as basic desiderata of balanced republican institutions. If the people and judges are outside government, they can better control their government's mistakes (Hamilton et al., 1787: p. LXIII).

#   Modern republicans such as Philip Pettit differ from democrats in viewing democracy as a derivative value, in service to the broader ideal of balanced or ‘contested’ government (Pettit, 1997: p. 187). All government decisions should be subject to challenge by institutions that prevent private inclinations from ruling public interests and ideas. Republicans have proposed bills of rights, public hearings, and many other devices designed to constrain and channel public decision making, so that ordinary citizens may influence their government's decisions, without diverting the public purposes of the state. For further references see Constitutionalism."""

#   getSummary(text)
