import openai
import re
import json


#TODO: REFECTOR THE CODE for N number of questions:: Optimization Needed.
#TODO: implement openai chatgpt for default questions
class GPTDataModel:
    def get_patient_name(self,db_data):
        # print(dict(db_data))
        # print(db_data)
        # mydata = (db_data.objects.all())
        for row in db_data:
            # print(row.__dict__)
            name  = row.prefix + row.first + row.last
            print(name)
            # print(rows.id)
            # print(rows.first_name)
        return name

# def NameExtractor(prompt):
#     '''nltk extractor for tokenization and regex extractor'''
#     regex = '\d*[/-]\d*[/-]\d*'
#     match = re.findall(regex, prompt)
#     if len(match) == 2:
#         name = get_patient_name(match[0], match[1])
#         return name
#
#
#
# def get_immunizations():
#     df = pd.read_csv("immunizations.csv")
#     patient_id = json.loads(open("patient_config").read())["patient_id"]
#     output_df = df.loc[df.PATIENT == patient_id]
#     data_set = set(output_df["DESCRIPTION"].to_list())
#     str = ''''''
#     for item in data_set:
#         str = str + "- " + item + "\n"
#     return str
#
#
# def get_diagnosis():
#     df = pd.read_csv("careplans.csv")
#     patient_id = json.loads(open("patient_config").read())["patient_id"]
#     output_df = df.loc[df.PATIENT == patient_id]
#     data_set = set(output_df["DESCRIPTION"].to_list())
#     str = ''''''
#     for item in data_set:
#         str = str + "- " + item + "\n"
#     return str
#
#
# def get_procedure():
#     df = pd.read_csv("procedures.csv")
#     patient_id = json.loads(open("patient_config").read())["patient_id"]
#     output_df = df.loc[df.PATIENT == patient_id]
#     data_set = set(output_df["DESCRIPTION"].to_list())
#     str = ''''''
#     for item in data_set:
#         str = str + "- " + item + "\n"
#     return str
#
# def get_outcome_procedure():
#     df = pd.read_csv("procedures.csv")
#     patient_id = json.loads(open("patient_config").read())["patient_id"]
#     output_df = df.loc[df.PATIENT == patient_id]
#     data_set = set(output_df["DESCRIPTION"].to_list())  #TODO: include date in output
#     str = ''''''
#     for item in data_set:
#         str = str + "- " + item + "\n"
#     return str
#
#
#
# prompt = str(input("Enter prompt:"))
# print(get(prompt))


