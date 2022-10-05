import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

razb_uch = pd.read_excel("razb_uch.xlsx")

routes_df = razb_uch[razb_uch.columns[:13]]
routes_df.drop_duplicates(inplace=True, ignore_index=True)
routes_df.columns = routes_df.columns.str.lower()
routes_df.set_index('id_uch_vost_pol', inplace=True)
routes_df.to_sql('route', con=engine, if_exists='append')

routeDetails_df = razb_uch[razb_uch.columns[13:]]
routeDetails_df.drop_duplicates(inplace=True, ignore_index=True)
routeDetails_df['route_id'] = razb_uch['ID_UCH_VOST_POL']
routeDetails_df.columns = routeDetails_df.columns.str.lower()
routeDetails_df.to_sql('routedetails', con=engine, if_exists='append', index=False)