from allennlp.predictors.predictor import Predictor
from allennlp.common.util import JsonDict, sanitize
from allennlp.data import Instance

'''
Predicts token of each word of a text
input : text with [TOKEN O] format
output : text with [TOKEN PREDICTED LABEL] format
'''

@Predictor.register("enp_fr_predictor")
class EnPFRPredictor(Predictor):
    def predict_instance(self, instance: Instance) -> JsonDict:
        outputs = self._model.forward_on_instance(instance)
        label_vocab = self._model.vocab.get_index_to_token_vocabulary("labels")
        outputs["tokens"] = [str(token) for token in instance.fields["tokens"].tokens]
        outputs["predicted"] = [label_vocab[l] for l in outputs["logits"].argmax(1)]
        outputs["labels"] = instance.fields["label"].labels
        return sanitize(outputs)


'''
Function to write predicted output on test data with known labels

for i,j,k in zip(outputs["tokens"], outputs["predicted"], outputs["labels"]):
    f.write(i + " pred : " + j + "------ true : " + k + "\n")
f.close()
'''
