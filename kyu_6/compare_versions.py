# Compare Versions

# https://www.codewars.com/kata/53b138b3b987275b46000115/train/python

# def compare_versions(version1, version2):
#     version1, version2 = version1.split('.'), version2.split('.')
#
#     for v1, v2 in zip(version1, version2):
#         if int(v1) > int(v2):
#             return True
#         if int(v1) < int(v2):
#             return False
#
#     return len(version1) >= len(version2)

def compare_versions(version1, version2):
    return [int(v) for v in version1.split('.')] >= [int(v) for v in version2.split('.')]
