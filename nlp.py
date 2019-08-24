from sklearn.externals import joblib

class NLP:

    def __init__(self):
            self.classifier = joblib.load("modelo.pkl")
            self.vectorizer = joblib.load("vectorizer.pkl")

    def classify(self, texts):
        """Retorna se comentario e ofensivo ou nao
        Arguments
        ---------
        texts: numpy.ndarray
        Lista contendo as frases/tweets eg: texts = ["Brazil JS 'e o bicho"]
        Returns
        -------
        results: list
        Lista numpy contendo 0 para se frase nao e ofensiva 1 se ela for
        """

        freq = self.vectorizer.transform(texts)
        return self.classifier.predict(freq)