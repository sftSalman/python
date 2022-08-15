# class CntxtMngr():
#     def __init__(self, obj):
#         self.obj = obj
#     def __enter__(self):
#         self.obj.preprocess()
#         return self.obj
#     def __exit__(self, type, value, traceback):
#         self.obj.postprocess()
#
#
# with CntxtMngr('hi') as CMObj:
#     CMObj.doWork()
with tf.GradientTape() as tape:
    predictions = model(images, training=True)
    loss = loss_object(labels, predictions)

# this is equvalent to the code bellow
def __enter__(self):
    """Enters a context inside which operations are recorded on this tape."""
    self._push_tape()
    return self


def __exit__(self, type, value, traceback):
    """Exits the recording context, no further operations are traced."""
    if self._recording:
        self._pop_tape()

# the flowing link have more details

https://ansel.braket.net/archives/536