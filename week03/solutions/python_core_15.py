def classify_weights(weights: list[int | float]) -> list[str]:
    classified_weights: list[str] = []

    for weight in weights:
        if weight <= 0:
            classified_weights.append('INVALID')
        elif 0 < weight <= 1:
            classified_weights.append('SMALL')
        elif 1 < weight <= 5:
            classified_weights.append('MEDIUM')
        else:
            classified_weights.append('LARGE')

    return classified_weights
