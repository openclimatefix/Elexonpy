def json_to_dataframe_with_metadata(data):
    # Extract metadata
    if isinstance(data, dict):
        metadata = data.get('metadata', [])
        if isinstance(metadata, dict):
            df_meta = pd.DataFrame.from_dict(metadata, orient='index').T
        else:
            df_meta = "No metadata provided"
    else:
        df_meta = "No metadata provided"

    # Normalize the JSON data into a flat table
    df = pd.json_normalize(data)

    # Identify columns with lists of dictionaries
    columns_with_list = [col for col in df.columns if isinstance(df[col].iloc[0], list)]

    # Explode columns containing lists
    for column in columns_with_list:
        df = df.explode(column)

        # Extract keys from dictionaries and use them as new column names
        dicts = df[column].dropna()

        if not dicts.empty:
            keys = set(k for d in dicts for k in (list(d.keys()) if isinstance(d, dict) else []))
            for key in keys:
                df[key] = df[column].apply(lambda x: x.get(key) if isinstance(x, dict) else None)

        # Drop the original column containing dictionaries
        df.drop(columns=[column], inplace=True)

    return df, df_meta
