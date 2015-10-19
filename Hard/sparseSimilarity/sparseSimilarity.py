# The similarity of two docs, each with distinct words, is defined as
# size of intersection divided by size of union. Intersection and union
# are performed on the words in the two docs. Eg: similarity of
# {1,5,3} and {1,7,2,3} is 2/5 = 0.4

# We have a long list of documents where the similarity between docs is
# really sparse. That is, any two arbitrarily selected documents will
# most likely have a similarity of 0.

# Design an algorithm to return the list of pairs of doc IDs and the
# associated similarity.

class DocPair:
    def __init__(self,d1,d2):
        self.doc1 = d1
        self.doc2 = d2

    def __eq__(self,other):
        return self.doc1 == other.doc1 and self.doc2 == other.doc2

    def __hash__(self):
        return (self.doc1 * 31) ^ self.doc2

class Document:
    def __init__(self,iden,values):
        self.iden = iden
        self.values = values

    def size(self):
        return len(self.values)

def computeSimilarities(documents):
    wordToDocs = groupWords(documents)
    similarities = computeIntersections(wordToDocs)
    adjustToSimilarities(documents, similarities)
    return similarities

# Return a hashtable from each word to where it appears
def groupWords(documents):
    wordToDocs = {}
    for iden in documents:
        doc = documents[iden]
        words = doc.values
        for word in words:
            if word in wordToDocs:
                wordToDocs[word].append(doc.iden)
            else:
                wordToDocs[word] = [doc.iden]

    return wordToDocs

# Compute the intersection of documents. Iterate though each list of
# documents and then for each pair in the list, increment the intersection.
def computeIntersections(wordToDocs):
    similarities = {}
    for word in wordToDocs:
        docs = wordToDocs[word]
        docs = sorted(docs)
        for i in range(len(docs)):
            for j in range(i+1,len(docs)):
                increment(similarities, docs[i], docs[j])

    return similarities

# Increment the intersection size of each document pairs.
def increment(similarities, doc1, doc2):
    pair = DocPair(doc1,doc2)
    if pair in similarities:
        similarities[pair] += 1
    else:
        similarities[pair] = 1.0

# Adjust the intersection value to become the similarity
def adjustToSimilarities(docs, similarities):
    for pair in similarities:
        d1 = docs[pair.doc1]
        d2 = docs[pair.doc2]
        union = float(d1.size()) + d2.size() - similarities[pair]
        similarities[pair] /= union
