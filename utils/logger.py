from torch.utils import tensorboard

class Logger(object):

    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""
        self.writer = tensorboard.writer.SummaryWriter(log_dir)

    def scalar_summary(self, tag, value, step):
        self.writer.add_scalar(tag, value, step)
        self.writer.flush()
