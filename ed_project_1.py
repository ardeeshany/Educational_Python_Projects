# Data Sctructure
## base python + {numpy}

## .py vs .ipynb = .Rmd
type("string")
type(12); type(12.3)
type(True)
type([1, "string", False])
type({
  "key1": "value1",
  "key2": 12.5
})


# function and methods on string
"string".capitalize(); "string".upper(); "string".lower()
"string".replace("i", "I")
len("string")


# working with dict
Dict = {"k1": 12, "k2": "str", True: 13.5, "k4": [1, False], 12: 24, "k5": {"k51": 1, "k52": True}}
Dict["k4"]
Dict["k5"]["k51"]
Dict["k6"] = "val1"
del(Dict["k4"])
Dict.keys()
Dict.values()
Dict.items()

len(Dict)


# Working with list
L = [2, "string", [True, "string2"], {"k1": 12, "k2": "str3"}]
L[0]; L[:2]; L[3]["k1"]; L[2][0]
## Wrangling lists
L[1] = "str"
del(L[1])
L + [1,[2,True]]

## functions on List
len(L)
max([1,12,13.5,2])

## methods on List
L = [1, 12.5, "str", 14, [2.5, False]]
L.index(12.5)
L.reverse()
L.append("str2")
L.remove(14)

# Copy a list
## Copy by reference
L1 = [1, True]; 
L2 = L1
L2[0] = True; 
L1

## Copy by value
L1 = [1, True]; 
L2 = list(L1)
L2[0] = False; 
L1


# Numpy: Element-wise list
L1 = [1, 12.5]; 
L2 = [2, 13]
L1 + L2
L1/L2   # not supported
L1 > 1  # not supported


import numpy as np
L1 = np.array([1, 12.5]); 
L2 = np.array([2, 13])
L1 + L2
(L1/L2) ** 2
L1 > 1
L1[L1 > 1]
L1_2_1 = np.array([L1, L2, L1])

type(L1)
type(L1_2_1)
L1.shape
L1_2_1.shape
L1_2_1[0][1]; L1_2_1[0, 1]; L1_2_1[0:3, 0]

# np functions are very fast!
L3 = [1, 0, 12.5, -2, 1, 1, -5.1234]
np.mean(L3)
np.median(L3)
np.std(L3)
np.round(L3, 2)
np.sum(L3)
np.sort(L3)
np.var(L3)
np.quantile(L3, .95)
np.cumsum(L3)



np.random.rand()
np.random.normal(0, 1, 3)
np.random.seed(2021)
np.column_stack([[L1, L2]]); [L1, L2]


# logical operators
np.logical_and(L1 >= 1, L2 > 1)
np.logical_or(L1 > 2, L2 > 2)
np.logical_not(L1 > 1)


# conditional
if (L1 > L2).any():
  print("Yes")
else:
  print("No")

# for
for i in range(1, 10):
  print(i)

for i in "HelLo":
  print(i.lower())

for i in ["s1", "s2"]: # np.array(["st1", "st2"])
  print(i + "dm")


for ind, val  in enumerate(["st1", "st2"]):
  print(str(ind) + "=" + "val")


for v in np.nditer(np.array([L1, L2])): # +2Darray
  print(v)

for k, v in {"k1": 12, "k2": True}.items():
  print(k + ": " + str(v))

