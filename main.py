from package import rick_morty_api as rm
from package import constants as c
from package import supabase_db as s


json = rm.request_api_base(c.CHARACTER_URL)

df = rm.json_to_dataframe(json)

supa = s.insert_data_from_df(c.SUPABASE_URL, c.SUPABASE_KEY, df, c.TABLE)