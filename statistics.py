import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  calculations = {'mean': [],
  'variance': [],
  'standard deviation': [],
  'max': [],
  'min': [],
  'sum': []}

  flat = np.array(list);
  arr = flat.reshape(3,3)

  calculations['mean'].append(arr.mean(0).tolist())
  calculations['mean'].append(arr.mean(1).tolist())
  calculations['mean'].append(flat.mean())

  calculations['variance'].append(arr.var(0).tolist())
  calculations['variance'].append(arr.var(1).tolist())
  calculations['variance'].append(flat.var())

  calculations['standard deviation'].append(arr.std(0).tolist())
  calculations['standard deviation'].append(arr.std(1).tolist())
  calculations['standard deviation'].append(flat.std())

  calculations['max'].append(arr.max(0).tolist())
  calculations['max'].append(arr.max(1).tolist())
  calculations['max'].append(flat.max())

  calculations['min'].append(arr.min(0).tolist())
  calculations['min'].append(arr.min(1).tolist())
  calculations['min'].append(flat.min())

  calculations['sum'].append(arr.sum(0).tolist())
  calculations['sum'].append(arr.sum(1).tolist())
  calculations['sum'].append(flat.sum())

  return calculations