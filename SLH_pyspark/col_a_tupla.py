def col_a_tupla(df, col):

    df_inter = df.select(f'{col}')
    df_inter = df_inter.dropDuplicates()
    n = df_inter.columns[0]
    row = df_inter.collect()
    s = str(row)
    s = s.replace('[', '').replace(']', '').replace(f'Row({n}=', '').replace(')', '').replace("'", "")
    tp = tuple(s.split(', '))

    return tp