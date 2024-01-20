from package import channel_id as ch
from package import constants as c
from package import supabase_db as s



id_list = ch.get_channel_ids_list(c.CHANNELS, c.KEY)

res = ch.auth(c.API_SERVICE_NAME, c.API_VERSION, c.KEY, c.PART, id_list)

data_channels = ch.data(res)

df = ch.create_dataframe(c.NAME_DF,data_channels)

s.insert_data(c.SUPABASE_URL, c.SUPABASE_KEY, df, c.TABLE)

