import pandas as pd
from sqlalchemy import create_engine, text
import json

with open('appsettings.json', 'r') as config_file: #параметры хранятся в .json файле
    config = json.load(config_file)
    connection_string = config['postgres']['connectionstring'] #connection string для подключения к БД
    if_exists_routes = config['if_exists_routes'] #что делать, если запись уже есть в Routes
    if_exists_route_details = config['if_exists_route_details'] #что делать, если запись уже есть в RouteDetails
    path = config['xlsx_file_path'] #путь к файлу, данные из которого нужно преобразовать

engine = create_engine(connection_string)

razb_uch = pd.read_excel(path) #считываем данные из .xlsx файла в pandas DataFrame

#разбиваем данные на два DataFrame-а, чтобы записать каждый из них в соответсвующую таблицу
#DataFrame маршрутов
routes_df = razb_uch[razb_uch.columns[:13]] #нам необходимы первые 13 колонок
routes_df = routes_df.drop_duplicates(ignore_index=True) #удаляем дубликаты (для каждой остановки будем хранить 
#ссылку на маршрут)
routes_df.columns = routes_df.columns.str.lower() #переводим названия колонок в нижний регистр, т.к. в БД названия 
#столбцов и таблиц записаны именно в нижнем
routes_df.set_index('id_uch_vost_pol', inplace=True) #устанавливаем индекс на поле, которое, судя по всему, им и является
routes_df.to_sql('route', con=engine, if_exists=if_exists_routes) #записываем данные из DataFrame в таблицу Routes

#DataFrmae отрезков пути между остановками
routeDetails_df = razb_uch[razb_uch.columns[13:]] #сюда входят все столбцы, ачиная с 14
routeDetails_df = routeDetails_df.drop_duplicates(ignore_index=True) #здесь дубликатов быть не должно, но на всякий случай
#лучше предусмотреть и этот вариант
routeDetails_df['route_id'] = razb_uch['ID_UCH_VOST_POL'] #добавляем столбец с id маршрута, к которому принадлежит данный
#путь между остановками
routeDetails_df.columns = routeDetails_df.columns.str.lower()#переводим названия колонок в нижний регистр, т.к. в БД
#названия столбцов и таблиц записаны именно в нижнем
routeDetails_df.to_sql('routedetails', con=engine, if_exists=if_exists_route_details, index=False) #записываем данные 
#из DataFrame в таблицу RouteDetails