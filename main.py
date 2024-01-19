import pandas as pd
from package import channel_id as ch
from package import constants as c



id_list = ch.get_channel_ids_list(c.CHANNELS, c.KEY)

res = ch.auth(c.API_SERVICE_NAME, c.API_VERSION, c.KEY, c.PART, id_list)

data_channels = ch.data(res)


df = pd.DataFrame(data_channels)



