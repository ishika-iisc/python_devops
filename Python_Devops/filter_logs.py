import re

logs =[ 
    "INFO - system started",
    "WARNING - system Warning",
    "ERROR - system failed to connect server",
    "ERROR - system timeout occurred",
    "system running, no ERRORs yet",
    "critical ERROR reported",
    "system throughs a SUPERERROR signal"
]
#  to see the statments which started with error
# for line in logs:
#     if re.search(r'^ERROR',line):
#         print(f"{line}")


# to match error anywhere in the line

# for line in logs:
#     if re.search(r'ERROR',line):
#         print(f"{line}")

#  to match the ERROR as a word not as a part of anyy other word

for line in logs:
    if re.search(r'\bERROR\b',line):
        print(f"{line}")