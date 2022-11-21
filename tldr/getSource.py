def getSource(text):
    import nltk
    from nltk.tokenize import word_tokenize
    from collections import Counter
    nltk.download('wordnet')      #download if using this module for the first time
    nltk.download('punkt')
    nltk.download('omw-1.4')

    from nltk.stem import WordNetLemmatizer 
    from nltk.corpus import stopwords
    nltk.download('stopwords')    #download if using this module for the first time

    tokens = word_tokenize(text1)
    lowercase_tokens = [t.lower() for t in tokens]
    # print(lowercase_tokens)
    bagofwords_1 = Counter(lowercase_tokens)
    alphabets = [t for t in lowercase_tokens if t.isalpha()]

    words = stopwords.words("english")
    stopwords_removed = [t for t in alphabets if t not in words]

    # print(stopwords_removed)

    lemmatizer = WordNetLemmatizer()

    lem_tokens = [lemmatizer.lemmatize(t) for t in stopwords_removed]

    bag_words = Counter(lem_tokens)
    # print(bag_words.most_common(6))

    G_search=''
    n=5
    for i in bag_words:
    if n==0:
        break
    G_search=G_search+i+' '
    n-=1
    print(G_search)

    # pip install beautifulsoup4
    # pip install google
    from googlesearch import search 
    query = G_search
    
    for j in search(query, tld="co.in", num=3, stop=3, pause=2):
        print(j)
    return 
text1 = """Ted Bundy, in full Theodore Robert Bundy, (born November 24, 1946, Burlington, Vermont, U.S.—died January 24, 1989, Starke, Florida), American serial killer and rapist, one of the most notorious criminals of the late 20th century.

Bundy had a difficult childhood; he had a strained relationship with his stepfather, and his shyness made him a frequent target of bullying. Later, however, his intelligence and social skills enabled him to enjoy a successful college career, and he developed a series of apparently normal emotional relationships with women. Despite this apparent stability, he sexually assaulted and killed several young women in Washington, Oregon, Colorado, Utah, and Florida between 1974 and 1978. Although he would ultimately confess to 28 murders, some estimated that he was responsible for hundreds of deaths. Following a well-publicized trial, he was sentenced to death in 1979 for the murder of two college students. In the following year he again was sentenced to death, this time for the rape and murder of a 12-year-old girl. Bundy was executed in Florida’s electric chair in 1989.
Despite the appalling nature of his crimes, Bundy became something of a celebrity, particularly following his escape from custody in Colorado in 1977. During his trial his charm and intelligence drew significant public attention. His case inspired a series of popular novels and films devoted to serial murder. It also galvanized feminist criminologists, who contended that the popular media had transformed Bundy into a romantic figure.
sexual abuse, in criminal law, any act of sexual contact that a person suffers, submits to, participates in, or performs as a result of force or violence, threats, fear, or deception or without having legally consented to the act. Sexual contact in this context is usually understood to encompass any intentional touching, fondling, or penetration of intimate parts of the victim’s body by the perpetrator for the purpose of arousing or satisfying the perpetrator’s sexual desires or as a means of degrading, humiliating, or punishing the victim. Criminal sexual contact thus includes acts of sexual violence such as rape. Although legal consent to an act of sexual contact has been defined in various ways, it is generally considered to be absent in most if not all of the following circumstances: (1) the victim actively resists the act, (2) the victim otherwise communicates to the perpetrator that he or she does not agree to the act, (3) the victim does not freely communicate or signal to the perpetrator his or her agreement to the act, (4) the victim is a minor or a child, (5) the victim lacks understanding of the significance or consequences of the act, or (6) the victim is mentally or physically incapacitated in relevant ways—e.g., by being intoxicated or unconscious.

As a category of crime, sexual abuse overlaps with sexual assault, as both involve sexual contact without the victim’s consent. The former, however, usually involves a series of acts of criminal sexual contact committed by a single perpetrator (or group of perpetrators) over a prolonged period, whereas the latter usually consists of a particular act committed by a perpetrator (or group of perpetrators) against a single person. Sexual abuse also frequently consists of crimes against minors or children by a perpetrator who is acquainted with the victims or is viewed by them as a figure of authority—as are older family members or relatives, teachers, coaches, doctors, employers, and others (see child abuse).

In the United States, almost all persons formally charged with sexual abuse are prosecuted under state laws, which vary in their definitions of sexual abuse and assault and in the penalties they assign to those crimes. Federal law also prohibits acts of sexual abuse, though the statutes apply only to acts committed within the maritime or territorial jurisdictions of the United States, including federal prisons (18 U.S. Code §2242).
"""    
getSource(text1)