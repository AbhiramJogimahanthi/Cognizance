import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
result = ser.map(lambda x: x[0].upper() + x[1:])
print("\nFirst character of each word to upper case:")
print(result)