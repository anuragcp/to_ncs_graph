import argparse
import tensorflow.keras as keras
import tensorflow.keras.backend as K
import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument("-m","--model",
dest="model")
parser.add_argument("-w","--weight",
dest="weight")
args=parser.parse_args()
if(args.model==None or args.model==None):
  print("Please provide  "\
         "complete\npath to model and "\
         "weight\n\t" \
         "use the flags\n\t\t-m --> for"\
         " path to model\n\t\t-w --> "\
         "for path to weights.")
  exit()

model_file = args.model
weights_file = args.weight
config=None

with open(model_file, "r") as file:
    config = file.read()

K.set_learning_phase(0)
model = keras.models.model_from_json(config)
model.load_weights(weights_file)

saver = tf.train.Saver()
sess = K.get_session()
saver.save(sess, "./TF_Model/tf_model")

fw = tf.summary.FileWriter('logs', 
sess.graph)
fw.close()
