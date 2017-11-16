import numpy as np

import torch
from torch.autograd import Variable

from divmachines.torch_utils import gpu


def _predict_process_ids(user_ids, item_ids, num_items, use_cuda):

    if item_ids is None:
        item_ids = np.arange(num_items, dtype=np.int64)

    if np.isscalar(user_ids):
        user_ids = np.array(user_ids, dtype=np.int64)

    if np.isscalar(item_ids):
        item_ids = np.array(item_ids, dtype=np.int64)

    user_ids = torch.from_numpy(user_ids.reshape(-1, 1).astype(np.int64))
    item_ids = torch.from_numpy(item_ids.reshape(-1, 1).astype(np.int64))

    if item_ids.size(0) != user_ids.size(0):
        user_ids = user_ids.expand(user_ids.size(0), item_ids.size()[0])

    user_var = Variable(gpu(user_ids, use_cuda))
    item_var = Variable(gpu(item_ids, use_cuda))

    return user_var.squeeze(), item_var.squeeze()
