import pandas as pd
import xmltodict

datapath = './export.xml'
with open(datapath, 'r') as xmlfile:
    data = xmltodict.parse(xmlfile.read())

records = data['HealthData']['Record']

df = pd.DataFrame(records)

print(df.columns)
print(df['@type'].unique())

blood_glucose = df[df['@type'] == 'HKQuantityTypeIdentifierBloodGlucose']

date_format = '%Y-%m-%d %H:%M:%S %z'
df['@creationDate'] = pd.to_datetime(df['@creationDate'], format=date_format)
df['@startDate'] = pd.to_datetime(df['@startDate'], format=date_format)
df['@endDate'] = pd.to_datetime(df['@endDate'], format=date_format)
# blood_glucose.loc[:, '@value'] = pd.to_numeric(blood_glucose.loc[:, '@value'])

print(blood_glucose.dtypes)

blood_glucose_by_creation = blood_glucose.groupby('@creationDate')

print(blood_glucose_by_creation)
