import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(word1.similarity(word2)) # 0.59
print(word3.similarity(word2)) # 0.40
print(word3.similarity(word1)) # 0.22

'''
    Cat and Monkey are most similar, probably because they are both animals
    Monkey and banana are more similar than cat and banana, probably because
    cats aren't known for eating bananas.
'''

word1 = nlp('car')
word2 = nlp('truck')
word3 = nlp('cargo')

print(word1.similarity(word2)) # 0.78
print(word3.similarity(word2)) # 0.55
print(word3.similarity(word1)) # 0.35

'''
    Car and Truck are very similar, both are vehicles, but cargo is slightly
    more similar with the truck than with the car.
'''

sentence_to_compare = 'Why is my cat on the car'
sentences = [
    'where did my dog go',
    'Hello, there is my car',
    'I\'ve lost my car in my car',
    'I\'d like my boat back',
    'I will name my dog Diana'
]

model_sentence = nlp(sentence_to_compare)
print(f'Model Sentence: {model_sentence}')
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f'{sentence} - {similarity}')

'''
    When running example.py with 'en_core_wb_sm' instead of 'en_core_wb_md'
        - Complaints similarity is reported as lower across the board, with 'md'
          you would be confident that the complaints are similar to one another,
          but not so with 'sm'
        - Similarly with the complaints similarity, 'md' is much more confident
          that the recipes are similar with one another.
        - Surprisingly to me, it found the complaints to still be relatively
          similar to the recipes, which suggests you can't rely solely on this
          method for certain tasks.
'''