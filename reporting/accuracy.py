from .bb_registry import register
from sklearn.metrics import f1_score


@register('acc')
def model_accuracy(y, pred):
    return f1_score(y, pred)
