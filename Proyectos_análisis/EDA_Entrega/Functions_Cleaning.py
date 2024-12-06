import pandas as pd
import numpy as np

# Diccionario de mapeo: define cómo reemplazar los valores en cada columna
mapping_dict = {
    'House': {
        'Gryffindor': 'Gryffindor',
        'Ravenclaw': 'Ravenclaw',
        'Slytherin': 'Slytherin',
        'Hufflepuff': 'Hufflepuff',
        'Beauxbatons Academy of Magic': 'Beauxbatons',
        'Durmstrang Institute': 'Durmstrang'
    },
    'Hair colour': {
        'Black': 'Black',
        'Red': 'Red',
        'Brown': 'Brown',
        'Blond': 'Blond',
        'Silver| formerly auburn': 'Silver',
        'Auburn': 'Auburn',
        'Grey': 'Grey',
        'White': 'White',
        'Light brown flecked with grey': 'Brown',
        'Colourless and balding': 'Bald',
        'Dirty-blonde': 'Blond',
        'Dark': 'Brown',  # Agrupamos "Dark" en "Brown"
        'Jet-black': 'Black',
        'Mousy': 'Brown',
        # Más agrupaciones según sea necesario
    },
    'Eye colour': {
        'Green': 'Green',
        'Blue': 'Blue',
        'Brown': 'Brown',
        'Black': 'Black',
        'Hazel': 'Hazel',
        'Grey': 'Grey',
        'Bright green': 'Green',
        'Bright brown': 'Brown',
        'Dark': 'Brown',  # Agrupamos "Dark" en "Brown"
        'Silvery': 'Grey',
        'Yellow': 'Yellow',
        'Scarlet': 'Red',
        'Grey/Blue[': 'Grey',  # Agrupación adicional
        # Más agrupaciones según sea necesario
    },
    'Species': {
        'Human': 'Human',
        'Half-Human/Half-Giant': 'Half-Human',
        'Werewolf': 'Werewolf',
        'Ghost': 'Ghost',
        'Centaur': 'Centaur',
        'Human (Metamorphmagus)': 'Human',
        'Human(goblin ancestry)': 'Human',
        # Más agrupaciones según sea necesario
    },
    # Agrega más columnas y mapeos aquí si es necesario
}

# Función para reemplazar valores en base al mapeo
def map_values(value, column_name):
    """
    Reemplaza un valor en función del mapeo definido para una columna.
    Si el valor no está en el mapeo, se pone Unknown (queda NaN si corresponde).
    Se usa para las columnas de "House", "Hair colour", "Eye colour", "Species".
    
    Args:
        value: Valor de la celda.
        column_name: Nombre de la columna correspondiente.
    
    Returns:
        El valor mapeado o "Unknown" si no se encuentra en el mapeo.
    """
    if pd.isna(value):
        return value  # Deja los NaN como están
    
    return mapping_dict[column_name].get(value, "Unknown")  # Mapea o pone "Unknown"

# Función para limpiar todo el dataframe
def map_dataframe(df):
    """
    Mapea los valores del dataframe en base al diccionario `mapping_dict`.
    
    Args:
        df (pd.DataFrame): Dataframe a limpiar.
    
    Returns:
        pd.DataFrame: Dataframe con valores mapeados.
    """
    for column in mapping_dict.keys():
        if column in df.columns:
            df[column] = df[column].apply(lambda x: map_values(x, column))

    return df



# Diccionarios para agrupar valores
loyalty_mapping = {
    'Hogwarts': ['Dumbledore\'s Army', 'Hogwarts School of Witchcraft and Wizardry'],
    'Order of the Phoenix': ['Order of the Phoenix', 'Original Order of the Phoenix', 'Albus Dumbledore'],
    'Death Eaters': ['Death Eaters', 'Lord Voldemort'],
    'Ministry of Magic': ['Ministry of Magic'],
    'Others': ['Gringotts Wizarding Bank', 'Gellert Grindelwald\'s Acolytes'],
    'Unknown': [None]  # Usamos None para cubrir NaN
}


skills_mapping = {
    'Quidditch and Magical Sports': ['Seeker', 'Chaser', 'Keeper', 'Beater', 'Quidditch'],
    'Defensive Magic': ['Defence Against the Dark Arts', 'Duelling', 'Non-verbal magic', 'Occlumency'],
    'Offensive and Dark Magic': ['Dark Arts', 'Cruciatus Curse', 'Imperius Curse', 'Avada Kedavra'],
    'Potions and Herbology': ['Potions', 'Skilled potioneer', 'Herbology'],
    'Transfiguration and Unique Abilities': ['Animagus', 'Metamorphmagus', 'Parseltongue'],
    'Practical or Everyday Magic': ['Household spells', 'Cooking charms', 'Healing magic'],
    'Non-magical Skills': ['Photography', 'Quidditch commentary', 'Writing'],
    'Unknown': [None]  # Usamos None para cubrir NaN
}



# Función para agrupar valores
def categorize_values(values, mapping):
    """
    Agrupa valores en listas según un diccionario de mapeo.
    Se usa para las columnas de "Loyalty" y "Skills".
    
    Args:
        values (list or str): Valores originales de la celda.
        mapping (dict): Diccionario de mapeo.
    
    Returns:
        list: Lista de categorías.
    """
    if pd.isna(values):  # Mantiene los NaN
        return values
    
    # Convertir valores individuales en listas para facilitar el procesamiento
    if isinstance(values, str):
        values = [val.strip() for val in values.split('|')]

    # Crear una lista de categorías correspondientes
    categories = []
    for val in values:
        categorized = False
        for key, group in mapping.items():
            if val in group:
                categories.append(key)
                categorized = True
                break
        if not categorized:
            categories.append('Others')  # Si no coincide, lo marcamos como 'Others'
    return list(set(categories))  # Devuelve categorías únicas
