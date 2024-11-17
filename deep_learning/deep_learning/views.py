from django.shortcuts import render
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


def home(request):
    return render(request, "home.html")


def predict_sentiment(review: str) -> str:
    tokenizer = Tokenizer(num_words=10000)
    MIN_POSITIVE = 0.55

    review = tokenizer.texts_to_sequences([review])
    review = pad_sequences(review, maxlen=200)

    model = load_model("deep_learning/model/imdb_sentiment_model.h5")
    prediction = model.predict(review)

    return "Positive" if prediction[0] >= MIN_POSITIVE else "Negative"


def predict(request):
    prediction = None

    if request.method == "GET":
        return render(request, "predict.html")

    if request.method == "POST":
        review = request.POST.get("review")
        prediction = predict_sentiment(review)

        return render(
            request, "predict.html", {"prediction": prediction, "review": review}
        )
