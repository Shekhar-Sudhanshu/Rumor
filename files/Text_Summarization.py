import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


def getsumValues(sentenceValue):
  sumValues = 0
  for sentence in sentenceValue:
    sumValues +=sentenceValue[sentence]
  average = int(sumValues/len(sentenceValue))
  return average




def getsentenceValue(sentences, freqTable):
  sentenceValue=dict()
  for sentence in sentences:
    for word, ferq in freqTable.items():#unpacking the word using freqTable
      if word in sentence.lower():
        if sentence in sentenceValue:
          sentenceValue[sentence] += ferq
        else:
          sentenceValue[sentence] = ferq

  return sentenceValue


def textsumarization(text):
  nltk.download('stopwords')
  nltk.download('punkt')

  stopWords= set(stopwords.words("english"))
  words = word_tokenize(text)#divied into words
  sentences = sent_tokenize(text)
  freqTable = dict()
  for word in words:
    word = word.lower()
    if word in stopWords:
      continue
    if word in freqTable:
      freqTable[word]=+ 1
    else:
      freqTable[word] = 1

  sentenceValue = getsentenceValue(sentences, freqTable)
  average = getsumValues(sentenceValue)
  summary = ''
  for sentence in sentences:
      if ((sentence in sentenceValue) and (sentenceValue[sentence] > ( 1.25 * average))):
        summary += " " + sentence
  return summary
