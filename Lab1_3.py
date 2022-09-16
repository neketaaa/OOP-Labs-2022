import argparse

parser = argparse.ArgumentParser()
parser.add_argument('formula', type=str)
args = parser.parse_args()
result = True
result_value = None
i = 1
for i in range(len(args.formula) - 1):
    if not args.formula[i].isdigit():
        if args.formula[i] == '+' or args.formula[i] == '+':
            if not args.formula[i-1].isdigit():
                result = False
        else:
            result = False
if result:
    result_value = eval(args.formula)
print('(', result, '/', result_value, ')')
#     if args.formula[i].isdigit():
#         temp_number_frst = str(temp_number_frst) + str(args.formula[i])
#         print(temp_number_frst)
#     else:
#         if args.formula[i] == '+' or args.formula[i] == '-':
#             if args.formula[i - 1] == '+' or args.formula[i - 1] == '-' or i == (len(args.formula) - 1):
#                 # break
#                 print('Error1')
#             else:
#                 match sighn:
#                     case '+':
#                         result_value += int(temp_number_frst)
#                     case '-':
#                         result_value -= int(temp_number_frst)
#                 temp_number_frst = None
#                 print(i, result_value)
#         else:
#             # break
#             print('Error2')
# print('res:',result_value)
# print('len:',len(args.formula))
# print('borders:',args.formula[0], args.formula[len(args.formula)-1])

    # print(args.formula[i])
    # if sighn is None:
    #     if args.formula[i].isdigit():
    #         temp_number_frst += args.formula[i]
    #     if args.formula[i] == '+':
    #         sighn = '+'
    #     if args.formula[i] == '-':
    #         sighn = '-'
    # else:
    #     if args.formula[i].isdigit():
    #         temp_number_scnd += args.formula[i]
    #     if args.formula[i] == '+' or args.formula[i] == '-':
    #         break
    #     if i == (len(args.formula) - 1) or not args.formula[i+1].isdigit():
    #         match sighn:
    #             case '+':
    #                 result_value = int(temp_number_frst) + int(temp_number_scnd)
    #             case '-':
    #                 result_value = int(temp_number_frst) - int(temp_number_scnd)
    #         temp_number_frst = result_value
    #         temp_number_scnd = str(None)

# print(temp_number)
