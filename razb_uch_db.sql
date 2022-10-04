create table Route (
	ID_UCH_VOST_POL integer primary key,
	NAME_BEGIN_VOST_UCH text,
	ESR_BEGIN_VOST_UCH integer,
	DOR_BEGIN_VOST_UCH integer,
	OKATO_BEGIN_VOST_UCH_NAME text,
	X_BEG_VOST_UCH decimal,
	Y_BEG_VOST_UCH decimal,
	NAME_END_VOST_UCH text,
	ESR_END_VOST_UCH integer,
	DOR_END_VOST_UCH integer,
	OKATO_END_VOST_UCH_NAME text,
	X_END_VOST_UCH decimal,
	Y_END_VOST_UCH decimal
);

create table RouteDetails (
	id SERIAL primary key,
	NUM_CNSI_MELK_SET integer,
	route_id integer references Route(ID_UCH_VOST_POL) on delete cascade,
	NAME_BEGIN_MELK_SET text,
	ESR_BEGIN_MELK_SET integer,
	DOR_BEGIN_MELK_SET integer,
	OKATO_BEGIN_MELK_SET_NAME text,
	NAME_END_MELK_SET text,
	ESR_END_MELK_SET integer,
	DOR_END_MELK_SET integer,
	OKATO_END_MELK_SET_NAME text
);