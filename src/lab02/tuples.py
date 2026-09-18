def str_to_tuple(row: str) -> tuple:

    a = tuple(map(str, row.strip('() ').split(',')))
    name = []
    first_flag = 0

    for word in a[0].strip('" ').split():
        word = word.strip()
        if len(word) and first_flag:
                    name.append(word[0].capitalize() + '.')
                    first_flag = 1
                    
        if len(word) and not(first_flag):
            name.append(word[0].capitalize() + word[1:] + ' ')
            first_flag = 1
       
    
    return tuple([''.join(name), a[1].strip('" '), round(float(a[2]), 2)])

def format_record(rec: tuple[str, str, float]) -> str:
    return f'{rec[0]}, гр. {rec[1]}, GPA {rec[2]:.2f}'

print(format_record(str_to_tuple('("  сидорова  анна   сергеевна ", "ABB-01", 3.999)')))