def cols_para_sql_athena(schema_str):
    import re

    schema_str = schema_str.replace('-', '').replace('|', '').replace(':', '').replace(' (nullable = true)', ',')
    pattern = re.compile(r'(\w+)\s+string')
    result = re.sub(pattern, r'"\1" string', schema_str)

    return result